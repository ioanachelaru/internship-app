"""app URL Configuration

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
from rest_framework import routers
from application.views import StudentViewSet, HrViewSet, CompanyViewSet, AnnouncementViewSet, JobApplicationViewSet, AnnouncementDetail


router = routers.DefaultRouter()
router.register('students', StudentViewSet, 'students')
router.register('hrs', HrViewSet, 'hrs')
router.register('companies', CompanyViewSet, 'companies')
router.register('announcements', AnnouncementViewSet, 'announcements')
router.register('applications', JobApplicationViewSet, 'applications')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('account.urls')),
    path('announcements/<int:id_ann>/', AnnouncementDetail.as_view()),
]

urlpatterns += router.urls
