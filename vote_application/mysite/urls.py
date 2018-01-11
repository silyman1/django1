from django.conf.urls import include, url
from django.contrib import admin
from polls import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^polls/', include('polls.urls',namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^upload', views.uploadImg),
    url(r'^show', views.showImg),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
