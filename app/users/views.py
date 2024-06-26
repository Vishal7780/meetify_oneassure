from django.shortcuts import render
import pytz
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from django.utils.dateparse import parse_datetime
from django.utils import timezone
from app.core.models import Meeting, User
from app.users.serializers import UserCreateSerializer, UserDisplaySerializer, UserUpdateSerializer

# Create your views here.
class UserCreate(GenericAPIView):
    """ View: Create User """

    def post(self, request):

        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserUpdate(GenericAPIView):
    """ View: Update User """

    def patch(self, request, pk):

        user = User.objects.get(pk=pk)

        serializer = UserUpdateSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserList(GenericAPIView):
    """ View: List User """

    def get(self, request):

        users = User.objects.all()

        serializer = UserDisplaySerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BookedMeeting(GenericAPIView):

    def get(self, request):
        
        user_id = request.query_params.get('user')
        start_time = request.query_params.get('start_time')
        end_time = request.query_params.get('end_time')
        
        if user_id and start_time and end_time:
            user = User.objects.get(pk=user_id)
            start_time = parse_datetime(start_time)
            end_time = parse_datetime(end_time)
            # print(start_time, end_time)
            meetings = Meeting.objects.filter(user=user, start_time__gte=start_time, end_time__lte=end_time).order_by('start_time')
            print(meetings)
            booked_meetings = []
            free_slots = []
            
            last_end_time = pytz.utc.localize(start_time)
            for meeting in meetings:
                booked_meetings.append({
                    "start_time": meeting.start_time,
                    "end_time": meeting.end_time,
                    "timezone": meeting.timezone,
                    "meeting_type": meeting.meeting_type,
                })
                if meeting.start_time > last_end_time:
                    free_slots.append({
                        "start_time": last_end_time,
                        "end_time": meeting.start_time,
                        "duration": (meeting.start_time - last_end_time).total_seconds() / 60
                    })
                    
                last_end_time = meeting.end_time
            end_time = pytz.utc.localize(end_time)
            if last_end_time < end_time:
                free_slots.append({
                    "start_time": last_end_time,
                    "end_time": end_time,
                    "duration": (end_time - last_end_time).total_seconds() / 60
                })
                
            data = {
                "booked_meetings": booked_meetings,
                "free_slots": free_slots,
            }
            
            return Response(data)
        
        return Response({"error": "Invalid parameters"}, status=400)