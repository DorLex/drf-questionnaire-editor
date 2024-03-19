from django.urls import path

from surveys.views import EditAnyLinkAPIView, EditConcreteLinkAPIView

urlpatterns = [
    path('edit-any-link', EditAnyLinkAPIView.as_view(), name='edit_any_link'),
    path('edit-concrete-link/<int:question_id>', EditConcreteLinkAPIView.as_view(), name='edit_concrete_link'),
]
