#Сервер по отправке сообщений(словарей) клиентам

import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind('tcp://127.0.0.1:2000')
time.sleep(1)
socket.send_pyobj({1:[7,12,0],
                   2: 'qweqw'})
