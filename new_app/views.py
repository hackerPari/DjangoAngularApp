from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse

from new_app.models import Battle
from new_app.serializers import BattleSerizlizer, BattleListSerializer, BattleTypeAggregateSerializer, AttackerKingAggregateSerializer, \
    DefenderKingAggregateSerializer, MaxMinAverageDefenderSizeSerializer
from django.db.models import Count, Max, Min, Avg


def get_battles(request):
    page_no = int(request.GET['page'])
    search_term = request.GET['searchTerm']
    page_length = 20
    battle_range_start = page_length * (page_no-1)
    battle_range_end = battle_range_start + page_length

    if len(search_term) > 0:
        data = Battle.objects.filter(name__icontains=search_term).values('id', 'name')[battle_range_start:battle_range_end]
    else:
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


def get_aggregate_battle_type(request):
    data = Battle.objects.values('battle_type').annotate(battle_type_count=Count('battle_type'))
    if request.method == 'GET':
        serializer = BattleTypeAggregateSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)


def get_aggregate_active_attacker_king(request):
    data = Battle.objects.values('attacker_king').annotate(battle_count=Count('attacker_king'))
    if request.method == 'GET':
        serializer = AttackerKingAggregateSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)


def get_aggregate_active_defender_king(request):
    data = Battle.objects.values('defender_king').annotate(battle_count=Count('defender_king'))
    if request.method == 'GET':
        serializer = DefenderKingAggregateSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)


def get_min_max_average_defender_size(request):
    data = Battle.objects.aggregate(Avg('defender_size'), Max('defender_size'), Min('defender_size'))
    return JsonResponse(data, safe=False)