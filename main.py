import pygame
import random
from pygame import mixer

pygame.init()

mixer.music.load("Heavy Music.mp3")
mixer.music.play(-1)

screen = pygame.display.set_mode((800, 650))

# Colors to be used in the game.
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Font to be used in the game.
font = "JetBrainsMono-Bold.ttf"

# Snake parameters.
snake_x = 400
snake_y = 200
snake_size = 15
snake_list = []
snake_length = 1

# Snake movements.
velocity_x = 0
velocity_y = 0

# Snake function.
def snake_func(surface, color, body, wow):
    for x, y in body:
        pygame.draw.rect(surface, color, [x, y, wow, wow])

# Food parameters.
food_x = random.randint(50, 690)
food_y = random.randint(50, 550)
food_radius = 5

# Score variable and parameters.
score = 0
score_font = pygame.font.SysFont(font, 35)
score_x = 5
score_y = 5

# Score function.
def score_func():
    score_text = score_font.render(f"Score: {score}", True, white)
    screen.blit(score_text, [score_x, score_y])

# Game over parameters.
game_over_font = pygame.font.SysFont(font, 50)
game_over_x = 270
game_over_y = 290

# Game over function.
def game_over_func():
    global snake_y, snake_size, food_y
    snake_y, snake_size, food_y = 900000, 0, 900
    game_over_text = game_over_font.render("Game Over!", True, white)
    screen.blit(game_over_text, [game_over_x, game_over_y])

# Frames per second(fps).
fps = 400
clock = pygame.time.Clock()

while True:
    screen.fill((0, 0, 0))
    
    # Snake head.
    head = []

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if velocity_x != 1:
                    velocity_x = -1
                    velocity_y = 0
            elif event.key == pygame.K_RIGHT:
                if velocity_x != -1:
                    velocity_x = 1
                    velocity_y = 0
            elif event.key == pygame.K_UP:
                if velocity_y != 1:
                    velocity_y = -1
                    velocity_x = 0
            elif event.key == pygame.K_DOWN:
                if velocity_y != -1:
                    velocity_y = 1
                    velocity_x = 0

    snake_x += velocity_x
    snake_y += velocity_y

    if abs(snake_x-food_x) < 13 and abs(snake_y-food_y) < 13:
        food_x = random.randint(50, 690)
        food_y = random.randint(50, 550)
        score += 1
        snake_length += 25

    head.append(snake_x)
    head.append(snake_y)
    snake_list.append(head)

    if len(snake_list) > snake_length:
        del snake_list[0]

    if snake_x <= 0 or snake_x >= 800 or snake_y <= 0 or snake_y >= 650:
        game_over_func()
    for part in snake_list[:-1]:
        if part == head:
            game_over_func()
    
    # Drawing the food.
    pygame.draw.circle(screen, red, [food_x, food_y], food_radius)
    # Drawing the snake.
    snake_func(screen, green, snake_list, snake_size)
    # Displaying the score.
    score_func()
    # Render frames per second.
    clock.tick(fps)
    pygame.display.update()
