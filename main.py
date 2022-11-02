from unicodedata import name
import pygame
from config import *
from computer_player import *
from draw import *
from tkinter import *
from PIL import ImageTk, Image
import ast
import operator

name = ''
def win(screen, winner = "Player"):
    if name.title() not in top:
        top.append((name.title(),0))
    if winner == "Player":
        # Label(root, text = name + win_text2  , font=text_font).pack()
        top[name]+=1
        display_text(screen, name.title() + win_text  , (screen_size[0] // 2, screen_size[1] // 2))
        
    else:
        # Label(root, text = name + lose_text  , font=text_font).pack()
        display_text(screen, name.title() + lose_text , (screen_size[0] // 2, screen_size[1] // 2))
    
    #write highscore
    with open('highscore.txt','w') as f: 
        f.write('{')
        for key,value in top:
            f.write("\'"+key+"\':"+str(value)+',\n')
        f.write('}')
def check_if_end_game(screen, board):
    if enemy_five_in_a_row(board, 1):
        win(screen, "Player")
        return 1
    elif enemy_five_in_a_row(board, -1):
        win(screen, "Computer")
        return 1
    return 0

def window_game():
    global name
    name = username.get()
    root.destroy()
    
    pygame.init()

    screen = draw_screen()
    

    board = new_board()

    pygame.display.update()

    game_over = False

    while True:
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONUP:
                if game_over:
                    pygame.quit()
                pos = pygame.mouse.get_pos()
                x = pos[0] // 60
                y = pos[1] // 60
                if board[x][y] != 0:
                    continue
                drawX(screen, x, y)
                board[x][y] = 1
                if check_if_end_game(screen, board):
                    pygame.display.update()
                    ev1 = pygame.event.get()
                    game_over = True
                    continue

                pygame.display.update()
                computer_reply(screen, board)
                if check_if_end_game(screen, board):
                    pygame.display.update()
                    ev = pygame.event.get()
                    game_over = True
                    continue

                pygame.display.update()
                

root = Tk()
root.geometry("600x600")
root.title("Caro")
bg=ImageTk.PhotoImage(Image.open("oa.png"))
back_ground = Label(root,image=bg).place(x=0,y=0,relwidth=1, relheight=1)

main_menu=Frame(root,width=600,height=600)
back_ground = Label(main_menu,image=bg)
back_ground.place(x=0,y=0,relwidth=1, relheight=1)


highscore=Frame(root,width=600,height=600)
back_ground = Label(highscore,image=bg)
back_ground.place(x=0,y=0,relwidth=1, relheight=1)

main_menu.grid(column=0,row=0)
highscore.grid(column=0,row=0)

ST = Button( main_menu,text ="START",bg="dim gray", fg="#27C5DB",command = window_game,font=("Arial", "30","bold"),relief="sunken") 
ST.place(x=50,y=450)
SC = Button( main_menu,text ="SCOREBOARD",bg="dim gray",fg="#27C5DB", command = lambda:highscore.tkraise(),font=("Arial", "30","bold"),relief="sunken")
SC.place(x=250,y=450)

tx = Label (main_menu,text="User name",font = ("Arial", "25","bold"),bg='#0E293C',fg="#27C5DB")
tx.place(x=50,y=350)

username = Entry(main_menu, font = ("Arial", "25","bold"), width = 15, background= 'white')
username.place(x=250,y=350)
username.focus()

with open('highscore.txt') as f:
    data = f.read()
d = ast.literal_eval(data)
f.close()
top=sorted(d.items(), key=operator.itemgetter(1) , reverse=True)


l=Label(highscore,text="HIGH SCORE",font = ("Arial", "25","bold"),bg='#0E293C',fg="#27C5DB")
l.place(x=180,y=220)
back=Button(highscore,text="Back",bg="dim gray",fg="#27C5DB", command = lambda:main_menu.tkraise(),font=("Arial", "30","bold"),relief="sunken")
back.place(x=10,y=10)
c=1
#top 5
k=Label(highscore,text="USERNAME",font = ("Arial", "25","bold"),bg='#0E293C',fg="#1abcd5")
k.place(x=180,y=280+c*40)
v=Label(highscore,text="SCORE",font = ("Arial", "25","bold"),bg='#0E293C',fg="#1abcd5")
v.place(x=400,y=280+c*40)
for key,value in top:
    c+=1
    stt=Label(highscore,text=str(c-1),font = ("Arial", "25","bold"),bg='#0E293C',fg="#1abcd5")
    stt.place(x=100,y=280+c*40)
    
    k=Label(highscore,text=key,font = ("Arial", "25","bold"),bg='#0E293C',fg="#1abcd5")
    k.place(x=180,y=280+c*40)
    v=Label(highscore,text=str(value),font = ("Arial", "25","bold"),bg='#0E293C',fg="#1abcd5")
    v.place(x=400,y=280+c*40)
    if c==6:
        break

main_menu.tkraise()     
root.mainloop()