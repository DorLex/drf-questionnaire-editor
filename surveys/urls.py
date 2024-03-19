from django.urls import path

from surveys.views import AnyLinkAPIView, ConcreteLinkAPIView

urlpatterns = [
    path('any-link/', AnyLinkAPIView.as_view(), name='any_link'),
    path('concrete-link/<int:question_id>', ConcreteLinkAPIView.as_view(), name='concrete_link'),
]
