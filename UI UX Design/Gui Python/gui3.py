
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\faqih\OneDrive\Dokumen\PlatformIO\Projects\Project Mikro\build\assets\frame3")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("412x917")
window.configure(bg = "#F1E4D9")


canvas = Canvas(
    window,
    bg = "#F1E4D9",
    height = 917,
    width = 412,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    31.0,
    52.0,
    381.0,
    100.0,
    fill="#000000",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    560.0,
    867.0,
    image=image_image_1
)

canvas.create_text(
    17.0,
    701.0,
    anchor="nw",
    text="TOTAL                      Rp. 97.500,00",
    fill="#FAF3F3",
    font=("LondrinaSolid Regular", 32 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    203.0,
    207.0,
    image=image_image_2
)

canvas.create_text(
    173.0,
    233.0,
    anchor="nw",
    text="Rp. 18.500,00",
    fill="#AE3838",
    font=("LondrinaSolid Regular", 20 * -1)
)

canvas.create_text(
    173.0,
    233.0,
    anchor="nw",
    text="Rp. 18.500,00",
    fill="#AE3838",
    font=("LondrinaSolid Regular", 20 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    208.0,
    383.0,
    image=image_image_3
)

canvas.create_text(
    325.0,
    364.0,
    anchor="nw",
    text="1",
    fill="#000000",
    font=("LondrinaSolid Regular", 24 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=343.0,
    y=363.0,
    width=30.0,
    height=30.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=287.0,
    y=362.0,
    width=30.0,
    height=30.0
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    208.0,
    560.0,
    image=image_image_4
)

canvas.create_text(
    36.0,
    114.0,
    anchor="nw",
    text="you have 3 items in your cart",
    fill="#000000",
    font=("Lohit Bengali", 20 * -1)
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    102.0,
    207.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    108.0,
    378.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    103.0,
    569.0,
    image=image_image_7
)

canvas.create_text(
    176.0,
    168.0,
    anchor="nw",
    text="MILK",
    fill="#000000",
    font=("LisuBosa Regular", 24 * -1)
)

canvas.create_text(
    181.0,
    350.0,
    anchor="nw",
    text="BREAD",
    fill="#000000",
    font=("LisuBosa Regular", 24 * -1)
)

canvas.create_text(
    181.0,
    350.0,
    anchor="nw",
    text="BREAD",
    fill="#000000",
    font=("LisuBosa Regular", 24 * -1)
)

canvas.create_text(
    181.0,
    200.0,
    anchor="nw",
    text="750 mL",
    fill="#000000",
    font=("LisuBosa Regular", 15 * -1)
)

canvas.create_text(
    181.0,
    200.0,
    anchor="nw",
    text="750 mL",
    fill="#000000",
    font=("LisuBosa Regular", 15 * -1)
)

canvas.create_text(
    173.0,
    392.0,
    anchor="nw",
    text="Rp. 14.000,00",
    fill="#AE3838",
    font=("LondrinaSolid Regular", 20 * -1)
)

canvas.create_text(
    173.0,
    392.0,
    anchor="nw",
    text="Rp. 14.000,00",
    fill="#AE3838",
    font=("LondrinaSolid Regular", 20 * -1)
)

canvas.create_text(
    181.0,
    524.0,
    anchor="nw",
    text="RICE",
    fill="#000000",
    font=("LisuBosa Regular", 24 * -1)
)

canvas.create_text(
    189.0,
    555.0,
    anchor="nw",
    text="5 Kg\n",
    fill="#000000",
    font=("LisuBosa Regular", 15 * -1)
)

canvas.create_text(
    177.0,
    581.0,
    anchor="nw",
    text="Rp. 65.000,00",
    fill="#AE3838",
    font=("LondrinaSolid Regular", 20 * -1)
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=285.0,
    y=546.0,
    width=30.0,
    height=30.0
)

canvas.create_text(
    321.0,
    546.0,
    anchor="nw",
    text="1",
    fill="#000000",
    font=("LondrinaSolid Regular", 24 * -1)
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=338.0,
    y=546.0,
    width=30.0,
    height=30.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=76.0,
    y=761.0,
    width=260.0,
    height=84.0
)
window.resizable(False, False)
window.mainloop()
