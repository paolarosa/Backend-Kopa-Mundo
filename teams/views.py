from django.shortcuts import render
from rest_framework.views import APIView, Response
from teams.models import Team
""" from rest_framework.response import Response """
from django.forms.models import model_to_dict
""" from django.core.exceptions import ObjectDoesNotExist """
from teams.utils import data_processing
from teams.exceptions import NegativeTitlesError
from teams.exceptions import InvalidYearCupError
from teams.exceptions import ImpossibleTitlesError

class TeamView(APIView):
    def post(self, request):
        team_data = request.data
        try:
            data_processing(team_data)
        except NegativeTitlesError as err:
            return Response({"error":err.message}, 400)
        except InvalidYearCupError as err:
            return Response({"error":err.message}, 400)
        except ImpossibleTitlesError as err:
            return Response({"error":err.message}, 400)

        team = Team.objects.create(
            name = team_data["name"],
            titles = team_data["titles"],
            top_scorer = team_data["top_scorer"],
            fifa_code = team_data["fifa_code"],
            first_cup = team_data["first_cup"]
        )
        #ou dava pra ter feito:   
        #team = Team.objects.create(**request.data)
        return Response(model_to_dict(team), 201)
    
    def get(self, request):
        teams = Team.objects.all()
        teams_dict = []
        for team in teams:
            t = model_to_dict(team)
            teams_dict.append(t)
        return Response(teams_dict, 200)

class TeamViewId(APIView):
    def get(self, request, team_id):
        try:
            team = Team.objects.get(id=team_id)
            print(team)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)
        return Response(model_to_dict(team), 200)
    
    def patch(self, request, team_id):
        team_data = request.data
        try:
            team = Team.objects.get(id= team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)
        for key, value in team_data.items():
            setattr(team, key, value)
        team.save()
        #? team.update()
        return Response(model_to_dict(team))

    def delete(self, request, team_id):
        try:
            team = Team.objects.get(id = team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)
        team.delete()
        return Response(status=204)
