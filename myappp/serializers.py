from django.db.models import fields
from rest_framework import serializers
from  myappp.models import *

class user_api(serializers.ModelSerializer):
    class Meta:
        model=ajaxx
        fields=('id','name','contact','email')

