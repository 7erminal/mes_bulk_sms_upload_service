import codecs
import csv
import openpyxl
from bulk_sms.models import BulkRecipients, Campaigns

import logging
logger = logging.getLogger("django")

def processRecipientFile(recipientSheet, campaign):
    logger.info("Recipient file received ")
    logger.info(recipientSheet)

    if recipientSheet.name.lower().endswith(".csv"):
        logger.info("File is a csv file ")
        spamreader = csv.reader(codecs.iterdecode(recipientSheet, 'utf-8'), delimiter=',', quotechar='|')

        # logger.info(spamreader)

        r=0
        for row in spamreader:
            # logger.info("Each row is "+row)
            recipientNumber = row[0].strip('"')
            if r > 0:
                t=0
                # Iterate through columns in the first row
                logger.info("Recipient number is "+recipientNumber)

                bulkRecipient = BulkRecipients(
                    campaign_id = campaign,
                    recipient = recipientNumber,
                    processed = 0
                )

                bulkRecipient.save()
                logger.info("Recipient number inserted ")

            r += 1
            logger.info(recipientNumber+" processed")
        logger.info("Done")
    else:
        logger.info("Invalid file uploaded")