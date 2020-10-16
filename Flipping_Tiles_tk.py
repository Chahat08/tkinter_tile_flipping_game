import tkinter as tk
import random
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)


pressed = -1
flipped_tiles = 16
moves = 0
high_score = 0



def check_win():
    global high_score, moves
    
    if flipped_tiles == 0:
        
        if moves <= high_score or high_score == -1:
            high_score = moves
            f = open('high_score.txt', 'w')
            f.write(str(high_score))
            f.close()

        win_lbl['text']='CLICKS: '+str(moves)+', BEST: '+str(high_score)

def print_moves():
    win_lbl['text'] = 'CLICKS: ' + str(moves)


def new_game():
    global pressed, flipped_tiles, buttons, colours, moves, win_lbl, high_score
    pressed = -1
    flipped_tiles = 16
    moves = 0
    buttons = {}
    win_lbl['text'] = ''

    f = open('high_score.txt', 'r')
    high_score = int(f.readline().strip())
    f.close()

    random.shuffle(colours)

    k=0
    for i in range(4):
        for j in range(4):
            btn = b(k)
            buttons[k] = btn
            if k!= len(colours)-1: k+=1
        
    k=0
    for i in range(4):
        for j in range(4):
            buttons[k].bttn.grid(row=i, column=j, sticky='nsew')
            if k!= len(colours)-1: k+=1




 
class b:
    
    def __init__(self, k):
        self.index = k
        self.bttn = tk.Button(frm,
                             width=6, height=2,
                             borderwidth=6, 
                             bg='white', activebackground = colours[self.index],
                             command=self.btn_press
                             )
    def btn_press(btn):
        global pressed, moves
        btn.bttn.configure(bg=colours[btn.index])
        moves += 1
        print_moves()
        if pressed == -1:
            pressed = btn.index
        else:
            btn.compare_pressed_btns()
    
    def compare_pressed_btns(btn):
        global pressed
        global flipped_tiles

        if (colours[btn.index] != colours[pressed]):
            btn.bttn.configure(bg='white')
            buttons[pressed].bttn.configure(bg='white')
            pressed = -1

        elif colours[btn.index] == colours[pressed] and (btn.index != pressed):
            btn.bttn['state'] = tk.DISABLED
            buttons[pressed].bttn['state']= tk.DISABLED
            pressed = -1
            flipped_tiles -= 2
            check_win()

        elif  btn.index == pressed:
            btn.bttn.configure(bg='white')
            pressed = -1
       

window = tk.Tk()
window.title('Flip!')
window.config(bg = 'black')

window.rowconfigure([0,1],weight=1,pad=2)
window.columnconfigure(0,weight =1, pad=2)

frm = tk.Frame(window, bg='Gray')
frm.grid(row = 0, column=0, sticky='nsew')

frm.rowconfigure(list(range(4)), minsize=50, pad=2)
frm.columnconfigure(list(range(4)), minsize=50, pad=2)

buttons = {}
colours=['YellowGreen', 'Violet', 'Tomato', 'SlateBlue', 'DarkCyan', 'Orange','DodgerBlue', 'ForestGreen']*2
random.shuffle(colours)

frm2 = tk.Frame(window, bg='Khaki')

win_lbl = tk.Label(frm2,
                  width=19, height=1,
                 bg='PowderBlue',
                 relief=tk.GROOVE,
                 borderwidth=2)
win_lbl.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')


new_game_btn = tk.Button(text='NEW GAME',
                        master=frm2,
                       width=10, height=1, borderwidth=3,
                       bg='Plum',
                       command=new_game)
new_game_btn.grid(row=0, column=1, padx=5, pady=5, sticky = 'nsew')

frm2.grid(row=1, column=0, sticky='nsew')

new_game()

window.mainloop()
