import pygame
pygame.init()
win = pygame.display.set_mode((850,480))

pygame.display.set_caption("Shooting Game")

bg = pygame.image.load('bg3.jpg')

pygame.display.update()

win.blit(bg, (0,0))



font1 = pygame.font.SysFont('comicsans', 60, True)
font2 = pygame.font.SysFont('comicsans', 25, True)

i=0
while i < 700:
    pygame.time.delay(10)
    i += 1

    text = font1.render('Press 1 For Level 1' , 1, (255,0,0))
    win.blit(text, (210, 150))
    pygame.display.update()

    text = font1.render('Press 2 For Level 2' , 1, (255,0,0))
    win.blit(text, (210, 250))
    pygame.display.update()

    text2 = font1.render('Press Q To Quite' , 1, (255,255,255))
    win.blit(text2, (230, 350))
    pygame.display.update()

    text2 = font2.render('Created By Ritik And Akshay' , 1, (255,255,255))
    win.blit(text2, (570, 440))
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            i = 201
            pygame.quit()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_1:
            import level1

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_2:
            import level2
    
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
            pygame.quit()
        
    


pygame.quit()
