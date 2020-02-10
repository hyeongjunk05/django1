from django.urls import path
from .views      import Comment
urlpatterns = [
    
    path('', Comment.as_view()),
    path('/comment', Comment.as_view()),
]