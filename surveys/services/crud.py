from surveys.models import Link


def get_queryset_links():
    links = (
        Link.objects.all()
        .select_related(
            'from_question__survey',
            'to_question__survey',
            'answer__question__survey'
        )
    )

    return links
