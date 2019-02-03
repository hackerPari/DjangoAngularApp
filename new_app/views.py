from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse

from new_app.models import ExampleModel, User, Battle
from new_app.serializers import ExampleModelSerializer, BattleSerizlizer, BattleListSerializer

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def get_battles(request):
    page_no = int(request.GET['page'])
    page_length = 20
    battle_range_start = page_length * (page_no-1)
    battle_range_end = battle_range_start + page_length

    data = Battle.objects.filter(id__gt=battle_range_start, id__lte=battle_range_end).values('id', 'name')
    if request.method == 'GET':
        serializer = BattleListSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)


def get_battle_details(request):
    battle_id = int(request.GET['id'])
    data = Battle.objects.get(pk=battle_id)

    if request.method == 'GET':
        serializer = BattleSerizlizer(data, many=False)
        return JsonResponse(serializer.data, safe=False)
