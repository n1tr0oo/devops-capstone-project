"""REST routes."""
from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError
from service import db
from service.models import Account

accounts_bp = Blueprint("accounts", __name__)


def error(message, status):
    return jsonify(error=message), status


@accounts_bp.post("/accounts")
def create_account():
    data = request.get_json(silent=True) or {}
    if not data.get("name") or not data.get("email"):
        return error("name and email are required", 400)
    account = Account()
    account.update_from(data)
    db.session.add(account)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return error("email already exists", 409)
    return jsonify(account.serialize()), 201


@accounts_bp.get("/accounts")
def list_accounts():
    accounts = db.session.execute(db.select(Account).order_by(Account.id)).scalars()
    return jsonify([account.serialize() for account in accounts]), 200


@accounts_bp.get("/accounts/<int:account_id>")
def read_account(account_id):
    account = db.session.get(Account, account_id)
    return (jsonify(account.serialize()), 200) if account else error("account not found", 404)


@accounts_bp.put("/accounts/<int:account_id>")
def update_account(account_id):
    account = db.session.get(Account, account_id)
    if not account:
        return error("account not found", 404)
    data = request.get_json(silent=True) or {}
    if "name" in data and not data["name"] or "email" in data and not data["email"]:
        return error("name and email cannot be empty", 400)
    account.update_from(data)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return error("email already exists", 409)
    return jsonify(account.serialize()), 200


@accounts_bp.delete("/accounts/<int:account_id>")
def delete_account(account_id):
    account = db.session.get(Account, account_id)
    if not account:
        return error("account not found", 404)
    db.session.delete(account)
    db.session.commit()
    return "", 204
