from rest_framework import viewsets
from main.models import Problem
from main.serializers import ProblemSerializer


class ProblemViewSet(viewsets.ViewSet):
    serializer_class = ProblemSerializer
    queryset = Problem.objects.all()

