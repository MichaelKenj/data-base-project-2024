import tkinter as tk
from tkinter import ttk, messagebox
import requests

BASE_URL = "http://127.0.0.1:8000"

def fetch_data(endpoint):
    try:
        response = requests.get(f"{BASE_URL}/{endpoint}/")
        if response.status_code == 200:
            return response.json()
        else:
            messagebox.showerror("Ошибка", f"Ошибка {response.status_code}: {response.text}")
            return []
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось получить данные: {e}")
        return []

def update_treeview(treeview, columns, data):
    for row in treeview.get_children():
        treeview.delete(row)
    for row in data:
        treeview.insert("", "end", values=[row.get(col, "N/A") for col in columns])

def create_item(endpoint, payload):
    try:
        response = requests.post(f"{BASE_URL}/{endpoint}/", json=payload)
        if response.status_code == 201:
            messagebox.showinfo("Успех", "Запись успешно создана")
        else:
            messagebox.showerror("Ошибка", f"Ошибка {response.status_code}: {response.text}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось создать запись: {e}")

def delete_item(endpoint, item_id):
    try:
        response = requests.delete(f"{BASE_URL}/{endpoint}/{item_id}")
        if response.status_code == 204:
            messagebox.showinfo("Успех", "Запись успешно удалена")
        else:
            messagebox.showerror("Ошибка", f"Ошибка {response.status_code}: {response.text}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось удалить запись: {e}")

def update_item(endpoint, item_id, payload):
    try:
        response = requests.put(f"{BASE_URL}/{endpoint}/{item_id}", json=payload)
        if response.status_code == 200:
            messagebox.showinfo("Успех", "Запись успешно обновлена")
        else:
            messagebox.showerror("Ошибка", f"Ошибка {response.status_code}: {response.text}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось обновить запись: {e}")

def search_item(endpoint, search_key, search_value, treeview, columns):
    try:
        response = requests.get(f"{BASE_URL}/{endpoint}/search", params={search_key: search_value})
        if response.status_code == 200:
            update_treeview(treeview, columns, response.json())
        else:
            messagebox.showerror("Ошибка", f"Ошибка {response.status_code}: {response.text}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось выполнить поиск: {e}")

def create_tab(tab, endpoint, columns):
    treeview = ttk.Treeview(tab, columns=columns, show="headings")
    for col in columns:
        treeview.heading(col, text=col)
    treeview.pack(fill="both", expand=True)

    def load_data():
        data = fetch_data(endpoint)
        update_treeview(treeview, columns, data)

    def add_item():
        entry_window = tk.Toplevel()
        entry_window.title("Добавить запись")

        entries = {}
        for col in columns[1:]:
            frame = tk.Frame(entry_window)
            frame.pack(fill="x")
            label = tk.Label(frame, text=col, width=15, anchor="w")
            label.pack(side="left")
            entry = tk.Entry(frame)
            entry.pack(side="right", expand=True, fill="x")
            entries[col] = entry

        def submit():
            payload = {col: entry.get() for col, entry in entries.items()}
            create_item(endpoint, payload)
            load_data()
            entry_window.destroy()

        button_submit = tk.Button(entry_window, text="Добавить", command=submit)
        button_submit.pack()

    def remove_item():
        selected = treeview.selection()
        if not selected:
            messagebox.showwarning("Внимание", "Выберите запись для удаления")
            return

        item = treeview.item(selected[0])
        item_id = item['values'][0]
        delete_item(endpoint, item_id)
        load_data()

    def edit_item():
        selected = treeview.selection()
        if not selected:
            messagebox.showwarning("Внимание", "Выберите запись для редактирования")
            return

        item = treeview.item(selected[0])
        item_id = item['values'][0]

        entry_window = tk.Toplevel()
        entry_window.title("Изменить запись")

        entries = {}
        for col, value in zip(columns[1:], item['values'][1:]):
            frame = tk.Frame(entry_window)
            frame.pack(fill="x")
            label = tk.Label(frame, text=col, width=15, anchor="w")
            label.pack(side="left")
            entry = tk.Entry(frame)
            entry.insert(0, value)
            entry.pack(side="right", expand=True, fill="x")
            entries[col] = entry

        def submit():
            payload = {col: entry.get() for col, entry in entries.items()}
            update_item(endpoint, item_id, payload)
            load_data()
            entry_window.destroy()

        button_submit = tk.Button(entry_window, text="Сохранить", command=submit)
        button_submit.pack()

    def search():
        search_window = tk.Toplevel()
        search_window.title("Поиск записи")

        frame = tk.Frame(search_window)
        frame.pack(fill="x")

        label_key = tk.Label(frame, text="Поле", width=15, anchor="w")
        label_key.pack(side="left")
        combo_key = ttk.Combobox(frame, values=columns[1:])
        combo_key.pack(side="left", expand=True, fill="x")

        label_value = tk.Label(frame, text="Значение", width=15, anchor="w")
        label_value.pack(side="left")
        entry_value = tk.Entry(frame)
        entry_value.pack(side="left", expand=True, fill="x")

        def submit():
            search_item(endpoint, combo_key.get(), entry_value.get(), treeview, columns)
            search_window.destroy()

        button_submit = tk.Button(search_window, text="Поиск", command=submit)
        button_submit.pack()

    button_frame = tk.Frame(tab)
    button_frame.pack(fill="x", pady=5)

    ttk.Button(button_frame, text="Загрузить данные", command=load_data).pack(side="left")
    ttk.Button(button_frame, text="Добавить", command=add_item).pack(side="left")
    ttk.Button(button_frame, text="Удалить", command=remove_item).pack(side="left")
    ttk.Button(button_frame, text="Изменить", command=edit_item).pack(side="left")
    ttk.Button(button_frame, text="Поиск", command=search).pack(side="left")

    return treeview

# Создание окна
window = tk.Tk()
window.title("Управление данными")
window.geometry("800x600")

tab_control = ttk.Notebook(window)

# Вкладки
cars_tab = ttk.Frame(tab_control)
mechanics_tab = ttk.Frame(tab_control)
orders_tab = ttk.Frame(tab_control)

tab_control.add(cars_tab, text="Автомобили")
tab_control.add(mechanics_tab, text="Механики")
tab_control.add(orders_tab, text="Заказы")

tab_control.pack(expand=1, fill="both")

# Колонки
columns_cars = ("id", "brand", "license_plate", "year", "owner_name", "color")
columns_mechanics = ("id", "name", "experience", "rank")
columns_orders = ("id", "cost", "issue_date", "work_type", "planned_end_date", "car_id", "mechanic_id")

# Создание вкладок
create_tab(cars_tab, "cars", columns_cars)
create_tab(mechanics_tab, "mechanics", columns_mechanics)
create_tab(orders_tab, "orders", columns_orders)

window.mainloop()
