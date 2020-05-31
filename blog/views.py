import json

from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Comment
from django.utils import timezone
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    page = request.GET.get('page', 1)

    paginator = Paginator(posts, 7)
    try:
        posts2 = paginator.page(page)
    except PageNotAnInteger:
        posts2 = paginator.page(1)
    except EmptyPage:
        posts2 = paginator.page(paginator.num_pages)
    return render(request, 'blog/post_list.html', {'posts': posts2})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        is_liked = True
    return render(request, 'blog/post_detail.html',
                  {'post': post, 'is_liked': is_liked, 'total_likes': post.total_likes(), })


def like_post(request):
    post = get_object_or_404(Post, id=request.POST.get('id'))
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True
    context = {
        'post': post,
        'is_liked': is_liked,
        'total_likes': post.total_likes(),
    }
    if request.is_ajax():
        html = render_to_string('blog/like_section.html', context, request=request)
        return JsonResponse({'form': html})
    # return redirect('post_detail', pk=post.pk)


def vote_comment(request):
    comment = get_object_or_404(Comment, id=request.POST.get('id'))
    mode = request.POST.get('mode')

    if mode == 'downvote':
        if comment.downvotes.filter(id=request.user.id).exists():
            comment.downvotes.remove(request.user)
        else:
            if comment.upvotes.filter(id=request.user.id).exists():
                comment.upvotes.remove(request.user)
            comment.downvotes.add(request.user)

    elif mode == 'upvote':
        if comment.upvotes.filter(id=request.user.id).exists():
            comment.upvotes.remove(request.user)
        else:
            if comment.downvotes.filter(id=request.user.id).exists():
                comment.downvotes.remove(request.user)
            comment.upvotes.add(request.user)

    context = {
        'post': comment.post
    }
    if request.is_ajax():
        html = render_to_string('blog/comment_section.html', context, request=request)
        return JsonResponse({'form': html})


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)


@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)
