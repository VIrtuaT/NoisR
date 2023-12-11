import pygame 
import sys
import random
import math 

# Initialize Pygame
pygame.init

# Constants
PI = math.pi
WIDTH, HEIGHT = 800, 600
FPS = 60
PARTICLE_RADIUS = 10
NUM_PARTICLES = 50
MAX_SPEED = 2
START_SPEED = random.uniform(0, MAX_SPEED)
START_ANGLE = random.uniform(0, 2*PI)

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Particle class
class Particle:
    def __init__(self, x, y, is_tracer=False):
        self.x = x
        self.y = y
        self.radius = PARTICLE_RADIUS
        self.color = RED
        self.speed = START_SPEED
        self.angle = START_ANGLE
        self.is_tracer = is_tracer
        self.path = []

    def move(self):
        START_POSITION = [self.x, self.y]
        START_x_VELOCITY = START_SPEED * math.cos(START_ANGLE)
        START_y_VELOCITY = START_SPEED * math.sin(START_ANGLE)
        current_velocity = START_SPEED
        current_x_velocity = START_x_VELOCITY
        current_y_velocity = START_y_VELOCITY
        current_position = [START_POSITION[0] + START_x_VELOCITY, START_POSITION[1] + START_y_VELOCITY]
        current_angle = START_ANGLE

        if self.check_collision(self, other_particle): 
            # you can find these expressions in collisions wikipedia, simplified since m1 = m2
            contact_angle = 0          
            velocity2 = 0  #other_particle velocity
            velocity1 = current_velocity
            angle1 = current_angle
            angle2 = 0 #other_particle angle
            current_x_velocity = (velocity2*math.cos(angle2 - contact_angle))*math.cos(contact_angle) + velocity1*math.sin(angle1 - contact_angle)*math.cos(contact_angle+(PI/2))
            current_y_velocity = (velocity2*math.cos(angle2 - contact_angle))*math.sin(contact_angle) + velocity1*math.sin(angle1 - contact_angle)*math.sin(contact_angle+(PI/2))
            
        return current_position






    
    def wall_collision(self):
        pass

    
    def particle_collision(self):
        pass
    def check_collision(self, other_particle):
        return True
    
# Create particles
particles = []

for i in (0, NUM_PARTICLES):
    particles.append(Particle(random.uniform(0, WIDTH), random.uniform(0, HEIGHT), False))

# Choose one particle as a tracer
tracer_index = random.randint(0, NUM_PARTICLES - 1) 

#Set up Pygame screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brownian Motion Simulation")
clock = pygame.time.Clock()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move particles and check collisions
    for particle in particles:
        particle.move()

    # Draw particles and paths
    screen.fill(WHITE)
    for particle in particles:
        pygame.draw.circle(screen, particle.color, (int(particle.x), int(particle.y), particle.radius))

        # Draw path for the tracer
        if particle.is_tracer and len(particle.path) >= 2:
            pygame.draw.lines(screen, particle.color, False, particle.path, 2)
    
    pygame.display.flip()
    clock.tick(FPS)