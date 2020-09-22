from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:page>/<int:counter>/', views.home, name='home'),
    path('comments/<int:post_id>/', views.show_comments, name='show_comments'),
    path('del_post/<int:post_id>/<int:page>/<int:counter>/',
         views.del_post, name='del_post'),
    path('new_post/', views.new_post, name='new_post'),
    # --------------------------------- API --------------------------------
    path('api/comments/<int:post_id>/', views.comments, name='comments'),
    path('api/add_comment/<int:post_id>/',
         views.add_comment, name='add_comment'),
    path('api/del_comment/<int:post_id>/<int:comment_id>/',
         views.del_comment, name='del_comment')
]
