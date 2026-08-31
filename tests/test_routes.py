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

    def test_it_should_return_a_cors_header(self):
        response = self.client.get("/", headers={"Origin": "https://coursera.org"})
        self.assertEqual(response.headers["Access-Control-Allow-Origin"], "https://coursera.org")

    def test_it_should_return_security_headers(self):
        response = self.client.get("/")
        self.assertEqual(response.headers["X-Content-Type-Options"], "nosniff")
        self.assertEqual(response.headers["X-Frame-Options"], "SAMEORIGIN")

    def test_root_returns_name_and_version(self):
        self.assertEqual(self.client.get("/").get_json(),
                         {"name": "Account REST API Service", "version": "1.0"})

    def test_list_is_initially_empty(self):
        self.assertEqual(self.client.get("/accounts").get_json(), [])

    def test_create_returns_json(self):
        self.assertEqual(self.create().content_type, "application/json")

    def test_create_assigns_id(self):
        self.assertEqual(self.create().get_json()["id"], 1)

    def test_create_preserves_address(self):
        self.assertEqual(self.create().get_json()["address"], "Astana")

    def test_create_preserves_phone_number(self):
        self.assertEqual(self.create().get_json()["phone_number"], "+77000000000")

    def test_create_adds_date_joined(self):
        self.assertIn("date_joined", self.create().get_json())

    def test_read_returns_created_email(self):
        self.create()
        self.assertEqual(self.client.get("/accounts/1").get_json()["email"], "john@example.com")

    def test_update_email(self):
        self.create()
        result = self.client.put("/accounts/1", json={"email": "new@example.com"})
        self.assertEqual(result.get_json()["email"], "new@example.com")

    def test_update_rejects_empty_email(self):
        self.create()
        self.assertEqual(self.client.put("/accounts/1", json={"email": ""}).status_code, 400)

    def test_duplicate_email_returns_conflict(self):
        self.create()
        self.assertEqual(self.create().status_code, 409)

    def test_delete_removes_account_from_list(self):
        self.create()
        self.client.delete("/accounts/1")
        self.assertEqual(self.client.get("/accounts").get_json(), [])

    def test_health_returns_ok(self):
        self.assertEqual(self.client.get("/health").get_json()["status"], "OK")

    def test_missing_read_returns_json_error(self):
        self.assertEqual(self.client.get("/accounts/99").get_json()["error"], "account not found")

    def test_missing_delete_returns_json_error(self):
        self.assertEqual(self.client.delete("/accounts/99").get_json()["error"], "account not found")

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
