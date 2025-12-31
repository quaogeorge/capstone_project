from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExpenseViewSet
from .views import ExpenseListCreateView, ExpenseDetailView


router = DefaultRouter()
router.register(r'expenses', ExpenseViewSet, basename='expense')

urlpatterns = [
    path('', include(router.urls)),
    path('expenses/', ExpenseListCreateView.as_view()),
    path('expenses/<int:pk>/', ExpenseDetailView.as_view()),
]
