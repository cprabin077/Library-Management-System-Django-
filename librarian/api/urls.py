from django.urls import path

from librarian.api.views import LibrarianView


urlpatterns = [
    path('', LibrarianView.as_view(), name="librarian"),
]