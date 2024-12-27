import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))

screen.fill((58,58,58))

Blood_Red = (153, 9, 9)
Teal = (17, 212, 212)

pygame.draw.circle(screen, Blood_Red, (300, 300), 50)
pygame.draw.circle(screen, Teal, (200, 200), 70,20)
pygame.display.update()

done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
pygame.quit


