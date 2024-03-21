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
        survey: ReturnDict = self.survey_service.create(request.data)
        return Response(survey)

    def retrieve(self, request, pk=None):
        filters = {'pk': pk}
        survey: ReturnDict = self.survey_service.get_where(filters)
        return Response(survey)

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
