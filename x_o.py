import numpy as np
import pygame , sys

pygame.init()
width = 600
height = 600
screen = pygame.display.set_mode((width,height))
win = pygame.display.set_mode((width,height))
pygame.display.set_caption(('X/O'))
screen.fill((172, 198, 173))
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
a=np.zeros((3,3))
font = pygame.font.SysFont("comicsansms", 72)
player = 1
game_over = False

def draw_lines():
    pygame.draw.line(screen , (60, 60, 60) , (200 , 0) , (200 , 600) , 10)
    pygame.draw.line(screen , (60, 60, 60) , (400 , 0) , (400 , 600) , 10)
    pygame.draw.line(screen , (60, 60, 60) , (0 , 200) , (600 , 200) , 10)
    pygame.draw.line(screen , (60, 60, 60) , (0 , 400) , (600 , 400) , 10)

def draw_figures():
	for i in range(3):
		for j in range(3):
			if a[i][j] == 1:
				pygame.draw.circle( screen, CIRCLE_COLOR, (int( j * 200 + 200//2 ), int( i * 200 + 200//2 )), CIRCLE_RADIUS, CIRCLE_WIDTH )
			elif a[i][j] == 2:
				pygame.draw.line( screen, CROSS_COLOR, (j * 200 + SPACE, i * 200 + 200 - SPACE), (j * 200 + 200 - SPACE, i * 200 + SPACE), CROSS_WIDTH )	
				pygame.draw.line( screen, CROSS_COLOR, (j * 200 + SPACE, i * 200 + SPACE), (j * 200 + 200 - SPACE, i * 200 + 200 - SPACE), CROSS_WIDTH )

draw_lines()

def valide(a,l,c):
    if a[l][c] == 0:
        return True
    return False

def play(l , c , player):
    if valide(a,l,c):
        a[l][c] = player

def blank_place(a):
    for i in range(3):
        for j in range(3):
            if a[i][j]==0:
                return True
    return False

def check_diag(a):
    for i in range(1,3):
        if a[0][0]!=a[i][i]:
            return False
    return True

def check_line(a,p):
    for i in range(1,3):
        if a[p][0]!=a[p][i]:
            return False
    return True

def check_anti_diag(a):
    for i in range(2):
        if a[2][0]!=a[i][2-i]:
            return False
        return True
    
def check_col(a,p):
    for i in range(1,3):
        if a[0][p]!=a[i][p]:
            return False
    return True
    
def check(a):
    if check_diag(a)==True:
        return a[0][0]
    if check_anti_diag(a)==True:
        return a[2][0]
    for i in range(3):
        if check_line(a,i)==True:
            return a[i][0]            
        if check_col(a, i)==True:            
            return a[0][i]
    return 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if game_over :
            win.fill((172, 198, 173))
            text = font.render('player '+str(int(check(a)))+' won', True,(172, 198, 173), (60, 60, 60))
            textRect = text.get_rect()
            textRect.center = ((600-72) // 2,(600-72) // 2)
            win.blit(text, textRect)
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0] 
            mouseY = event.pos[1] 
            X = int(mouseY // 200)
            Y = int(mouseX // 200)
            if valide(a,X,Y):
                play( X, Y, player )
            if check(a) != 0:
                game_over = True
            player = player % 2 + 1
            draw_figures()
    pygame.display.update()