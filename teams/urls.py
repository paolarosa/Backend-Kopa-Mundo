from django.urls import path
from .views import TeamView
from .views import TeamViewId

urlpatterns = [
    path('teams/', TeamView.as_view()),
    path('teams/<int:team_id>/', TeamViewId.as_view())
]