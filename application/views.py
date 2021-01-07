from django.shortcuts import render
from rest_framework import viewsets
from application.models import Student
from application.serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
