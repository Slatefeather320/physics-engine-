import pygame

# make window
window = pygame.display.set_mode((1000,700))

#define ball start point and vilosity
x = 100
y = 200
r = 20
vx = 0
vy = 0
dampning = 1.2
gravity = True
friction = True
colour = (255,255,255)
bgcolour = (50,50,70)
xhistory = []
yhistory = []
i = 0
showrec = False
temp = 0

#frame cleaning and drawing next frame
def drawframe():
    global x, y, r, colour, showrec, temp
    
    window.fill(bgcolour) #clears screen
    pygame.draw.circle(window,colour,(x,y),r) #draws new circle
    

    if showrec:
       temp = 0
       for entry in xhistory:
          
          pygame.draw.circle(window,(200,100,100),(entry,yhistory[temp]),8)
          temp += 1
    pygame.display.update() #updates frame


    

def updatepos():
   global x, y, vx, vy
   x += vx
   y += vy


def calphysics():
   global vx, vy, x, y, dampning, gravity

   if gravity:
      vy += 0.001  #gravity

   #side colisions
   if y > 670:
      vy = (abs(vy)*-1)/ dampning
   if y < 30:
      vy = abs(vy)/ dampning
   if x > 970:
      vx = (abs(vx) * -1) / dampning
   if x < 30:
      vx = abs(vx) / dampning

   if friction:
      if y > 670 or y < 30 :
         if vx > 0:
            vx += -0.005
         if vx < 0:
            vx += 0.005
      


def togglegrav():
   global gravity, colour
   if gravity:
      gravity = False
      colour = (255,255,0)
   else:
      gravity = True
      colour = (255,255,255)

def togglefric():
   global friction, bgcolour, dampning
   if friction:
      friction = False
      bgcolour = (0,0,0)
      dampning = 1
   else:
      friction = True
      bgcolour = (50,50,70)
      dampning = 1.2


def rechistory():
   global xhistory, yhistory, x, y
   xhistory.append(x)
   yhistory.append(y)

def togrec():
   global showrec
   if showrec:
      showrec = False
   else:
      showrec = True

#active loop 
active = True

while active:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         active = False
      
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_LEFT:
            vx += -1
         if event.key == pygame.K_RIGHT:
            vx += 1
         if event.key == pygame.K_UP:
            vy += -1
         if event.key == pygame.K_DOWN:
            vy += 1
         if event.key == pygame.K_g:
            togglegrav()
         if event.key == pygame.K_f:
            togglefric()
         if event.key == pygame.K_x:
            vx = 0
            vy = 0
         if event.key == pygame.K_c:
            xhistory = []
            yhistory = []
         if event.key == pygame.K_r:
            togrec()

   #main game loop
   
   drawframe()
   updatepos()
   calphysics()

   i += 1

   if i%70 == 0 and showrec:
      rechistory()
   
   

      