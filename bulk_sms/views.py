from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, viewsets
from bulk_sms.models import Campaigns
from bulk_sms.serializers import CampaignResponseSerializer, CampaignRequestSerializer
from bulk_sms.models_existing import Users
from bulk_sms.functions import file_processor
import threading
import logging

logger = logging.getLogger("django")

class Resp:
	def __init__(self, StatusDesc, Result, StatusCode):
		self.StatusDesc=StatusDesc
		self.Result=Result
		self.StatusCode=StatusCode

# Create your views here.

class CampaignsView(viewsets.ViewSet):
    def create(self, request):
        serializer = CampaignRequestSerializer(data=request.data)

        logger.info(serializer)

        if serializer.is_valid(raise_exception=True):
            title = serializer.data['campaignName']
            message = serializer.data['campaignMessage']
            scheduledTime = serializer.data['deliveryTime']
            recipientNumber = serializer.data['recipientNumber']
            recipientEmail = serializer.data['recipientEmail']
            type = serializer.data['type']

            logger.info("Data received::\nTitle:: "+title+"\nMessage:: "+message+"\nScheduled Time:: "+scheduledTime+"\nRecipient Number:: "+recipientNumber+"\nRecipient Email:: "+recipientEmail)

            requestBy = serializer.data['requestBy']

            user = Users.objects.get(user_id=requestBy)

            if 'recipients' in request.FILES:
                recipientList = request.FILES['recipients']

                campaign = Campaigns(
                        title = title,
                        message = message,
                        scheduledTime = scheduledTime,
                        recipient_number = recipientNumber,
                        recipient_email = recipientEmail,
                        type=type,
                        created_by = user,
                        recipient_file = recipientList
                )
                campaign.save()

                t1 = threading.Thread(target=file_processor.processRecipientFile, args=(recipientList, campaign))
                t1.start()
            else:
                campaign = Campaigns(
                        title = title,
                        message = message,
                        type=type,
                        scheduledTime = scheduledTime,
                        recipient_number = recipientNumber,
                        recipient_email = recipientEmail,
                        created_by = user
                )
                campaign.save()

                

        #   balanceObj = file_processor.processRecipientFile(recipientList)

            message = "Details added successfully. You will be notified once your request is processed."
            status_ = 200
            
            resp = Resp(StatusDesc=message, StatusCode=status_, Result=campaign)
            logger.info("About to send response")

            return Response(CampaignResponseSerializer(resp).data,status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)