from django.db import models
from bulk_sms.models_existing import Users

# Create your models here.
class Campaigns(models.Model):
	campaignId = models.AutoField(primary_key=True)
	title = models.CharField(max_length=200, null=True, blank=True)
	type = models.CharField(max_length=20, null=True, blank=True)
	message = models.CharField(max_length=400, null=True, blank=True)
	scheduledTime = models.DateTimeField(null=True)
	recipient_file = models.FileField(upload_to='recipients', null=True, blank=True)
	recipient_number = models.CharField(max_length=200, null=True, blank=True)
	recipient_email = models.CharField(max_length=200, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	updated_at = models.DateTimeField(auto_now=True, blank=True)
	active = models.IntegerField(default=0)
	created_by = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='campaign_setup_by', null=True)
	updated_by = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='campaign_authorized_by', null=True)

class BulkRecipients(models.Model):
	bulk_recipient_id = models.AutoField(primary_key=True)
	campaign_id = models.ForeignKey(Campaigns, on_delete=models.CASCADE, related_name='campaign_id_bulk', null=True)
	recipient = models.CharField(max_length=200, null=True, blank=True)
	processed = models.IntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	updated_at = models.DateTimeField(auto_now=True, blank=True)
	active = models.IntegerField(default=1)
	created_by = models.IntegerField(default=1)
	updated_by = models.IntegerField(default=1)