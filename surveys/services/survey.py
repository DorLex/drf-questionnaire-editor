from django.db.models import QuerySet
from rest_framework.generics import get_object_or_404
from rest_framework.utils.serializer_helpers import ReturnList, ReturnDict

from surveys.factories.survey import SurveyFactory
from surveys.models import Survey
from surveys.repositories.survey import SurveyRepository
from surveys.serializers.survey import SurveySerializer


class SurveyService:
    _repository = SurveyRepository()
    _factory = SurveyFactory()
    _serializer = SurveySerializer

    def get_all(self) -> ReturnList:
        surveys: QuerySet = self._repository.get_all()
        serializer = self._serializer(surveys, many=True)
        return serializer.data

    def get_where(self, filters: dict) -> ReturnDict:
        surveys_qs: QuerySet = self._repository.get_where(filters)
        survey: Survey = get_object_or_404(surveys_qs)
        serializer = self._serializer(survey)

        return serializer.data

    def create(self, data: dict) -> ReturnDict:
        survey: ReturnDict = self._factory.create(data)
        return survey
