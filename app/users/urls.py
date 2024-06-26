from django.urls import path
from app.users.views import (
    BookedMeeting,
    UserCreate,
    UserList,
    UserUpdate,
)

urlpatterns = [
    path('', UserCreate.as_view(), name='user-create'),
    path('<int:pk>/', UserUpdate.as_view(), name='user-update'),
    path('list/', UserList.as_view(), name='user-list'),

    path('booked-meetings/', BookedMeeting.as_view(), name='booked-meetings'),
]