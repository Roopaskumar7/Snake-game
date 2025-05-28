import pygame
import time
import random

# Initialize pygame
pygame.init()

# CONFIGURATION
WIDTH, HEIGHT = 800, 600
BLOCK_SIZE = 20
FPS = 15

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 255)
GRAY = (100, 100, 100)

# Fonts
FONT_STYLE = pygame.font.SysFont("comicsansms", 35)
SCORE_FONT = pygame.font.SysFont("comicsansms", 25)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game - Python Pro Edition')

clock = pygame.time.Clock()


#  FUNCTIONS 

def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, GREEN, [x[0], x[1], snake_block, snake_block])


def draw_score(score):
    value = SCORE_FONT.render("Score: " + str(score), True, BLUE)
    screen.blit(value, [10, 10])


def message(msg, color):
    mesg = FONT_STYLE.render(msg, True, color)
    screen.blit(mesg, [WIDTH / 6, HEIGHT / 3])


def game_loop():
    game_over = False
    game_close = False

    x = WIDTH // 2
    y = HEIGHT // 2

    dx = 0
    dy = 0

    snake_list = []
    length_of_snake = 1

    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 20.0) * 20.0
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 20.0) * 20.0

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            message("Game Over! Press Q-Quit or C-Play Again", RED)
            draw_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx = -BLOCK_SIZE
                    dy = 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx = BLOCK_SIZE
                    dy = 0
                elif event.key == pygame.K_UP and dy == 0:
                    dy = -BLOCK_SIZE
                    dx = 0
                elif event.key == pygame.K_DOWN and dy == 0:
                    dy = BLOCK_SIZE
                    dx = 0

        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        x += dx
        y += dy

        screen.fill(GRAY)
        pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(BLOCK_SIZE, snake_list)
        draw_score(length_of_snake - 1)

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 20.0) * 20.0
            food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 20.0) * 20.0
            length_of_snake += 1

        clock.tick(FPS)

    pygame.quit()
    quit()


#  RUN GAME 
if __name__ == "__main__":
    game_loop()
