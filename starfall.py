import pygame
import sys
import random

pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My First Python Game")

#player
player_size = 50
player_x = width // 2
player_y = height // 2
speed = 5

#enemy
enemy_size = 50
enemy_x = 400
enemy_y = 0
enemy_speed = 4

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

    score = 0

    if enemy_y > height:
        enemy_y = 0
        enemy_x = random.randint(0, 800)
        score += 1


    screen.fill((60, 30, 30))

    pygame.draw.rect(screen, (0, 225, 0), (player_x, player_y, player_size, player_size)) # RGB value: green
    pygame.draw.rect(screen, (255, 0, 0),(enemy_x, enemy_y, enemy_size, enemy_size))

    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size)

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    if player_rect.colliderect(enemy_rect):
        print("Game over!")
        running = False

    pygame.display.flip()

pygame.quit()

sys.exit()

