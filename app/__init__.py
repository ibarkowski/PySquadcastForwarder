import logging
from flask import Flask, request, abort
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

gunicorn_logger = logging.getLogger('gunicorn.error')
app.logger.handlers = gunicorn_logger.handlers
app.logger.setLevel(logging.INFO)


def getMailsAndTransfer():
    app.logger.info ("Run background job: check mail and forward event")


# initialize scheduler
scheduler = BackgroundScheduler({'apscheduler.timezone': 'Europe/Warsaw'})
scheduler.add_job(getMailsAndTransfer, 'interval', id='my_job_id', seconds=15)
scheduler.start()


from app import api
from app import admin



if __name__ == '__main__':
    app.run()