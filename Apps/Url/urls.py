from django.urls import path, include
from . import views



app_name = 'Url'

urlpatterns = [

    path('create/', views.CreateUrlView.as_view(template_name='Url/Create.html'), name='Create'),

    path('<int:Url_id>/', views.UrlView.as_view(template_name='Url/Url.html'), name='Url'),

    path('', views.UrlsView.as_view(template_name='Url/Home.html'), name='Home'),

    path('<slug:Short_Url>/', views.RedirectUrlView.as_view(), name='Redirect'),
]
