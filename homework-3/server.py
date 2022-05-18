# save this as app.py
import time
from datetime import datetime
import flask
from flask import Flask, abort

app = Flask(__name__)
db = []
db.append({
    'name': 'СЕРВЕР',
    'time': time.time(),
    'text': 'Запущен'
})

counter_messages = 0
users = []

@app.route("/")
def hello():
    return "МЕССЕНДЖЕР. Страница статуса находится по адресу, содержащему /status в конце адресной строки."

@app.route("/send", methods= ['POST'])
def send_message():
    '''
    функция для отправки нового сообщения пользователем
    :return:
    '''
    # TODO
    # проверить, является ли присланное пользователем правильным json-объектом
    # проверить, есть ли там имя и текст
    # Добавить сообщение в базу данных db

    global counter_messages
    global users

    data = flask.request.json
    if not isinstance(data, dict):
        return abort(400)

    if 'name' not in data or \
        'text' not in data:
        return abort(400)

    if not isinstance(data['name'], str) or \
        not isinstance(data['text'], str) or \
        len(data['name']) == 0 or \
        len(data['text']) == 0:
        return abort(400)

    text = data['text']
    name = data['name']
    
    anonymous = text[0] == '~'
    if anonymous:
        text = text[1:]
        name = 'Анонимное сообщение'
    
    message = {
        'text': text,
        'name': name,
        'time': time.time()
    }
    db.append(message)
    
    counter_messages += 1
    if not anonymous and name not in users:
        users.append(name)

    if text.strip() == "\help":
        text_help = "Мессенджер позволяет отправлять в чат сообщения и читать чат. \n" + \
                    "Сообщения отправляются от указанного вами имени. \n" + \
                    "Если хотите отправить анонимное сообщение, поставьте в начале его знак ~ \n" + \
                    "Запрос на получение данной справки осуществляется отправкой сообщения \help \n" + \
                    "Веб-страница статуса мессенджера: http://127.0.0.1:5000/status"
        message = {
            'text': text_help,
            'name': 'СПРАВКА',
            'time': time.time()
        }
        db.append(message)
    
    return {'ok': True}

@app.route("/messages")
def get_messages():
    try:
        after = float(flask.request.args['after'])
    except:
        abort(400)
    db_after = []
    for message in db:
        if message['time'] > after:
            db_after.append(message)
    return {'messages': db_after}

@app.route("/status")
def print_status():
    return {
       "Статус мессенджера": {
           "Teкущее время": datetime.now().strftime("%H:%M:%S"),
           "Пользователей": len(users),
           "Сообщений": counter_messages
       }
    }



app.run()
