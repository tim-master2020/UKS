"""github URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from wiki.models import Wiki
from . import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('labels/', include('label.urls')),
    path('admin/', admin.site.urls),
    path('',views.landing, name='landing'),
    path('repository/', include('repository.url')),
    path('register/', views.register, name="register"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('wiki/', include('wiki.url')),
    path('task/',include('task.urls')),
    path('project/', include('project.urls')),
    path('milestone/', include('milestone.urls')),
    path('comments/', include('comment.urls')),
    path('profile/', views.profile, name='profile'),
    path('photo/', include('photo.urls')),
    path('user/', include('user.urls')),
    path('branch/', include('branch.url')),
    path('commit/', include('commit.urls'))
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
