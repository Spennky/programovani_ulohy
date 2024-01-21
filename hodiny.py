import tkinter as tk
import time


class CasovyGraf(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Časový Graf")
        self.geometry("1200x200")

        self.canvas_sec = tk.Canvas(self, width=1200, height=25)
        self.canvas_sec.pack()

        self.canvas_min = tk.Canvas(self, width=1200, height=25)
        self.canvas_min.pack()

        self.canvas_hour = tk.Canvas(self, width=1200, height=25)
        self.canvas_hour.pack()

        self.canvas_time = tk.Canvas(self, width=1200, height=25)
        self.canvas_time.pack()

        self.label = tk.Label(self, font=("Helvetica", 16), pady=10)
        self.label.pack()

        self.update_seconds()
        self.update_minutes()
        self.update_hours()
        self.update_current_time()

    def update_seconds(self):
        current_second = int(time.strftime("%S"))
        self.canvas_sec.delete("all")

        for i in range(60):
            x1 = i * 20
            x2 = (i + 1) * 20
            y1 = 0
            y2 = 25

            color = "green" if i <= current_second % 60 else "white"

            self.canvas_sec.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")
            self.canvas_sec.create_text(x1 + 5, y2 - 10, text=str(i), anchor=tk.SW)

        self.after(1000, self.update_seconds)

    def update_minutes(self):
        current_minute = int(time.strftime("%M"))
        self.canvas_min.delete("all")

        for i in range(60):
            x1 = i * 20
            x2 = (i + 1) * 20
            y1 = 0
            y2 = 25

            color = "#add8e6" if i <= current_minute % 60 else "white"

            self.canvas_min.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")
            self.canvas_min.create_text(x1 + 5, y2 - 10, text=str(i), anchor=tk.SW)

        self.after(1000, self.update_minutes)

    def update_hours(self):
        current_hour = int(time.strftime("%H"))*5
        hour_part = int(time.strftime("%M")) // 12

        self.canvas_hour.delete("all")

        for i in range(60):
            x1 = i * 20
            x2 = (i + 1) * 20
            y1 = 0
            y2 = 25

            color = "#b55c5c" if i <= (current_hour + hour_part) % 60 else "white"

            self.canvas_hour.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")
            if i % 5 == 0:
                self.canvas_hour.create_text(x1 + 5, y2 - 10, text=str(i // 5), anchor=tk.SW)

        self.after(1000, self.update_hours)

    def update_current_time(self):
        current_time = time.strftime("Aktuální čas %H:%M:%S")
        self.canvas_time.delete("all")
        self.canvas_time.create_text(600, 15, text=current_time, anchor=tk.CENTER, font=("Helvetica", 16))

        self.after(1000, self.update_current_time)

if __name__ == "__main__":
    app = CasovyGraf()
    app.mainloop()
