from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^log-in$', views.log_in, name='log-in'),
    url(r'^sign-up$', views.sign_up, name='sign-up'),
    url(r'^password-reset$', views.password_reset, name='password-reset'),
]
