from subscription.api.views import SubscriptionUpdateAndDelete, SubscriptionView

from django.urls import path
urlpatterns = [
    path('', SubscriptionView.as_view(), name = "subscription" ),
    path('<int:pk>', SubscriptionUpdateAndDelete.as_view(), name = 'subscription-update'),
]
