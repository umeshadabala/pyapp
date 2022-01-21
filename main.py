#om🕉
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import random
import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

from random import choice
from random import shuffle

import requests
import os
from tkinter.font import Font
import pickle
import time
from tkinter import ttk, colorchooser

from datetime import datetime
from random import randint
from random import choice
import turtle
s=Tk()
s.title('ALL IN ONE PYTHON APPS')
s.geometry('500x500')
s.resizable(0,0)
s.config(bg='blue')

def calculator():


    root = Tk()
    root.title("Simple Calculator")
   
    e = Entry(root, width=35, borderwidth=5)
    e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    # e.insert(0, "")

    def button_click(number):
        # e.delete(0, END)
        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current) + str(number))

    def button_clear():
        e.delete(0, END)

    def button_add():
        first_number = e.get()
        global f_num
        global math
        math = "addition"
        f_num = int(first_number)
        e.delete(0, END)

    def button_equal():
        second_number = e.get()
        e.delete(0, END)

        if math == "addition":
            e.insert(0, f_num + int(second_number))

        if math == "subtraction":
            e.insert(0, f_num - int(second_number))

        if math == "multiplication":
            e.insert(0, f_num * int(second_number))

        if math == "division":
            e.insert(0, f_num / int(second_number))

    def button_subtract():
        first_number = e.get()
        global f_num
        global math
        math = "subtraction"
        f_num = int(first_number)
        e.delete(0, END)

    def button_multiply():
        first_number = e.get()
        global f_num
        global math
        math = "multiplication"
        f_num = int(first_number)
        e.delete(0, END)

    def button_divide():
        first_number = e.get()
        global f_num
        global math
        math = "division"
        f_num = int(first_number)
        e.delete(0, END)

    # Define Buttons

    button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
    button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
    button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
    button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
    button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
    button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
    button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
    button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
    button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
    button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
    button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
    button_equal = Button(root, text="=", padx=91, pady=20, command=button_equal)
    button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear)

    button_subtract = Button(root, text="-", padx=41, pady=20, command=button_subtract)
    button_multiply = Button(root, text="*", padx=40, pady=20, command=button_multiply)
    button_divide = Button(root, text="/", padx=41, pady=20, command=button_divide)

    # Put the buttons on the screen

    button_1.grid(row=3, column=0)
    button_2.grid(row=3, column=1)
    button_3.grid(row=3, column=2)

    button_4.grid(row=2, column=0)
    button_5.grid(row=2, column=1)
    button_6.grid(row=2, column=2)

    button_7.grid(row=1, column=0)
    button_8.grid(row=1, column=1)
    button_9.grid(row=1, column=2)

    button_0.grid(row=4, column=0)
    button_clear.grid(row=4, column=1, columnspan=2)
    button_add.grid(row=5, column=0)
    button_equal.grid(row=5, column=1, columnspan=2)

    button_subtract.grid(row=6, column=0)
    button_multiply.grid(row=6, column=1)
    button_divide.grid(row=6, column=2)

    root.mainloop()
