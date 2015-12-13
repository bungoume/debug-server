from django.conf.urls import url
from webfront import views as webfront_views


urlpatterns = [
    url(r'', webfront_views.index, name='index')
]

handler400 = 'webfront.views.handler400'
handler403 = 'webfront.views.handler403'
handler404 = 'webfront.views.handler404'
handler500 = 'webfront.views.handler500'
