import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttkbs


class NavigationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TTK Bootstrap Navigation Menu")
        self.root.geometry("800x600")

        # Apply a ttkbootstrap theme
        self.style = ttkbs.Style(theme="darkly")

        # Create container frames
        self.create_sidebar()
        self.create_content_area()

        # Initialize default view
        self.show_frame("home")

    def create_sidebar(self):
        # Sidebar frame
        self.sidebar = ttk.Frame(self.root, width=200, bootstyle="secondary")
        self.sidebar.pack(side="left", fill="y")

        # Menu buttons
        menu_buttons = [
            ("🏠 Home", "home"),
            ("📊 Dashboard", "dashboard"),
            ("⚙️ Settings", "settings"),
            ("📧 Contact", "contact")
        ]

        for text, command in menu_buttons:
            btn = ttkbs.Button(
                self.sidebar,
                text=text,
                command=lambda cmd=command: self.show_frame(cmd),
                bootstyle="light-outline",
                width=20
            )
            btn.pack(pady=5, padx=10, ipady=5)

    def create_content_area(self):
        # Content frame container
        self.content_frame = ttk.Frame(self.root)
        self.content_frame.pack(side="right", fill="both", expand=True)

        # Create all frames
        self.frames = {}
        for page in ["home", "dashboard", "settings", "contact"]:
            frame = ttkbs.Frame(self.content_frame)
            self.frames[page] = frame
            self.create_page_content(page, frame)

    def create_page_content(self, page_name, frame):
        # Add content to each page
        label = ttkbs.Label(
            frame,
            text=f"{page_name.capitalize()} Page",
            font=("Helvetica", 24),
            bootstyle="inverse-primary"
        )
        label.pack(pady=50)

        # Add example content
        if page_name == "dashboard":
            ttkbs.Label(frame, text="Sales Data").pack()
            ttkbs.Progressbar(frame, bootstyle="success-striped", length=200).pack(pady=10)

    def show_frame(self, page_name):
        # Hide all frames
        for frame in self.frames.values():
            frame.pack_forget()

        # Show selected frame
        self.frames[page_name].pack(fill="both", expand=True)


if __name__ == "__main__":
    root = ttkbs.Window()
    app = NavigationApp(root)
    root.mainloop()