def col():

    class main:
        def __init__(self, master):
            self.master = master
            self.color_fg = 'black'
            self.color_bg = 'white'
            self.old_x = None
            self.old_y = None
            self.penwidth = 5
            self.drawWidgets()
            self.c.bind('<B1-Motion>', self.paint)  # drwaing the line
            self.c.bind('<ButtonRelease-1>', self.reset)

        def paint(self, e):
            if self.old_x and self.old_y:
                self.c.create_line(self.old_x, self.old_y, e.x, e.y, width=self.penwidth, fill=self.color_fg,
                                   capstyle=ROUND, smooth=True)

            self.old_x = e.x
            self.old_y = e.y

        def reset(self, e):  # reseting or cleaning the canvas
            self.old_x = None
            self.old_y = None

        def changeW(self, e):  # change Width of pen through slider
            self.penwidth = e

        def clear(self):
            self.c.delete(ALL)

        def change_fg(self):  # changing the pen color
            self.color_fg = colorchooser.askcolor(color=self.color_fg)[1]

        def change_bg(self):  # changing the background color canvas
            self.color_bg = colorchooser.askcolor(color=self.color_bg)[1]
            self.c['bg'] = self.color_bg

        def drawWidgets(self):
            self.controls = Frame(self.master, padx=5, pady=5)
            Label(self.controls, text='Pen Width:', font=('arial 18')).grid(row=0, column=0)
            self.slider = ttk.Scale(self.controls, from_=5, to=100, command=self.changeW, orient=HORIZONTAL)
            self.slider.set(self.penwidth)
            self.slider.grid(row=0, column=1, ipadx=30)
            self.controls.pack(side=LEFT)

            self.c = Canvas(self.master, width=500, height=500, bg=self.color_bg, )
            self.c.pack(fill=BOTH, expand=True)

            menu = Menu(self.master)
            self.master.config(menu=menu)
            filemenu = Menu(menu)
            colormenu = Menu(menu)
            menu.add_cascade(label='Colors', menu=colormenu)
            colormenu.add_command(label='Brush Color', command=self.change_fg)
            colormenu.add_command(label='Background Color', command=self.change_bg)
            optionmenu = Menu(menu)
            menu.add_cascade(label='Options', menu=optionmenu)
            optionmenu.add_command(label='Clear Canvas', command=self.clear)
            optionmenu.add_command(label='Exit', command=self.master.destroy)

    if __name__ == '__main__':
        root = Toplevel()
        
        main(root)
        root.title('Paint App')
        root.mainloop()




def todo():

    root = Toplevel(s)
    root.title('ToDo List!')

    root.geometry("500x500")

    # Define our Font
    my_font = Font(
        family="Brush Script MT",
        size=30,
        weight="bold")

    # Creat frame
    my_frame = Frame(root)
    my_frame.pack(pady=10)

    # Create listbox
    my_list = Listbox(my_frame,
                      font=my_font,
                      width=25,
                      height=5,
                      bg="SystemButtonFace",
                      bd=0,
                      fg="#464646",
                      highlightthickness=0,
                      selectbackground="#a6a6a6",
                      activestyle="none")

    my_list.pack(side=LEFT, fill=BOTH)

    # Create dummy list
    # stuff = ["Walk The Dog", "Buy Groceries", "Take A Nap", "Learn Tkinter", "Rule The World"]
    # Add dummy list to list box
    # for item in stuff:
    #	my_list.insert(END, item)

    # Create scrollbar
    my_scrollbar = Scrollbar(my_frame)
    my_scrollbar.pack(side=RIGHT, fill=BOTH)

    # Add scrollbar
    my_list.config(yscrollcommand=my_scrollbar.set)
    my_scrollbar.config(command=my_list.yview)

    # create entry box to add items to the list
    my_entry = Entry(root, font=("Helvetica", 24), width=26)
    my_entry.pack(pady=20)

    # Create a button frame
    button_frame = Frame(root)
    button_frame.pack(pady=20)

    # FUNCTIONS
    def delete_item():
        my_list.delete(ANCHOR)

    def add_item():
        my_list.insert(END, my_entry.get())
        my_entry.delete(0, END)

    def cross_off_item():
        # Cross off item
        my_list.itemconfig(
            my_list.curselection(),
            fg="#dedede")
        # Get rid of selection bar
        my_list.selection_clear(0, END)

    def uncross_item():
        # Cross off item
        my_list.itemconfig(
            my_list.curselection(),
            fg="#464646")
        # Get rid of selection bar
        my_list.selection_clear(0, END)

    def delete_crossed():
        count = 0
        while count < my_list.size():
            if my_list.itemcget(count, "fg") == "#dedede":
                my_list.delete(my_list.index(count))

            else:
                count += 1

    def save_list():
        file_name = filedialog.asksaveasfilename(
            initialdir="C:/gui/data",
            title="Save File",
            filetypes=(
                ("Dat Files", "*.dat"),
                ("All Files", "*.*"))
        )
        if file_name:
            if file_name.endswith(".dat"):
                pass
            else:
                file_name = f'{file_name}.dat'

            # Delete crossed off items before saving
            count = 0
            while count < my_list.size():
                if my_list.itemcget(count, "fg") == "#dedede":
                    my_list.delete(my_list.index(count))

                else:
                    count += 1

            # grab all the stuff from the list
            stuff = my_list.get(0, END)

            # Open the file
            output_file = open(file_name, 'wb')

            # Actually add the stuff to the file
            pickle.dump(stuff, output_file)

    def open_list():
        file_name = filedialog.askopenfilename(
            initialdir="C:/gui/data",
            title="Open File",
            filetypes=(
                ("Dat Files", "*.dat"),
                ("All Files", "*.*"))
        )

        if file_name:
            # Delete currently open list
            my_list.delete(0, END)

            # Open the file
            input_file = open(file_name, 'rb')

            # Load the data from the file
            stuff = pickle.load(input_file)

            # Output stuff to the screen
            for item in stuff:
                my_list.insert(END, item)

    def delete_list():
        my_list.delete(0, END)

    # Create Menu
    my_menu = Menu(root)
    root.config(menu=my_menu)

    # Add items to the menu
    file_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="File", menu=file_menu)
    # Add dropdown items
    file_menu.add_command(label="Save List", command=save_list)
    file_menu.add_command(label="Open List", command=open_list)
    file_menu.add_separator()
    file_menu.add_command(label="Clear List", command=delete_list)

    # Add some buttons
    delete_button = Button(button_frame, text="Delete Item", command=delete_item)
    add_button = Button(button_frame, text="Add Item", command=add_item)
    cross_off_button = Button(button_frame, text="Cross Off Item", command=cross_off_item)
    uncross_button = Button(button_frame, text="Uncross Item", command=uncross_item)
    delete_crossed_button = Button(button_frame, text="Delete Crossed", command=delete_crossed)

    delete_button.grid(row=0, column=0)
    add_button.grid(row=0, column=1, padx=20)
    cross_off_button.grid(row=0, column=2)
    uncross_button.grid(row=0, column=3, padx=20)
    delete_crossed_button.grid(row=0, column=4)

    root.mainloop()
