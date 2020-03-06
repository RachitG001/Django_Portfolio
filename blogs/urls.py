from django.urls import path,include
from .views import allblogs,detail

urlpatterns = [
    path('',allblogs,name='blog_page'),
    path('<int:blog_id>/',detail,name='details')
]