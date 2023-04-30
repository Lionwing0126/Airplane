import pygame
import math
import random
# 1.2 - Initialize the game 
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
keep_going = True


# 1.3 - Load images
background = pygame.image.load("images/bluesky.jpg")
background = pygame.transform.scale(background, (width, height))
cargo = pygame.image.load("images/rabbitnobackground.png")
player = pygame.image.load("images/airplane1.png")
player = pygame.transform.scale(player, (170, 170))

key_up=key_down=key_left=key_right = False
player_pos=[130,100] #change the position to list

bullets=[]
bullet = pygame.image.load("images/bulletsnb.png")
bullet = pygame.transform.scale(bullet, (100, 100))

enemyImg = pygame.image.load("images/owlnobackground.png")
enemyImg = pygame.transform.scale(enemyImg, (100, 100))
enemys=[[640,100]]
enemySpeed=-0.5
enemyMaxnumber=5
enemyImg = pygame.image.load("images/nobackgroundenemy1.png")
enemyImg=pygame.transform.scale(enemyImg, (75, 75))
enemys=[[640,100]]
enemySpeed=-0.3
enemyMaxnumber=5

explosions=[] 
explosion_anim=[] 
BLACK = (0, 0, 0)
explosion_time=60
for i in range(9):
    filename = 'Explosion0{}.png'.format(i)
    img = pygame.image.load("images/"+ filename).convert()   
    img.set_colorkey(BLACK)
    img= pygame.transform.scale(img, (75, 75))
    explosion_anim.append(img)
    
#smiley face is cool
while keep_going:
    # 1.5 - clear the screen before drawing it again
    screen.fill(0)
    #1.6 - draw the screen elements
    screen.blit(background, (0,0))
    #1.7 - update the screen
    cargo = pygame.transform.scale(cargo, (90, 90))
    screen.blit(cargo,(0,30))
    screen.blit(cargo,(0,135))
    screen.blit(cargo,(0,240))
    screen.blit(cargo,(0,345))

    

    screen.blit(player, player_pos)

    index=0
    for bulletPos in bullets:

        bulletPos[0]=bulletPos[0]+2
        screen.blit(bullet,bulletPos)


        if bulletPos[0]<-64 or bulletPos[0]>width or bulletPos[1]<-64 or bulletPos[1]>height:
            bullets.pop(index)  
                
        index+=1

    
    if(random.randint(1,100)<3 and len(enemys)<enemyMaxnumber):
        #screen.blit(enemy, badguy)
        enemys.append([640, random.randint(50,430)])
        print("enemys length"+str(len(enemys)))
    
    enemy_index=0
    for enemyPos in enemys:               
        enemyPos[0]+=enemySpeed
        if enemyPos[0]<50:
            enemys.pop(enemy_index)
        screen.blit(enemyImg, enemyPos)

        enemy_index+=1   

        enemyRect=pygame.Rect(enemyImg.get_rect())
        enemyRect.left=enemyPos[0]
        enemyRect.top=enemyPos[1]
        bullet_index=0
        for bulletPos in bullets:
            bulletRect=pygame.Rect(bullet.get_rect()) # get rect of bullet image size
            bulletRect.left=bulletPos[0]
            bulletRect.top=bulletPos[1]            
            if bulletRect.colliderect(enemyRect):
                enemys.pop(enemy_index)
                bullets.pop(bullet_index)
                # step7 play explosion in the location of enemy
                explosions.append([enemyPos,0,explosion_time])
                
            bullet_index+=1
        enemy_index+=1       
    

    pygame.display.flip() # will update the contents of the entire display, and faster than .update()
    # 1.8 - loop through the events
    for event in pygame.event.get():
        
        if event.type==pygame.QUIT:
            keep_going=False    

        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_w:
                key_up=True
            elif event.key==pygame.K_a:
                key_left=True
            elif event.key==pygame.K_s:
                key_down=True
            elif event.key==pygame.K_d:
                key_right=True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_w:
                key_up=False
            elif event.key==pygame.K_a:
                key_left=False
            elif event.key==pygame.K_s:
                key_down=False
            elif event.key==pygame.K_d:
                key_right=False
        if event.type==pygame.MOUSEBUTTONDOWN or (event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE):
            bullets.append([player_pos[0]+50,player_pos[1]+50])   # bullets.append([player_pos) 
        
    
        

        if(explosion[1]<9):
            screen.blit(explosion_anim[explosion[1]],explosion[0])
            explosion[2]=explosion[2]-1
            if(explosion[2]<0):     
                explosion[1]=explosion[1]+1
                explosion[2]=explosion_time

        else:
            explosions.pop(0)
                


    
        # check if the event is the X buttony
    if key_up and player_pos[1]>0:
        player_pos[1]-=1
    elif key_down and player_pos[1]<height-150:
        player_pos[1]+=1
    if key_left and player_pos[0]>0:
        player_pos[0]-=1
    elif key_right and player_pos[0]<width-550:
        player_pos[0]+=1
     
        if key_up:
            player_pos[1]-=2
        elif key_down:
            player_pos[1]+=2
        if key_left:
            player_pos[0]-=2
        elif key_right:
            player_pos[0]+=2
    
    
        

 
     #6 Check for collisions


    # end step 6
        

    

            



  #remove bullet if out the screen

            

#1.9 exit pygame and python
pygame.quit()
exit(0) 
