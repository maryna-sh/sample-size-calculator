import tkinter
import math

window = tkinter.Tk()
window.title("Calculator")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

title = tkinter.Label(text="Calculate sample size", font=("Times New Roman", 20, "bold"))
title.grid(column=2, row=1)

confidence = tkinter.Label(text="Confidence level", font=("Times New Roman", 15, "normal"))
confidence.grid(column=1, row=5)
input_conf = tkinter.Entry()
input_conf.grid(column=2, row=5)

perc = tkinter.Label(text="%", font=("Times New Roman", 15, "normal"))
perc.grid(column=3, row=5)



# margin of error
margin_error = tkinter.Label(text="Margin of error", font=("Times New Roman", 15, "normal"))
margin_error.grid(column=1, row=10)
input_margin_error = tkinter.Entry()
input_margin_error.grid(column=2, row=10)

margin_perc = tkinter.Label(text="%", font=("Times New Roman", 15, "normal"))
margin_perc.grid(column=3, row=10)

pop_size = tkinter.Label(text="Population size (if known)", font=("Times New Roman", 15, "normal"))
pop_size.grid(column=1, row=30)
input_pop_size = tkinter.Entry()
input_pop_size.grid(column=2, row=30)


pop_prop = tkinter.Label(text="Population Proportion", font=("Times New Roman", 15, "normal"))
pop_prop.grid(column=1, row=40)
input_pop_prop = tkinter.Entry()
input_pop_prop.grid(column=2, row=40)

pop_perc = tkinter.Label(text="%", font=("Times New Roman", 15, "normal"))
pop_perc.grid(column=3, row=40)

resizer_button1 = tkinter.Label(text="", font=("Times New Roman", 15, "normal"), height=1)
resizer_button1.grid(column=1, row=41)

# resizer = tkinter.Label(text="", font=("Times New Roman", 15, "normal"), width=12)
# resizer.grid(column=3, row=2)

def calc():
    conf = float(input_conf.get())
    pp = float(input_pop_prop.get())
    me = float(input_margin_error.get())
    z = 0
    conf = conf / 100
    pp = pp / 100
    me = me/100
    if conf > 0.70 and conf < 0.75:
        z = 1.04
    elif conf >= 0.75 and conf < 0.80:
        z = 1.15
    elif conf >= 0.80 and conf < 0.85:
        z = 1.28
    elif conf >= 0.85 and conf < 0.92:
        z = 1.44
    elif conf >= 0.92 and conf < 0.95:
        z = 1.75
    elif conf >= 0.95 and conf < 0.96:
        z = 1.96
    elif conf >= 0.96 and conf < 0.98:
        z = 2.05
    elif conf >= 0.98 and conf < 0.99:
        z = 2.33
    elif conf >= 0.98 and conf < 0.99:
        z = 3.29
    elif conf >= 0.9:
        z = 3.89

    if input_pop_size.get():
       N = int(input_pop_size.get())
       n = math.ceil((N*((z**2 * pp * (1-pp)) / (me**2))) / (((z**2 * pp*(1-pp)) / (me**2)) + N - 1))
    else:
       n = math.ceil((z*z*pp*(1-pp))/(me*me))

    result.config(text=n)



button = tkinter.Button(text="Calculate", width=10, height=1, command=calc)
button.grid(column=1, row=50)
button.config(padx=3, pady=10)

resizer_button2 = tkinter.Label(text="", font=("Times New Roman", 15, "normal"))
resizer_button2.grid(column=1, row=51)



ss = tkinter.Label(text="Your minimum sample size: ", font=("Times New Roman", 15, "normal"))
ss.grid(column=1, row=60)

result = tkinter.Label(text="", font=("Times New Roman", 18, "bold"))
result.grid(column=2, row=60)




tkinter.mainloop()
