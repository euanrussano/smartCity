from django.urls import path

from .views import AccountAPIListView, AccountAPIDetailView, TransactionAPIListView, TransactionAPIDetailView

urlpatterns = [
    path('accounts/',AccountAPIListView.as_view()),
    path('accounts/<int:pk>/',AccountAPIDetailView.as_view()),
    path('transactions/',TransactionAPIListView.as_view()),
    path('transactions/<int:pk>/',TransactionAPIDetailView.as_view()),
]
