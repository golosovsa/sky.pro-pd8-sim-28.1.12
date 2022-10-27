# TODO настраиваем urls здесь
from django.urls import path
from discounts import views

urlpatterns = [
    path("", views.DiscountListView.as_view(), name="discount-list"),
    path("<int:pk>/", views.DiscountDetailView.as_view(), name="discount-detail"),
]
