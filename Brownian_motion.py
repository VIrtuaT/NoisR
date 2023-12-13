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

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

PARTICLE_COUNTER = 0

def random_starting_speed():
    return random.uniform(0, MAX_SPEED)

def random_starting_angle():
    return random.uniform(0, 2*PI)

# Particle class
class Particle:
    def __init__(self, x, y, is_tracer=False):
        global PARTICLE_COUNTER
        PARTICLE_COUNTER += 1
        # particle number
        self.id = PARTICLE_COUNTER
        self.x = x
        self.y = y
        
        self.radius = PARTICLE_RADIUS
        self.path = []

        self.current_position  = pygame.math.Vector2(self.x, self.y)

        self.speed = random_starting_speed()
        self.angle = random_starting_angle()
        self.current_angle = self.angle
        self.current_velocity = pygame.math.Vector2(self.speed * math.cos(self.angle), self.speed * math.sin(self.angle))
        
        self.is_tracer = is_tracer
        if is_tracer:
            self.color = RED
        else:
            self.color = BLUE

    def move(self):   
        self.current_position = self.current_position + self.current_velocity 
        
        if self.is_wall_collision():
            # right wall collision
            if self.x >= WIDTH - PARTICLE_RADIUS:
                self.current_velocity.x *= -1
                self.current_position -= (2,0)
            # left wall
            if self.x <= PARTICLE_RADIUS:
                self.current_velocity.x *= -1
                self.current_position += (2,0)
            
            # floor
            if self.y <= PARTICLE_RADIUS:
                self.current_velocity.y *= -1
                self.current_position += (0,2)
            
            # ceiling
            if self.y > HEIGHT - PARTICLE_RADIUS:
                 self.current_velocity.y *= -1
                 self.current_position -= (0,2)
            
    
        for other_particle in particles:
            if other_particle.id == self.id:
                continue      
            if self.is_particle_collision(other_particle):
                # you can find these expressions in collisions wikipedia, simplified since m1 = m2
                contact_angle = math.atan2(self.current_velocity.x, self.current_velocity.y)
                velocity1 = self.current_velocity
                velocity2 = other_particle.current_velocity
                angle1 = self.current_angle
                angle2 = other_particle.current_angle
                self.current_velocity.x = (velocity2.x*math.cos(angle2 - contact_angle))*math.cos(contact_angle) + velocity1.x*math.sin(angle1 - contact_angle)*math.cos(contact_angle+(PI/2))
                self.current_velocity.y = (velocity2.y*math.cos(angle2 - contact_angle))*math.sin(contact_angle) + velocity1.y*math.sin(angle1 - contact_angle)*math.sin(contact_angle+(PI/2))

                self.current_velocity = other_particle.current_velocity 
        self.x = self.current_position.x
        self.y = self.current_position.y
        self.angle = self.current_angle

    def is_wall_collision(self):
        # right wall
        if self.x >= WIDTH - PARTICLE_RADIUS:
            return True
        # left wall
        if self.x <= PARTICLE_RADIUS:
            return True
        # floor
        if self.y <= PARTICLE_RADIUS:
            return True
        # ceiling
        if self.y > HEIGHT - PARTICLE_RADIUS:
            return True
        return False

    #precisamos de arranjar uma forma de arranjar os atributos da other_particle
    def is_particle_collision(self, other_particle):
        return False
        #particle_distance = 100 #calcular distancia entre a particula e outra

        #if particle_distance <= 2*PARTICLE_RADIUS:
           # return True
    
# Create particles
# And choose one particle as a tracer
tracer_index = random.randint(0, NUM_PARTICLES - 1)

particles = []
for i in range(NUM_PARTICLES):
    random_x = random.uniform(0, WIDTH)
    random_y = random.uniform(0, HEIGHT)
    if i == tracer_index:
        particles.append(Particle(random_x, random_y, True))
    else:
        particles.append(Particle(random_x, random_y, False))
    

#--------------------------------------------------------------------------------------------------------
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
        pygame.draw.circle(screen, particle.color, (int(particle.x), int(particle.y)), particle.radius)

        # Draw path for the tracer
        if particle.is_tracer and len(particle.path) >= 2:
            pygame.draw.lines(screen, particle.color, False, particle.path, 2)
    
    pygame.display.flip()
    clock.tick(FPS)