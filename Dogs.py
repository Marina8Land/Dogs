"""Собачки"""

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import requests
from PIL import Image, ImageTk
from io import BytesIO


def get_dog_image():
    """Выводит ссылку на изображение"""
    try:
        response = requests.get('https://dog.ceo/api/breeds/image/random')
        response.raise_for_status()
        data = response.json()
        print(data)
        print(data['message'])
        print(data['status'])
        return data['message']
    except Exception as e:
        messagebox.showerror('Ошибка', f'Возникла ошибка при запросе API {e}')
        return None


def show_image():
    """Выводит изображение"""
    image_url = get_dog_image()
    if image_url:
        try:
            response = requests.get(image_url, stream=True)
            response.raise_for_status()
            img_data = BytesIO(response.content)
            img = Image.open(img_data)
            img_size = (int(width_spinbox.get()), int(height_spinbox.get()))
            img.thumbnail(img_size)
            img = ImageTk.PhotoImage(img)
            # new_window = Toplevel(window)
            # new_window.title('Случайное изображение')
            tab = ttk.Frame(notebook)
            notebook.add(tab, text=f'Изображение № {notebook.index('end')+1} ')
            lb = ttk.Label(tab, image=img)
            lb.pack(pady=10, padx=10)
            lb.image = img
        except Exception as e:
            messagebox.showerror('Ошибка', f'Возникла ошибка при загрузке изображения {e}')
    progres.stop()


def prog():
    progres['value'] = 0
    progres.start(30)
    window.after(3000, show_image)


window = Tk()
window.title('Картинки с собачками')
window.geometry('360x420')

label = ttk.Label()
label.pack(pady=10)

button = ttk.Button(text='Загрузить изображение', command=prog)
button.pack(pady=10)

progres = ttk.Progressbar(mode='determinate', length=300)
progres.pack(pady=10)

width_lable = ttk.Label(text='Ширина:')
width_lable.pack(side='left', padx=(10, 0))
width_spinbox = ttk.Spinbox(from_=200, to=500, increment=50, width=5)
width_spinbox.pack(side='left', padx=(0, 10))
width_spinbox.set(300)

height_label = ttk.Label(text='Высота:')
height_label.pack(side='left', padx=(10, 0))
height_spinbox = ttk.Spinbox(from_=200, to=500, increment=50, width=5)
height_spinbox.pack(side='left', padx=(0, 10))
height_spinbox.set(300)

top_level_window = Toplevel(window)
top_level_window.title('Изображения собачек')

notebook = ttk.Notebook(top_level_window)
notebook.pack(expand=True, fill='both', padx=10, pady=10)

window.mainloop()
