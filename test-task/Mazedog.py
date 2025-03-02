import time
import json

import pygame


RES = WIDTH, HEIGHT =600,600
TILE=60
# cols,rows=WIDTH//TILE,HEIGHT//TILE
Labirinth=((5,6,12,5,7,12,6,13,5,6),
           (12,3,9,6,12,2,9,5,5,3),
           (9,4,5,1,2,10,13,5,5,6),
           (14,10,12,5,2,9,5,5,5,3),
           (9,3,10,14,9,4,5,5,5,6),
           (12,5,3,10,14,9,6,12,5,3),
           (10,12,5,3,8,5,3,8,4,6),
           (10,10,13,6,10,14,12,3,8,2),
           (10,9,6,10,10,9,1,6,9,3),
           (9,5,1,3,9,5,7,9,5,5)
           )
Lose_cell=((4,0),(7,0),(6,2),(0,3),(3,4),(4,5),(2,7),(5,7),(6,9),(8,8),(9,8))



class Cell:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.visited=False
        self.thickness=4

    def dec_to_bin(self,dec):
        cell_bin = bin(int(dec))


        if len(cell_bin) == 5:
            cell_bin = '0' + cell_bin[2::]
        elif len(cell_bin) == 4:
            cell_bin = '00' + cell_bin[2::]
        else:
            if len(cell_bin) == 3:
                cell_bin = '000' + cell_bin[2::]
            else:
                cell_bin = cell_bin[2::]



        return cell_bin



    def draw_cell(self,cell_code,sc):
        x=self.x
        y=self.y
        a = cell_code
        if a[3]=="1":
             pygame.draw.line(sc,pygame.Color("orange"),(x,y+TILE),(x+TILE,y+TILE),self.thickness)
        if a[2] == "1":
            pygame.draw.line(sc, pygame.Color("orange"), (x + TILE, y + TILE), (x + TILE, y), self.thickness)
        if a[1] == "1":
            pygame.draw.line(sc, pygame.Color("orange"), (x, y), (x + TILE, y), self.thickness)

        if a[0] == "1":
            pygame.draw.line(sc, pygame.Color("orange"), (x, y), (x, y + TILE), self.thickness)



    def create_maze(self,map,sf):
        x=self.x
        y=self.y
        for line in range(len(map)):
            y= line
            self.y=y*TILE
            for column in range(len(map[line])):
                x = column
                self.x=x*TILE
                self.draw_cell(self.dec_to_bin(map[line][column]),sf)


            self.y=0

class Dog:
    def __init__(self):
       pass

    def dog_cell(self,lab_num_x,lab_num_y):
        self.lab_num_x = lab_num_x
        self.lab_num_y = lab_num_y
        cell_x = self.lab_num_x // TILE
        cell_y = self.lab_num_y // TILE
        cell_xy = (cell_x, cell_y)
        return (cell_xy)


    def move_dog(self,lab_cell,direct):
        cell_x = lab_cell[0]
        cell_y=lab_cell[1]
        dog_cell_now = Cell(0, 0).dec_to_bin(Labirinth[cell_y][cell_x])
        if dog_cell_now[direct] == '1':
            g_over = True
            return g_over





FPS=60
pygame.init()

font = pygame.font.Font(None, 100)
text = font.render("Game over!", True, [255, 255, 255])
font = pygame.font.Font(None, 50)
text1 = font.render("Вы ударились о стену", True, [255, 255, 255])
text2 = font.render("Вы зашли в тупик", True, [255, 255, 255])
font = pygame.font.Font(None, 30)
text3 = font.render("Нажмите 'y',что бы сохранить ", True, [255, 255, 255])
text4 = font.render(" или любую клавишу для продолжения", True, [255, 255, 255])
text5 = font.render("Нажмите 'n',для новой игры ", True, [255, 255, 255])
text6 = font.render(" или любую клавишу для выхода", True, [255, 255, 255])
font = pygame.font.Font(None, 100)
text7 = font.render("ПОБЕДА", True, [255, 255, 255])

