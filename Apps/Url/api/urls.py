from django.urls import path
from . import views


app_name = 'Url.api'

urlpatterns = [

    path('<int:Url_id>/', views.UrlAPI.as_view(), name='Url'),

    path('', views.UrlsAPI.as_view(), name='Urls'),
]
