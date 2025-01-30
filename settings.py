# GAME
RATIO = 0.5
RESOLUTION = WIDTH, HEIGHT = 1700*RATIO, 1100*RATIO
PLAYER_BUDGET = 1500

# needed to differentiate between players, gonna use 1 example and to change later
names = [chr(65+i)+str(j) for i in range(20) for j in range(1,100)]
colors = ['red', 'green', 'blue', 'cyan', 'yellow', 'magenta', 'white']
positions = [
  (0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0), (8,0), (9,0),  (10,0), 
  (10,1),  (10,2),  (10,3),  (10,4), (10,5),  (10,6),  (10,7),  (10,8),  (10,9), 
  (10,10),  (9,10), (8,10),  (7,10),  (6,10),  (5,10),  (4,10),  (3,10),  (2,10), 
  (1,10),  (0,10),  (0,9),  (0,8),  (0,7),  (0,6),  (0,5), (0,4),  (0,3),  (0,2),  (0,1)
  ]


f = lambda txt, idx : txt.split(',')[idx]

# SOCKETS
SERVER_IP = "192.168.1.12"
PORT = 12345
HEADER= 128
FORMAT = 'utf-8'
ADDR = (SERVER_IP, PORT)
DM = "@disconnect"