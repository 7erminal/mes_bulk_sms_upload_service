from rest_framework import serializers
from bulk_sms.models import Campaigns
from bulk_sms.models_existing import Users

class IdSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=25)

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class CampaignsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaigns
        fields = '__all__'

class CampaignRequestSerializer(serializers.Serializer):
    campaignName = serializers.CharField(max_length=255)
    campaignMessage = serializers.CharField(max_length=500)
    deliveryTime = serializers.CharField(max_length=255)
    recipientNumber=serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    recipientEmail=serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    type=serializers.CharField(max_length=40)
    # recipients=serializers.FileField()
    requestBy = serializers.IntegerField()

class CampaignResponseSerializer(serializers.Serializer):
    StatusDesc = serializers.CharField(max_length=255)
    StatusCode = serializers.IntegerField()
    Result = CampaignsSerializer()

class CampaignsResponseSerializer(serializers.Serializer):
    StatusDesc = serializers.CharField(max_length=255)
    StatusCode = serializers.IntegerField()
    Result = CampaignsSerializer(many=True)