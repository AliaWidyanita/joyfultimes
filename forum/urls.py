from django.urls import path
from .views import *

app_name = 'forum'

urlpatterns = [
    path('', index, name='Forum'),
    path('postToForum/',post_to_forum,name='postToForum'),
    path('detail/<int:id>/', forum_post_detail, name="detail"),
    path('api/ForumHome/', get_forum_list, name="getForumList"),
    path('api/addForum/', create_post_ajax, name="addNewForum"),
    path('api/comment/<int:id>/', get_comment_list, name="getCommentList"),
    path('api/addComment/<int:id>', create_comment_ajax, name="addNewComment")
]