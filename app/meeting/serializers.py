from rest_framework import serializers

from app.core.models import Meeting
from app.users.serializers import UserDisplaySerializer

class MeetingCreateSerializer(serializers.ModelSerializer):
    """ Serializer: Meeting Create """

    class Meta:
        model = Meeting
        fields = ('pk', 'user', 'meeting_type', 'start_time', 'end_time', 'timezone', 'notification_interval')


class MeetingDisplaySerializer(serializers.ModelSerializer):
    """ Serializer: Meeting Display """

    user = UserDisplaySerializer()

    class Meta:
        model = Meeting
        fields = ('pk', 'user', 'meeting_type', 'start_time', 'end_time', 'timezone', 'notification_interval')

