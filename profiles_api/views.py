from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from rest_framework import filters

from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profiles_api import serializers
from profiles_api import models

from profiles_api import permissions

# Create your views here.

class HelloApiView(APIView):
    serializer_class =  serializers.HelloSerializer

    def get(self,request,format=None):

        an_apiView = [
            'Uses HTTP methods as function(get,post,patch,put,delete)',
            'Is similar to a teadational django view',
            'gives you the most control over you application logic',
            'is mapped manually to URLs'
        ]
        return Response({'message': 'Hello!','an_apiview':an_apiView})

    def post(self,request):

        serializer = self.serializer_class(data = request.data)
        if(serializer.is_valid()):
            name = serializer.validated_data.get("name")
            message = f'hello {name}'
            return(Response({'message':message}))
        else:
            return(Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)
                )


class HelloViewSet(viewsets.ViewSet):
    serializer_class =  serializers.HelloSerializer
    def list(self,request):

        a_viewset = [
            'Uses actions (list,create,retrieve,update,partial_update)',
            'Automatically maps to urls using routers',
            'provide more functionality with more code'
        ]
        return(Response({'message':'Hello','a_viewset':a_viewset}))

    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if(serializer.is_valid()):
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return(Response({'message':message}))
        else:
            return(Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST))

    def retrieve(self,request,pk = None):
        return(Response({'method':'get'}))

    def update(self,request,pk=None):
        return(Response({'method':'put'}))

    def partial_update(self,request,pk=None):
        return(Response({'method':'patch'}))
 
    def destroy(self,request,pk=None):
        return(Response({'method':'delete'}))


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class =serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES