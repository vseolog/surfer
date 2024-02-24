import matplotlib.pyplot as plt
import math
import matplotlib.animation as animation
from matplotlib.animation import writers
import keyboard

fig = plt.figure()
ax = fig.add_subplot(111)
axes = plt.gca()


##------One-dimension wave simulation

#-------Settings-------------
area_size = 300
K = 0.1
speed_coef = 1
K2=0.0005
player_k = 0.07
player_v_attenuation = 0.9
#----------------------------


nodes = [0 for i in range(area_size)]
velocity = [0 for i in range(area_size)]
nodes_prev = list(nodes)
#velocity = [0 for i in range(area_size)]
player_pos = 35
player_v = 0
player_h = 0
print(nodes)

def disturb(x,y,amplitude):
    global nodes
    for k in range(x,y):
        nodes[k] = amplitude

def update():
    global nodes,nodes_prev,player_v,player_pos,player_h
    for i in range(area_size):
        if i == round(player_pos):
            player_v = player_v_attenuation * player_v
            player_pos += player_v
            player_h = nodes_prev[i]
            if i == area_size -1 or i <=2:
                player_pos = area_size//2
            else:
                player_v-=player_k*(nodes_prev[i+1]-nodes_prev[i])
        if i == 0:
            velocity[i] += K2*(nodes_prev[i+1]-nodes_prev[i])
        elif i == area_size-1:
            velocity[i] += K2*(nodes_prev[i-1] - nodes_prev[i])
        else:
            velocity[i] +=K * ((nodes_prev[i+1]-nodes_prev[i]) + (nodes_prev[i-1]-nodes_prev[i]))
        nodes[i] += velocity[i]
        velocity[i] = speed_coef * velocity[i]
    
    nodes_prev = list(nodes)
f = 0
def anim(i):
    global f
    '''if keyboard.is_pressed('d'):
        disturb(100,150,3)
        f = 1
    if f == 1 and i%10== 0:
        disturb(100,15,0)
        f=2
    if f==2:
        disturb(100,150,0)'''
    if i < 60:    
        disturb(50,70,2*math.sin(0.15*i))
        # disturb(30,40,2*math.sin(0.09*i))
        # disturb(50,60,2*math.sin(0.09*i))
    
    
    update()
    ax.clear()
    ax.set_ylim(-3,3)
    ax.plot(nodes)
    ax.plot(player_pos,player_h,'ro')
    # print(player_pos,player_v)
    print(i/10)
   
        #break

ani = animation.FuncAnimation(fig, anim,frames=1000, cache_frame_data=False)
# plt.show()
Writer = writers['ffmpeg']
writer = Writer(fps=30,bitrate=1800)

ani.save('player position-2.mp4',writer)