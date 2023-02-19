from flask import Flask, request, session
import route_function
from datetime import timedelta
import time
now = time.strftime("%Y-%m-%d", time.gmtime())

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.add_url_rule("/cdn/<token>","index",route_function.main) # main site
app.add_url_rule("/","upload",route_function.upload) # main site
app.add_url_rule("/uploadapi","uploadapi",route_function.uploadapi,  methods=["POST"]) # main site

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80)