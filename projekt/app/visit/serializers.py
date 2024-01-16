from rest_framework import serializers
from .models import Visit

class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        # fields = '__all__'
        fields = ('kind_of_visit', 'date', 'time', 'opinion_user' )

class OpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ('kind_of_visit', 'opinion_user', 'opinion_admin_answer' )