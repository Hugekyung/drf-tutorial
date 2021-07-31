from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views_fbv, views_cbv


urlpatterns = [
    path('snippets/', views_cbv.SnippetList.as_view()),
    path('snippets/<int:pk>/', views_cbv.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)