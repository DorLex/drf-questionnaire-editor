from rest_framework.utils.serializer_helpers import ReturnDict

from surveys.models import Survey
from surveys.serializers.survey import SurveySerializer


class SurveyFactory:
    _model = Survey
    _serializer = SurveySerializer

    def create(self, data: dict) -> ReturnDict:
        serializer = self._serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return serializer.data
