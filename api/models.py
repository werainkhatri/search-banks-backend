# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from rest_framework import serializers


class Branch(models.Model):
    # id = models.BigAutoField(primary_key=True)
    ifsc = models.CharField(max_length=11, primary_key=True)
    bank_id = models.BigIntegerField()
    branch = models.CharField(max_length=74)
    address = models.CharField(max_length=195)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=26)
    bank_name = models.CharField(max_length=49)

    class Meta:
        managed = False
        db_table = 'bank_branches'

class BranchSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Branch
        fields = ['ifsc', 'bank_id', 'branch', 'address', 'city', 'district', 'state', 'bank_name']