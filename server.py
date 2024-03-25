import socket, pickle, time

SERVER_IP = "192.168.1.9"
PORT = 12345
HEADER= 128
FORMAT = 'utf-8'
ADDR = (SERVER_IP, PORT)
DM = "@disconnect"
t = 0.00001

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(ADDR)

def send_msg(msg: bytes, client : socket.socket):
  msg += b' '*(HEADER - len(msg))
  server.sendto(msg, client)

def update_data(msg: str, data: dict):
  client_data = msg.split(',')
  data[client_data[2]] = ','.join([client_data[0], client_data[1], client_data[3]])
  return client_data[2]

def handle_client(client_data: bytes, data: dict, client_adress) -> None:
  msg = pickle.loads(client_data)
  if msg:
    msg = msg.split(' ')[0]
    try : 
      prev_key = msg.split(':')[1]
      msg = msg.split(':')[0]
    except IndexError:
      prev_key = msg.split(',')[2]
    if msg == DM:
      data = data.pop(prev_key)
    else:
      prev_key = update_data(msg, data)

def run_server() -> None:
  data = {}
  print('STARTING THE SERVER...')
  while True:
    client_data, client_address = server.recvfrom(HEADER)
    handle_client(client_data, data, client_address)
    msg = pickle.dumps(data)
    # for _ in range(len(data)):
    send_msg(msg, client_address)


run_server()