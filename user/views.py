from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.authentication import TokenAuthentication
from airport.permissions import IsAdminOrIfAuthenticatedReadOnly

from user.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
   serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
   renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class ManageUserView(generics.RetrieveUpdateAPIView):
   serializer_class = UserSerializer
   authentication_classes = (TokenAuthentication,)
   permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)

   def get_object(self):
       return self.request.user
