import pygame

from src.player import Player 

def main():
     
    pygame.init()
    clk = pygame.time.Clock()
    

    pygame.display.set_caption("Jeu")
    screen = pygame.display.set_mode((1080,720))

    player = Player()
    shop = pygame.image.load("resources/tiles/png/v1.png")

    
    products = []
    products.append(pygame.transform.scale(pygame.image.load("resources/products/16x16/beef.png"), (32,32)))
    products.append(pygame.transform.scale(pygame.image.load("resources/products/16x16/porkchop.png"), (32,32)))
    products.append(pygame.transform.scale(pygame.image.load("resources/products/16x16/salmon.png"), (32,32)))
    products.append(pygame.transform.scale(pygame.image.load("resources/products/16x16/cod.png"), (32,32)))
    products.append(pygame.transform.scale(pygame.image.load("resources/products/16x16/chicken.png"), (32,32)))
    products.append(pygame.transform.scale(pygame.image.load("resources/products/16x16/carrot.png"), (64,64)))


    pixels32 = pygame.font.Font("resources/fonts/pixels.ttf", 32)
    name1 = pixels32.render("Titouan", True, (250,250,250))

    running = True
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if(keys[pygame.K_UP]): player.move_up()
        if(keys[pygame.K_DOWN]): player.move_down()
        if(keys[pygame.K_LEFT]): player.move_left()
        if(keys[pygame.K_RIGHT]): player.move_right()

        screen.fill((58,58,80))

        screen.blit(shop, (0,0))
        player.draw(screen)
        
        screen.blit(name1, (200,200))

        for i, product in enumerate(products):
            screen.blit(product, (40*i, 0))

        pygame.display.update();

        clk.tick(60)

    pygame.quit()
     
     
if __name__=="__main__":
    main()