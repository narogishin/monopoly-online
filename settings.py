# GAME
RATIO = 0.5
RESOLUTION = WIDTH, HEIGHT = 1100*RATIO, 1100*RATIO

# needed to differentiate between players, gonna use 1 example and to change later
names = [chr(65+i)+str(j) for i in range(20) for j in range(1,100)]
colors = ['red', 'green', 'blue', 'cyan', 'yellow', 'magenta', 'white']
positions = {
  0: (0,0), 1: (1,0), 2: (2,0), 3: (3,0), 4: (4,0), 5: (5,0), 6: (6,0),
  7: (7,0), 8: (8,0), 9: (9,0), 10: (10,0), 11: (10,1), 12: (10,2), 13: (10,3), 14: (10,4),
   15: (10,5), 16: (10,6), 17: (10,7), 18: (10,8), 19: (10,9), 20: (10,10), 21: (9,10),
     22: (8,10), 23: (7,10), 24: (6,10), 25: (5,10), 26: (4,10), 27: (3,10), 28: (2,10),
       29: (1,10), 30: (0,10), 31: (0,9), 32: (0,8), 33: (0,7), 34: (0,6), 35: (0,5),
         36: (0,4), 37: (0,3), 38: (0,2), 39: (0,1)
         }
# f = lambda txt, idx: txt.split(',')[idx]

# SOCKETS
SERVER_IP = "192.168.1.16"
PORT = 12345
HEADER= 128
FORMAT = 'utf-8'
ADDR = (SERVER_IP, PORT)
DM = "@disconnect"