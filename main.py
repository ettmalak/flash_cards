from tkinter import *
import pandas


BACKGROUND_COLOR = "#B1DDC6"



window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

data = pandas.read_csv("data/french_words.csv")
word = data["French"].sample(1).values[0]



canvas = Canvas(width=800, height=526)

card_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front)
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
word_text=canvas.create_text(400, 263, text=word, font=("Ariel", 60, "bold"))
def pick_new_word():
    word = data["French"].sample(1).values[0]
    canvas.itemconfig(word_text, text=word)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image)
unknown_button.grid(row=1, column=0)
unknown_button.config(background=BACKGROUND_COLOR, highlightthickness=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, command=pick_new_word)
known_button.grid(row=1, column=1)
known_button.config(background=BACKGROUND_COLOR, highlightthickness=0)


window.mainloop()