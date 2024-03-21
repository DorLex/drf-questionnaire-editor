from django.urls import path

from surveys.views import survey, link

urlpatterns = [
    path('surveys/', survey.SurveyAPIView.as_view(), name='surveys'),

    path('any-link/', link.AnyLinkAPIView.as_view(), name='any_link'),
    path('concrete-link/<int:question_id>', link.ConcreteLinkAPIView.as_view(), name='concrete_link'),
]
