from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from django.urls import path, include


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('', views.api_root),
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)