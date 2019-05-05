"""Newbie_6 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import meetup.views
import joinResult.views
import movie.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/', meetup.views.board, name="board"),
    path('boardform/', meetup.views.boardform, name="boardform"),
    path('<int:pk>/edit/', meetup.views.edit, name="edit"),
    path('<int:pk>/remove/', meetup.views.remove, name="remove"),
    path('joinResult/', meetup.views.joinResult, name="joinResult"),
    path('<int:pk>/attend/', meetup.views.attend, name="attend"),
    path('postlist/', meetup.views.postlist, name="postlist"),
    path('result_page/', meetup.views.result_page, name="result_page"),
    path('attend/', meetup.views.attend, name="attend"),
    # path('joinResult/', joinResult.views.joinResult, name="joinResult"),
    path('', meetup.views.main, name='main'),
    path('makepage/', meetup.views.makepage, name='makepage'),
    path('login/', meetup.views.login, name='login'),
    path('signup/', meetup.views.signup, name='signup'),
    path('postlist/', meetup.views.postlist, name='postlist'),
    path('mypage/', meetup.views.mypage, name='mypage'),
    path('movie/',movie.views.MovieList.as_view(),name="home"),
    path('parse',movie.views.parse,name="parse"),
    # 아래 부터 CRUD 4가지 
    # 영화를 생성할 url (Create)
    path('create/',movie.views.MovieCreate.as_view(),name="create"),
    # 각 영화 detail url(Read)
    path('detail/<int:pk>',movie.views.MovieDetail.as_view(),name="detail"),
    # 영화를 수정할 url (Update)
    path('update/<int:pk>',movie.views.MovieUpdate.as_view(),name="update"),
    # 영화를 제거할 url (Delete)
    path('delete/<int:pk>',movie.views.MovieDelete.as_view(),name="delete"),
   
    #url(r'^join/$', views.signup, name='join'),
    # path('', include('meetup.urls')),   
]
