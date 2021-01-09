from django.shortcuts import render
from rest_framework import viewsets
from application.models import Student, Company, Hr, Announcement, JobApplication
from application.serializers import StudentSerializer, CompanySerializer, HrSerializer, JobApplicationSerializer, \
    AnnouncementSerializer
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class HrViewSet(viewsets.ModelViewSet):
    queryset = Hr.objects.all()
    serializer_class = HrSerializer


class JobApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer


class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

class AnnouncementDetail(generics.RetrieveAPIView):
    lookup_field = 'id_ann'
    queryset = Announcement.objects.all()
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('annourcementDetail get', request.user)
        return Response({'announcement': self.object, 'user': request.user}, template_name='announcement_detail.html')

    def post(self, request, *args, **kwargs):
        print('Hello World')
        print('announcementDetail post', request.user)
        user = serializers.HiddenField(default=serializers.CurrentUserDefault())
        # JobApplication.objects.create(
        #     student='',
        #     announcement='',
        # )
        return