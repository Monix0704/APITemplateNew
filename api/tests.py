from rest_framework.test import APITestCase


class HealthCheckTests(APITestCase):
    def test_api_root_returns_success(self):
        response = self.client.get("/api/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "API is working", "status": "success"})
