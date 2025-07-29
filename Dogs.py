"""Собачки"""

from tkinter import *
from tkinter import messagebox
import requests
from PIL import Image, ImageTK
from io import BytesIO


def show_image():
    """Выводит изображение"""
    image_url = get_dog_image()
    if image_url:
        try:
            response = requests.get(image_url, stream=True)
            response.raise_for_status()
            img.data = BytesIO(response.content)
            img = Image.open(img_data)
            img.thumbnail((300, 300))
            label.config(image=img)
            label.image = img
        except Exception as e:
            messagebox.showerror('Ошибка', f'Возникла ошибка {e}')


window = Tk()
window.title('Картинки с собачками')
window.geometry('360x420')

label = Label()
label.pack(pady=10)

button = Button(text='Загрузить изображение', command=show_image)
button.pack(pady=10)

window.mainloop()
