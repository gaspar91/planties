from . import views
from django.urls import path

urlpatterns = [
    path('', views.posts, name='posts'),
    # path('<slug:slug>/', views.post_detail, name='post_detail'),
]