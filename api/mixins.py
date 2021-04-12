from rest_framework.mixins import ListModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet


class ListUpdateModelMixin(
    ListModelMixin,
    UpdateModelMixin,
    GenericViewSet
    ):
    pass