def tic():
    root = Toplevel()
   
    root.title('Tic-Tac-Toe')
    root.resizable(0,0)
    # root.geometry("1200x710")

    # X starts so true
    clicked = True
    count = 0

    # disable all the buttons
    def disable_all_buttons():
        b1.config(state=DISABLED)
        b2.config(state=DISABLED)
        b3.config(state=DISABLED)
        b4.config(state=DISABLED)
        b5.config(state=DISABLED)
        b6.config(state=DISABLED)
        b7.config(state=DISABLED)
        b8.config(state=DISABLED)
        b9.config(state=DISABLED)

    # Check to see if someone won
    def checkifwon():
        global winner
        winner = False

        if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
            b1.config(bg="red")
            b2.config(bg="red")
            b3.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
            disable_all_buttons()
        elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
            b4.config(bg="red")
            b5.config(bg="red")
            b6.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
            disable_all_buttons()

        elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
            b7.config(bg="red")
            b8.config(bg="red")
            b9.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
            disable_all_buttons()

        elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
            b1.config(bg="red")
            b4.config(bg="red")
            b7.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
            disable_all_buttons()

        elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
            b2.config(bg="red")
            b5.config(bg="red")
            b8.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
            disable_all_buttons()

        elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
            b3.config(bg="red")
            b6.config(bg="red")
            b9.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
            disable_all_buttons()

        elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
            b1.config(bg="red")
            b5.config(bg="red")
            b9.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
            disable_all_buttons()

        elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
            b3.config(bg="red")
            b5.config(bg="red")
            b7.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
            disable_all_buttons()

        #### CHECK FOR O's Win
        elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
            b1.config(bg="red")
            b2.config(bg="red")
            b3.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
            disable_all_buttons()
        elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
            b4.config(bg="red")
            b5.config(bg="red")
            b6.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
            disable_all_buttons()

        elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
            b7.config(bg="red")
            b8.config(bg="red")
            b9.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
            disable_all_buttons()

        elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
            b1.config(bg="red")
            b4.config(bg="red")
            b7.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
            disable_all_buttons()

        elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
            b2.config(bg="red")
            b5.config(bg="red")
            b8.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
            disable_all_buttons()

        elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
            b3.config(bg="red")
            b6.config(bg="red")
            b9.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
            disable_all_buttons()

        elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
            b1.config(bg="red")
            b5.config(bg="red")
            b9.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
            disable_all_buttons()

        elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
            b3.config(bg="red")
            b5.config(bg="red")
            b7.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
            disable_all_buttons()

        # Check if tie
        if count == 9 and winner == False:
            messagebox.showinfo("Tic Tac Toe", "It's A Tie!\n No One Wins!")
            disable_all_buttons()

    # Button clicked function
    def b_click(b):
        global clicked, count

        if b["text"] == " " and clicked == True:
            b["text"] = "X"
            clicked = False
            count += 1
            checkifwon()
        elif b["text"] == " " and clicked == False:
            b["text"] = "O"
            clicked = True
            count += 1
            checkifwon()
        else:
            messagebox.showerror("Tic Tac Toe", "Hey! That box has already been selected\nPick Another Box...")

    # Start the game over!
    def reset():
        global b1, b2, b3, b4, b5, b6, b7, b8, b9
        global clicked, count
        clicked = True
        count = 0

        # Build our buttons
        b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                    command=lambda: b_click(b1))
        b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                    command=lambda: b_click(b2))
        b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                    command=lambda: b_click(b3))

        b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                    command=lambda: b_click(b4))
        b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                    command=lambda: b_click(b5))
        b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                    command=lambda: b_click(b6))

        b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                    command=lambda: b_click(b7))
        b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                    command=lambda: b_click(b8))
        b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                    command=lambda: b_click(b9))

        # Grid our buttons to the screen
        b1.grid(row=0, column=0)
        b2.grid(row=0, column=1)
        b3.grid(row=0, column=2)

        b4.grid(row=1, column=0)
        b5.grid(row=1, column=1)
        b6.grid(row=1, column=2)

        b7.grid(row=2, column=0)
        b8.grid(row=2, column=1)
        b9.grid(row=2, column=2)

    # Create menue
    my_menu = Menu(root)
    root.config(menu=my_menu)

    # Create Options Menu
    options_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Options", menu=options_menu)
    options_menu.add_command(label="Rest Game", command=reset)

    reset()

    root.mainloop()


