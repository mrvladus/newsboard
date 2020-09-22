from math import ceil
import json

from django.shortcuts import render, redirect
from django.http import JsonResponse

from .services import get_posts, get_comments, publish_comment, delete_comment, delete_post, get_post
from .models import Comment

# ------------------------ ГЛАВНАЯ СТРАНИЦА --------------------------------


def index(request):
    return redirect('home', page=1, counter=0)


def home(request, page, counter):
    # Количество постов на странице
    posts_on_page = 3
    # Получение нужных постов из базы
    posts, number_of_posts = get_posts(counter, posts_on_page)
    # Кол-во страниц
    pages = ceil(number_of_posts / posts_on_page)
    # Проверка для показа кнопок НАЗАД и ВПЕРЕД
    next_counter = counter + posts_on_page
    next_page = page + 1
    if page == 1:
        prev_page = page
        prev_counter = counter
    else:
        prev_page = page - 1
        prev_counter = counter - posts_on_page
    # Передаваемые переменные в шаблон
    context = {'posts': posts, 'page': page, 'next_page': next_page, 'prev_page': prev_page,
               'counter': counter, 'next_counter': next_counter, 'prev_counter': prev_counter,
               'pages': pages}
    return render(request, 'news/home.html', context=context)

# ------------------------ КОММЕНТАРИИ --------------------------------


def show_comments(request, post_id):  # Рендер страницы комментариев
    # Загрузка поста
    post = get_post(post_id)
    context = {'post_id': post_id, 'post': post}
    return render(request, 'news/comments.html', context=context)

# ------ API ------


def comments(request, post_id):  # Получение комментариев
    comments = list(get_comments(post_id))
    return JsonResponse(comments, safe=False)


def add_comment(request, post_id):  # Добавление комментария
    if request.method == 'POST':
        # Загрузка JSON
        comment_text = json.loads(request.body.decode())
        # Добавление в базу
        publish_comment(post_id, comment_text)
        return JsonResponse({'comment': 'added'})


def del_comment(request, post_id, comment_id):  # Удаление комментария
    delete_comment(comment_id)
    return JsonResponse({'deleted': 'ok'})


def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm()
        context = {'form': form}
        return render(request, 'news/newpost.html', context=context)


def del_post(request, post_id, page, counter):
    delete_post(post_id)
    return redirect('home', page=page, counter=counter)
