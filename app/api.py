import logging
from flask import request, abort
from app import app


@app.route('/api/event-forwarder/dynatrace', methods=['POST'])
def dynatraceReceiver():
    if request.method == 'POST':
        app.logger.info(request.json)
        print(request.json)
        return 'success', 200
    else:
        abort(400)
