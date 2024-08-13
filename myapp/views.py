import random
import time
from datetime import datetime

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from myapp.models import CadastralQuery
from myapp.serializers import CadastralQuerySerializer


class CadastralQueryViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['post'])
    def query(self, request):
        """
        Создаем запрос в базу данных и возвращаем результат
        """
        # Сначала создаем запись с дефолтным значением для response
        query = CadastralQuery.objects.create(
            cadastral_number=request.data['cadastral_number'],
            latitude=request.data['latitude'],
            longitude=request.data['longitude'],
        )

        # time.sleep(random.randint(1, 60))  # cимуляция задержки до 60 секунд
        response = random.choice([True, False])  # эмуляция ответа внешнего сервера

        # Обновление записи с результатом
        query.response = response
        query.save()

        return Response({'response': response}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def history(self, request):
        """
        Возвращает историю запросов
        """
        queries = CadastralQuery.objects.all() # Получаем все записи
        serializer = CadastralQuerySerializer(queries, many=True)

        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def history_by_cadastral_number(self, request):
        """
        Возвращает историю запросов по кадастровому номеру
        """
        cadastral_number = request.query_params.get('cadastral_number', None) # Получаем кадастровый номер из параметров запроса

        # Проверяем, что кадастровый номер указан
        if cadastral_number is not None:
            # Проверяем, что кадастровый номер существует
            if not CadastralQuery.objects.filter(cadastral_number=cadastral_number).exists():
                return Response({"error": "Кадастровый номер не найден"}, status=status.HTTP_404_NOT_FOUND)

            # Если кадастровый номер существует в базе, возвращаем историю запросов
            queries = CadastralQuery.objects.filter(cadastral_number=cadastral_number)
            serializer = CadastralQuerySerializer(queries, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # Если кадастровый номер не указан, возвращаем ошибку
        return Response({"error": "Кадастровый номер не указан"}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def ping(self, request):
        """
        Проверка соединения с внешним сервером
        """
        return Response({"message": "pong"}, status=status.HTTP_200_OK)
