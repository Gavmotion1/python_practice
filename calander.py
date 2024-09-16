import tkinter as tk
from tkinter import simpledialog, messagebox
from datetime import datetime, timedelta
import calendar

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calendar App")
        
        self.events = {}
        
        self.selected_date = datetime.now()
        
        self.create_widgets()
        self.update_calendar()

    def create_widgets(self):
        # Header Frame
        header_frame = tk.Frame(self.root)
        header_frame.pack(pady=10)

        self.prev_button = tk.Button(header_frame, text="<< Prev", command=self.prev_month)
        self.prev_button.pack(side=tk.LEFT)

        self.month_year_label = tk.Label(header_frame, text="", font=("Helvetica", 16))
        self.month_year_label.pack(side=tk.LEFT, padx=20)

        self.next_button = tk.Button(header_frame, text="Next >>", command=self.next_month)
        self.next_button.pack(side=tk.LEFT)

        # Calendar Frame
        self.calendar_frame = tk.Frame(self.root)
        self.calendar_frame.pack()

        # Event Button
        self.event_button = tk.Button(self.root, text="Add/View/Delete Event", command=self.manage_event)
        self.event_button.pack(pady=10)

    def update_calendar(self):
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()
        
        month_days = calendar.monthcalendar(self.selected_date.year, self.selected_date.month)
        month_year_text = self.selected_date.strftime("%B %Y")
        self.month_year_label.config(text=month_year_text)
        
        # Get day names and map to their indices
        day_names = list(calendar.day_name)
        day_indices = {day: idx for idx, day in enumerate(day_names)}
        
        for day in day_names:
            tk.Label(self.calendar_frame, text=day[:2]).grid(row=0, column=day_indices[day])
        
        for row, week in enumerate(month_days):
            for col, day in enumerate(week):
                if day != 0:
                    button = tk.Button(self.calendar_frame, text=day, command=lambda day=day: self.select_date(day))
                    button.grid(row=row+1, column=col, padx=5, pady=5)

    def select_date(self, day):
        self.selected_date = self.selected_date.replace(day=day)
        self.update_calendar()

    def prev_month(self):
        self.selected_date = self.selected_date.replace(day=1) - timedelta(days=1)
        self.update_calendar()

    def next_month(self):
        next_month = self.selected_date.replace(day=28) + timedelta(days=4)
        self.selected_date = next_month.replace(day=1)
        self.update_calendar()

    def manage_event(self):
        event_date = self.selected_date.strftime("%Y-%m-%d")
        action = simpledialog.askstring("Event Manager", "Enter action (add/view/delete):")
        
        if action:
            action = action.strip().lower()
        
            if action == "add":
                event = simpledialog.askstring("Add Event", f"Enter event for {event_date}:")
                if event:
                    self.events[event_date] = event
                    messagebox.showinfo("Event Added", f"Event added for {event_date}.")
                    
            elif action == "view":
                event = self.events.get(event_date, "No events")
                messagebox.showinfo("View Event", f"Event for {event_date}: {event}")
                
            elif action == "delete":
                if event_date in self.events:
                    del self.events[event_date]
                    messagebox.showinfo("Event Deleted", f"Event deleted for {event_date}.")
                else:
                    messagebox.showinfo("No Event", f"No event found for {event_date}.")
                    
            else:
                messagebox.showwarning("Invalid Action", "Action must be 'add', 'view', or 'delete'.")
        else:
            messagebox.showwarning("No Action", "Action cannot be empty.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()
