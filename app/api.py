from flask import request, abort
from app import app
from modules.dynatraceModifier import dynatraceModifier

@app.route('/api/event-forwarder/dynatrace', methods=['POST'])
def dynatraceReceiver():
    if request.method == 'POST':
        
        transformer = dynatraceModifier(request.get_json())
        transformer.process()
      
        
        return 'success', 200
    else:
        abort(400)
