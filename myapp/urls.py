from django.urls import path

from myapp.apps import MyappConfig
from myapp.views import CadastralQueryViewSet

app_name = MyappConfig.name

urlpatterns = [
    path('query/', CadastralQueryViewSet.as_view({'post': 'query'}), name='query'),
    path('history/', CadastralQueryViewSet.as_view({'get': 'history'}), name='history'),
    path('history_by_cadastral/', CadastralQueryViewSet.as_view({'get': 'history_by_cadastral_number'}), name='history_by_cadastral'),
    path('ping/', CadastralQueryViewSet.as_view({'get': 'ping'}), name='ping'),
]
