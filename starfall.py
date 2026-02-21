import pygame
import sys
import random

pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Starfall")

background_img = pygame.image.load("background.png").convert()
player_img =pygame.image.load("player img.png").convert_alpha()
enemy_img = pygame.image.load("enemy.png").convert_alpha()

player_img = pygame.transform.scale(player_img, (50, 50))
enemy_img = pygame.transform.scale(enemy_img, (50, 50))
background_img = pygame.transform.scale(background_img, (width, height))


#player attributes
player_size = 50
player_x = width // 2
player_y = height // 2
speed = 5

#enemy attributes
enemy_size = 50
enemy_x = 400
enemy_y = 0
enemy_speed = 4

#game variables
score = 0
level = 1
points_per_level = 5

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= speed
    if keys[pygame.K_RIGHT]:
        player_x += speed
    if keys[pygame.K_UP]:
        player_y -= speed
    if keys[pygame.K_DOWN]:
        player_y += speed

    enemy_y += enemy_speed

    if enemy_y > height:
        enemy_y = 0
        enemy_x = random.randint(0, 750)
        score += 1

    #level system
    if score >= level * points_per_level:
        level += 1
        enemy_speed += 1


    screen.blit(background_img, (0, 0))

    screen.blit(player_img, (player_x, player_y))
    screen.blit(enemy_img, (enemy_x, enemy_y))


    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size)

    # Draw UI
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    level_text = font.render(f"Level: {level}", True, (200, 200, 255))

    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 50))

    if player_rect.colliderect(enemy_rect):
        print("Game over!")
        running = False

    pygame.display.flip()

pygame.quit()
sys.exit()

