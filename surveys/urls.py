from django.urls import path, include
from rest_framework.routers import DefaultRouter

from surveys.views import survey, link

router = DefaultRouter()
router.register(r'surveys', survey.SurveyViewSet, basename='surveys')

urlpatterns = [
    path('', include(router.urls)),

    path('any-link/', link.AnyLinkAPIView.as_view(), name='any_link'),
    path('concrete-link/<int:question_id>', link.ConcreteLinkAPIView.as_view(), name='concrete_link'),
]
