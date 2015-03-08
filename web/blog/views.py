from django.shortcuts import render
from django.views.decorators.http import *
from .models import *
from constance import config
import os


@require_GET
def post_list(request):
    context = {'post_list': Post.objects.all()}
    return render(request, 'post_list.html', context)

@require_GET
def sync_posts(request):
    context = {}
    Tag.objects.all().delete()
    Post.objects.all().delete()
    context['post_folders'] = subdirectories(config.POSTS_DIR)
    context['posts'] = []
    for post_folder in context['post_folders']:
        post = Post.objects.create()
        context['posts'].append(post)
        post.slug = os.path.basename(post_folder)
        meta_populator(post, post_folder)
        post.save()

    return render(request, 'sync_posts.html', context)


def subdirectories(parent):
    return [
        os.path.join(parent, name)
        for name in os.listdir(parent)
        if os.path.isdir(os.path.join(parent, name))
    ]


def meta_populator(post, post_folder):
    meta_file = open(post_folder + "/meta.txt", "r")
    lines = meta_file.readlines()
    tags = lines[0].split(' ')
    tag_models = [
    ]
    for t in tags:
        tag_model = Tag.objects.get_or_create(name=t)[0]
        tag_model.save()
        tag_models.append(tag_model)

    for tm in tag_models:
        post.tags.add(tm)
    meta_file.close()
