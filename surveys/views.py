from rest_framework.response import Response
from rest_framework.views import APIView


class EditAnyLinkAPIView(APIView):
    """Любой вопрос - любой ответ"""

    def put(self, request):
        return Response({'test': 'put'})


class EditConcreteLinkAPIView(APIView):
    """Конкретного вопрос - любой ответ"""

    def patch(self, request, question_id):
        return Response({'test': question_id})
