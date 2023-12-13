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
        
        self.future_position = self.current_position + self.current_velocity

        self.is_tracer = is_tracer
        if is_tracer:
            self.color = RED
        else:
            self.color = BLUE
        

    def move(self):   
        self.current_position = self.current_position + self.current_velocity 
      
        if self.is_tracer:
            self.path.append(self.current_position)
            
        if self.is_wall_collision():
            # right wall 
            if self.future_position.x >= WIDTH - PARTICLE_RADIUS:
                # supposedly avoids some errors, not sure yet
                if self.current_velocity.x < 0:
                    pass
                else:
                    self.current_velocity.x *= -1
                
            # left wall
            if self.future_position.x <= PARTICLE_RADIUS:
                self.current_velocity.x *= -1
               
            # floor
            if self.future_position.y <= PARTICLE_RADIUS:
                self.current_velocity.y *= -1
             
            
            # ceiling
            if self.future_position.y > HEIGHT - PARTICLE_RADIUS:
                self.current_velocity.y *= -1
                 
            
        for other_particle in particles:
            if other_particle.id == self.id:
                continue      
            if self.is_particle_collision(other_particle):
                # makes balls sticky rarely??
                self.current_velocity, other_particle.current_velocity = other_particle.current_velocity, self.current_velocity 

        self.x = self.current_position.x
        self.y = self.current_position.y
        self.angle = self.current_angle
        self.future_position = self.current_position + self.current_velocity


    def is_wall_collision(self):
        # right wall
        if self.future_position.x >= WIDTH - PARTICLE_RADIUS:
            return True
        # left wall
        if self.future_position.x <= PARTICLE_RADIUS:
            return True
        # floor
        if self.future_position.y <= PARTICLE_RADIUS:
            return True
        # ceiling
        if self.future_position.y > HEIGHT - PARTICLE_RADIUS:
            return True
        return False

   
    def is_particle_collision(self, other_particle):
       distance = self.future_position.distance_to(other_particle.future_position)
       if distance <= 2*PARTICLE_RADIUS:
           return True
       else:
           return False

    
# Create particles
# And choose one particle as a tracer
tracer_index = random.randint(0, NUM_PARTICLES - 1)

particles = []
for i in range(NUM_PARTICLES):
    random_x = random.uniform(0 + PARTICLE_RADIUS, WIDTH - PARTICLE_RADIUS)
    random_y = random.uniform(0 + PARTICLE_RADIUS, HEIGHT - PARTICLE_RADIUS)
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