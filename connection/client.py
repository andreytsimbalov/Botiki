# Клиент для принятия сообщений(словарей) от сервера

import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect('tcp://127.0.0.1:2000')
socket.setsockopt_string(zmq.SUBSCRIBE, '')

while 1:
    message = socket.recv_pyobj()
    tag=message.get(1)[0] # первый тег
    print(tag)
    print(message.get(tag)) # номер элемента словаря с данным тегом
    print(type(message))
    print(message)

