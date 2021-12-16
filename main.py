import pygame
import Life as lf

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Движущийся круг 2')
    size = width, height = 400, 400
    screen = pygame.display.set_mode(size)

    game = lf.Life(5, 5, 50)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                game.get_click(event.pos)

        screen.fill((0, 0, 0))
        game.render(screen)
        pygame.display.flip()