def snake():
    GRADUATION = 18
    PIXEL = 22
    STEP = 2 * PIXEL
    WD = PIXEL * GRADUATION
    HT = PIXEL * GRADUATION
    # constants that go into specifying the shapes' sizes
    OB_SIZE_FACTOR = 1
    SN_SIZE_FACTOR = 0.9
    OB_SIZE = PIXEL * OB_SIZE_FACTOR
    SN_SIZE = PIXEL * SN_SIZE_FACTOR
    # color constants
    BG_COLOR = 'black'
    OB_COLOR = 'red'
    SN_COLOR = 'green'
    # a dictionary to ease access to a shape's type in the Shape class
    SN = 'snake'
    OB = 'obstacle'
    SIZE = {SN: SN_SIZE, OB: OB_SIZE}
    # constants for keyboard input
    UP = 'Up'
    DOWN = 'Down'
    RIGHT = 'Right'
    LEFT = 'Left'
    # a dictionary to ease access to 'directions'
    DIRECTIONS = {UP: [0, -1], DOWN: [0, 1], RIGHT: [1, 0], LEFT: [-1, 0]}
    AXES = {UP: 'Vertical', DOWN: 'Vertical', RIGHT: 'Horizontal', LEFT: 'Horizontal'}
    # refresh time for the perpetual motion
    REFRESH_TIME = 100

    class Master(Canvas):
        """create the game canvas, the snake, the obstacle, keep track of the score"""

        def __init__(self, boss=None):
            super().__init__(boss)
            self.configure(width=WD, height=HT, bg=BG_COLOR)
            self.running = 0
            self.snake = None
            self.obstacle = None
            self.direction = None
            self.current = None
            self.score = Scores(boss)

        def start(self):
            """start snake game"""
            if self.running == 0:
                self.snake = Snake(self)
                self.obstacle = Obstacle(self)
                self.direction = RIGHT
                self.current = Movement(self, RIGHT)
                self.current.begin()
                self.running = 1

        def clean(self):
            """restarting the game"""
            if self.running == 1:
                self.score.reset()
                self.current.stop()
                self.running = 0
                self.obstacle.delete()
                for block in self.snake.blocks:
                    block.delete()

        def redirect(self, event):
            """taking keyboard inputs and moving the snake accordingly"""
            if 1 == self.running and \
                    event.keysym in AXES.keys() and \
                    AXES[event.keysym] != AXES[self.direction]:
                self.current.flag = 0
                self.direction = event.keysym
                self.current = Movement(self, event.keysym)  # a new instance at each turn to avoid confusion/tricking
                self.current.begin()  # program gets tricked if the user presses two arrow keys really quickly

    class Scores:
        """Objects that keep track of the score and high score"""

        def __init__(self, boss=None):
            self.counter = StringVar(boss, '0')
            self.maximum = StringVar(boss, '0')

        def increment(self):
            score = int(self.counter.get()) + 1
            maximum = max(score, int(self.maximum.get()))
            self.counter.set(str(score))
            self.maximum.set(str(maximum))

        def reset(self):
            self.counter.set('0')

    class Shape:
        """This is a template to make obstacles and snake body parts"""

        def __init__(self, can, a, b, kind):
            self.can = can
            self.x, self.y = a, b
            self.kind = kind
            if kind == SN:
                self.ref = Canvas.create_rectangle(self.can,
                                                   a - SN_SIZE, b - SN_SIZE,
                                                   a + SN_SIZE, b + SN_SIZE,
                                                   fill=SN_COLOR,
                                                   width=2)
            elif kind == OB:
                self.ref = Canvas.create_oval(self.can,
                                              a - OB_SIZE, b - OB_SIZE,
                                              a + SN_SIZE, b + SN_SIZE,
                                              fill=OB_COLOR,
                                              width=2)

        def modify(self, a, b):
            self.x, self.y = a, b
            self.can.coords(self.ref,
                            a - SIZE[self.kind], b - SIZE[self.kind],
                            a + SIZE[self.kind], b + SIZE[self.kind])

        def delete(self):
            self.can.delete(self.ref)

    class Obstacle(Shape):
        """snake food"""

        def __init__(self, can):
            """only create the obstacles where there is no snake body part"""
            self.can = can
            p = int(GRADUATION / 2 - 1)
            n, m = randint(0, p), randint(0, p)
            a, b = PIXEL * (2 * n + 1), PIXEL * (2 * m + 1)
            while [a, b] in [[block.x, block.y] for block in self.can.snake.blocks]:
                n, m = randint(0, p), randint(0, p)
                a, b = PIXEL * (2 * n + 1), PIXEL * (2 * m + 1)
            super().__init__(can, a, b, OB)

    class Block(Shape):
        """snake body part"""

        def __init__(self, can, a, y):
            super().__init__(can, a, y, SN)

    class Snake:
        """a snake keeps track of its body parts"""

        def __init__(self, can):
            """initial position chosen by me"""
            self.can = can
            a = PIXEL + 2 * int(GRADUATION / 4) * PIXEL
            self.blocks = [Block(can, a, a), Block(can, a, a + STEP)]

        def move(self, path):
            """an elementary step consisting of putting the tail of the snake in the first position"""
            a = (self.blocks[-1].x + STEP * path[0]) % WD
            b = (self.blocks[-1].y + STEP * path[1]) % HT
            if a == self.can.obstacle.x and b == self.can.obstacle.y:  # check if we find food
                self.can.score.increment()
                self.can.obstacle.delete()
                self.blocks.append(Block(self.can, a, b))
                self.can.obstacle = Obstacle(self.can)
            elif [a, b] in [[block.x, block.y] for block in self.blocks]:  # check if we hit a body part
                self.can.clean()
            else:
                self.blocks[0].modify(a, b)
                self.blocks = self.blocks[1:] + [self.blocks[0]]

    class Movement:
        """object that enters the snake into a perpetual state of motion in a predefined direction"""

        def __init__(self, can, direction):
            self.flag = 1
            self.can = can
            self.direction = direction

        def begin(self):
            """start the perpetual motion"""
            if self.flag > 0:
                self.can.snake.move(DIRECTIONS[self.direction])
                self.can.after(REFRESH_TIME, self.begin)

        def stop(self):
            """stop the perpetual movement"""
            self.flag = 0

    root = Toplevel()
    root.title("Snake Game")
    root.config(bg='white')
    # ---------------------------------
    style = ttk.Style()
    style.map("C.TButton",
              foreground=[('pressed', 'red'), ('active', 'blue')],
              background=[('pressed', '!disabled', 'black'), ('active', 'white')]
              )
    Estyle = ttk.Style()
    Estyle.configure('TEntry', foreground='green')

    game = Master(root)
    game.grid(column=1, row=0, rowspan=3)
    root.bind("<Key>", game.redirect)
    buttons = Frame(root, width=35, height=3 * HT / 5)
    ttk.Button(buttons, text='Start', command=game.start).grid()
    ttk.Button(buttons, text='Stop', command=game.clean).grid()
    ttk.Button(buttons, text='Quit', command=root.destroy).grid()
    buttons.grid(column=0, row=0)
    scoreboard = Frame(root, width=35, height=2 * HT / 5, bg='white')

    Label(scoreboard, text='Game Score', font=('Comic Sans MS', 10, 'bold'), fg='green', bg="white").grid()
    Label(scoreboard, textvariable=game.score.counter, font=('Comic Sans MS', 10, 'bold'), fg='#d76737',
          bg="white").grid()
    Label(scoreboard, text='High Score', font=('Comic Sans MS', 10, 'bold'), fg='#d76737', bg="white").grid()
    Label(scoreboard, textvariable=game.score.maximum, font=('Comic Sans MS', 10, 'bold'), fg='#d76737',
          bg="white").grid()
    scoreboard.grid(column=0, row=2)
    root.mainloop()