game_surface=pygame.Surface(RES)
surface=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Шарик и лабиринт")


dog_face=pygame.image.load('foni.png').convert_alpha()
new_image=pygame.transform.scale(dog_face,(30,30))

with open('save.json', 'r') as file1:
    save = json.load(file1)

if save!= {}:

    start_x = save["start_x"]
    start_y = save["start_y"]
    save_flag=True
else:
    start_x = 555
    start_y = 555

wh_1=1
save_in_game=True
surface.blit(new_image, (start_x, start_y))
Cell(0,0).create_maze(Labirinth,surface)


clock=pygame.time.Clock()
while wh_1==1:
    Wall = False
    dead_end = False
    win=False
    while wh_1==1:

        for i in pygame.event.get():
            if Dog().dog_cell(start_x, start_y)==(0,0):
                win=True
                break

            if (Dog().dog_cell(start_x, start_y) in Lose_cell) and save_flag==False:
                Game_over = True
                dead_end=True

                break

            if i.type == pygame.QUIT:
                sys.exit()
            elif i.type == pygame.KEYDOWN:
                save_flag = False
                if i.key == pygame.K_LEFT:
                    Wall = Dog().move_dog(Dog().dog_cell(start_x, start_y), 0)
                    if not Wall:
                        start_x -= 60

                elif i.key == pygame.K_RIGHT:
                    Wall = Dog().move_dog(Dog().dog_cell(start_x, start_y), 2)
                    if not Wall:
                        start_x += 60

                else:
                    if i.key == pygame.K_UP:
                        Wall = Dog().move_dog(Dog().dog_cell(start_x, start_y), 1)
                        if not Wall:
                            start_y -= 60

                    elif i.key == pygame.K_DOWN:
                        Wall = Dog().move_dog(Dog().dog_cell(start_x, start_y), 3)
                        if not Wall:
                           start_y += 60
        if Wall == True :
            surface.fill((56, 50, 31))
            textpos = (100, 250)
            surface.blit(text, textpos)

            textpos = (100, 150)
            surface.blit(text1, textpos)
            textpos = (160, 350)
            surface.blit(text3, textpos)
            textpos = (120, 400)
            surface.blit(text4, textpos)
            wh_1=2
        elif dead_end == True:
            surface.fill((56, 50, 31))
            textpos = (100, 250)
            surface.blit(text, textpos)
            textpos = (140, 150)
            surface.blit(text2, textpos)
            textpos = (160, 350)
            surface.blit(text3, textpos)
            textpos = (120, 400)
            surface.blit(text4, textpos)
            save_flag=True
            wh_1=2
        else:
            if win==True:
                surface.fill((56, 50, 31))
                textpos = (140, 150)
                surface.blit(text7, textpos)
                wh_1=3
                pygame.display.flip()
                time.sleep(2)
            else:
                surface.fill((0, 0, 0))
                Cell(0, 0).create_maze(Labirinth, surface)
                surface.blit(new_image, (start_x, start_y))

        pygame.display.flip()
   # wh_1=2
    while wh_1==2:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit()
            if i.type == pygame.KEYDOWN:
                if i.key==pygame.K_y:
                    with open('save.json', 'w') as file1:
                        savejson={"start_x":start_x,"start_y":start_y}
                        file1.write(json.dumps(savejson))
                    wh_1=3

                else:
                    with open('save.json', 'w') as file1:
                        savejson={}
                        file1.write(json.dumps(savejson))
                    save_in_game=False
                    wh_1=3
    surface.fill((56, 50, 31))
    textpos = (160, 350)
    surface.blit(text5, textpos)
    textpos = (120, 400)
    surface.blit(text6, textpos)
    pygame.display.flip()
    win == False
    while wh_1==3:

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit()
            if i.type == pygame.KEYDOWN:
                if i.key==pygame.K_n:
                    wh_1 = 1
                    if save_in_game==False or win==True:
                        start_x = 555
                        start_y = 555
                        save_in_game=True

                else:
                    wh_1=4



