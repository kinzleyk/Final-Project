import pygame

pygame.init()

screen = pygame.display.set_mode((900, 650))
pygame.display.set_caption("Character Design Editor")

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill ("#F4F0FA")

    pygame.display.flip()
    clock.tick(60)

pygame.quit()