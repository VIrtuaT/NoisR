import random
import matplotlib.pyplot as plt

class Particle:
    position : int
    
def create_particle_path(num_steps, prob_right) -> list :
    Particle.position = 0
    particle_path = [Particle.position]
    i = 0

    while i < num_steps:
        # random.random dá um float aleatorio entre 0 e 1 
        x = random.random()  

        if x <= prob_right:
            Particle.position += 1
       

        else:
            Particle.position -= 1

        particle_path.append(Particle.position)

        i += 1

    return particle_path
       
def random_walk(num_steps, prob_right, num_particles):
  
    u = 0
    walks = []

    while u < num_particles:
        u +=1

        temp = create_particle_path(num_steps, prob_right)

        walks.append(temp)
        

    create_plot(num_steps, walks)

def create_plot(num_steps, particle_paths):

    time = [x for x in range(len(particle_paths[0]))]

    for particle_path in particle_paths:
        plt.plot(particle_path, time)

    plt.title("Random Walk - N particles")
    plt.xlabel("Position")
    plt.ylabel("Time")
    plt.show()

num_steps = 100 #number of steps
prob_right = 0.5 #probability of moving to the right
num_particles = 10 #number of particles

random_walk(num_steps, prob_right, num_particles)