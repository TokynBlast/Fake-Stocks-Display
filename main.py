import random, time

def clr():print('\033[2J\033[H', end='')

# ANSI escape codes for colors
RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"

import random
import time

# ANSI escape codes for colors
RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"

stocks = ["JPL", "GPA", "FRJ", "GME", "AMZ", "APL", "MSF", "TSL", "CZL", "NFX", "TSA", "GOG", "FBI", "NDA", "JPM", "ORC"]

GC_NUM = [[' '] * 23 for _ in range(11)]
start = random.randint(0, 10)
DIRP = '▼'
GC_NUM[start][0] = DIRP

# Setup the grid
for i in range(1):
    DIR = random.randint(0, 1)
    
    UD = []
    U = 0
    D = 0
    for stock in stocks:
      up = random.choice([True, False])
      UD.append(up)
      if up:
          print(f"{stock} {GREEN}▲{RESET}")
      else:
          print(f"{stock} {RED}▼{RESET}")
    time.sleep(0.5)
    clr()
    for dir in UD:
      if dir == True: DIRP = GREEN + '▲' + RESET
      else:  DIRP = RED + '▼' + RESET

    GC_NUM[start][i] = DIRP

while True:
  UD = []
  U = 0
  D = 0
  for stock in stocks:
    up = random.choice([True, False])
    UD.append(up)
    if up:
        print(f"{stock} {GREEN}▲{RESET}")
    else:
        print(f"{stock} {RED}▼{RESET}")
  time.sleep(0.5)
  #clr()
  for dir in UD:
    if dir == True: U += 1
    else:  D += 1
  time.sleep(.5)
  for i in range(len(GC_NUM)):
      GC_NUM[i].remove(GC_NUM[i][0])
      GC_NUM[i].append(' ')

  if U < D and start - 1 > -1:
      start -= 1
      DIRP = RED + '▼' + RESET
  elif U > D and start + 1 < 11:
      start += 1
      DIRP = GREEN + '▲' + RESET

  GC_NUM[start][22] = DIRP
  GC = f'''\x1b[38;2;0;255;0m
  {''.join(GC_NUM[10])}\x1b[38;2;0;0;0m├─ 10
  {''.join(GC_NUM[9])}\x1b[38;2;0;0;0m├─ 9
  {''.join(GC_NUM[8])}\x1b[38;2;0;0;0m├─ 8
  {''.join(GC_NUM[7])}\x1b[38;2;0;0;0m├─ 7
  {''.join(GC_NUM[6])}\x1b[38;2;0;0;0m├─ 6
  {''.join(GC_NUM[5])}\x1b[38;2;0;0;0m├─ 5
  {''.join(GC_NUM[4])}\x1b[38;2;0;0;0m├─ 4
  {''.join(GC_NUM[3])}\x1b[38;2;0;0;0m├─ 3
  {''.join(GC_NUM[2])}\x1b[38;2;0;0;0m├─ 2
  {''.join(GC_NUM[1])}\x1b[38;2;0;0;0m├─ 1
  {''.join(GC_NUM[0])}\x1b[38;2;0;0;0m├─ 0
  \x1b[38;2;0;0;0m───────────────────────┘\033[0m'''
  clr()
  print(GC)
