import os
from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Привет!</title>
                  </head>
                  <body>
                    <h1>Первая HTML-страница</h1>
                    <img src = {url_for('static', filename='img/picture.jpg')} width = 100% />
                  </body>
                </html>"""

@app.route('/news')
def news():
    with open("templates/news.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    return render_template('news.html', news=news_list)

if __name__ == '__main__':
    app.run()