from rest_framework import serializers

from surveys.models import Answer
from surveys.serializers.question import QuestionSerializer


class AnswerSerializer(serializers.ModelSerializer):
    question = QuestionSerializer()

    class Meta:
        model = Answer
        fields = '__all__'
