from googletrans import Translator
import tkinter as tk


def translate(message: str, language: str):
    global lbl_translated

    translater = Translator()
    translated = translater.translate(message.get(), dest=language)
    lbl_translated['text'] = translated.text


def create_frame(master: object, pad_y: int):
    return tk.Frame(master=master, pady=pad_y)


def create_button(parent: object, text: str, message: object, language: str):
    return tk.Button(
        master=parent,
        text=text,
        pady=4,
        padx=40,
        font=("Courier", 12),
        command=lambda: translate(message, language)
    )


window = tk.Tk()
window.geometry("450x450")

frm_title = create_frame(window, 10)
lbl_title = tk.Label(
    master=frm_title,
    text="Translate",
    font=("Courier", 20, "bold"),
    pady=10
)

frm_text = create_frame(window, 15)
ent_text = tk.Entry(master=frm_text, width=35, font=("Courier", 12))

frm_en_btn = create_frame(window, 5)
btn_en = create_button(frm_en_btn, "English", ent_text, "en")

frm_pt_btn = create_frame(window, 5)
btn_pt = create_button(frm_pt_btn, "Portuguese", ent_text, "pt")

frm_spn_btn = create_frame(window, 5)
btn_spn = create_button(frm_spn_btn, "Spanish", ent_text, "es")


frm_translated = create_frame(window, 5)
lbl_translated = tk.Label(
    master=frm_translated,
    font=("Courier", 14)
)

frm_title.pack()
lbl_title.pack()

frm_text.pack()
ent_text.pack()

frm_en_btn.pack()
frm_pt_btn.pack()
frm_spn_btn.pack()
btn_en.pack()
btn_pt.pack()
btn_spn.pack()

frm_translated.pack()
lbl_translated.pack()

window.mainloop()
