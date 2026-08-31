"""Account model tests."""
import unittest
from service import create_app, db
from service.models import Account


class AccountModelTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app({"TESTING": True, "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"})
        self.context = self.app.app_context()
        self.context.push()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.context.pop()

    def test_create_and_serialize_account(self):
        account = Account(name="Ada", email="ada@example.com", address="London")
        db.session.add(account)
        db.session.commit()
        result = account.serialize()
        self.assertEqual(result["name"], "Ada")
        self.assertEqual(result["email"], "ada@example.com")
        self.assertIsInstance(result["id"], int)
        self.assertIn("date_joined", result)

    def test_update_from(self):
        account = Account(name="Old", email="old@example.com")
        account.update_from({"name": "New", "ignored": "value"})
        self.assertEqual(account.name, "New")
        self.assertFalse(hasattr(account, "ignored"))

    def test_account_table_name(self):
        self.assertEqual(Account.__tablename__, "account")

    def test_new_account_has_no_id_before_save(self):
        self.assertIsNone(Account(name="A", email="a@example.com").id)

    def test_optional_fields_default_to_none(self):
        account = Account(name="A", email="a@example.com")
        self.assertIsNone(account.address)
        self.assertIsNone(account.phone_number)
