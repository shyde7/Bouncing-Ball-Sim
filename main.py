# Example file showing a circle moving on screen
import pygame
import math
import random

# pygame setup
pygame.init()

pygame.display.set_caption("Bouncing Ball Sim")
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

balls = []

ball_radius = 200
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

class Ball:
    def __init__(self,x,y,radius,color,speed_x,speed_y):
        self.pos = pygame.Vector2(x,y)
        self.radius = radius
        self.color = color
        self.speed = pygame.Vector2(speed_x, speed_y)
        
    def move(self, dt, center, container_radius):
        self.pos += self.speed * dt

        distance_from_center = self.pos.distance_to(center)
        if distance_from_center + self.radius > container_radius:
            to_center = (self.pos - center).normalize()
            self.speed = self.speed.reflect(to_center)
            self.pos = center + to_center * (container_radius - self.radius)
            
    def draw(self, screen):
        pygame.draw.circle(screen,self.color, (int(self.pos.x), int(self.pos.y)), self.radius)
            
        


speed = [1,1]


def spawnRandCircleOnPress(center, container_radius):
    color_names = ["red", "blue", "white", "purple", "green"]
    color_picked = random.choice(color_names)
    circle_size = [2,5,10,15,20,7,25]
    size_picked = random.choice(circle_size)
    
    while True:
        spawn_x = random.uniform(center.x - container_radius, center.x + container_radius )
        spawn_y = random.uniform(center.y - container_radius, center.y + container_radius )
        spawn_pos = pygame.Vector2(spawn_x, spawn_y)
        if spawn_pos.distance_to(center) + size_picked <= container_radius:
            break

        
        
    speed_x = random.uniform(-200, 200)
    speed_y = random.uniform(-200, 200)

        
    new_ball = Ball(spawn_x, spawn_y, size_picked, color_picked, speed_x, speed_y)
    balls.append(new_ball)
    
def spawnSingleBall(center, container_radius):
    color_names = ["red", "blue", "white", "purple", "green"]
    color_picked = random.choice(color_names)
    circle_size = [2,5,10,15,20,7,25]
    size_picked = random.choice(circle_size)
    
    while True:
        spawn_x = random.uniform(center.x - container_radius, center.x + container_radius )
        spawn_y = random.uniform(center.y - container_radius, center.y + container_radius )
        spawn_pos = pygame.Vector2(spawn_x, spawn_y)
        if spawn_pos.distance_to(center) + size_picked <= container_radius:
            break

        
        
    speed_x = random.uniform(-200, 200)
    speed_y = random.uniform(-200, 200)

        
    new_ball = Ball(spawn_x, spawn_y, size_picked, color_picked, speed_x, speed_y)
    balls.append(new_ball)
    
    


while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    
    center_circle = pygame.draw.circle(screen, "white", player_pos, ball_radius, 3)



    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
    if keys[pygame.K_q]:
        pygame.quit()
    if keys[pygame.K_SPACE]:
        spawnRandCircleOnPress(player_pos, ball_radius)
        
    for ball in balls:
        ball.move(dt, player_pos, ball_radius)
        ball.draw(screen)
        
        
        

        

    pygame.display.flip()

   
    dt = clock.tick(60) / 1000

pygame.quit()