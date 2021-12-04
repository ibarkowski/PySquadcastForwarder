import logging
from flask import Flask, request, abort

app = Flask(__name__)

gunicorn_logger = logging.getLogger('gunicorn.error')
app.logger.handlers = gunicorn_logger.handlers
app.logger.setLevel(logging.INFO)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        app.logger.info(request.json)
        print(request.json)
        return 'success', 200
    else:
        abort(400)


if __name__ == '__main__':
    app.run()