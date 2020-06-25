import schedule
import os
from services.rfid_response_service import RFIDResponseService

prune_job_time = os.environ['PRUNE_JOB_TIME']


def prune_rfid_response():
    RFIDResponseService.delete_rfid_response()


# schedule.every(2).seconds.do(job)
schedule.every().day.at(prune_job_time).do(prune_rfid_response)

while True:
    schedule.run_pending()
