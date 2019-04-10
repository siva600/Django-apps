# from django.http import Http404
# from django.http import JsonResponse
# from Game.models import Game
# from rest_framework.renderers import JSONRenderer
# from Game.serializer import GameSerializer
# from rest_framework.parsers import JSONParser
# from rest_framework import status
# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Game.models import Game
from Game.serializer import GameSerializer


# class JSONResponse(HttpResponse):
#     def __init__(self, data, **kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         super(JSONResponse, self).__init__(content, **kwargs)
#
#
# # game_list request to retrieve and add new data.
# @csrf_exempt
# def game_list(request):
#     # if the request is get, then retrieve all data from db
#     # then use game serializer to serialize all of them and
#     # return a JSON response instance built with the data generated
#     # by the game serializer.
#     if request.method == 'GET':
#         games = Game.objects.all()
#         # django uses list serializer when many many=True.
#         game_serializer = GameSerializer(games, many=True)
#         return JsonResponse(game_serializer.data, safe=False)
#
#     # if the data is post, use the JSONParser() method to parse the JSON data
#     # from HTTP request.
#     # Use the GameSerializer method to create a serializer instance using the
#     # streaming data obtained from JSONParser(), then check the validataion and save it.
#
#     elif request.method == 'POST':
#         game_data = JSONParser().parse(request)
#         game_serializer = GameSerializer(data=game_data)
#         if game_serializer.is_valid():
#             game_serializer.save()
#             return JsonResponse(game_serializer.data, status=status.HTTP_201_CREATED, safe=False)
#         return JsonResponse(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# # game_detail method to update and delete the data.
# # pk arg is passed to identify the game.
# @csrf_exempt
# def game_detail(request, pk):
#     # First check if the game with that pk is available or not.
#     try:
#         game = Game.objects.get(pk=pk)
#     except Game.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         # if the request is GET the create a serializer instance with the
#         # game object created with the retrieved data
#         # this response will also include default 200 status
#         game_serializer = GameSerializer(game)
#         return JsonResponse(data=game_serializer.data, safe=False)
#
#     elif request.method == 'PUT':
#         game_data = JSONParser().parse(request)
#         game_serializer = GameSerializer(game, data=game_data)
#         # determine the game instance is valid or not.
#         if game_serializer.is_valid():
#             game_serializer.save()
#             return JsonResponse(game_serializer.data, safe=False)
#         return JsonResponse(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         game.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)
#


# game_list request to retrieve and add new data.
# Using default parsing and rendering methods can automatically identify the request.
@api_view(['GET', 'POST'])
def game_list(request):
    # if the request is get, then retrieve all data from db
    # then use game serializer to serialize all of them and
    # return a JSON response instance built with the data generated
    # by the game serializer.
    if request.method == 'GET':
        games = Game.objects.all()
        # django uses list serializer when many many=True.
        game_serializer = GameSerializer(games, many=True)
        return Response(game_serializer.data)

    # if the data is post, use the JSONParser() method to parse the JSON data
    # from HTTP request.
    # Use the GameSerializer method to create a serializer instance using the
    # streaming data obtained from JSONParser(), then check the validataion and save it.

    elif request.method == 'POST':
        game_serializer = GameSerializer(data=request.data)
        if game_serializer.is_valid():
            game_serializer.save()
            return Response(game_serializer.data, status=status.HTTP_201_CREATED)
        return Response(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# game_detail method to update and delete the data.
# pk arg is passed to identify the game.
@api_view(['GET', 'PUT', 'POST'])
def game_detail(request, pk):
    # First check if the game with that pk is available or not.
    try:
        game = Game.objects.get(pk=pk)
    except Game.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # if the request is GET the create a serializer instance with the
        # game object created with the retrieved data
        # this response will also include default 200 status
        game_serializer = GameSerializer(game)
        return Response(data=game_serializer.data)

    elif request.method == 'PUT':
        game_serializer = GameSerializer(game, data=request.data)
        # determine the game instance is valid or not.
        if game_serializer.is_valid():
            game_serializer.save()
            return Response(game_serializer.data)
        return Response(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        game.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


###########################################################################################3
#
#     Using generic Class based views
#
#
############################################################################################

from Game.models import GameCategory
from Game.models import Game
from Game.models import Player
from Game.models import PlayerScore
from Game.serializer import GameCategorySerializer
from Game.serializer import GameSerializer
from Game.serializer import PlayerSerializer
from Game.serializer import PlayerScoreSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse


class GameCategoryList(generics.ListCreateAPIView):
    queryset = GameCategory.objects.all()
    serializer_class = GameCategorySerializer
    name = 'gamecategory-list'


class GameCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GameCategory.objects.all()
    serializer_class = GameCategorySerializer
    name = 'gamecategory-detail'


class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    name = 'game-list'


class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    name = 'game-detail'


class PlayerList(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    name = 'player-list'


class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    name = 'player-detail'


class PlayerScoreList(generics.ListCreateAPIView):
    queryset = PlayerScore.objects.all()
    serializer_class = PlayerScoreSerializer
    name = 'playerscore-list'


class PlayerScoreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlayerScore.objects.all()
    serializer_class = PlayerScoreSerializer
    name = 'playerscore-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'players': reverse(PlayerList.name, request=request),
            'game-categories': reverse(GameCategoryList.name, request=request),
            'games': reverse(GameList.name, request=request),
            'scores': reverse(PlayerScoreList.name, request=request)
            })