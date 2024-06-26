from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, ListAPIView

from app.core.models import User
from app.meeting.serializers import MeetingCreateSerializer

# Create your views here.
class MeetingCreate(GenericAPIView):
    """ View: Create Meeting """

    def post(self, request):

        serializer = MeetingCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

