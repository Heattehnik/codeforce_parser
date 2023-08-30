from main.apps import MainConfig
from rest_framework.routers import DefaultRouter
from main.views import ProblemViewSet

problems = DefaultRouter()
problems.register(r"problems", ProblemViewSet, basename="problems")
app_name = MainConfig.name

urlpatterns = [

] + problems.urls
