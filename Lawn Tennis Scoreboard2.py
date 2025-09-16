#MODULE IMPORTATION OF USED PYTHON LIBRARIES
import tkinter as tk
from tkinter import messagebox
import sqlite3 as lite
from datetime import datetime
import csv
from PIL import ImageTk, Image
from tkinter import filedialog as fd

#2D ARRAY COMPOSED OF DATE, PLAYERS NAME, AND SCORES IN EACH ROW
data = [[],[]]
date_now = datetime.now().strftime('%Y-%m-%d')
data[0].append(date_now);data[1].append(date_now)
def save_function():
    conn = lite.connect('storage1.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS RecordOne(Date TEXT, Name TEXT, Set1_Score INT, Set2_Score INT, Set3_Score INT,Set4_Score INT, Set5_Score INT)')
    listed1 = (data[0],data[1])
    count = len(data[0])
    print(count)
    if count == 5:
        c.executemany('INSERT INTO RecordONE (Date, Name, Set1_Score, Set2_Score, Set3_Score)VALUES(?,?,?,?,?)',listed1)
    elif count == 6:
        c.executemany('INSERT INTO RecordONE (Date, Name, Set1_Score, Set2_Score, Set3_Score,Set4_Score)VALUES(?,?,?,?,?,?)',listed1)
    elif count == 7:
        c.executemany('INSERT INTO RecordONE (Date, Name, Set1_Score, Set2_Score, Set3_Score,Set4_Score, Set5_Score)VALUES(?,?,?,?,?,?,?)',listed1)
    else:
        tk.messagebox.showinfo("Message", "Did not met set requirement of more than 3 sets")
    conn.commit()
    def show_data():
        c.execute('SELECT * FROM RecordONE')
        show = c.fetchall()
        print(show)
    show_data()
    c.close()
    conn.close()

def export():
    listed1 = (data[0],data[1])
    date = datetime.now().strftime('%Y%m%d%H%M%S')
    with open(f"{date}_{stored}vs{stored1}.csv",'w') as f:
        writer = csv.writer(f)
        for i in listed1:
            writer.writerow(i)
        f.close()

def history():
        conn = lite.connect('storage.db')
        c = conn.cursor()
        c.execute('SELECT * FROM RecordONE')
        show = c.fetchall()
        print(show)
        conn.commit()
        c.close()
        conn.close()

