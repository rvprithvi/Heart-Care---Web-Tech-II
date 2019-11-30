from django.urls import path
from . import views
from django.conf.urls import url,include

urlpatterns = [
url(r'home',views.home, name="home"),
url(r'content',views.content, name="content"),
url(r'image',views.image, name="image"),

url(r'check',views.check, name = "check"),
url(r'predict',views.pred,name='predict'),
url(r'result',views.result, name='result'),
url(r'doctors',views.doc,name='doc'),
#url(r'audio',views.audio,name='audio'),
url(r'video',views.video,name='video'),
url(r'link',views.link,name='link')

]
