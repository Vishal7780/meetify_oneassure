from django.urls import path
from app.meeting.views import MeetingCreate 

urlpatterns = [
    path('', MeetingCreate.as_view(), name='user-create'),
]