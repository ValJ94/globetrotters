from django.shortcuts import render, redirect
# from django.urls import reverse
from .models import ForumPost, PostReply
from .forms import ForumPostForm, PostReplyForm
from django.contrib.auth.decorators import login_required
from django.views import View
from django.utils.decorators import method_decorator




def forum(request):
    post_list = ForumPost.objects.all().values().order_by('-timestamp')

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

    post_replies = PostReply.objects.filter(post__id__contains=id)

    context_dict = {'post_replies': post_replies, 'post': post}
    return render(request, 'forum_templates/view_post.html', context_dict)


def reply_view(request, id=-1):
    
    if request.method == 'POST':
        form = PostReplyForm(request.POST)
        post = ForumPost.objects.get(id=id)
        if form.is_valid():
            if post:
                reply = form.save(commit=False)
                reply.reply_writer = request.user
                reply.post = post
                reply.save()
            return redirect('forum_app:view_post', id=id)
        else:
            print(form.errors)  
    elif  request.method == 'GET':
        if id==-1:
            # This will handle the case where the URL doesn't contain id
            pass
        else:
            post = ForumPost.objects.filter(id=id)
            # post = ForumPost.objects.get(id=id)
            form = PostReplyForm()
            context_dict = {'form': form, 'post': post, 'post_id': post[0].id}
            return render(request, 'forum_templates/add_reply.html', context_dict)


