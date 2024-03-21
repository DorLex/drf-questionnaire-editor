from django.db.models import QuerySet
from rest_framework.utils.serializer_helpers import ReturnList

from surveys.repositories.link import LinkRepository
from surveys.serializers.link import LinkSerializer


class LinkService:
    _repository = LinkRepository()
    _factory = ...
    _serializer = LinkSerializer

    def get_all(self) -> ReturnList:
        links: QuerySet = self._repository.get_all()
        serializer = self._serializer(links, many=True)
        return serializer.data
