from rest_framework import serializers

from surveys.models import Link
from surveys.serializers.answer import AnswerSerializer
from surveys.serializers.question import QuestionSerializer


class LinkSerializer(serializers.ModelSerializer):
    from_question = QuestionSerializer()
    to_question = QuestionSerializer()
    answer = AnswerSerializer()

    class Meta:
        model = Link
        fields = '__all__'


class LinkUpdateSerializer(serializers.ModelSerializer):
    from_question_id = serializers.IntegerField()
    to_question_id = serializers.IntegerField()
    answer_id = serializers.IntegerField()

    class Meta:
        model = Link
        fields = (
            'from_question_id',
            'to_question_id',
            'answer_id',
        )
