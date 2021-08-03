""" Authentication & permissions를 위한 views """

from rest_framework import renderers
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view, action
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import generics
from snippets.serializers import SnippetSerializer
from snippets.models import Snippet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from snippets.permissions import IsOwnerOrReadOnly


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ReadOnlyModleViewSet은 'read-only' 제공
    이 viewset은 `list` 와 `retrieve` 액션을 자동으로 제공한다
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    """
    이 viewset은 `list`, `create`, `retrive`, `update`, `destroy`
    액션을 자동으로 제공한다
    
    추가적으로 highlight 액션만 따로 적어주었다
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format), # user-list view 반환
        'snippets': reverse('snippet-list', request=request, format=format) # snippet_list view 반환
    })