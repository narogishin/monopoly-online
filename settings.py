# GAME
RATIO = 0.5
RESOLUTION = WIDTH, HEIGHT = 1100*RATIO, 1100*RATIO

# needed to differentiate between players , gonna use 1 example and to change later
names = [chr(65+i)+str(j) for i in range(20) for j in range(1,100)]
colors = ['red', 'green', 'blue', 'cyan', 'yellow', 'magenta', 'white']
f = lambda txt, idx: txt.split(',')[idx]

# SOCKETS
SERVER_IP = "192.168.1.16"
PORT = 12345
HEADER= 128
FORMAT = 'utf-8'
ADDR = (SERVER_IP, PORT)
DM = "@disconnect"