from django.shortcuts import render, redirect
from requests import Response
from forum.models import ForumPost
from .forms import *
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
import datetime

# Create your views here.
@csrf_exempt
def get_forum_list(request):
    list_post = ForumPost.objects.all().order_by('-date_created')

    ret = []
    for posts in list_post:
        temp = {
            "pk": posts.pk,
            "author": posts.author,
            "topic": posts.topic,
            "description":posts.description,
            "date_created":posts.date_created.date(),
        }
        ret.append(temp)

    data = json.dumps(ret, default=str)
    return HttpResponse(data, content_type='application/json')

@csrf_exempt
def get_comment_list(request, id):
    forumPost = ForumPost.objects.get(pk=id)
    comments = Comment.objects.all().filter(parentForum=forumPost)
    ret = []
    for comment in comments:
        temp = {
            "pk": comment.pk,
            "author": comment.author,
            "parentForum": comment.parentForum,
            "description": comment.description
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

        new_forum = ForumPost.objects.create(
            topic=topic,
            description=description,
            date_created=datetime.date.today(),
            author=request.user,
        )
        result = {
            'pk':new_forum.pk,
            'author':new_forum.author.username,
            'topic':new_forum.topic,
            'description':new_forum.description,
            'date_created':new_forum.date_created    
        }
        return JsonResponse(result, status=200)
    return render(request, "forumHome.html")


@login_required(login_url='/authentications/login')
@csrf_exempt
def create_comment_ajax(request, id):
    forumPost = ForumPost.objects.get(pk=id)
    if request.method == "POST":
        description = request.POST.get("description")

        new_comment = Comment.objects.create(
            parentForum=forumPost,
            description=description,
            date_created=datetime.date.today(),
            author=request.user,
        )
        result = {
            'pk':new_comment.pk,
            'author':new_comment.author.username,
            'description':new_comment.description,
            'date_created':new_comment.date_created    
        }
        return JsonResponse(result, status=200)
    return render(request, "forumHome.html")

def index(request):
    forumPost = ForumPost.objects.all().order_by('-date_created')
    response = {'forumPost': forumPost}
    return render(request, 'forumHome.html', response)

@login_required(login_url='/authentications/login')
@csrf_exempt
def post_to_forum(request):
    form = ForumForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('/forum/')
    
    context = dict()
    context["form"] = form
    return render(request, "postToForum.html", context)

# TODO: Implement function that will view individual post
def forum_post_detail(request, id):

    forumPost = ForumPost.objects.get(pk=id)
    comments = Comment.objects.all().filter(parentForum=forumPost)
    if (len(comments) == 0):
        dummy = Comment()
        dummy.description = "Belum ada komentar"
        # dummy.author = ""
        comments = [dummy]
    if request.method == 'POST' and request.is_ajax():
        description = request.POST.get('description')

        response_data = {'description':description, 'author': request.user.get_username()}

        tmp = Comment(author=request.user,description=description, parentForum=forumPost)
        tmp.save()

        return JsonResponse(response_data)
    return render(request, 'forumDetail.html', {'forumPost':forumPost, 'comments':comments})

@login_required(login_url ='/authentications/login/')
def post_comment(request, id):
    form = CommentForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.parentForum = ForumPost.objects.get(id=id)
            instance.save()
            return redirect('/forum/' + id)
    
    context = dict()
    context["form"] = form
    return render(request, "postComment.html", context)
