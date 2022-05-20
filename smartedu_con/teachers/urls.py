from django.urls import path
from teachers.views import TeacherView


urlpatterns = [
    path('', TeacherView.as_view(), name='teachers'),
]