# Pong
# Written by Andrew Bailey
# CS 235

import pygame, sys
import random

pygame.init()
clock = pygame.time.Clock()

class moving_object:
    # moving object is used for both players and the ball
    velocityX = 5    # Adjusting velocity will increase or decrease difficulty
    velocityY = 5
    score_p1 = 0
    score_p2 = 0    

    def __init__(self, velocityX, velocityY):   #default constructor
        self.velocityX = velocityX
        self.velocityY = velocityY


    def change_yup(self, change):
        self.velocityY += change
        
    
    def change_ydown(self, change):
        self.velocityY -= change



screen_width = 980
screen_height = 660
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')

#text_variables
score_p1 = 0
score_p2 = 0
font = pygame.font.Font(None, 40)
#global score_p1
#global score_p2

# Set parameters for the players and ball
ball = pygame.Rect(int(screen_width/2 - 15), int(screen_height/2 - 15),30,30)
center_circle = pygame.Rect(int(screen_width/2 - 75), int(screen_height/2 - 75), 150, 150 )
player1 = pygame.Rect(int(screen_width - 10), int(screen_height/2 - 70),10,140)
player2 = pygame.Rect(10, int(screen_height/2 - 70),10,140)


# Customizable background and individual piece colors
game_color = (50, 200, 200)
background_color = (100, 100, 100)
circle_color = (0, 70, 10)


# Handle all collisions and movement of the Ball
def ball_movement():        # handle collisions
    ball_velocity = moving_object
    global score_p1
    global score_p2
  

    ball.x += ball_velocity.velocityX 
    ball.y += ball_velocity.velocityY 

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_velocity.velocityY *= -1

    if ball.left <= 0:
        score_p1 += 1
        ball_reset(ball_velocity)
        

    if ball.right >= screen_width:
        score_p2 += 1
        ball_reset(ball_velocity)
        
    
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_velocity.velocityX *= -1


# Handle ball going out of bounds
def ball_reset(ball_velocity):
    ball.center = (screen_width/2, screen_height/2)
    ball_velocity.velocityY *= random.choice((1,-1))
    ball_velocity.velocityX *= random.choice((1,-1))


# Handles movement of each player
def player_movement():

    #Player 1 Controls
    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_DOWN:
                player1_velocity.change_yup(5)
        if event.key == pygame.K_UP:
                player1_velocity.change_ydown(5)

    if event.type == pygame.KEYUP:

        if event.key == pygame.K_DOWN:
                player1_velocity.change_ydown(5)
        if event.key == pygame.K_UP:
                player1_velocity.change_yup(5)

    #Player 2 Controls
    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_s:
                player2_velocity.change_yup(5)
        if event.key == pygame.K_w:
                player2_velocity.change_ydown(5)

    if event.type == pygame.KEYUP:

        if event.key == pygame.K_s:
                player2_velocity.change_ydown(5)
        if event.key == pygame.K_w:
                player2_velocity.change_yup(5)





# Keeps both players within the screen bounds
def bounds_check():
    if player1.top <= 0:
        player1.top = 0
    if player1.bottom >= screen_height:
        player1.bottom = screen_height

    if player2.top <= 0:
        player2.top = 0
    if player2.bottom >= screen_height:
        player2.bottom = screen_height

# Initialize objects for each of the Players
player1_velocity = moving_object(0, 0)
player2_velocity = moving_object(0, 0)

# Main game loop
while True: 
    
    for event in pygame.event.get():

        # Handle closing program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        player_movement()

    ball_movement()
    bounds_check()
    
    
    player1.y += player1_velocity.velocityY 
    player2.y += player2_velocity.velocityY


    # Draw everything
    screen.fill(background_color)
    pygame.draw.ellipse(screen, circle_color, center_circle)
    pygame.draw.rect(screen, game_color, player1)
    pygame.draw.ellipse(screen, game_color, ball)
    player_text = font.render(f"{score_p1}", False, game_color)
    player_text2 = font.render(f"{score_p2}", False, game_color)

    pygame.draw.rect(screen, game_color, player2)
    pygame.draw.aaline(screen, game_color, (screen_width/2, 2), (screen_width/2, screen_height), )
    screen.blit(player_text,(505,325))
    screen.blit(player_text2,(465,325))




    pygame.display.flip()

    # Run the game at 60fps
    clock.tick(60)
