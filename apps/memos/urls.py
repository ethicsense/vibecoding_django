from django.urls import path
from .views import (
    MemoListView, MemoDetailView, MemoCreateView,
    MemoUpdateView, MemoDeleteView
)

app_name = 'memos'

urlpatterns = [
    path('', MemoListView.as_view(), name='list'),
    path('create/', MemoCreateView.as_view(), name='create'),
    path('<int:pk>/', MemoDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', MemoUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', MemoDeleteView.as_view(), name='delete'),
]
