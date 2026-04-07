import tkinter as tk
from storage import Storage
from manager import WorkoutManager
from gui import WorkoutGUI

def main():
    root = tk.Tk()
    storage = Storage()
    manager = WorkoutManager(storage)
    app = WorkoutGUI(root, manager)
    root.mainloop()

if __name__ == "__main__":
    main()