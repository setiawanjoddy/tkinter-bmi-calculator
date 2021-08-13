import tkinter as tk
from tkinter.constants import CENTER, NSEW

def bmi_convert():
    height_to_m = float(entry_height.get())/100
    weight_pow2 = float(entry_weight.get())**2
    

window = tk.Tk()
window.title("BMI Calculator")
window.grid_rowconfigure([0,1,2,3], weight=1)
window.grid_columnconfigure(0, weight=1)
window.resizable(width=False, height=False)

#Row 1
label_welcome = tk.Label(master=window, text="Hello, Welcome to BMI Calculator!")
label_welcome.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)

#Row2
frame_input = tk.Frame(master=window)
frame_input.grid(row=1, column=0, sticky = "nswe", padx=10, pady=10)
frame_input.grid_rowconfigure([0,1], weight=1)
frame_input.grid_columnconfigure([0,1], weight=1)

label_height = tk.Label(master=frame_input, text="Height(cm):")
label_height.grid(row=0, column=0, sticky="nswe")
label_weight = tk.Label(master=frame_input, text="Weight(kg):")
label_weight.grid(row=0, column=1, sticky="nswe")

entry_height = tk.Entry(master=frame_input)
entry_height.grid(row=1, column=0, sticky="we", padx=8, pady=8)
entry_weight = tk.Entry(master=frame_input)
entry_weight.grid(row=1, column=1, sticky="we", padx=8, pady=8)

#Row3

#Row4
frame_count = tk.Frame(master=window)
frame_count.grid(row=3, column=0, sticky="nswe")
frame_count.rowconfigure(0, weight=1)
frame_count.columnconfigure(0, weight=1)

button_count = tk.Button(master=frame_count, text="Count", command=bmi_convert)
button_count.grid(row=0, column=0, padx=5, pady=5)


window.mainloop()