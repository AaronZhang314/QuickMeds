import pygame, random, time

pygame.init() #initializes the game

#---Color Settings---
white = (255,255,255) #theese are RGB color things
green = (0,255,0)
blue = (0,0,255)
black= (0,0,0)
red=(255,0,0)
pink=(255,102,255)
orange= (255,153,51)

#---Basic Settings---
screen = pygame.display.set_mode((600,1067)) #game window dimensions
screen_rect=screen.get_rect()
pygame.display.set_caption('QuickMeds')#game name
clock=pygame.time.Clock() #chooses the FPS
gameExit=False #when to end game

#---Font Settings---
myfont=pygame.font.SysFont(None, 35) 
smallfont=pygame.font.SysFont(None, 24)
agency=pygame.font.SysFont("agencyfb", 35)


#---Loading Images---
background=pygame.image.load("background.png").convert_alpha()
info_page=pygame.image.load("info_page.png").convert_alpha()
contactz=pygame.image.load("contacts.png").convert_alpha()
medical=pygame.image.load("Medical_Conditions.png").convert_alpha()
locaOff=pygame.image.load("LocationOff.png").convert_alpha()
locaOnz=pygame.image.load("LocationOn.png").convert_alpha()
EmerCon=pygame.image.load("EmergencyCon.png").convert_alpha()
Setting=pygame.image.load("Settings.png").convert_alpha()
EmerRes=pygame.image.load("EmergencyRes.png").convert_alpha()
widget=pygame.image.load("Widget.png").convert_alpha()
frontPic = pygame.image.load("Front.png").convert_alpha()
#---Assigning Variables
keys = pygame.key.get_pressed()
pressed=True      
alert_911=False
my_info=False
over_911=False
over_info=False
mouse_click=False           
over_contacts=False
contacts=False
over_condits = False
loca = False
locaOn= False
Emer = False
Sett = False
Front = False
Screen = False
widscreen = False


