from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.utils.serializer_helpers import ReturnList
from rest_framework.views import APIView

from surveys.models import Link
from surveys.serializers.link import LinkUpdateSerializer
from surveys.services.link import LinkService


class AnyLinkAPIView(APIView):
    """Любой вопрос - любой ответ"""

    link_service = LinkService()

    def get(self, request):
        links: ReturnList = self.link_service.get_all()
        return Response(links)

    def put(self, request):
        from_question_id = request.data.get('from_question_id')

        link = get_object_or_404(Link, from_question_id=from_question_id)

        serializer = LinkUpdateSerializer(link, request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class ConcreteLinkAPIView(APIView):
    """Конкретного вопрос - любой ответ"""

    def patch(self, request, question_id):
        link = get_object_or_404(Link, from_question_id=question_id)

        serializer = LinkUpdateSerializer(link, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
