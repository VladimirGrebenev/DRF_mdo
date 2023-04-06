from rest_framework.serializers import ModelSerializer, IntegerField, CharField
from rest_framework import serializers
from .models import Property, Entity


class PropertySerializer(ModelSerializer):
    key = CharField(max_length=128)
    value = CharField(max_length=500)

    class Meta:
        model = Property
        fields = '__all__'


class EntitySerializer(ModelSerializer):
    value = IntegerField()
    properties = PropertySerializer(read_only=True, many=True)

    def validate_value(self, value):
        if value < 0:
            raise serializers.ValidationError('значение должно быть больше '
                                              'или равно нулю')
        return value

    class Meta:
        model = Entity
        fields = '__all__'
