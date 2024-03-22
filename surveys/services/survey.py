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
        surveys: QuerySet = self._repository.get_where(filters)
        serializer = self._serializer(surveys, many=True)

        return serializer.data

    def get_by_id(self, pk: int) -> ReturnDict:
        survey: Survey = self._repository.get_by_id(pk)
        serializer = self._serializer(survey)

        return serializer.data

    def create(self, data: dict) -> ReturnDict:
        survey_data: ReturnDict = self._factory.create(data)
        return survey_data

    def update(self, pk: int, data: dict, partial=False) -> ReturnDict:
        survey_data: ReturnDict = self._repository.update(pk, data, partial)
        return survey_data

    def delete(self, pk: int) -> ReturnDict:
        survey: Survey = self._repository.delete(pk)
        serializer = self._serializer(survey)

        return serializer.data
