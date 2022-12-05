from django.shortcuts import render, redirect, get_object_or_404
from requests import Response
from forum.models import ForumPost
from .forms import *
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
import datetime

@csrf_exempt
def flutter_forum(request):
    list_post = ForumPost.objects.all().order_by('-date_created')
    ret = []
    for posts in list_post:
        temp = {
            "pk": posts.pk,
            "author": posts.author.username,
            "topic": posts.topic,
            "description":posts.description,
            "date_created":posts.date_created.date(),
            "role":posts.role
        }
        ret.append(temp)

    data = json.dumps(ret, default=str)
    return HttpResponse(data, content_type='application/json')

@csrf_exempt
def flutter_comment(request, id):
    forumPost = ForumPost.objects.get(pk=id)
    comments = Comment.objects.all().filter(parentForum=forumPost).order_by('-date_created')
    ret = []
    for comment in comments:
        temp = {
            "pk": comment.pk,
            "author": comment.author,
            "parentForum": comment.parentForum.pk,
            "description": comment.description,
            "role": comment.role,
            "date_created": comment.date_created.date(),
        }
        ret.append(temp)
    data = json.dumps(ret, default=str)
    return HttpResponse(data, content_type='application/json')
    
# Create your views here.
@csrf_exempt
def get_forum_list(request):
    list_post = ForumPost.objects.all().order_by('-date_created')
    user = request.user.username
    ret = [user]
    for posts in list_post:
        temp = {
            "pk": posts.pk,
            "author": posts.author.username,
            "topic": posts.topic,
            "description":posts.description,
            "date_created":posts.date_created.date(),
            "role":posts.role
        }
        ret.append(temp)

    data = json.dumps(ret, default=str)
    return HttpResponse(data, content_type='application/json')

@csrf_exempt
def get_comment_list(request, id):
    forumPost = ForumPost.objects.get(pk=id)
    comments = Comment.objects.all().filter(parentForum=forumPost).order_by('-date_created')
    user = request.user.username
    ret = [user]
    for comment in comments:
        temp = {
            "pk": comment.pk,
            "author": comment.author,
            "parentForum": comment.parentForum,
            "description": comment.description,
            "role": comment.role,
            "date_created": comment.date_created.date(),
        }
        ret.append(temp)
    data = json.dumps(ret, default=str)
    return HttpResponse(data, content_type='application/json')

@login_required(login_url='/authentications/login')
@csrf_exempt
def create_post_ajax(request):
    if request.method == "POST":
        topic = request.POST.get("topic")
        description = request.POST.get("description")
        role=request.POST.get("role")

        new_forum = ForumPost.objects.create(
            topic=topic,
            description=description,
            date_created=datetime.date.today(),
            author=request.user,
            role=role
        )
        result = {
            'pk':new_forum.pk,
            'author':new_forum.author.username,
            'topic':new_forum.topic,
            'description':new_forum.description,
            'date_created':new_forum.date_created.date(),
            'role':new_forum.role    
        }
        return JsonResponse(result, status=200)
    return render(request, "forumHome.html")


@login_required(login_url='/authentications/login')
@csrf_exempt
def create_comment_ajax(request, id):
    forumPost = ForumPost.objects.get(pk=id)
    if request.method == "POST":
        description = request.POST.get("description")
        role = request.POST.get('role')
        new_comment = Comment.objects.create(
            parentForum=forumPost,
            description=description,
            date_created=datetime.date.today(),
            author=request.user,
            role=role
        )
        result = {
            'pk':new_comment.pk,
            'author':new_comment.author.username,
            'description':new_comment.description,
            'date_created':new_comment.date_created.date(),
            'role':new_comment.role  
        }
        return JsonResponse(result, status=200)
    return render(request, "forumHome.html")

def index(request):
    forumPost = ForumPost.objects.all().order_by('-date_created')
    response = {'forumPost': forumPost}
    return render(request, 'forumHome.html', response)

# TODO: Implement function that will view individual post
def forum_post_detail(request, id):

    forumPost = ForumPost.objects.get(pk=id)
   
    return render(request, 'forumDetail.html', {'forumPost':forumPost})



@login_required(login_url='/authentications/login')
@csrf_exempt
def delete_forum(request, id):
    if request.method == "DELETE":
        forum = get_object_or_404(ForumPost, id=id)
        forum.delete()
    return HttpResponse(status=202)

@login_required(login_url='/authentications/login')
@csrf_exempt
def delete_comment(request, id):
    if request.method == "DELETE":
        comment = get_object_or_404(Comment, id=id)
        comment.delete()
    return HttpResponse(status=202)