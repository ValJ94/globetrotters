from django.shortcuts import render, redirect
from django.urls import reverse
from .models import ForumPost, PostReply
from .forms import ForumPostForm, PostReplyForm
from django.contrib.auth.decorators import login_required



def forum(request):
    post_list = ForumPost.objects.all().values()

    context_dict = {'post_list': post_list}
    return render(request, 'forum_templates/forum.html', context_dict)


@login_required
def add_post(request):
    form = ForumPostForm()
    
    if request.method == 'POST':
        form = ForumPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.writer = request.user
            post.save()
            return redirect('forum_app:forum')
        else:
            print(form.errors)  
    else:
        # user = request.user
        form = ForumPostForm()

    context_dict = {'form': form}
    return render(request, 'forum_templates/add_post.html', context_dict)


def view_post(request, id):
    post = ForumPost.objects.get(id=id)
    form = PostReplyForm()
    
    if request.method == 'POST':
        form = PostReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.writer = request.user
            reply.save()
            return redirect('forum_app/{{ post.id }}/')
        else:
            print(form.errors)  
    else:
        # user = request.user
        form = PostReplyForm()


    post_replies = PostReply.objects.filter(post__id__contains=id)

    # context_dict = {'post': post, 'form': form}
    context_dict = {'post_replies': post_replies, 'post': post, 'form': form}
    return render(request, 'forum_templates/view_post.html', context_dict)


@login_required
def add_reply(request):
    form = PostReplyForm()
    
    if request.method == 'POST':
        form = PostReplyForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.writer = request.user
            post.save()
            return redirect('forum_app/{{ post.id }}/')
        else:
            print(form.errors)  
    else:
        # user = request.user
        form = PostReplyForm()

    context_dict = {'form': form}
    return render(request, 'forum_templates/view_post.html', context_dict)