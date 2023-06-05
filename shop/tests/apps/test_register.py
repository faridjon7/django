import pytest
from django.contrib.auth.models import User
from django.test.client import Client


@pytest.mark.django_db
class TestRegister:
    def setup_method(self):
        self.client = Client()

    def test_register_and_login(self):
        response = self.client.get("/register/")
        assert response.status_code == 200

        response = self.client.post(
            "/register/",
            data={
                "first_name": "Test",
                "last_name": "Test",
                "email": "test@test.com",
                "password": "test@test.com",
            },
            follow=True,
        )
        assert response.status_code == 200
        assert User.objects.exists()

        response = self.client.post(
            "/login/",
            data={
                "email": "test@test.com",
                "password": "test@test.com",
            },
            follow=True,
        )
        assert response.status_code == 200
