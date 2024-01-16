from tokenize import Comment

from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from salonapp.models import Auto
from visit.models import Visit
from .serializers import UserSerializer, AuthTokenSerializer, AutoSerializer, VisitSerializer, OpinionSerializer
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse

class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""

    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):

        send_mail(
            'NOWY USER',
            render_to_string('plik.txt'),
            'salon.app.com.pl',
            ['email.pl'],
            fail_silently=False,
        )

        return super(CreateUserView, self).post(request, *args, **kwargs)

class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""

    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""

    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

    def get_object(self):
        """Retrieve and return authenticated user"""

        return self.request.user

class AutoListAPIView(generics.ListAPIView):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer

class VisitListAPIView(generics.ListAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer

class ObtainAuthToken(APIView):
    """Obtain an authentication token"""

    def post(self, request, *args, **kwargs):
        serializer = AuthTokenSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

class OpinionListAPIView(generics.ListAPIView):
    queryset = Visit.objects.all()
    serializer_class = OpinionSerializer

