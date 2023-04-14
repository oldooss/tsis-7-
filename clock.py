import pygame
from datetime import datetime


def main():

    # initialization for python
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    # to get current time
    curr_time = datetime.now()
    curr_sec = curr_time.second
    curr_min = curr_time.minute

    # images
    clock_image = pygame.transform.scale(pygame.image.load('C:/Users/Admin/pyimages/mickeyclock.jpeg'), (800, 600))

    sechand_image = pygame.image.load('C:/Users/Admin/pyimages/sechand.png')
    sechand_image = pygame.transform.scale(sechand_image, (250,50))
    sechand_rect = sechand_image.get_rect()
    sechand_rect.center = (400, 300)

    minhand_image = pygame.image.load('C:/Users/Admin/pyimages/minhand.png')
    minhand_image = pygame.transform.scale(minhand_image, (200, 50))
    minhand_rect = minhand_image.get_rect()
    minhand_rect.center = (400, 300)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        screen.fill(0)
        screen.blit(clock_image, (0, 0))

        rotation_minhand = pygame.transform.rotate(minhand_image, -1 * (6 * curr_min) - 90)
        rotation_minhand_rect = rotation_minhand.get_rect()
        rotation_minhand_rect.center = minhand_rect.center
        screen.blit(rotation_minhand, rotation_minhand_rect)

        rotation_sechand = pygame.transform.rotate(sechand_image, -1 * (6 * curr_sec) + 90)
        rotation_sechand_rect = rotation_sechand.get_rect()
        rotation_sechand_rect.center = sechand_rect.center
        screen.blit(rotation_sechand, rotation_sechand_rect)

        curr_time = datetime.now()
        curr_sec = curr_time.second
        curr_min = curr_time.minute

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    pygame.init()
    main()
    pygame.quit()

