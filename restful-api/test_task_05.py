#!/usr/bin/python3
"""
Module Name: test_task_05.

Contains unittest tests for the RESTful API created using Flask for
task_05 of RESTfulAPI project.
"""

import unittest
import requests
import time

BASE_URL = "http://localhost:5000"

class TestFlaskAPI(unittest.TestCase):

    def setUp(self):
        self.user1 = {"username": "user1", "password": "password"}
        self.admin1 = {"username": "admin1", "password": "password"}
        self.token_user = self.get_token(self.user1["username"], self.user1["password"])
        self.token_admin = self.get_token(self.admin1["username"], self.admin1["password"])

    def get_token(self, username, password):
        res = requests.post(f"{BASE_URL}/login", json={"username": username, "password": password})
        self.assertEqual(res.status_code, 200)
        return res.json()["access_token"]

    def test_root_route(self):
        res = requests.get(f"{BASE_URL}/")
        self.assertEqual(res.status_code, 200)
        self.assertIn("Unrequired Homepage", res.text)

    def test_basic_auth_success(self):
        res = requests.get(f"{BASE_URL}/basic-protected", auth=(self.user1["username"], self.user1["password"]))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.text, "Basic Auth: Access Granted")
    
    def test_basic_auth_failure(self):
        res = requests.get(f"{BASE_URL}/basic-protected", auth=(self.user1["username"], "wrong_password"))
        self.assertEqual(res.status_code, 401)
        self.assertEqual(res.text, "Unauthorized Access")

    def test_jwt_protected_with_token(self):
        headers = {"Authorization": f"Bearer {self.token_user}"}
        res = requests.get(f"{BASE_URL}/jwt-protected", headers=headers)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.text, "JWT Auth: Access Granted")

    def test_jwt_protected_without_token(self):
        res = requests.get(f"{BASE_URL}/jwt-protected")
        self.assertEqual(res.status_code, 401)
        self.assertEqual(res.json().get("error"), "Missing or invalid token")

    def test_admin_only_access(self):
        headers_user = {"Authorization": f"Bearer {self.token_user}"}
        res_user = requests.get(f"{BASE_URL}/admin-only", headers=headers_user)
        self.assertEqual(res_user.status_code, 403)
        self.assertIn("Admin access required", res_user.text)

        headers_admin = {"Authorization": f"Bearer {self.token_admin}"}
        res_admin = requests.get(f"{BASE_URL}/admin-only", headers=headers_admin)
        self.assertEqual(res_admin.status_code, 200)
        self.assertIn("Admin Access: Granted", res_admin.text)

    def test_invalid_login(self):
        res = requests.post(f"{BASE_URL}/login", json={"username": "bad", "password": "bad"})
        self.assertEqual(res.status_code, 401)
        self.assertIn("no token for you", res.text)

    def test_token_structure(self):
        token = self.get_token(self.user1["username"], self.user1["password"])
        self.assertTrue(isinstance(token, str))
        self.assertGreater(len(token.split(".")), 2)  # Should be in JWT format

    def test_missing_fields_in_login(self):
        res = requests.post(f"{BASE_URL}/login", json={"username": "user1"})
        self.assertEqual(res.status_code, 401)

    def test_post_login_no_json(self):
        res = requests.post(f"{BASE_URL}/login", data="not json")
        self.assertEqual(res.status_code, 400)  # should fail gracefully if server checks content type

if __name__ == "__main__":
    unittest.main()
