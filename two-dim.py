import matplotlib.pyplot as plt
import math
import matplotlib
import matplotlib.animation as animation
from matplotlib.animation import writers
# import keyboard
import matplotlib.cm as cm
fig = plt.figure()
ax = fig.add_subplot(111)
axes = plt.gca()


##------One-dimension wave simulation

#-------Settings-------------
area_size = 60
K = 0.2
speed_coef = 0.96
K2=0.05
#----------------------------


nodes = [[0 for j in range(area_size)] for i in range(area_size)]
velocity = [[0 for j in range(area_size)] for i in range(area_size)]

nodes_prev = list(nodes)
velocity_prev = list(velocity)
def disturb(fromx,tox,fromy,toy,amplitude):
    global nodes
    for i in range(fromx,tox):
        for j in range(fromy,toy):
            nodes[i][j] = amplitude
    

def update():
    global nodes,nodes_prev
    for m in range(area_size):
        for n in range(area_size):
            if n == 36 and m<20:
                nodes[m][n] = 0
            elif n == 36 and m>27 and m < 33:
                nodes[m][n] = 0
            elif n == 36 and m>40:
                nodes[m][n] = 0
            else:
                nodes[m][n]+=velocity[m][n]
                velocity[m][n] *= speed_coef
    for m in range(area_size):
        for n in range(area_size):
            if m == 0 or n == 0 or m == area_size-1 or n == area_size-1:
                velocity[m][n] = 0
            elif n == 35 and m<24:
                velocity[m][n] = 0
            elif n == 35 and m>35 and m < 35:
                velocity[m][n] = 0
            elif n == 35 and m>36:
                velocity[m][n] = 0
            else:
                velocity[m][n] +=K*(nodes[m-1][n]+nodes[m+1][n]+nodes[m][n-1]+nodes[m][n+1] - 4*nodes[m][n])
    # nodes_prev = list(nodes)

    ''' if i == 0:
            velocity[i] += K*(nodes_prev[i+1]-nodes_prev[i])
        elif i == area_size-1:
            velocity[i] += K*(nodes_prev[i-1] - nodes_prev[i])
        else:
            velocity[i] +=K* ((nodes_prev[i+1]-nodes_prev[i]) + (nodes_prev[i-1]-nodes_prev[i]))
        nodes[i] += velocity[i]
        velocity[i] = speed_coef * velocity[i]
    nodes_prev = list(nodes)'''
f = 0
def anim(i):
    global f    
    disturb(18,42,29,31,3.0*math.sin(0.5*i))
        # disturb(30,40,2*math.sin(0.09*i))
        # disturb(50,60,2*math.sin(0.09*i))
    
    update()
    ax.clear()
    # ax.set_ylim(-3,3)
    # u = []
    # for l in range(area_size):
        # u.append(nodes[l][54])
    # ax.plot(u)
    # u = []
    plt.imshow(nodes, extent=(0,area_size, 0, area_size),
           interpolation='gaussian', cmap=cm.Greys,norm=matplotlib.colors.Normalize(vmin=-3, vmax=3))
    print(i/10)
   
        #break

ani = animation.FuncAnimation(fig, anim,frames=400, cache_frame_data=False)
# plt.show()
Writer = writers['ffmpeg']
writer = Writer(fps=30,bitrate=1800)
ani.save('twoholes-2dim.mp4',writer)