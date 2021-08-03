""" Authentication & permissions를 위한 views """

from rest_framework import renderers
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from snippets.serializers import SnippetSerializer
from snippets.models import Snippet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SnippetList(APIView):
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        # 추가된 부분 context
        serializer = SnippetSerializer(snippets, many=True, context={'request': request})
        return Response(serializer.data)

	
class SnippetDetail(APIView):
    def get(self, request, pk ,format=None):
        snippet = self.get_object(pk)
        # 추가된 부분 context
        serializer = SnippetSerializer(snippet, context={'request': request})
        return Response(serializer.data)


class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format), # user-list view 반환
        'snippets': reverse('snippet-list', request=request, format=format) # snippet_list view 반환
    })