import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def are_floats_equal(a, b, epsilon):
    return abs(a - b) < epsilon

def ball_collided(pos1, pos2, radius):
   radius = 0.1
  
   distance_ball = abs(pos1 - pos2)
   
   return distance_ball < 2*radius or are_floats_equal(distance_ball, 2*radius, 0.000001)

def wall_collided(pos, box_size, radius):
   return pos - radius < 0 or pos + radius > box_size or are_floats_equal(pos, radius, 0.000001) or are_floats_equal(pos + radius, box_size, 0.000001)
   
def simulate_collision ( initial_pos1 , initial_pos2 , initial_velocity1 ,
initial_velocity2 , mass1 , mass2 , num_frames , box_size ):
    #antes dos corpos colidirem
    ball1_x = [initial_pos1]                     
    ball2_x = [initial_pos2]        
    radius = 0.1
                                             
    frame_counter = 0                                               

    current_pos_1 = initial_pos1
    current_pos_2 = initial_pos2
    current_vel1 = initial_velocity1
    current_vel2 = initial_velocity2

    while frame_counter < num_frames:                                
        if ball_collided(current_pos_1, current_pos_2, radius):
           #bolas colidiram, formula deduzida atraves conserv. do momento linear e Energia cinetica
           current_vel1 = ((mass1 - mass2)*initial_velocity1/(mass1+mass2)) + (2*mass2*initial_velocity2)/(mass1+mass2)    
           current_vel2 = ((mass2 - mass1)*initial_velocity2/(mass1+mass2)) + (2*mass1*initial_velocity1)/(mass1+mass2)
       
       
        if wall_collided(current_pos_1, box_size, radius):
           current_vel1 = -current_vel1
        

        if wall_collided(current_pos_2, box_size, radius):
           current_vel2 = -current_vel2
     
        current_pos_1 += current_vel1
        current_pos_2 += current_vel2    

        ball1_x.append(current_pos_1)                          
        ball2_x.append(current_pos_2)   

        frame_counter += 1


    create_animation(ball1_x , ball2_x , box_size)

    return

def create_animation (positions1 , positions2 , box_size ):

    num_frames = len ( positions1 )

    fig , ax=plt.subplots()

    ax.set_xlim(0, box_size)

        
    ax.set_ylim ( -0.1, 0.1)

    ball1, = ax.plot(positions1[0], 0, "bo", markersize=10)

    ball2, = ax.plot(positions2[0], 0, "ro", markersize=10)

    def update(frame ):
     ball1.set_xdata(positions1[frame]) 

     ball2.set_xdata(positions2[frame]) 

     return ball1 , ball2

    ani = FuncAnimation( fig , update , frames= num_frames , blit=True)
    plt .show()


    plt.close(fig)


initial_pos1 = 1
initial_pos2 = 4
initial_velocity1 = 0.1
initial_velocity2 = -0.1
mass1 = 1
mass2 = 1.5
num_frames = 100
box_size = 5

simulate_collision(initial_pos1 , initial_pos2 , initial_velocity1 ,
initial_velocity2 , mass1 , mass2 , num_frames , box_size)