from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>', views.detail, name='detail'),
    path('download/<int:file_id>', views.download_file, name='download_file')
]
