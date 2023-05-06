# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
pygame.display.set_caption("MyGame")
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

count = 0 
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        # print("some action happened")
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    
    
    
    # font1 = pygame.font.SysFont('Calibri', 25, True, False)
    # test_text = font1.render("string getting upgdate", True, (255, 125, 0))
    # screen.blit(test_text, [25, 265])
    
    
    # font1 = pygame.font.SysFont('Calibri', 25, True, False)
    # test_text = font1.render("--------------------", True, (255, 125, 0))
    # screen.blit(test_text, [25, 265])
    
    # count  =count+1
    # font1 = pygame.font.SysFont('Calibri', 25, True, False)
    # test_text = font1.render(str(count), True, (255, 125, 0))
    # screen.blit(test_text, [25, 265])
    # print("count will be increase"+str(count))

    height = 100
    width = 80
    GRAY = (128, 128, 128)
    zoom =  20
    x = 10
    y = 5
    for i in range(height):
        for j in range(width):
            if (x +zoom * j) < 1000 and (y +zoom * i) < 700:
                pygame.draw.rect(screen, GRAY, [x +zoom * j, y +zoom * i,zoom,zoom], 1)

    # GRAY = (128, 128, 128)
    # pygame.draw.rect(screen,GRAY, [100,200,300,500], 1)
    position =[0,1, 5, 9, 13,15]
    
    
    for i in range(4):
        for j in range(4):
            p = i * 4 + j
            if p in position:
                pygame.draw.rect(screen, 'green',
                                    [x + zoom * (j + x) + 1,
                                    y + zoom * (i + y) + 1,
                                    zoom - 2, zoom - 2])
    
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60, frames per second

pygame.quit()