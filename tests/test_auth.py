from http import HTTPStatus


class TestAuthAPI:

    def test_auth(self, client):
        """Тест существования эндпоинта аутентификации."""
        url = '/api/v1/api-token-auth/'
        response = client.post(url, data={})

        assert response.status_code != HTTPStatus.NOT_FOUND, (
            f'Страница `{url}` не найдена, проверьте этот адрес в *urls.py*.'
        )

    def test_auth_with_invalid_data(self, client):
        """Тест аутентификации с некорректными данными."""
        url = '/api/v1/api-token-auth/'
        response = client.post(url, data={})

        assert response.status_code == HTTPStatus.BAD_REQUEST, (
            f'Проверьте, что POST-запрос к `{url}` с некорректными данными '
            'возвращает ответ со статусом 400.'
        )
