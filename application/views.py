from django.shortcuts import render
from rest_framework import viewsets
from application.models import Student, Company, Hr, Announcement, Job_appl
from application.serializers import StudentSerializer, CompanySerializer, HrSerializer, Job_applSerializer, \
    AnnouncementSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class HrViewSet(viewsets.ModelViewSet):
    queryset = Hr.objects.all()
    serializer_class = HrSerializer


class Job_applViewSet(viewsets.ModelViewSet):
    queryset = Job_appl.objects.all()
    serializer_class = Job_applSerializer


class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
