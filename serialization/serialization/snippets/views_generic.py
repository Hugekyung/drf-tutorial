""" genteric class-based views 
- drf에서 제공하는 generics는 이미 FBV나 CBV, Mixin에서 등장했던
각종 기능이 포함된 클래스들을 다중상속했다
- ListCreateAPIView와 RetrieveUpdateDestroyAPIView의 클래스 이름에서도
알 수 있듯이, 앞서 구현했던 list, create, retrieve, update, destroy까지
모든 기능을 다 가지고 있다.
- 이를 활용하면 기본적인 기능을 가진 api를 생성할 때 아주 쉽고 빠르게
구현할 수 있다."""

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer