from rest_framework import serializers
from new_app.models import Battle


class BattleSerizlizer(serializers.ModelSerializer):
    class Meta:
        model = Battle
        fields = ('id', 'name', 'year', 'attacker_king', 'defender_king', 'attacker_1', 'attacker_2', 'attacker_3', 'attacker_4', 'defender_1',
                  'defender_2', 'defender_3', 'defender_4', 'attacker_outcome', 'battle_type', 'major_death', 'major_capture', 'attacker_size',
                  'defender_size', 'attacker_commander', 'defender_commander', 'summer', 'location', 'region', 'note')


class BattleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Battle
        fields = ('id', 'name')


class BattleTypeAggregateSerializer(serializers.Serializer):
    battle_type = serializers.CharField()
    battle_type_count = serializers.IntegerField()


class AttackerKingAggregateSerializer(serializers.Serializer):
    attacker_king = serializers.CharField()
    battle_count = serializers.IntegerField()


class DefenderKingAggregateSerializer(serializers.Serializer):
    defender_king = serializers.CharField()
    battle_count = serializers.IntegerField()


class MaxMinAverageDefenderSizeSerializer(serializers.Serializer):
    max = serializers.IntegerField()
    min = serializers.IntegerField()
    average = serializers.IntegerField()
