import tkinter as tk
from tkinter.constants import CENTER, NSEW

def bmi_convert():
    height_to_mpow = (float(entry_height.get())/100)**2
    weight = float(entry_weight.get())
    result = "Normal"

    bmi = round(weight/height_to_mpow, 2)
    if bmi < 18.5:
        result = "Underweight"
    elif bmi >= 18.5 and bmi < 25:
        result = "Normal"
    elif bmi >= 25 and bmi < 30:
        result = "Overweight"
    elif bmi >= 30:
        result = "Obese"
    else:
        result = "Can't be defined"

    label_bmiresult["text"] = f"BMI: {str(bmi)}"
    label_bmistatus["text"] = f"Status: {result}"
    
window = tk.Tk()
window.title("BMI Calculator")
window.grid_rowconfigure([0,1,2,3], weight=1)
window.grid_columnconfigure(0, weight=1)
window.resizable(width=False, height=False)

#Row1
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
frame_result = tk.Frame(master=window)
frame_result.grid(row=2, column=0, sticky="nswe")
frame_result.grid_rowconfigure([0,1], weight=1)
frame_result.grid_columnconfigure([0], weight=1)

label_bmiresult = tk.Label(master=frame_result, text="BMI: --")
label_bmiresult.grid(row=0, column=0, sticky="nswe", padx=10, pady=5)
label_bmistatus = tk.Label(master=frame_result, text="Status: --")
label_bmistatus.grid(row=1, column=0, sticky="nswe", padx=10, pady=5)

#Row4
frame_count = tk.Frame(master=window)
frame_count.grid(row=3, column=0, sticky="nswe")
frame_count.grid_rowconfigure(0, weight=1)
frame_count.grid_columnconfigure(0, weight=1)

button_count = tk.Button(master=frame_count, text="Count", command=bmi_convert)
button_count.grid(row=0, column=0, padx=10, pady=10)


window.mainloop()