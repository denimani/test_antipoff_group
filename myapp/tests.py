from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from myapp.models import CadastralQuery


class CadastralQueryTestCase(APITestCase):
    def setUp(self):
        self.maxDiff = None
        self.cadastral_query = CadastralQuery.objects.create(
            cadastral_number='9g785h4',
            latitude=27.3456,
            longitude=91.2893
        )

    def test_cadastral_query_create(self):
        """
        Тест на создание запроса в базу данных
        """
        response = self.client.post(reverse('myapp:query'), {'cadastral_number': '128eq1',
                                                             'latitude': 11.1235,
                                                             'longitude': 87.8973})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cadastral_query_history(self):
        """
        Тест на получение истории запросов
        """
        response = self.client.get(reverse('myapp:history'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cadastral_query_by_cadastral_number(self):
        """
        Тест на получение запроса по кадастровому номеру
        """
        response = self.client.get(
            reverse('myapp:history_by_cadastral'),
            {'cadastral_number': self.cadastral_query.cadastral_number}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cadastral_query_by_invalid_cadastral_number(self):
        """
        Тест на получение запроса по несуществующему кадастровому номеру
        """
        response = self.client.get(
            reverse('myapp:history_by_cadastral'),
            {'cadastral_number': 'invalid_number'}
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_cadastral_query_by_missing_cadastral_number(self):
        """
        Тест на отсутствие кадастрового номера в запросе
        """
        response = self.client.get(reverse('myapp:history_by_cadastral'))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_cadastral_query_ping(self):
        """
        Тест на проверку соединения с внешним сервером
        """
        response = self.client.get(reverse('myapp:ping'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
