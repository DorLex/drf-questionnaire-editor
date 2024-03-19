from rest_framework import serializers

from surveys.models import Question
from surveys.serializers.survey import SurveySerializer


class QuestionSerializer(serializers.ModelSerializer):
    survey = SurveySerializer()

    class Meta:
        model = Question
        fields = '__all__'
