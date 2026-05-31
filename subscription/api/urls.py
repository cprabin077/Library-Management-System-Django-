from subscription.api.views import SubscriptionView

from django.urls import path
urlpatterns = [
    path('', SubscriptionView.as_view(), name = "subscription" ),

]
