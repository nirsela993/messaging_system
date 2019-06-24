from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response

from user_messages.models import Message
from user_messages.serializers import MessageSerializer
from users.models import User

str_to_bool = {"true": True, "false": False}


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()

    def list(self, request, *args, **kwargs):
        if "receiver" not in request.data:
            return Response("'receiver' parameter is missing",
                            status=status.HTTP_400_BAD_REQUEST)
        email = request.data["receiver"]
        user = get_object_or_404(User, email=email)

        if "unread" not in request.data:
            queryset = user.received_messages.all()
        else:
            if request.data["unread"] not in str_to_bool:
                return Response("'unread' parameter should be 'true' or 'false'",
                                status=status.HTTP_400_BAD_REQUEST)

            unread = str_to_bool[request.data["unread"]]
            queryset = user.received_messages.filter(unread=unread).all()

        serializer = MessageSerializer(queryset.select_related('receiver',
                                                               'sender'),
                                       many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        response = super(MessageViewSet, self).retrieve(request, *args,
                                                        **kwargs)
        Message.objects.get(pk=kwargs['pk']).read()
        return response
