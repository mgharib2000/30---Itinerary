from tkinter import *

def write():
    date = date_entry.get()
    text = text_entry.get()
    Itinerary = open("Itinerary.txt", "a")
    Itinerary.write(date + ":" + "\n" + text + "\n" + "\n")
    Itinerary.close()



app = Tk()
app.title("Itinerary")
app.geometry = ("400x200")
app.config(bg="GREY")

date_label = Label(app, text="Enter date here: ")
date_label.grid(row=0, column=0, padx=1, pady=1, sticky="EW")
date_entry = Entry(app)
date_entry.grid(row=0, column=1, padx=1, pady=1, sticky="EW")


text_label = Label(app, text="Enter text here: ")
text_label.grid(row=1, column=0, padx=1, pady=1, sticky="EW")
text_entry = Entry(app)
text_entry.grid(row=1, column=1, padx=1, pady=1, sticky="EW")


quit_button = Button(app, text = "Quit", command = app.destroy)
quit_button.grid(row=2, column=0, padx=1, pady=1, sticky="EW")

print_button = Button(app, text = "Print", command = write)
print_button.grid(row=2, column=1, padx=1, pady=1, sticky="EW")


app.mainloop()

