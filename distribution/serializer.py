from django.shortcuts import get_object_or_404

from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from rest_framework.validators import UniqueValidator

from .models import Good



class GoodSerializer(serializers.ModelSerializer):
    # output_author = SerializerMethodField()
    # reply_list = SerializerMethodField()
    # is_mine = SerializerMethodField()
    # to_comment_object = SerializerMethodField()

    class Meta:
        model = Good
        fields = ("name", "shop", "tags", "created_at", "pk")
    