class app(tk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.y_axis = int(root.winfo_screenwidth()/4)
        self.x_axis = int(root.winfo_screenheight()/4)
        self.parent.geometry(f"680x350+{self.y_axis}+{self.x_axis}")
        self.players()
        
    def players(self, event =None):
        for i in self.parent.winfo_children():
            i.destroy()
# BACKGROUND IMAGE DECLARATION
        self.parent.geometry(f"680x350+{self.y_axis}+{self.x_axis}")
        self.parent.title("Enter Player Names")
        self.parent.resizable(0,0)
        self.bgimg = Image.open("IT122 SYSTEM TRIAL/ImgeResources/1.png")
        self.bgimg= self.bgimg.resize((680, 350), Image.Resampling.LANCZOS)
        self.Bgbg = ImageTk.PhotoImage(self.bgimg)
        self.canvas = tk.Canvas(self.parent)
        self.canvas.pack(fill= "both", expand=True)
        self.canvas.create_image(0, 0, image=self.Bgbg, anchor="nw")
#ENTRY WIDGETS
        self.frame = tk.Frame(self.parent, padx=10, pady=10, background="#666699")
        self.frame.place(x=340, y = 150, anchor=tk.CENTER)
        self.l_1=tk.Label(self.frame, text="Enter Player 1 Name:",font =("Constantia", 12, "bold"), justify = "left")
        self.l_1.grid()
        self.e_1 = tk.Entry(self.frame, bd = 3, font = ("Cambria 15 bold"), width=20,)
        self.e_1.focus_set()
        self.e_1.grid(row = 0,column = 1,pady=2)
        self.l_2=tk.Label(self.frame, text="Enter Player 2 Name:", font =("Constantia", 12, "bold"), justify="left")
        self.l_2.grid(row=1, sticky = "ew")
        self.e_2 = tk.Entry(self.frame, bd = 3,font = ("Cambria 15 bold"), width=20)
        self.e_2.grid(row = 1, column = 1, pady=3)
#STORING METHOD
        self.incount = 0
        def store_all(event = None):
            var_1 = self.e_1.get().upper()
            var_2 = self.e_2.get().upper()
            self.incount += 1
            if var_1 == "":
                messagebox.showinfo("Message", "Enter Player 1")
            elif var_2 =="":
                if self.incount == 1:
                    self.e_2.focus_set()
                elif self.incount >=2:
                    messagebox.showinfo("Message", "Enter Player 2")
            else:
                global stored
                stored = var_1
                global stored1
                stored1 = var_2
                data[0].append(stored)
                data[1].append(stored1)
                self.start()
                print(data[0][1])
                print(data[1][1])
        self.parent.bind('<Return>', store_all)
        b = tk.Button(self.frame, text="ENTER", font = ("Modern No. 20", 13, "bold"),width=10, command= store_all)
        b.grid(columnspan = 2, sticky="ew", pady= 5)

    def start(self):
        for i in self.parent.winfo_children():
            i.destroy()
        self.parent.bind('<Return>', self.TennisScoreboard)
        self.parent.title("Instruction")
        self.parent.geometry(f"720x390+{self.y_axis}+{self.x_axis}")
        self.Menu()
        self.File_menu.entryconfig(2, state = "disabled")
        self.File_menu.entryconfig(3, state = "disabled")
        self.Help_menu.entryconfig(0, state = "disabled")
        self.canvas = tk.Canvas(self.parent)
        self.canvas.pack(fill= "both", expand=True)
        self.star(self.canvas)
        self.register_btn = tk.Button(self.parent, text="START",font=("Arial Rounded MT Bold", 13,"bold"),border= 3,command=self.TennisScoreboard)
        self.canvas.create_window(315, 345, window=self.register_btn)

    def star(self, head):
#IMPORTING IMAGES:
        self.Simg1 = Image.open("IT122 SYSTEM TRIAL/ImgeResources/2.png")
        self.SImg1= self.Simg1.resize((760, 430), Image.Resampling.LANCZOS)
        self.SBg1 = ImageTk.PhotoImage(self.SImg1)
        def resz(path):
            img_open = Image.open(path).convert("RGBA")
            img_open = img_open.resize((60, 45), Image.Resampling.LANCZOS)
            final = ImageTk.PhotoImage(img_open)
            return final
        self.Left = resz("IT122 SYSTEM TRIAL/ImgeResources/Left.png")
        self.Right = resz("IT122 SYSTEM TRIAL/ImgeResources/Right.png")
        self.Space = resz("IT122 SYSTEM TRIAL/ImgeResources/spacey.png")
        self.X_K = resz("IT122 SYSTEM TRIAL/ImgeResources/X_K.png")
#DISPLAYING IMAGES TO UI
        head.create_image(340, 175, image=self.SBg1)
        head.create_image(140, 100, image=self.Left)
        head.create_image(140, 150, image=self.Right)
        head.create_image(140, 200, image=self.Space)
        head.create_image(140, 250, image=self.X_K)
        head.create_text(340, 50, text="GENERAL INSTRUCTION",font=("Rockwell Extra Bold", 19,"bold", "underline"), anchor="center")
        head.create_text(200, 100, text="ADD PLAYER ONE SCORE",font=("Arial Black", 14,"bold"), fill = "#ccffcc",anchor="w")
        head.create_text(200, 150, text="ADD PLAYER TWO SCORE",font=("Arial Black", 14,"bold"), fill = "#ccffcc", anchor="w")
        head.create_text(200, 200, text="NEXT SET",font=("Arial Black", 14,"bold"), fill = "#f4fdff", anchor="w")
        head.create_text(200, 250, text="NEW GAME",font=("Arial Black", 14,"bold"), fill = "#f4fdff", anchor="w")


    def congratulatory_message(self):
        data[0].append(self.counter1)
        data[1].append(self.counter2)
        save_function()
        self.tops = tk.Toplevel(self.parent)
        self.tops.geometry(f'{int(root.winfo_screenwidth()-60)}x{int(root.winfo_screenheight()-60)}+20+20')
        self.tops.resizable(0,0)
        self.canvas = tk.Canvas(self.tops)
        self.canvas.pack(fill= "both", expand=True)
        self.img = self.acshesh('IT122 SYSTEM TRIAL/ImgeResources/win.png',int(root.winfo_screenwidth()-60),int(root.winfo_screenheight()-60) )
        self.canvas.create_image(0, 0, image=self.img, anchor="nw")
        self.reg_txt1 = tk.Label(self.parent, image= self.img)
        self.canvas.create_text(680, 330, text=f'{self.variad}',font=("Cambria", 80), anchor="center")
        self.bck_btn = tk.Button(self.tops, text = 'BACK',command= self.tops.destroy)
        self.bck_btn.place(x='1300',y='670',anchor=tk.CENTER)

    def TennisScoreboard(self, event = None):
        for i in self.parent.winfo_children():
            i.destroy()
#CONFIGURATION OF TKINTER WINDOW AND BINDING TO KEYS
        self.parent.title("Tennis Scoreboard")
        self.parent.bind('<Left>',self.update_player1_score)
        self.parent.bind('<Return>',"")
        self.parent.bind('<Right>',self.update_player2_score)
        self.parent.bind('<x>',self.players)
        self.parent.geometry(f'{int(root.winfo_screenwidth())}x{int(root.winfo_screenheight())}+0+0')
        self.parent.resizable(0,0)
# INITIALIZATION OF VARIABLES
        self.reset_press = 0
        self.counter1 = 0
        self.counter2 = 0
        self.variad = 0 
        self.pressed = 0
        self.pressed1 = 0
        self.player1_score = "LOVE"
        self.player2_score = "LOVE"
        self.set = 1
# BACKGROUND IMAGE ACCESSING AND DISPLAY
        self.border = self.acshesh("IT122 SYSTEM TRIAL/ImgeResources/recborder.png", 400, 150)
        self.sign = self.acshesh("IT122 SYSTEM TRIAL/ImgeResources/border.png", 50, 50)
        self.MainBg = self.acshesh("IT122 SYSTEM TRIAL/ImgeResources/main_bg.webp", int(root.winfo_screenwidth()),int(root.winfo_screenheight()))
        self.canvas = tk.Canvas(self.parent)
        self.canvas.pack(fill= "both", expand=True)
        self.canvas.create_image(0, 0, image=self.MainBg, anchor="nw")
        self.canvas.create_image(340,350, image=self.border, anchor="center")
        self.canvas.create_image(1020,350, image=self.border, anchor="center")
# MENU
        self.Menu()
# DISPLAY TEXT TO CANVAS FRAME
        self.disp_playered = self.canvas.create_text(340, 250, text=f"{stored}",fill = "white",font=("Times New Roman", 30, "bold","underline"))
        self.disp_playered1 = self.canvas.create_text(1020, 250, text=f"{stored1}", fill="white",font=("Times New Roman", 30, "bold","underline"))
        self.set_disp = self.canvas.create_text(680, 120, text=f"{self.set}",fill="red", font=("Arial", 90))
        self.canvas.create_text(680, 220, text="SET",fill="white",font=("Arial", 50))
        self.disp1_score= self.canvas.create_text(340, 440, text=f"{self.counter1}",fill ="white",font=("Arial", 30))
        self.disp2_score=self.canvas.create_text(1020, 440, text=f"{self.counter2}",fill="white",font=("Arial", 30))   
        self.score_label1 = self.canvas.create_text(340,350,text=f"{self.player1_score}",font=("Helvetica", 100))
        self.score_label2 = self.canvas.create_text(1020,350,text=f"{self.player2_score}",font=("Helvetica", 100))
#FUNCTIONS USED
    def save_as(self):
        name = fd.asksaveasfilename(initialfile = f"{date_now}_{stored}vs{stored1}", defaultextension=".csv", filetypes=[("CSV_file \".csv\"","*.csv")])
        listed1 = (data[0],data[1])
        with open(f"{name}",'w') as f:
            writer = csv.writer(f)
            for i in listed1:
                writer.writerow(i)
            f.close()
            
    def Menu(self):
        self.Mnu = tk.Menu(self.parent)
        self.File_menu = tk.Menu(self.Mnu, tearoff=0)
        self.File_menu.add_command(label="New Game", command =self.new_game)
        self.File_menu.add_separator()
        self.File_menu.add_command(label="Save", command = export)
        self.File_menu.add_command(label="Save As", command =self.save_as)
        self.File_menu.add_separator()
        self.File_menu.add_command(label="Exit", comman = self.parent.destroy)
        self.Help_menu = tk.Menu(self.Mnu, tearoff=0)
        self.Help_menu.add_command(label="Instruction", comman = self.inst_top)
        self.Help_menu.add_separator()
        self.Help_menu.add_command(label="About", command = self.about)
        self.Mnu.add_cascade(label = "File", menu = self.File_menu)
        self.Mnu.add_cascade(label = "Help", menu = self.Help_menu)
        self.parent.config(menu = self.Mnu)
        
    def inst_top(self):
        self.top = tk.Toplevel(self.parent)
        self.top.title("Instruction")
        self.top.geometry(f"720x390+{self.y_axis}+{self.x_axis}")
        self.canva = tk.Canvas(self.top)
        self.canva.pack(fill= "both", expand=True)
        self.star(self.canva)
        self.top.mainloop()

    def about(self):
        self.top_lev = tk.Toplevel(self.parent)
        self.top_lev.title("About")
        self.top_lev.geometry(f"720x390+{self.y_axis}+{self.x_axis}")
        self.canvas1 = tk.Canvas(self.top_lev)
        self.canvas1.pack()
        self.canvas1.create_text(100, 30, text = "Version\n      Lawn_Tennis_ScoreBoard Version 1.0.10 \n", justify = "center", anchor="center")
        self.canvas1.create_text(40, 60, text = "Credits\n                       Group 3:", justify = "center", anchor="center")
        self.canvas1.create_text(140, 120, text = " Aganao, Kathlyn\n Cabanigan John Micheal\n Durog Noe\n Jaglawan Karren \n Namata Rusty \n Pecato Justine ", justify = "left", anchor="center")
        self.top_lev.mainloop()

    def new_game(self):
        del data[0][1:]
        del data[1][1:]
        self.players()

    def new_set(self, event): 
        data[0].append(self.counter1)
        data[1].append(self.counter2)
        self.parent.bind('<Left>',self.update_player1_score)
        self.parent.bind('<Right>',self.update_player2_score)
        self.counter1 = 0
        self.counter2 = 0
        self.set += 1
        self.player1_score = "LOVE"
        self.player2_score = "LOVE"
        self.canvas.itemconfig(self.disp1_score, text="0")
        self.canvas.itemconfig(self.disp2_score,text="0")
        self.canvas.itemconfig(self.score_label1, text=f"{self.player1_score}")
        self.canvas.itemconfig(self.score_label2,text=f"{self.player2_score}")
        self.canvas.itemconfig(self.set_disp,text=f'{self.set}')
        for i in data:
            print(i)
        self.parent.unbind('<space>',self.new_set)

    def update_player1_score(self, event):
        if self.player2_score != "GAME" and  self.player1_score != "GAME":
            self.counter1 += 1
        else:
            self.parent.unbind('<Left>',self.update_player1_score)
            self.parent.unbind('<Right>',self.update_player2_score)
            self.parent.bind('<space>',self.new_set)

        if self.counter1 == 1:
            self.player1_score = "15"
        elif self.counter1 == 2 and self.player2_score != 'GAME':
            self.player1_score = "30"
        elif self.counter1 == 3 and self.player2_score =="40":
            self.player1_score = "40"
            self.duece = self.canvas.create_text(680, 300, text='DUECE', fill="white",font=("Arial", 30))
        elif self.counter1 == 3 and self.player2_score != 'GAME':
            self.player1_score = "40"
        elif self.player1_score =="40" and self.player2_score =="40":
            self.player2_score = "add"
            self.canvas.delete(self.duece)
        elif self.player1_score =="add" and self.player2_score =="40":
            self.duece = self.canvas.create_text(680, 300, text='DUECE',fill = "white",font=("Arial", 30))
            self.player1_score = "40"
        elif  self.player2_score == "GAME":
            self.player1_score = ""
        else:
            self.player1_score = "GAME"
            self.pressed +=1
            self.parent.bind('<space>',self.new_set)
            print('this1',self.pressed)
            if self.pressed == 1:
                self.canvas.create_image(300, 490, image = self.sign, anchor ="center")
            elif self.pressed == 2:
                self.canvas.create_image(340, 490, image = self.sign, anchor ="center")
            elif self.pressed == 3:
                self.variad = stored
                self.after(1000, self.congratulatory_message)

        self.canvas.itemconfig(self.disp1_score, text=f"{self.counter1}")
        self.canvas.itemconfig(self.score_label1, text=f"{self.player1_score}")
        self.canvas.itemconfig(self.score_label2, text=f"{self.player2_score}")                

    def update_player2_score(self, event):
        if self.player2_score != "GAME" and  self.player1_score != "GAME":
            self.counter2 += 1
        else:
            self.parent.unbind('<Left>',self.update_player1_score)
            self.parent.unbind('<Right>',self.update_player2_score)
            self.parent.bind('<space>',self.new_set)
            
        if self.counter2 == 1:
            self.player2_score = "15"
        elif self.counter2 == 2 and self.player1_score != 'GAME':
            self.player2_score = "30"
        elif self.counter2 == 3 and self.player1_score == "40":
            self.player2_score = "40"
            self.duece = self.canvas.create_text(680, 300, text='DUECE',font=("Arial", 30))
        elif self.counter2 == 3 and self.player1_score != 'GAME':
            self.player2_score = "40"
        elif self.player1_score =="40" and self.player2_score =="40":
            self.player1_score = "add"
            self.canvas.delete(self.duece)
        elif self.player1_score =="40" and self.player2_score =="add":
            self.player2_score = "40"
            self.duece = self.canvas.create_text(680, 300, text='DUECE',font=("Arial", 30))
        elif self.player1_score == 'GAME':
            self.player2_score = ""
        else:
            self.player2_score = "GAME"
            self.pressed1 +=1
            self.parent.bind('<space>',self.new_set)
            print('this2',self.pressed1)
            if self.pressed1 == 1:
                self.canvas.create_image(980, 490, image = self.sign, anchor ="center")
            elif self.pressed1 == 2:
                self.canvas.create_image(1020, 490, image = self.sign, anchor ="center")
            elif self.pressed1 == 3:
                self.variad = stored1
                self.after(1000, self.congratulatory_message)

        self.canvas.itemconfig(self.disp2_score, text=f"{self.counter2}")
        self.canvas.itemconfig(self.score_label1, text=f"{self.player1_score}")
        self.canvas.itemconfig(self.score_label2, text=f"{self.player2_score}")
    def acshesh(self, path, width, height):
        img_open = Image.open(path).convert("RGBA")
        img_open = img_open.resize((width, height), Image.Resampling.LANCZOS)
        final = ImageTk.PhotoImage(img_open)
        return final
#MAIN ROOT TO DISPLAY
root = tk.Tk()
app(root)
root.mainloop()