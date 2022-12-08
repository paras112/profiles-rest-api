from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):

    def get(self,request,format=None):

        an_apiView = [
            'Uses HTTP methods as function(get,post,patch,put,delete)',
            'Is similar to a teadational django view',
            'gives you the most control over you application logic',
            'is mapped manually to URLs'
        ]
        return Response({'message': 'Hello!','an_apiview':an_apiView})
