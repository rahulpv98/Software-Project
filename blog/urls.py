from django.conf.urls import url
from . import views

urlpatterns= [
    url(r'^$',views.post_list,name='post_list'),
    url(r'^post/(?P<pk>\d+)/$',views.post_detail,name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^index/$', views.index, name='index'),
    url(r'^index1/$', views.index1, name='index1'),
    url(r'^content/$', views.content, name='content'),
    url(r'^logged/$', views.logged, name='logged'),
     url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^success$', views.success),
    url(r'^login$', views.login)
    

    
]