def wea():
    HEIGHT = 500
    WIDTH = 600

    def test_function(entry):
        print("This is the entry:", entry)

    # api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
    # a4aa5e3d83ffefaba8c00284de6ef7c3

    def format_response(weather):
        try:
            name = weather['name']
            desc = weather['weather'][0]['description']
            temp = weather['main']['temp']

            final_str = 'City: %s \nConditions: %s \nTemperature (°F): %s' % (name, desc, temp)
        except:
            final_str = 'There was a problem retrieving that information'

        return final_str

    def get_weather(city):
        weather_key = 'a4aa5e3d83ffefaba8c00284de6ef7c3'
        url = 'https://api.openweathermap.org/data/2.5/weather'
        params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
        response = requests.get(url, params=params)
        weather = response.json()

        label['text'] = format_response(weather)

    root = Toplevel()
   
    root.title('weather')
    canvas = Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()

    t = Label(root, text='enter your city name in the below box').place(x=70, y=30)

    frame = Frame(root, bg='#80c1ff', bd=5)
    frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

    entry = Entry(frame, font=40)
    entry.place(relwidth=0.65, relheight=1)

    button = Button(frame, text="Get Weather", font=40, command=lambda: get_weather(entry.get()))
    button.place(relx=0.7, relheight=1, relwidth=0.3)

    lower_frame = Frame(root, bg='#80c1ff', bd=10)
    lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

    label = Label(lower_frame)
    label.place(relwidth=1, relheight=1)

    root.mainloop()

