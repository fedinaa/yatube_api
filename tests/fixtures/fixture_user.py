import pytest
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token


@pytest.fixture
def user(django_user_model):
    return django_user_model.objects.create_user(
        username="TestUser", password="1234567"
    )


@pytest.fixture
def user_2(django_user_model):
    return django_user_model.objects.create_user(
        username="TestUser2", password="1234567"
    )


@pytest.fixture
def another_user(django_user_model):
    return django_user_model.objects.create_user(
        username="TestUserAnother", password="1234567"
    )


@pytest.fixture
def token(user):
    token, created = Token.objects.get_or_create(user=user)
    return token


@pytest.fixture
def user_client(token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
    return client


@pytest.fixture
def token_2(user_2):
    token, created = Token.objects.get_or_create(user=user_2)
    return token


@pytest.fixture
def user_client_2(token_2):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Token {token_2.key}')
    return client


@pytest.fixture
def client():
    return APIClient()