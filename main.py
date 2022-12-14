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
    if name.title() not in d:
        d[name.title()]=0
    if winner == "Player":
        # Label(root, text = name + win_text2  , font=text_font).pack()
        d[name.title()]+=1
        display_text(screen, name.title() + win_text  , (screen_size[0] // 2, screen_size[1] // 2))
        
    else:
        # Label(root, text = name + lose_text  , font=text_font).pack()
        display_text(screen, name.title() + lose_text , (screen_size[0] // 2, screen_size[1] // 2))
        
    pygame.mixer.music.pause()
    
    #write highscore
    with open('highscore.txt','w') as f: 
        f.write('{')
        for key in d:
            f.write("\'"+key+"\':"+str(d[key])+',\n')
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
    # Music
    
    pygame.event.wait()
    click_sound=pygame.mixer.Sound('click.wav')

    board = new_board()
    pygame.display.update()
    pygame.display.set_caption('Caro game')

    game_over = False

    while True:
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONUP:
                if (sfx.get()==1):
                    click_sound.play()
                if game_over:
                    pygame.quit()
                pos = pygame.mouse.get_pos()
                x = pos[0] // 40
                y = pos[1] // 40
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
                computer_reply(screen, board, x, y)
                if check_if_end_game(screen, board):
                    pygame.display.update()
                    ev = pygame.event.get()
                    game_over = True
                    continue

                pygame.display.update()
def sound_options():
    if (music.get()==0):
        pygame.mixer.music.pause()
    elif pygame.mixer.get_busy()==False:
        pygame.mixer.music.unpause()
    main_menu.tkraise()
    
    
#MAIN
pygame.mixer.init()
pygame.mixer.music.load('nhacnen.wav')
pygame.mixer.music.play(-1)
root = Tk()
root.geometry("600x800")
root.title("Caro Game")
bg=ImageTk.PhotoImage(Image.open("oa.png"))
back_ground = Label(root,image=bg).place(x=0,y=0,relwidth=1, relheight=1)

main_menu=Frame(root,width=600,height=800)
back_ground = Label(main_menu,image=bg)
back_ground.place(x=0,y=0,relwidth=1, relheight=1)


highscore=Frame(root,width=600,height=800)
back_ground = Label(highscore,image=bg)
back_ground.place(x=0,y=0,relwidth=1, relheight=1)

setting_frame=Frame(root,width=600,height=800)
back_ground = Label(setting_frame,image=bg)
back_ground.place(x=0,y=0,relwidth=1, relheight=1)

main_menu.grid(column=0,row=0)
highscore.grid(column=0,row=0)
setting_frame.grid(column=0,row=0)

ST = Button( main_menu,text ="START",bg="dim gray", fg="#27C5DB",command = window_game,font=("Arial", "30","bold"),relief="sunken",width=10) 
ST.place(x=190,y=450)
SC = Button( main_menu,text ="SCORE",bg="dim gray",fg="#27C5DB", command = lambda:highscore.tkraise(),font=("Arial", "30","bold"),relief="sunken",width=10)
SC.place(x=190,y=550)

tx = Label (main_menu,text="User name",font = ("Arial", "25","bold"),bg='#0E293C',fg="#27C5DB")
tx.place(x=50,y=350)

username = Entry(main_menu, font = ("Arial", "25","bold"), width = 15, background= 'white')
username.place(x=250,y=350)
username.focus()

setting=Button(main_menu,text ="OPTIONS",bg="dim gray", fg="#27C5DB",command = lambda:setting_frame.tkraise(),font=("Arial", "30","bold"),relief="sunken",width=10)
setting.place(x=190,y=650)

se=Label(setting_frame,text="OPTIONS",font = ("Arial", "30","bold"), bg='#0E293C',fg="snow")
se.place(x=200,y=220)
music_=Label(setting_frame,text="MUSIC",font = ("Arial", "30","bold"), bg='#0E293C',fg="snow")
music_.place(x=120,y=350)
sfx_=Label(setting_frame,text="SFX",font = ("Arial", "30","bold"), bg='#0E293C',fg="snow")
sfx_.place(x=120,y=450)
music = IntVar(value=1)
sfx = IntVar(value=1)
yes=ImageTk.PhotoImage(Image.open("otick.png"))
no=ImageTk.PhotoImage(Image.open("no.png"))
music_box=Checkbutton(setting_frame, image=no, selectimage=yes, indicatoron=False,onvalue=1, offvalue=0, bd=0,
                    variable=music , relief="flat",bg='#0E293C',selectcolor='#0E293C')
sfx_box=Checkbutton(setting_frame, image=no, selectimage=yes, indicatoron=False,onvalue=1, offvalue=0, bd=0,
                    variable=sfx , relief="flat",bg='#0E293C',selectcolor='#0E293C')
music_box.place(x=300,y=350)
sfx_box.place(x=300,y=450)
Save_button = Button( setting_frame,text ="SAVE",bg="dim gray", fg="#27C5DB",command = sound_options ,font=("Arial", "30","bold"),relief="sunken") 
Save_button.place(x=250,y=650)
with open('highscore.txt') as f:
    data = f.read()
d = ast.literal_eval(data)
f.close()
top=sorted(d.items(), key=operator.itemgetter(1) , reverse=True)


l=Label(highscore,text="HIGH SCORE",font = ("Arial", "25","bold"),bg='#0E293C',fg="snow")
l.place(x=180,y=220)
c=1
#top 5
ba=ImageTk.PhotoImage(Image.open("oback.png"))
backButton=Button(highscore,image=ba,command = lambda:main_menu.tkraise(),relief='flat')
backButton.place(x=10,y=700,relheight=0.1,relwidth=0.1)
k=Label(highscore,text="NAME",font = ("Arial", "25","bold"),bg='#0E293C',fg="snow")
k.place(x=180,y=280+c*60)
v=Label(highscore,text="SCORE",font = ("Arial", "25","bold"),bg='#0E293C',fg="snow")
v.place(x=400,y=280+c*60)
for key,value in top:
    c+=1
    stt=Label(highscore,text=str(c-1),font = ("Arial", "20","bold"),bg='#0E293C',fg="snow")
    stt.place(x=100,y=280+c*60)
    
    k=Label(highscore,text=key,font = ("Arial", "20","bold"),bg='#0E293C',fg="snow")
    k.place(x=180,y=280+c*60)
    v=Label(highscore,text=str(value),font = ("Arial", "20","bold"),bg='#0E293C',fg="snow")
    v.place(x=400,y=280+c*60)
    if c==6:
        break

main_menu.tkraise()     
root.mainloop()