#---Starting Menu Loop---
while pressed:
    screen.blit(frontPic, (0,0))
    mouse_pos=pygame.mouse.get_pos()
    print mouse_pos
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #when i click the x button it exits the loop, therefore closing it
                gameExit=True
                pressed=True
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_click=True
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_click=False
    if  mouse_pos[1]< 950 and mouse_click == True:
        Screen = True
        pressed=True
    if mouse_pos[1]> 950 and mouse_click == True:
        widscreen = True
        pressed=True
    else:
        Screen = False
         
    if pressed and widscreen:
        for i in range(1067, 0, -50):
            screen.blit(widget, (0,i))
            pygame.display.update()
            clock.tick(60) #frames per second
    while pressed and widscreen:
        screen.blit(widget, (0,0))
        mouse_pos=pygame.mouse.get_pos()
        print mouse_pos
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #when i click the x button it exits the loop, therefore closing it
                    gameExit=True
                    pressed=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click=True
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_click=False
        if  184<mouse_pos[0]<282 and 917<mouse_pos[1]<1020 and mouse_click == True:
            Screen= True
            pressed=True
            widscreen = False
        pygame.display.update()
        clock.tick(60) #frames per second
    while pressed and Screen:
        screen.blit(background, (0,0))
        mouse_pos=pygame.mouse.get_pos()
        print mouse_pos
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #when i click the x button it exits the loop, therefore closing it
                    gameExit=True
                    pressed=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click=True
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_click=False
        
        if 50<mouse_pos[0]<630 and 630<mouse_pos[1]<703 and mouse_click == True:
            over_911=True
            pressed=True
        else:
            over_911=False
        if 15<mouse_pos[0]<145 and 45<mouse_pos[1]<87 and mouse_click == True:
            pressed=True
            my_info=True
        else:
            over_info=False
            




        while over_911 and pressed:
            screen.blit(EmerRes, (0,0))
            for event in pygame.event.get():
             if event.type == pygame.QUIT:
                     gameExit=True
                     pressed=True
             if event.type == pygame.MOUSEBUTTONDOWN:
                 mouse_click=True
             if event.type == pygame.MOUSEBUTTONUP:
                 mouse_click=False

            pygame.display.update()
            clock.tick(60) 


            
        while my_info and pressed:
            screen.blit(info_page, (0,0))
            mouse_pos=pygame.mouse.get_pos()
            print mouse_pos
            for event in pygame.event.get():
             if event.type == pygame.QUIT: 
                     gameExit=True
                     pressed=True
             if event.type == pygame.MOUSEBUTTONDOWN:
                 mouse_click=True
             if event.type == pygame.MOUSEBUTTONUP:
                 mouse_click=False
            
             if 135<mouse_pos[0]<317 and 202<mouse_pos[1] < 231 and mouse_click:
                 over_contacts=True
                 my_info = False
             else:
                 over_contacts=False

            if 123<mouse_pos[0]<362 and 353<mouse_pos[1]<388 and mouse_click:
                over_condits=True
                my_info = False
            else:
                over_condits=False
            if 152<mouse_pos[0]<315 and 520<mouse_pos[1]<552 and mouse_click:
                loca=True
                my_info = False
            else:
                loca=False

            if 148<mouse_pos[0]<651 and 649<mouse_pos[1]<684 and mouse_click:
                Emer=True
                my_info = False
            else:
                Emer=False
            if 184<mouse_pos[0]<290 and 853<mouse_pos[1]<883 and mouse_click:
                Sett=True
                my_info = False
            else:
                Sett=False
            pygame.display.update()
            clock.tick(60) #frames per second

        while over_contacts and pressed:
            mouse_pos=pygame.mouse.get_pos()
            print mouse_pos
            screen.blit(contactz, (0,0))
            for event in pygame.event.get():
             if event.type == pygame.QUIT: #when i click the x button it exits the loop, therefore closing it
                     gameExit=True
                     pressed=True
             if event.type == pygame.MOUSEBUTTONDOWN:
                 mouse_click=True
             if event.type == pygame.MOUSEBUTTONUP:
                 mouse_click=False
            if 30<mouse_pos[0]<70 and 50<mouse_pos[1]<85 and mouse_click:
                over_contacts = False
                my_info = True
                pressed = True
            else:
                over_contacts = True
            pygame.display.update()
            clock.tick(60) #frames per second
            
        while over_condits and pressed:
            mouse_pos=pygame.mouse.get_pos()
            print mouse_pos
            screen.blit(medical, (0,0))
            for event in pygame.event.get():
             if event.type == pygame.QUIT: #when i click the x button it exits the loop, therefore closing it
                     gameExit=True
                     pressed=True
             if event.type == pygame.MOUSEBUTTONDOWN:
                 mouse_click=True
             if event.type == pygame.MOUSEBUTTONUP:
                 mouse_click=False
            if 30<mouse_pos[0]<70 and 50<mouse_pos[1]<85 and mouse_click:
                over_condits = False
                my_info = True
                pressed = True
            else:
                over_condits= True
            pygame.display.update()
            clock.tick(60) #frames per second

        while loca and pressed:
            mouse_pos=pygame.mouse.get_pos()
            print mouse_pos
            screen.blit(info_page, (0,0))
            screen.blit(locaOff, (0,0))
            for event in pygame.event.get():
             if event.type == pygame.QUIT: #when i click the x button it exits the loop, therefore closing it
                     gameExit=True
                     pressed=True
             if event.type == pygame.MOUSEBUTTONDOWN:
                 mouse_click=True
             if event.type == pygame.MOUSEBUTTONUP:
                 mouse_click=False
            if 49<mouse_pos[0]<553 and 932<mouse_pos[1]<1017 and mouse_click:
                locaOn=True
                loca = False
                pressed = True
                print "REEEE"
            else:
                locaOn = False
            if 30<mouse_pos[0]<70 and 50<mouse_pos[1]<85 and mouse_click:
                loca = False
                my_info = True
                pressed = True
            else:
                loca= True


            
            while locaOn and pressed:
                mouse_pos=pygame.mouse.get_pos()
                print mouse_pos
                screen.blit(locaOnz, (0,0))
                for event in pygame.event.get():
                 if event.type == pygame.QUIT: #when i click the x button it exits the loop, therefore closing it
                         gameExit=True
                         pressed=True
                 if event.type == pygame.MOUSEBUTTONDOWN:
                     mouse_click=True
                 if event.type == pygame.MOUSEBUTTONUP:
                     mouse_click=False
                if 30<mouse_pos[0]<70 and 50<mouse_pos[1]<85 and mouse_click:
                    locaOn = False
                    my_info = True
                    pressed = True
                else:
                    locaOn= True
                pygame.display.update()
                clock.tick(60) #frames per second

            pygame.display.update()
            clock.tick(60) #frames per second

        while Emer and pressed:
            mouse_pos=pygame.mouse.get_pos()
            print mouse_pos
            screen.blit(EmerCon, (0,0))
            for event in pygame.event.get():
             if event.type == pygame.QUIT: #when i click the x button it exits the loop, therefore closing it
                     gameExit=True
                     pressed=True
             if event.type == pygame.MOUSEBUTTONDOWN:
                 mouse_click=True
             if event.type == pygame.MOUSEBUTTONUP:
                 mouse_click=False
            if 30<mouse_pos[0]<70 and 50<mouse_pos[1]<85 and mouse_click:
                Emer = False
                my_info = True
                pressed = True
            else:
                Emer= True
            pygame.display.update()
            clock.tick(60) #frames per second


            
        while Sett and pressed:
            mouse_pos=pygame.mouse.get_pos()
            print mouse_pos
            
            screen.blit(Setting, (0,0))
            for event in pygame.event.get():
             if event.type == pygame.QUIT: #when i click the x button it exits the loop, therefore closing it
                     gameExit=True
                     pressed=True
             if event.type == pygame.MOUSEBUTTONDOWN:
                 mouse_click=True
             if event.type == pygame.MOUSEBUTTONUP:
                 mouse_click=False
            if 30<mouse_pos[0]<70 and 50<mouse_pos[1]<85 and mouse_click:
                Sett = False
                my_info = True
                pressed = True
            else:
                Sett= True
            pygame.display.update()
            clock.tick(60) #frames per second
        pygame.display.update()
        clock.tick(60) #frames per second
    pygame.display.update()
    clock.tick(60) #frames per second
pygame.quit()
quit()
