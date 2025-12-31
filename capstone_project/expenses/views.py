from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .models import Expense
from .serializers import ExpenseSerializer
from django.db.models import Sum
from rest_framework.decorators import action
from rest_framework.response import Response


class ExpenseListCreateView(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class ExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        queryset = Expense.objects.filter(user=self.request.user)

        category = self.request.query_params.get('category')
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')

        if category:
            queryset = queryset.filter(category=category)

        if start_date and end_date:
            queryset = queryset.filter(date__range=[start_date, end_date])

        return queryset
    
    @action(detail=False, methods=['get'])
    def summary(self, request):
        expenses = Expense.objects.filter(user=request.user)

        total = expenses.aggregate(total_spent=Sum('amount'))['total_spent'] or 0

        return Response({
        'total_spent': total
    })