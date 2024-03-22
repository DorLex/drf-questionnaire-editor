from django.db.models import QuerySet
from rest_framework.generics import get_object_or_404
from rest_framework.utils.serializer_helpers import ReturnDict

from surveys.models import Survey
from surveys.serializers.survey import SurveySerializer


class SurveyRepository:
    _model = Survey
    _serializer = SurveySerializer

    def get_all(self) -> QuerySet:
        surveys: QuerySet = self._model.objects.all()
        return surveys

    def get_where(self, filters: dict) -> QuerySet:
        surveys: QuerySet = self._model.objects.filter(**filters)
        return surveys

    def get_by_id(self, pk: int) -> Survey:
        survey: Survey = get_object_or_404(self._model, pk=pk)
        return survey

    def update(self, pk: int, data: dict, partial=False) -> ReturnDict:
        survey: Survey = self.get_by_id(pk)

        serializer = self._serializer(survey, data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return serializer.data
