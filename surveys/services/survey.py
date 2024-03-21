from django.db.models import QuerySet
from rest_framework.utils.serializer_helpers import ReturnList

from surveys.factories.survey import SurveyFactory
from surveys.repositories.survey import SurveyRepository
from surveys.serializers.survey import SurveySerializer


class SurveyService:
    _repository = SurveyRepository()
    _factory = SurveyFactory()

    def get_all(self) -> ReturnList:
        surveys: QuerySet = self._repository.get_all()
        serializer = SurveySerializer(surveys, many=True)
        return serializer.data

    def create(self):
        self._factory.create()
