from rest_framework import serializers
from application.models import Student, Company, Hr, Job_appl, Announcement


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class HrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hr
        fields = '__all__'


class Job_applSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job_appl
        exclude = ('date',)


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'
