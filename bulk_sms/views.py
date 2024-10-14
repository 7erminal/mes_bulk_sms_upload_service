from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, viewsets
from bulk_sms.models import Campaigns
from bulk_sms.serializers import CampaignResponseSerializer, CampaignRequestSerializer, IdSerializer, CampaignsSerializer, CampaignsResponseSerializer
from bulk_sms.models_existing import Users
from bulk_sms.functions import file_processor
from dateutil import parser
from datetime import datetime
import time
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

        # logger.info(serializer)

        if serializer.is_valid(raise_exception=True):
            title = serializer.data['campaignName']
            message = serializer.data['campaignMessage']
            scheduledTime = serializer.data['deliveryTime']
            recipientNumber = serializer.data['recipientNumber']
            recipientEmail = serializer.data['recipientEmail']
            type = serializer.data['type']


            logger.info("Data received::\nTitle:: "+title+"\nMessage:: "+message+"\nScheduled Time:: "+scheduledTime+"\nRecipient Number:: "+recipientNumber+"\nRecipient Email:: "+recipientEmail)

            respMessage = "Details added successfully. You will be notified once your request is processed."
            status_ = 200

            # formatedDate = parser.parse(scheduledTime)
            # datetime_object = datetime(formatedDate)
            # format_string = '%Y-%m-%d %H:%M:%S'
            # date_string = datetime_object.strftime(format_string)
            # logger.info("Formated date is ", date_string)
            convertedDate = datetime.fromisoformat(scheduledTime)
            # scheduledTime_object = datetime.strptime(convertedDate, '%y/%m/%dT%H:%M:%S')
            logger.info(convertedDate)

            requestBy = serializer.data['requestBy']

            user = Users.objects.get(user_id=requestBy)

            if 'recipients' in request.FILES:
                recipientList = request.FILES['recipients']

                campaign = Campaigns(
                        title = title,
                        message = message,
                        scheduledTime = convertedDate,
                        recipient_number = recipientNumber,
                        recipient_email = recipientEmail,
                        type=type,
                        created_by = user,
                        recipient_file = recipientList
                )
                campaign.save()

                if recipientList.name.lower().endswith(".csv"):
                    t1 = threading.Thread(target=file_processor.processRecipientFile, args=(recipientList, campaign))
                    t1.start()
                else:
                    respMessage = "Invalid file format."
                    status_ = 400
            else:
                campaign = Campaigns(
                        title = title,
                        message = message,
                        type=type,
                        scheduledTime = convertedDate,
                        recipient_number = recipientNumber,
                        recipient_email = recipientEmail,
                        created_by = user
                )
                campaign.save()

            
            with open("../bulk_sms_file_checker/recipients.txt", "a+") as file:
                 file.write(str(campaign.campaignId)+" "+str(campaign.scheduledTime)+"\n")

        #   balanceObj = file_processor.processRecipientFile(recipientList)
            
            resp = Resp(StatusDesc=respMessage, StatusCode=status_, Result=campaign)
            logger.info("About to send response")

            return Response(CampaignResponseSerializer(resp).data,status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class GetCampaignsView(viewsets.ViewSet):
    def retrieve(self, request):
        serializer = IdSerializer(data=request.query_params)

        logger.info("request received is ")
        logger.info(request.query_params)

        if serializer.is_valid(raise_exception=True):
            id = serializer.data['id']
            user = Users.objects.get(user_id=id)
            queryset_data = Campaigns.objects.filter(created_by=user)
            logger.info("Data returned for campaigns is ")
            logger.info(queryset_data.values)
            logger.info(CampaignsSerializer(queryset_data, many=True).data)

            message = "Details added successfully. You will be notified once your request is processed."
            status_ = 200
            
            resp = Resp(StatusDesc=message, StatusCode=status_, Result=queryset_data)

            return Response(CampaignsResponseSerializer(resp).data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response("Request Failed", status=status.HTTP_201_CREATED)