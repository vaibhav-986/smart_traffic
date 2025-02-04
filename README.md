# smart_traffic
import tkinter as tk
from tkinter import messagebox

users = {"user1": "password1", "user2": "password2"}

zones = {
    "Zone A": 100,
    "Zone B": 100,
    "Zone C": 100
}


def login():
    username = username_entry.get()
    password = password_entry.get()
    if username in users and users[username] == password:
        messagebox.showinfo("Login Success", f"Welcome, {username}!")
        show_base_page()
    else:
        messagebox.showerror("Login Failed", "Invalid credentials")


def show_base_page():
    login_frame.pack_forget()
    base_frame.pack()


def update_slots(zone, slots_change):
    if zone in zones:
        if 0 <= zones[zone] + slots_change <= 100:
            zones[zone] += slots_change
            zone_info.set('\n'.join([f"{zone}: {slots} slots left" for zone, slots in zones.items()]))
        else:
            messagebox.showerror("Error", f"Slots update exceeds limits for {zone}. Available slots: {zones[zone]}")
    else:
        messagebox.showerror("Error", "Invalid zone")


# Create main window
root = tk.Tk()
root.title("Smart Traffic Parking")

# Create login frame
login_frame = tk.Frame(root)
login_frame.pack()

tk.Label(login_frame, text="Username:").grid(row=0, column=0)
username_entry = tk.Entry(login_frame)
username_entry.grid(row=0, column=1)

tk.Label(login_frame, text="Password:").grid(row=1, column=0)
password_entry = tk.Entry(login_frame, show="*")
password_entry.grid(row=1, column=1)

tk.Button(login_frame, text="Login", command=login).grid(row=2, columnspan=2)

# Create base frame
base_frame = tk.Frame(root)

tk.Label(base_frame, text="Welcome to the Smart Traffic Parking!").pack()
tk.Label(base_frame, text="Manage your parking space efficiently.").pack()

tk.Label(base_frame, text="Zones and available slots:").pack()

# Display zones and slots
zone_info = tk.StringVar()
zone_info.set('\n'.join([f"{zone}: {slots} slots left" for zone, slots in zones.items()]))
zone_label = tk.Label(base_frame, textvariable=zone_info)
zone_label.pack()


# Sensor buttons for car entry and exit
def car_entry(zone):
    update_slots(zone, -1)


def car_exit(zone):
    update_slots(zone, 1)


tk.Label(base_frame, text="Simulate Car Entry/Exit:").pack()

entry_buttons = tk.Frame(base_frame)
entry_buttons.pack()

# Create columns for each zone
for i, zone in enumerate(zones):
    zone_frame = tk.Frame(entry_buttons)
    zone_frame.grid(row=0, column=i, padx=10)

    tk.Label(zone_frame, text=zone).pack()
    enter_button = tk.Button(zone_frame, text=f"Car Enter {zone}", command=lambda z=zone: car_entry(z), width=15,
                             height=2)
    enter_button.pack(pady=5)
    exit_button = tk.Button(zone_frame, text=f"Car Exit {zone}", command=lambda z=zone: car_exit(z), width=15, height=2)
    exit_button.pack(pady=5)

    # Bind Enter key to the buttons
    enter_button.bind('<Return>', lambda event, z=zone: car_entry(z))
    exit_button.bind('<Return>', lambda event, z=zone: car_exit(z))

# Start the main event loop
root.mainloop()
