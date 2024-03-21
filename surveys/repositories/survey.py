from django.db.models import QuerySet

from surveys.models import Survey


class SurveyRepository:
    _model = Survey

    def get_all(self) -> QuerySet:
        surveys: QuerySet = self._model.objects.all()
        return surveys