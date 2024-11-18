import curses,time, copy, random

stdscr = curses.initscr()
curses.noecho()
curses.curs_set(0)
n=25
offset = 1

def countt(a):
    r=0
    h=0
    for sd in a:
        for dd in sd:
            if dd==1:
                r+=1
            else:
                h+=1
    return (r,h)


for i in range(n+offset+1):
    for j in range(n+offset+1):
        if i == 0 and j == 0:
            stdscr.addch(i, j, "╔")
        elif i == n+offset and j == 0:
            stdscr.addch(i, j, "╚")
        
        elif i == n+offset and j == n+offset:
            stdscr.addch(i, j, "╝")
        elif i == 0 and j == n+offset:
            stdscr.addch(i, j, "╗")
        elif j == 0 and i > 0 or j == n+offset and i>0:
            stdscr.addch(i, j, "║")   
        else:
            stdscr.addch(i, j, "═")        
            # stdscr.addch(i, j, str(j)) 

b = ((0,1), (1,0), (1,1), (-1,0), (0,-1), (-1, -1), (-1, 1), (1, -1))
# a = [[1 for j in range(n)] for i in range(n)]
# a = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
a = [[random.randint(0,1) for j in range(n)] for i in range(n)]
anew = copy.deepcopy(a)

for i in range(n):
        for j in range(n):
            stdscr.addch(i+offset, j+offset, "░" if anew[i][j] == 0 else '█')
stdscr.refresh()
time.sleep(0.1)
while True:
    for i in range(n):
        for j in range(n):
            g = 0
            for k in b:
                try:
                    if a[i+k[0]][j+k[1]] == 1 and i+k[0] > -1 and j+k[1] > -1:
                        g+=1
                except: pass
            if a[i][j]==1:
                if g == 2 or g == 3:
                    anew[i][j]=1
                else:
                    anew[i][j]=0
            elif a[i][j]==0:
                if g == 3:
                    anew[i][j]=1
            stdscr.addch(i+offset, j+offset, "░" if anew[i][j] == 0 else '█') #
    inittd=countt(a)
    stdscr.addstr(n+offset+1, 0,f" {inittd[0]} live | {inittd[1]} death")
    a = copy.deepcopy(anew) 
    stdscr.clrtoeol()
    stdscr.refresh()
    time.sleep(0.1)

curses.endwin()