def wj():
    root = Toplevel()
    root.title('word jumble')

    my_label = Label(root, text="", font=("Helvetica", 48))
    my_label.pack(pady=20)

    def shuffler():
        # Clear Hint Label
        hint_label.config(text='')

        # Clear Hint Count
        global hint_count
        hint_count = 0

        # Clear Answer Box
        entry_answer.delete(0, END)

        # Clear Answer Label
        answer_label.config(text='')

        # List of state words
        states = ['Washington', 'Oregon', 'California', 'Ohio', 'Nebraska', 'Colorado', 'Michigan', 'Massachusetts',
                  'Florida', 'Texas', 'Oklahoma', 'Hawaii', 'Alaska', 'Utah', 'New Mexico', 'North Dakota',
                  'South Dakota', 'West Virginia', 'Virginia', 'New Jersey', 'Minnesota', 'Illinois', 'Indiana',
                  'Kentucky', 'Tennessee', 'Georgia', 'Alabama', 'Mississippi', 'North Carolina', 'South Carolina',
                  'Maine', 'Vermont', 'New Hampshire', 'Connecticut', 'Rhode Island', 'Wyoming', 'Montana', 'Kansas',
                  'Iowa', 'Pennsylvania', 'Maryland', 'Missouri', 'Arizona', 'Nevada', 'New York', 'Wisconsin',
                  'Delaware', 'Idaho', 'Arkansas', 'Louisiana']

        # Pick random state from list
        global word
        word = choice(states)

        # Break apart our chosen word
        break_apart_word = list(word)
        shuffle(break_apart_word)

        # Turn shuffeled List into a word
        global shuffled_word
        shuffled_word = ''
        for letter in break_apart_word:
            shuffled_word += letter

        # print shuffled word to the screen
        my_label.config(text=shuffled_word)

    # Create answer Function
    def answer():
        if word == entry_answer.get():
            answer_label.config(text="Correct!!")
        else:
            answer_label.config(text="Incorrect!!")

    # Create Hint Counter
    global hint_count
    hint_count = 0

    # Create Hint Function
    def hint(count):
        global hint_count
        hint_count = count

        # Get the length of the chosen word
        word_length = len(word)

        # Show Hint
        if count < word_length:
            hint_label.config(text=f'{hint_label["text"]} {word[count]}')
            hint_count += 1

    entry_answer = Entry(root, font=("Helvetica", 24))
    entry_answer.pack(pady=20)

    button_frame = Frame(root)
    button_frame.pack(pady=20)

    answer_button = Button(button_frame, text="Answer", command=answer)
    answer_button.grid(row=0, column=0, padx=10)

    my_button = Button(button_frame, text="Pick Another Word", command=shuffler)
    my_button.grid(row=0, column=1, padx=10)

    hint_button = Button(button_frame, text="Hint", command=lambda: hint(hint_count))
    hint_button.grid(row=0, column=2, padx=10)

    answer_label = Label(root, text='', font=("Helvetica", 18))
    answer_label.pack(pady=20)

    hint_label = Label(root, text='', font=("Helvetica", 18))
    hint_label.pack(pady=10)

    shuffler()
    root.mainloop()




