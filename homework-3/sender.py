import requests

name = input('Введите имя: ')
print('Чтобы увидеть в чате справку по мессенджеру, отправьте сообщение \help')
while True:
    text = input('Введите сообщение: ')
    text_lstrip = text.lstrip()
    if text_lstrip[0] != '~':
        response = requests.post('http://127.0.0.1:5000/send',
                                 json={
                                     'name': name,
                                     'text': text
                                 }
                                )
    else:
        response = requests.post('http://127.0.0.1:5000/send',
                                 json={
                                     'name': '-',
                                     'text': text_lstrip
                                 }
                                )
