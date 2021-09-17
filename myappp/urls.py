from django.urls import path,include
from django.conf.urls import url

from . import views

urlpatterns = [
    path('test1', views.test1,name='test1'),
    path('test2', views.test2,name='test2'),
    path('jinja/', views.jinja,name='jinja'),
    path('displayusers/', views.displayusers,name='displayusers'),
    path('dbconnection/', views.dbconnection,name='dbconnection'),
    path('text/', views.text,name='text'),
    # path('text2/', views.text2,name='text2'),
    path('sample/', views.sample,name='sample'),
    path('display/', views.display,name='display'),
    path('todo/', views.todo,name='todo'),
    path('deleteuser/<int:id>',views.delete,name='delete'),
    path('viewsingledata/<int:id>',views.viewdata,name='viewdata'),
    path('update/<int:id>',views.update,name='update'),
    path('login/',views.login,name='login'),
    path('user/',views.user,name='user'),
    path('file/',views.file,name='file'),

    path('ajax/',views.ajax,name='ajax'),
    path('add_ajax/',views.add_ajax,name='add_ajax'),
    path('viewajax/',views.viewajax,name='viewajax'),
    path('delajax/',views.delajax,name='delajax'),
    
    path('ajax2/',views.ajax2,name='ajax2'),
    path('add_ajax2/',views.add_ajax2,name='add_ajax2'),
    path('viewajax2/',views.viewajax2,name='viewajax2'),
    path('delajax2/',views.delajax2,name='delajax2'),


    # path('select/',views.select,name='select'),
    # path('select/<int:id>',views.select,name='select'),

    url(r'^select/$',views.select_data,name='select_data'),
    url(r'^select/([0-9]+)$',views.select_data,name='select_data')

]
