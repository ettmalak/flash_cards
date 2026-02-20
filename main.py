from tkinter import *
import pandas, random
import time

BACKGROUND_COLOR = "#B1DDC6"



window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")



canvas = Canvas(width=800, height=526)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
card_title=canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word=canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
current_card = {}
def pick_new_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer=window.after(3000, show_english)

def show_english():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill = "white")

flip_timer = window.after(3000, show_english)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, command=pick_new_word)
unknown_button.grid(row=1, column=0)
unknown_button.config(background=BACKGROUND_COLOR, highlightthickness=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, command=pick_new_word)
known_button.grid(row=1, column=1)
known_button.config(background=BACKGROUND_COLOR, highlightthickness=0)

pick_new_word()


window.mainloop()