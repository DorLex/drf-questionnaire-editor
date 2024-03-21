from rest_framework.response import Response
from rest_framework.utils.serializer_helpers import ReturnList
from rest_framework.views import APIView

from surveys.services.survey import SurveyService


class SurveyAPIView(APIView):
    survey_service = SurveyService()

    def get(self, request):
        surveys: ReturnList = self.survey_service.get_all()
        return Response(surveys)
