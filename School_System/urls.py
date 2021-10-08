"""School_System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from School_System import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/",include("api.urls")),
    path("",include("landing.urls")),
    path("core",include("core.urls")),
    path("dashboard/",include("dashboard.urls")),
    path("student/",include("student.urls")),
    path("trainer/",include("trainer.urls")),
    path("courses/",include("courses.urls")),
    path("staff/",include("staff.urls")),
    path("myCalendar/",include("myCalendar.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
