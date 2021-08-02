""" 2. Class-Based Views 
- 기본적인 구현 내용은 FBV와 동일
- 확장성과 재사용성이 높아 활용성 높음
- 다중상속, Mixin 가능
- (단점)읽기 상속과 Mixin 코드에 대한 이해가 필요하다. 복잠. """

from snippets.serializers import SnippetSerializer
from snippets.permissions import IsOwnerOrReadOnly
from snippets.models import Snippet
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

# APIView 클래스를 상속받는다.
class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # django 버전문제로 튜토리얼대로 수행하면 오류가 발생한다.
    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user) # snippet를 생성한 user 정보를 model의 owner 필드로 저장한다. snippets-user의 연동


class SnippetDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)