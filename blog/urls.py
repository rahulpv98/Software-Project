from django.conf.urls import url
from . import views

urlpatterns= [
    url(r'^$',views.home,name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^content/$', views.post_list, name='content'),
    url(r'^post/(?P<pk>\d+)/$',views.post_detail,name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^sign_up/$', views.signup, name='signup'),
    url(r'^sign_in/$', views.signin, name='signin'),
    url(r'^log_out/$', views.log_out, name='log_out'),
    url(r'^post/(?P<pk>\d+)/delete/$', views.post_delete, name='post_delete'),
    url(r'^topic_dis/$', views.topic_dis, name='topic_dis'),
    url(r'^topic_list/$', views.topic_list,name='topic_list'),
    url(r'^search_list/$', views.search_list,name='topic_list'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/delete/', views.comment_delete, name='comment_delete'),
]   
