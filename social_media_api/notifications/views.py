from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Notification

# Create your views here.
class NotificationListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        notifications = Notification.objects.filter(recipient=request.user).order_by('-created_at')
        unread_notifications = notifications.filter(read=False)
        data = [{"verb": notif.verb, "created_at": notif.created_at} for notif in unread_notifications]

        return Response(data, status=status.HTTP_200_OK)
    
class MarkNotificationReadView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, notification_id):
        try:
            notification = Notification.objects.get(id=notification_id, recipient=request.user)
            notification.read = True
            notification.save()
            return Response({"detail": "Notification marked as read"}, status=status.HTTP_200_OK)

        except Notification.DoesNotExist:
            return Response({"detail": "Notification Not Found"}, status=status.HTTP_404_NOT_FOUND)