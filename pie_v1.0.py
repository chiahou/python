

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
from statistics import mean
import numpy
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

root = Tk()
root.attributes('-fullscreen', True)
root.counter = 0

"""Scores"""
ideas = []
p_scores = []
i_scores = []
e_scores = []
mean_scores = []
idea_index = []

"""buttons"""
style = ttk.Style()
ttk.Style().configure("Primary.Tbutton", relief="flat", background="#FCC9BE")
style.map("Primary.TButton", 
	background=[('pressed', '#FA8167'),('active', '#FA8167')],
	foreground=[('pressed', '#ffffff'),('active', '#0055ac')],
    )
style.map("Round.TButton",
    background=[('pressed', '#FA8167'),('active','#C70039')],
    foreground=[('pressed', '#ffffff'),('active','#C70039')],
    )


"""Font Types"""
h1 = ("Helvetica", 32)

"""Site Name"""
var = StringVar()
site_name = Label(root, textvariable=var, font=h1, anchor=CENTER, height=5)
var.set("PIE Calculator")
site_name.pack(side=TOP)

"""frame1"""
def add_idea():
    root.counter += 1
    btn_submit.config(state='normal')
    idea = LabelFrame(subframe2, text=f'Please give idea No.{root.counter} a P,I,E score', bg="#ffffff")
    idea.pack(side = TOP)
    ideas.append(idea)
    title_p = Label(idea, text="P")
    title_p.pack(side=LEFT)
    p = Entry(idea)
    p.pack(side = LEFT)
    p_scores.append(p)
    title_i = Label(idea, text="I")
    title_i.pack(side=LEFT)
    i = Entry(idea)
    i.pack(side = LEFT)
    i_scores.append(i)
    title_e = Label(idea, text="E")
    title_e.pack(side=LEFT)
    e = Entry(idea)
    e.pack(side = LEFT)
    e_scores.append(e)

def submit_answer():
    project_name = input_name.get()
    if len(project_name) == 0:
        messagebox.showinfo('Alert','Please enter a project name')
    else:
        messagebox.showinfo('Congrats!',f'You score has been submitted!')
        quantity = len(ideas)
        for i in range(0,quantity):
            mean_score = mean([int(p_scores[i].get()), int(i_scores[i].get()), int(e_scores[i].get())])
            mean_scores.append(mean_score)
            idea_index.append(f'No.{i+1}')
        """score_dict = {'P' : p_scores, 'I' : i_scores, 'E' : e_scores, 'Mean' : mean_scores}
        print(pd.DataFrame.from_dict(score_dict))
        plt.plot(idea_index, mean_scores)"""
        fig = Figure(figsize=(5,4), dpi=100)
        print(idea_index)
        fig.add_subplot(111).barh(idea_index,width=mean_scores, height=-0.5, align='edge', tick_label=idea_index)
        fig.suptitle(project_name, fontsize=16)
        canvas = FigureCanvasTkAgg(fig, master=frame2)
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH)
        def on_key_press(event):
            print("you pressed {}".format(event.key))
            key_press_handler(event, canvas)
        canvas.mpl_connect("key_press_event", on_key_press)

frame1 = Frame(root)
frame1.pack(side=LEFT, fill=BOTH, expand=True)
subframe1 = Frame(frame1)
subframe1.pack(side=TOP)
label_name = Label(subframe1, text="Project Name", bg="#ffffff")
label_name.pack(side=LEFT)
input_name = Entry(subframe1, bd = 1)
input_name.pack(side=LEFT)
btn_add = ttk.Button(subframe1, text='add an idea', style="Round.TButton", command=add_idea)
btn_add.pack(side=LEFT, pady=10, padx=5)
subframe2= Frame(frame1)
subframe2.pack(side=TOP)
subframe3= Frame(frame1)
subframe3.pack(side=TOP)
btn_submit = ttk.Button(subframe3, text="Submit", width=20, style="Primary.TButton", command=submit_answer, state=DISABLED)
btn_submit.pack(side=TOP)



frame2 = Frame(root, bg="#f7f7f7")
frame2.pack(side=RIGHT, fill=BOTH, expand=True)
figure_title = Label(frame2, text="Your Final Results", fg="#e9e9e9")
figure_title.pack(side=TOP)


mainloop()