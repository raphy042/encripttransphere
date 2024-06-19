#imports the pygame library module
thy=100000000
def primes(thy):
    import pygame# initilize the pygame module
    from pynput import keyboard
    h = True
    from pynput.keyboard import Key, Listener
    import math
    n=0
    r=0
    width=1000
    height=1000
    pygame.init()# Setting your screen size with a tuple of the screen width and screen height
    from pygame.locals import (

        K_UP,

        K_DOWN,

        K_LEFT,

        K_RIGHT,

        K_ESCAPE,

        KEYDOWN,

        QUIT,

    )


    g=0
    b=0
    d=333
    #thy=int(input('spiral srart number: '))

    htht=5
    
    while h==True:
        
        
        
        s = pygame.display.set_mode((width,height))# Setting a random caption title for your pygame graphical window.
        
        
        surf = pygame.Surface((htht,htht))
        
        # Give the surface a color to separate it from the background
        z=0
        w=0
        r=0
        y=0
        r=0
        f=0

        z=500
        hhh=500


        ff=True
        
        num=0
        gg=1
        pp=1
        rotation=3
        thy+=1
        while y<thy:
            
            
            
            
            

            rotation+=1
            if rotation==4:
                rotation=0
            while gg>0:





                num+=1
                isPrime = False
                y+=1
                if num == 1:
                    print(num, "is not a prime number")
                elif num > 1:
                    # check for factors
                    for i in range(2, num):
                        if (num % i) == 0:
                        # if factor is found, set flag to True
                            isPrime = True
                        # break out of loop
                            break
                    if not isPrime:
                        r=255
                        g=255
                        b=255
                    else:
                        r=255
                        g=0
                        b=0
                    
                    surf.fill((r, g, b))
                    s.blit(surf, (z, hhh))
                    if rotation==0:
                        z+=htht
                    if rotation==1:
                        hhh-=htht
                    if rotation==2:
                        z-=htht
                    if rotation==3:
                        hhh+=htht
                    
                    pygame.display.update()

                    print(num)
                    print(gg)
                    gg-=2

                    if y==thy:
                        gg=0





            pp+=1
            gg=pp

            
            
            
        f=0













        pygame.display.set_caption("testall?")# Update your screen when required
        pygame.display.update()# quit the pygame initialization and module

        

        
        
        if n==1000:
            n=0
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.type == K_ESCAPE:

                    h = False
            if event.type == pygame.QUIT:
                
                h=False
        h=False
    pygame.quit()# End the program
    
