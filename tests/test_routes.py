"""REST API tests."""
import unittest
from service import create_app, db


class AccountRoutesTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app({"TESTING": True, "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"})
        self.client = self.app.test_client()
        self.context = self.app.app_context()
        self.context.push()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.context.pop()

    def create(self, email="john@example.com"):
        return self.client.post("/accounts", json={"name": "John", "email": email,
                                "address": "Astana", "phone_number": "+77000000000"})

    def test_health_and_security_headers(self):
        response = self.client.get("/health", headers={"Origin": "https://example.com"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Access-Control-Allow-Origin"], "https://example.com")
        self.assertIn("X-Frame-Options", response.headers)

    def test_create_list_read_update_delete(self):
        created = self.create()
        self.assertEqual(created.status_code, 201)
        account_id = created.get_json()["id"]
        self.assertEqual(len(self.client.get("/accounts").get_json()), 1)
        self.assertEqual(self.client.get(f"/accounts/{account_id}").status_code, 200)
        updated = self.client.put(f"/accounts/{account_id}", json={"name": "Jane"})
        self.assertEqual(updated.get_json()["name"], "Jane")
        self.assertEqual(self.client.delete(f"/accounts/{account_id}").status_code, 204)
        self.assertEqual(self.client.get(f"/accounts/{account_id}").status_code, 404)

    def test_validation_conflict_and_missing(self):
        self.assertEqual(self.client.post("/accounts", json={}).status_code, 400)
        self.create()
        self.assertEqual(self.create().status_code, 409)
        self.assertEqual(self.client.put("/accounts/999", json={"name": "x"}).status_code, 404)
        self.assertEqual(self.client.delete("/accounts/999").status_code, 404)
        self.assertEqual(self.client.put("/accounts/1", json={"name": ""}).status_code, 400)
