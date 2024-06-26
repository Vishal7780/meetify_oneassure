from rest_framework import serializers

from app.core.models import User

class UserCreateSerializer(serializers.ModelSerializer):
    """ Serializer: User Create """

    class Meta:
        model = User
        fields = ('pk', 'name', 'email', 'dnd_start_time', 'dnd_end_time', 'preferred_timezone')


class UserUpdateSerializer(serializers.ModelSerializer):
    """ Serializer: User Update """

    class Meta:
        model = User
        fields = ('pk', 'dnd_start_time', 'dnd_end_time', 'preferred_timezone')


class UserDisplaySerializer(serializers.ModelSerializer):
    """ Serializer: User Display """

    class Meta:
        model = User
        fields = ('pk', 'name', 'email', 'dnd_start_time', 'dnd_end_time', 'preferred_timezone')

