from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('processes/', views.ProcessListView.as_view(), name='processes'),
    path('processes/<int:pk>', views.ProcessDetailView.as_view(), name='process-detail'),
]
