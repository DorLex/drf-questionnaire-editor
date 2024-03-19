from surveys.models import Link


def get_all_links():
    links = (
        Link.objects.all()
        .select_related(
            'from_question__survey',
            'to_question__survey',
            'answer__question__survey'
        )
    )

    return links
