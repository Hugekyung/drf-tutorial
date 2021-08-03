from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from snippets import views, views_viewset


# urlpatterns = [
#     path('', views.api_root),
#     path('snippets/', views.SnippetList.as_view(), name='snippet-list'),
#     path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
#     path('users/', views.UserList.as_view(), name='user-list'),
#     path('users/<int:pk>', views.UserDetail.as_view(), name='user-detail'),
#     path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)

""" ViewSet을 Url과 연동하기 
    - ViewSet 자체는 반복적인 코드를 최소화시킬 수 있다
    - 일정한 방식으로 URL을 설정하기 때문에 URL 연동에 크게 신경쓸 필요 없이 API 로직에 집중할 수 있다
    - 하지만 굉장히 추상화되어 있고, 항상 옳은 접근만을 하는 것은 아니다
    - 보다 명시적인 방식이 필요하다면 ViewSet을 활용하는 것보다는 View를 개별적으로 구축하는 것이 좋다
"""
# snippet_list = views_viewset.SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# snippet_detail = views_viewset.SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# snippet_highlight = views_viewset.SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = views_viewset.UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = views_viewset.UserViewSet.as_view({
#     'get': 'retrieve'
# })


# urlpatterns = format_suffix_patterns([
#     path('', views_viewset.api_root),
#     path('snippets/', snippet_list, name='snippet-list'),
#     path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
#     path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
#     path('users/', user_list, name='user-list'),
#     path('users/<int:pk>/', user_detail, name='user-detail')
# ])


""" Routers 활용한 ViewSet 연동 방법 """
# router를 생성하고 viewset을 등록한다
router = DefaultRouter()
router.register(r'snippets', views_viewset.SnippetViewSet)
router.register(r'users', views_viewset.UserViewSet)

# API URL은 router에 의해 자동적으로 결정되어진다
# DefaultRouter 클래스는 자동으로 API root view를 생성하므로 이제 view 모듈에서 api_root 메서드를 제거할 수 있다.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]