t=Label(s,text='time',font=("Helvetica",20)).place(x=350,y=55)
t1=Label(s,text='WELCOME TO ALL IN ONE PYTHON APPS',font=("Helvetica",10)).place(x=50,y=55)
t2=Label(s,text='more apps coming soon',font=("Helvetica",20)).place(x=200,y=200)
t3=Label(s,text='thanks for installing me ',font=("Helvetica",15)).place(x=200,y=250)
b1=Button(s,text='calculator',command=calculator).place(x=50,y=150)
b2=Button(s,text='paint',command=col).place(x=50,y=200)
b3=Button(s,text='todo',command=todo).place(x=50,y=250)
b4=Button(s,text='tic tac toe',command=tic).place(x=50,y=300)
b6=Button(s,text='snake',command=snake).place(x=50,y=350)
b7=Button(s,text='weather',command=wea).place(x=50,y=400)
b8=Button(s,text='word jumble game',command=wj).place(x=50,y=450)
def clock():
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    day = time.strftime("%A")
    am_pm = time.strftime("%p")
    time_zone = time.strftime("%Z")

    my_label.config(text=hour + ":" + minute + ":" + second + " " + am_pm)
    my_label.after(1000, clock)




def update():
    my_label.config(text="New Text")


my_label = Label(s, text="", font=("Helvetica", 15), fg="green", bg="black")
my_label.place(x=300,y=100)
clock()

# my_label.after(5000, update)
s.mainloop()
