from django.db.models import QuerySet

from surveys.models import Link


class LinkRepository:
    _model = Link

    def get_all(self) -> QuerySet:
        links: QuerySet = (
            self._model.objects.all()
            .select_related(
                'from_question__survey',
                'to_question__survey',
                'answer__question__survey'
            )
        )

        return links
