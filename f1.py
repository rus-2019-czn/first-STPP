# -*- coding: utf-8 -*-
from flask import *
import os
#from flask_ngrok import run_with_ngrok

app = Flask(__name__)
#run_with_ngrok(app)

@app.route('/')
def index():
    user = "Магзумов Руслан"
    return render_template('index.html', title='Домашняя страница', 
                           username=user)

@app.route('/news')
def news():
    with open("templates/news.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    return render_template('news.html', news=news_list, title = 'Новости')


@app.route('/picture')
def first():
    name = url_for('static', filename='img/picture.jpg')
    return render_template('picture.html', name=name)


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                            crossorigin="anonymous"> 
                            <link rel="stylesheet" type="text/css" href="static/style.css" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>Форма для регистрации</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <input type="password" class="form-control" id="password" placeholder="Введите пароль" name="password">
                                    <div class="form-group">
                                        <label for="about">Немного о себе</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите резюме</label>
                                        <input type="file" class="form-control-file" id="resume" name="file">
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Согласен на обработку данных </label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form.get('email'))
        print(request.form.get('password'))
        print(request.form.get('file'))
        print(request.form.get('about'))
        print(request.form.get('accept'))
        print(request.form.get('sex'))
        return render_template('second.html', title='Вторая страница')
        

if __name__ == '__main__':
    #app.run(port=8080, host='127.0.0.1')
    #app.run()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)    
