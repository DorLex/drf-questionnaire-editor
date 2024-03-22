from rest_framework import status
from rest_framework.response import Response
from rest_framework.utils.serializer_helpers import ReturnList, ReturnDict
from rest_framework.viewsets import ViewSet

from surveys.services.survey import SurveyService


class SurveyViewSet(ViewSet):
    survey_service = SurveyService()

    def list(self, request):
        surveys: ReturnList = self.survey_service.get_all()
        return Response(surveys)

    def create(self, request):
        survey_data: ReturnDict = self.survey_service.create(request.data)
        return Response(survey_data, status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        survey_data: ReturnDict = self.survey_service.get_by_id(pk)
        return Response(survey_data)

    def update(self, request, pk=None):
        survey_data: ReturnDict = self.survey_service.update(pk, request.data)
        return Response(survey_data)

    def partial_update(self, request, pk=None):
        survey_data: ReturnDict = self.survey_service.update(pk, request.data, partial=True)
        return Response(survey_data)

    def destroy(self, request, pk=None):
        survey_data: ReturnDict = self.survey_service.delete(pk)
        return Response(survey_data, status.HTTP_204_NO_CONTENT)
