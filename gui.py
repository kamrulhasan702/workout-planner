import tkinter as tk
from tkinter import ttk, messagebox
from workout import Workout


class WorkoutGUI:
    def __init__(self, root, manager):
        self.root = root
        self.manager = manager

        self.root.title("Workout Planner GUI")
        self.root.geometry("1250x700")
        self.root.configure(bg="#e3f2fd")

        self.main_container = tk.Frame(self.root, bg="#e3f2fd")
        self.main_container.pack(fill="both", expand=True)

        self.sidebar = tk.Frame(self.main_container, bg="#0d47a1", width=220)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        self.content = tk.Frame(self.main_container, bg="#e3f2fd")
        self.content.pack(side="right", fill="both", expand=True)

        self.create_sidebar()
        self.create_pages()
        self.show_page("dashboard")

    def create_sidebar(self):
        tk.Label(
            self.sidebar,
            text="Workout Planner",
            font=("Arial", 18, "bold"),
            bg="#0d47a1",
            fg="white"
        ).pack(pady=20)

        tk.Button(
            self.sidebar, text="Dashboard", width=18, height=2,
            bg="#1565c0", fg="white", command=lambda: self.show_page("dashboard")
        ).pack(pady=10)

        tk.Button(
            self.sidebar, text="Add Workout", width=18, height=2,
            bg="#1565c0", fg="white", command=lambda: self.show_page("add")
        ).pack(pady=10)

        tk.Button(
            self.sidebar, text="View Workouts", width=18, height=2,
            bg="#1565c0", fg="white", command=lambda: self.show_page("view")
        ).pack(pady=10)

        tk.Button(
            self.sidebar, text="Report", width=18, height=2,
            bg="#1565c0", fg="white", command=lambda: self.show_page("report")
        ).pack(pady=10)

    def create_pages(self):
        self.pages = {}

        self.pages["dashboard"] = tk.Frame(self.content, bg="#e3f2fd")
        self.create_dashboard_page()

        self.pages["add"] = tk.Frame(self.content, bg="#e3f2fd")
        self.create_add_page()

        self.pages["view"] = tk.Frame(self.content, bg="#e3f2fd")
        self.create_view_page()

        self.pages["report"] = tk.Frame(self.content, bg="#e3f2fd")
        self.create_report_page()

    def show_page(self, page_name):
        for page in self.pages.values():
            page.pack_forget()

        self.pages[page_name].pack(fill="both", expand=True)

        if page_name == "dashboard":
            self.refresh_dashboard()
        elif page_name == "view":
            self.load_table_data()
        elif page_name == "report":
            self.refresh_report()

    def create_dashboard_page(self):
        page = self.pages["dashboard"]

        tk.Label(
            page,
            text="Dashboard",
            font=("Arial", 24, "bold"),
            bg="#e3f2fd",
            fg="#0d47a1"
        ).pack(pady=20)

        self.dashboard_total = tk.Label(page, text="", font=("Arial", 16), bg="white", width=25, height=3, relief="ridge")
        self.dashboard_total.pack(pady=10)

        self.dashboard_completed = tk.Label(page, text="", font=("Arial", 16), bg="white", width=25, height=3, relief="ridge")
        self.dashboard_completed.pack(pady=10)

        self.dashboard_pending = tk.Label(page, text="", font=("Arial", 16), bg="white", width=25, height=3, relief="ridge")
        self.dashboard_pending.pack(pady=10)

        self.dashboard_duration = tk.Label(page, text="", font=("Arial", 16), bg="white", width=25, height=3, relief="ridge")
        self.dashboard_duration.pack(pady=10)

    def refresh_dashboard(self):
        report = self.manager.generate_report()
        self.dashboard_total.config(text=f"Total Workouts\n{report['total_workouts']}")
        self.dashboard_completed.config(text=f"Completed Workouts\n{report['completed']}")
        self.dashboard_pending.config(text=f"Pending Workouts\n{report['pending']}")
        self.dashboard_duration.config(text=f"Total Duration\n{report['total_duration']} min")

    def create_add_page(self):
        page = self.pages["add"]

        tk.Label(
            page,
            text="Add / Update Workout",
            font=("Arial", 24, "bold"),
            bg="#e3f2fd",
            fg="#0d47a1"
        ).pack(pady=20)

        form_frame = tk.Frame(page, bg="#e3f2fd")
        form_frame.pack(pady=20)

        tk.Label(form_frame, text="ID", bg="#e3f2fd", font=("Arial", 11, "bold")).grid(row=0, column=0, padx=10, pady=10)
        self.id_entry = tk.Entry(form_frame, width=18)
        self.id_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(form_frame, text="Name", bg="#e3f2fd", font=("Arial", 11, "bold")).grid(row=0, column=2, padx=10, pady=10)
        self.name_entry = tk.Entry(form_frame, width=18)
        self.name_entry.grid(row=0, column=3, padx=10, pady=10)

        tk.Label(form_frame, text="Category", bg="#e3f2fd", font=("Arial", 11, "bold")).grid(row=1, column=0, padx=10, pady=10)
        self.category_var = tk.StringVar()
        self.category_dropdown = ttk.Combobox(
            form_frame,
            textvariable=self.category_var,
            values=["Cardio", "Strength", "Yoga"],
            state="readonly",
            width=15
        )
        self.category_dropdown.grid(row=1, column=1, padx=10, pady=10)
        self.category_dropdown.current(0)

        tk.Label(form_frame, text="Duration", bg="#e3f2fd", font=("Arial", 11, "bold")).grid(row=1, column=2, padx=10, pady=10)
        self.duration_entry = tk.Entry(form_frame, width=18)
        self.duration_entry.grid(row=1, column=3, padx=10, pady=10)

        tk.Label(form_frame, text="Difficulty", bg="#e3f2fd", font=("Arial", 11, "bold")).grid(row=2, column=0, padx=10, pady=10)
        self.difficulty_var = tk.StringVar()
        self.difficulty_dropdown = ttk.Combobox(
            form_frame,
            textvariable=self.difficulty_var,
            values=["Easy", "Medium", "Hard"],
            state="readonly",
            width=15
        )
        self.difficulty_dropdown.grid(row=2, column=1, padx=10, pady=10)
        self.difficulty_dropdown.current(0)

        tk.Label(form_frame, text="Calories", bg="#e3f2fd", font=("Arial", 11, "bold")).grid(row=2, column=2, padx=10, pady=10)
        self.calories_entry = tk.Entry(form_frame, width=18)
        self.calories_entry.grid(row=2, column=3, padx=10, pady=10)

        tk.Label(form_frame, text="Day", bg="#e3f2fd", font=("Arial", 11, "bold")).grid(row=3, column=0, padx=10, pady=10)
        self.day_entry = tk.Entry(form_frame, width=18)
        self.day_entry.grid(row=3, column=1, padx=10, pady=10)

        button_frame = tk.Frame(page, bg="#e3f2fd")
        button_frame.pack(pady=20)

        tk.Button(button_frame, text="Add", width=14, bg="#4caf50", fg="white", command=self.add_workout).grid(row=0, column=0, padx=10)
        tk.Button(button_frame, text="Update", width=14, bg="#ff9800", fg="white", command=self.update_workout).grid(row=0, column=1, padx=10)
        tk.Button(button_frame, text="Delete", width=14, bg="#f44336", fg="white", command=self.delete_workout).grid(row=0, column=2, padx=10)
        tk.Button(button_frame, text="Mark Completed", width=16, bg="#009688", fg="white", command=self.mark_completed).grid(row=0, column=3, padx=10)
        tk.Button(button_frame, text="Clear", width=14, bg="#795548", fg="white", command=self.clear_fields).grid(row=0, column=4, padx=10)

    def create_view_page(self):
        page = self.pages["view"]

        tk.Label(
            page,
            text="View Workouts",
            font=("Arial", 24, "bold"),
            bg="#e3f2fd",
            fg="#0d47a1"
        ).pack(pady=20)

        search_frame = tk.Frame(page, bg="#e3f2fd")
        search_frame.pack(pady=10)

        tk.Label(search_frame, text="Search", bg="#e3f2fd", font=("Arial", 11, "bold")).pack(side="left", padx=5)
        self.search_entry = tk.Entry(search_frame, width=30)
        self.search_entry.pack(side="left", padx=5)

        tk.Button(search_frame, text="Search", width=12, bg="#1565c0", fg="white", command=self.search_workout).pack(side="left", padx=5)
        tk.Button(search_frame, text="Show All", width=12, bg="#607d8b", fg="white", command=self.load_table_data).pack(side="left", padx=5)

        table_frame = tk.Frame(page, bg="#e3f2fd")
        table_frame.pack(padx=10, pady=20, fill="both", expand=True)

        columns = ("ID", "Name", "Category", "Duration", "Difficulty", "Calories", "Day", "Completed")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings")

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=130, anchor="center")

        self.tree.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.bind("<<TreeviewSelect>>", self.on_row_select)

    def create_report_page(self):
        page = self.pages["report"]

        tk.Label(
            page,
            text="Workout Report",
            font=("Arial", 24, "bold"),
            bg="#e3f2fd",
            fg="#0d47a1"
        ).pack(pady=20)

        self.report_box = tk.Label(
            page,
            text="",
            font=("Arial", 15),
            bg="white",
            fg="black",
            width=40,
            height=12,
            relief="ridge",
            justify="left",
            anchor="nw",
            padx=20,
            pady=20
        )
        self.report_box.pack(pady=20)

    def refresh_report(self):
        report = self.manager.generate_report()
        report_text = (
            f"Total Workouts: {report['total_workouts']}\n\n"
            f"Completed: {report['completed']}\n\n"
            f"Pending: {report['pending']}\n\n"
            f"Total Duration: {report['total_duration']} min\n\n"
            f"Average Duration: {report['average_duration']:.2f} min\n\n"
            f"Total Calories: {report['total_calories']}\n\n"
            f"Top Category: {report['top_category']}"
        )
        self.report_box.config(text=report_text)

    def get_form_data(self):
        try:
            workout_id = int(self.id_entry.get().strip())
            name = self.name_entry.get().strip()
            category = self.category_var.get()
            duration = int(self.duration_entry.get().strip())
            difficulty = self.difficulty_var.get()
            calories = int(self.calories_entry.get().strip())
            day = self.day_entry.get().strip()

            if not name or not day:
                raise ValueError

            if duration < 0 or calories < 0:
                raise ValueError

            return workout_id, name, category, duration, difficulty, calories, day
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid data in all fields.")
            return None

    def add_workout(self):
        data = self.get_form_data()
        if not data:
            return

        workout_id, name, category, duration, difficulty, calories, day = data

        if self.manager.find_workout_by_id(workout_id):
            messagebox.showerror("Duplicate ID", "Workout ID already exists.")
            return

        workout = Workout(workout_id, name, category, duration, difficulty, calories, day)
        self.manager.add_workout(workout)
        self.load_table_data()
        self.refresh_dashboard()
        self.refresh_report()
        self.clear_fields()
        messagebox.showinfo("Success", "Workout added successfully.")

    def update_workout(self):
        data = self.get_form_data()
        if not data:
            return

        workout_id, name, category, duration, difficulty, calories, day = data

        if self.manager.update_workout(workout_id, name, category, duration, difficulty, calories, day):
            self.load_table_data()
            self.refresh_dashboard()
            self.refresh_report()
            self.clear_fields()
            messagebox.showinfo("Success", "Workout updated successfully.")
        else:
            messagebox.showerror("Error", "Workout not found.")

    def delete_workout(self):
        try:
            workout_id = int(self.id_entry.get().strip())
        except ValueError:
            messagebox.showerror("Error", "Select or enter a valid workout ID first.")
            return

        if self.manager.delete_workout(workout_id):
            self.load_table_data()
            self.refresh_dashboard()
            self.refresh_report()
            self.clear_fields()
            messagebox.showinfo("Deleted", "Workout deleted successfully.")
        else:
            messagebox.showerror("Error", "Workout not found.")

    def mark_completed(self):
        try:
            workout_id = int(self.id_entry.get().strip())
        except ValueError:
            messagebox.showerror("Error", "Select or enter a valid workout ID first.")
            return

        if self.manager.mark_completed(workout_id):
            self.load_table_data()
            self.refresh_dashboard()
            self.refresh_report()
            self.clear_fields()
            messagebox.showinfo("Success", "Workout marked as completed.")
        else:
            messagebox.showerror("Error", "Workout not found.")

    def search_workout(self):
        keyword = self.search_entry.get().strip()
        if not keyword:
            messagebox.showerror("Error", "Enter a keyword to search.")
            return

        results = self.manager.search_workouts(keyword)
        self.load_tree_with_data(results)

        if not results:
            messagebox.showinfo("No Results", "No matching workout found.")

    def load_table_data(self):
        workouts = self.manager.get_all_workouts()
        self.load_tree_with_data(workouts)

    def load_tree_with_data(self, workouts):
        for row in self.tree.get_children():
            self.tree.delete(row)

        for workout in workouts:
            self.tree.insert(
                "",
                "end",
                values=(
                    workout.workout_id,
                    workout.name,
                    workout.category,
                    f"{workout.duration} min",
                    workout.difficulty,
                    f"{workout.calories} kcal",
                    workout.day,
                    "Yes" if workout.completed else "No"
                )
            )

    def on_row_select(self, event):
        selected = self.tree.focus()
        if not selected:
            return

        values = self.tree.item(selected, "values")
        if not values:
            return

        self.show_page("add")
        self.clear_fields()

        self.id_entry.insert(0, values[0])
        self.name_entry.insert(0, values[1])
        self.category_var.set(values[2])

        duration_value = str(values[3]).replace(" min", "")
        calories_value = str(values[5]).replace(" kcal", "")

        self.duration_entry.insert(0, duration_value)
        self.difficulty_var.set(values[4])
        self.calories_entry.insert(0, calories_value)
        self.day_entry.insert(0, values[6])

    def clear_fields(self):
        self.id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.duration_entry.delete(0, tk.END)
        self.calories_entry.delete(0, tk.END)
        self.day_entry.delete(0, tk.END)
        self.category_dropdown.current(0)
        self.difficulty_dropdown.current(0)