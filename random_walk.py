import random
import matplotlib.pyplot as plt

def random_walk(num_steps, prob_right, num_particles):
    #meu codigo

    create_plot(num_steps, particle_paths)

    return particle_paths

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