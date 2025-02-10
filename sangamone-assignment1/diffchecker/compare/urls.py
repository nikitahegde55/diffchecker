from django.urls import path
from .views import compare_view

urlpatterns = [
    path('', compare_view, name='compare'),  # This makes "/" load compare.html
]

from django.urls import path
from .views import feedback_view

urlpatterns = [
    path("feedback/", feedback_view, name="feedback"),  # URL for feedback page
]
