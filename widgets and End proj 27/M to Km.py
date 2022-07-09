from tkinter import *

window = Tk()
window.title("Miles to Km")
window.config(padx=50, pady=50)

#input
miles_entry = Entry(width=10)
miles_entry.grid(column=1, row=0)

#is equal to
is_equal = Label(text="is equal to")
is_equal.grid(column=0, row=1)

#Final value in kms
final_val = Label(text=0)
final_val.grid(column=1, row=1)
final_val.config(text=0)


def Button_clicked():
    input = float(miles_entry.get())
    km_value = input * 1.609
    final_val.config(text=f"{km_value}")

#Calculate Button
calc = Button(text="Calculate", command=Button_clicked)
calc.grid(column=1, row=2)

#Miles Label
miles = Label(text="Miles")
miles.grid(column=2, row=0)

#Km Label
Km = Label(text="Km")
Km.grid(column=2, row=1)













window.mainloop()
