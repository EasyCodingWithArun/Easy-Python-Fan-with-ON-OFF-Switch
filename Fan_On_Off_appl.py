from tkinter import *
import math

angle = 0
running = False
fan_speed = 20
animation_delay = 30

def draw_fan():
    global angle
    canvas.delete("all")
    cx, cy = 150, 150
    r_blade = 100
    r_hub = 25

    for i in range(3):
        current_blade_angle = angle + i * 120
        x_tip = cx + r_blade * math.cos(math.radians(current_blade_angle))
        y_tip = cy + r_blade * math.sin(math.radians(current_blade_angle))
        canvas.create_line(cx, cy, x_tip, y_tip, width=25, fill="#3498db", capstyle=ROUND)

    canvas.create_oval(cx - r_hub, cy - r_hub, cx + r_hub, cy + r_hub,
                       fill="#2c3e50", outline="#7f8c8d", width=2)

    if running:
        angle = (angle + fan_speed) % 360
        root.after(animation_delay, draw_fan)

def start_fan():
    global running
    if not running:
        running = True
        status_label.config(text="Fan is ON", fg="#2ecc71")
        draw_fan()

def stop_fan():
    global running
    if running:
        running = False
        status_label.config(text="Fan is OFF", fg="#e74c3c")

root = Tk()
root.title("Fan ON/OFF")
root.geometry("400x450")
root.resizable(False, False)
root.configure(bg="#34495e")

canvas = Canvas(root, width=300, height=300, bg='#ecf0f1', bd=2, relief="ridge")
canvas.pack(pady=20)

status_label = Label(root, text="Fan is OFF", font=("Arial", 16, "bold"),
                      bg="#34495e", fg="white")
status_label.pack(pady=(0, 10))

button_frame = Frame(root, bg="#34495e")
button_frame.pack(pady=10)

on_button = Button(button_frame, text="Fan ON", command=start_fan,
                   font=("Arial", 14, "bold"), bg="#27ae60", fg="white",
                   activebackground="#2ecc71", activeforeground="white",
                   relief="raised", bd=3, padx=15, pady=8, cursor="hand2")
on_button.pack(side=LEFT, padx=10)

off_button = Button(button_frame, text="Fan OFF", command=stop_fan,
                    font=("Arial", 14, "bold"), bg="#c0392b", fg="white",
                    activebackground="#e74c3c", activeforeground="white",
                    relief="raised", bd=3, padx=15, pady=8, cursor="hand2")
off_button.pack(side=RIGHT, padx=10)

draw_fan()

root.mainloop()
