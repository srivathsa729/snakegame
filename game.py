import pygame
import time
import random

pygame.init()

dis_width = 400
dis_length = 400

dis = pygame.display.set_mode((dis_width, dis_length))
pygame.display.update()
pygame.display.set_caption("Snake Game")

blue = (0, 0, 156)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 102)
green = (0, 255, 255)

snake_block = 10
snake_speed = 10

font_style = pygame.font.SysFont("bahnschrift", 10)
score_font = pygame.font.SysFont("comicsansms", 35)

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

def my_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/5, dis_length/5])

clock = pygame.time.Clock()

def gameLoop():

    game_over = False
    game_close = False

    x_pos = dis_width/2
    y_pos = dis_width/2
    x_change = 0
    y_change = 0

    snakeList = []
    snakeLength = 1

    foodx = round(random.randrange(0, dis_width - snake_block)/10) * 10
    foody =  round(random.randrange(0, dis_length - snake_block)/10) * 10

    while not game_over:

        while game_close == True:
            dis.fill(white)
            message("Game Over! Press Q - Quit C - New Game", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            pygame.display.update()
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = snake_block
                elif event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -snake_block
                elif event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0

        x_pos += x_change
        y_pos += y_change

        if x_pos + snake_block > dis_width or x_pos < 0 or y_pos + snake_block > dis_length or y_pos < 0:
            game_close = True

        dis.fill(blue)

        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x_pos)
        snake_head.append(y_pos)
        snakeList.append(snake_head)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for x in snakeList[:-1]:
            if x == snake_head:
                game_close = True

        my_snake(snake_block, snakeList)
        Your_score(snakeLength - 1)

        pygame.display.update()

        if x_pos == foodx and y_pos == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10) * 10
            foody = round(random.randrange(0, dis_length - snake_block) / 10) * 10
            snakeLength += 1

        pygame.display.update()
        clock.tick(snake_speed)


    pygame.display.update()

    pygame.quit()
    quit()


gameLoop()
