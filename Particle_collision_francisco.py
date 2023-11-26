import numpy as np
import matplotlib . pyplot as plt
from matplotlib . animation import FuncAnimation




def create_animation (positions1 , positions2 , box_size ):

    num_frames = len ( positions1 )


    fig , ax=plt.subplots()


    ax.set_xlim(0, box_size)

        
    ax.set_ylim ( −0.1, 0.1)

    ball1, = ax.plot(positions1[0], 0, ’bo’, markersize=10)

    ball2, = ax.plot(positions2[0], 0, ’ro’, markersize=10)

    def update(frame ):
     ball1.set_xdata(positions1[frame]) 

     ball2.set_xdata(positions2[frame]) 

    return ball1 , ball2
ani = FuncAnimation( fig , update , frames=num_frames , blit=True)
plt .show()


plt.close(fig )



def simulate_collision ( initial_pos1 , initial_pos2 , initial_velocity1 ,
initial_velocity2 , mass1 , mass2 , num_frames , box_size ):
    










    create_animation(ball1_x , ball2_x , box_size)

    return

