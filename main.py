from tkinter import *
#Grammatik Tester einbauen
import time
from tkinter import messagebox

dauer = 0
def timer_start():
    geschwindigkeit = None
    global start
    end = 0
    if button_state.get() == 0:
        textfeld.config(state="normal")
        start = int(time.time())

        counter_start_button.config(text="Stopp")
        button_state.set(1)
        canvas.delete("all")

    elif button_state.get() == 1:
        end = int(time.time())
        dauer = end - start
        counter_start_button.config(text="Start")
        button_state.set(0)
        geschwindigkeit = int(len(textfeld.get("1.0", "end-1c")) / dauer)
        textfeld.delete("1.0", "end-1c")

        if geschwindigkeit == 0:
            canvas.create_text(170, 25, text = f"Ihre Schreibgeschwindigkeit beträgt:", anchor="center", font=("Arial", 12, "bold"), fill="red")
            canvas.create_text(170, 50, text = f"{geschwindigkeit} Zeichen pro Sekunde", anchor="center", font=("Arial", 12, "bold"), fill="red")
            canvas.create_text(170, 75, text="Sind Sie eingeschalfen??", anchor="center",
                               font=("Arial", 12, "bold"), fill="red")

        elif geschwindigkeit > 0 and geschwindigkeit < 4:
            canvas.create_text(170, 25, text=f"Ihre Schreibgeschwindigkeit beträgt:", anchor="center",
                               font=("Arial", 12, "bold"), fill="orange")
            canvas.create_text(170, 50, text=f"{geschwindigkeit} Zeichen pro Sekunde", anchor="center",
                               font=("Arial", 12, "bold"), fill="orange")


        elif geschwindigkeit >= 5:
            canvas.create_text(170, 25, text=f"Ihre Schreibgeschwindigkeit beträgt:", anchor="center",
                               font=("Arial", 12, "bold"), fill="green")
            canvas.create_text(170, 50, text=f"{geschwindigkeit} Zeichen pro Sekunde", anchor="center",
                               font=("Arial", 12, "bold"), fill="green")
            canvas.create_text(170, 75, text="AUSGEZEICHNET !!!", anchor="center",
                               font=("Arial", 12, "bold"), fill="red")

        textfeld.config(state="disabled")

        #textfeld.config(text ="")


def klick_auf_deaktiviertes_textfeld(event):
    if textfeld.cget("state") == "disabled":
        messagebox.showerror("Fehler", "Das Textfeld ist deaktiviert! Drücken Sie auf Start")


window = Tk()
window.title("Typing Speed Tester")
window.config(background="#F5F5DC")
window.geometry("500x750")

label_befehl = Label(window, text="Geben Sie ihren Text ein", background="#F5F5DC", font=("Arial", 16, "bold"))
label_befehl.pack(pady=20)



textfeld = Text(window, wrap="word", width=40, height=20, pady=20, state="disabled")
textfeld.pack(pady=50)
textfeld.bind("<Button-1>", klick_auf_deaktiviertes_textfeld)


#label_geschwindigkeit = Label(window, text="")
#label_geschwindigkeit.pack()

canvas = Canvas(window, width=350, height=100, background="#F5F5DC", highlightthickness=0)
canvas.pack(pady=20)

button_state = IntVar(value=0)
counter_start_button = Button(window, text="Start", command=timer_start, width=10, height=3 )

counter_start_button.pack()






window.mainloop()

