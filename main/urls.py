from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('post/<int:pk>/', views.WebsterBlog_detail, name='post_detail' ),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('WebsterBlog_create/', views.WebsterBlog_create, name='WebsterBlog_create'),
    path('about/' , views.about, name='about'),
    path('<int:pk>/like-post/' , views.like_post, name='like-post'),
    path('confirmpage/' , views.confirmpage, name='confirmpage'),  
    path('question/' , views.question, name='question'),
    path('ScheduleApp/' , views.ScheduleApp, name='ScheduleApp'),
    path('delete/<str:pk>', views.delete, name='delete'),
    path('search_profile' , views.search_profile, name='search_profile'),
    path('<int:pk>/comment/',views.commentView,name='comment'),
    path('allsetting/' , views.allsetting, name='allsetting'),
    path('settings/', views.settings, name='settings'),
    path('opening/', views.opening, name='opening'),
    path('deletepost/<int:pk>', views.deletepost, name='deletepost'), 
]