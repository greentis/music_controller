from django.urls import path

from .views import RoomView

# generics.createAPIView.asView(): creates
urlpatterns = [
    path('home', RoomView.as_view()),
]
