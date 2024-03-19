from django.db import connection
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from surveys.models import Link
from surveys.serializers.link import LinkSerializer, LinkUpdateSerializer
from surveys.services.crud import get_all_links


class AnyLinkAPIView(APIView):
    """Любой вопрос - любой ответ"""

    def get(self, request):
        links = get_all_links()
        serializer = LinkSerializer(links, many=True)

        return Response(serializer.data)

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
