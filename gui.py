import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

from chatbot_py import chat


class HealthCareChatInterface(tk.Frame):
    """Original Tkinter interface for the healthcare chatbot."""

    COLORS = {
        "window": "#0b1220",
        "panel": "#111c2e",
        "panel_light": "#17263b",
        "input": "#1b2d45",
        "text": "#edf4ff",
        "muted": "#9db0c9",
        "accent": "#36d1b4",
        "accent_dark": "#1b9b89",
        "border": "#2a3c54",
    }

    def __init__(self, master=None):
        super().__init__(master, bg=self.COLORS["window"])
        self.master = master
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.font_family = "Segoe UI"
        self._build_styles()
        self._build_menu()
        self._build_header()
        self._build_chat_area()
        self._build_input_area()
        self._build_status_bar()

        self.master.bind("<Return>", self.send_message)
        self.entry_field.focus_set()
        self._add_bot_message(
            "Hi! I’m HealthCare Assistant. Tell me what you’re experiencing, "
            "and I’ll share general information to help you decide what to do next."
        )

    def _build_styles(self):
        style = ttk.Style(self.master)
        style.theme_use("clam")
        style.configure(
            "Accent.TButton",
            background=self.COLORS["accent"],
            foreground="#07151a",
            borderwidth=0,
            padding=(16, 9),
            font=(self.font_family, 10, "bold"),
        )
        style.map(
            "Accent.TButton",
            background=[("active", "#5ae2ca"), ("pressed", self.COLORS["accent_dark"])],
        )
        style.configure(
            "Secondary.TButton",
            background=self.COLORS["panel_light"],
            foreground=self.COLORS["muted"],
            borderwidth=0,
            padding=(12, 8),
            font=(self.font_family, 9),
        )

    def _build_menu(self):
        menu = tk.Menu(
            self.master,
            tearoff=False,
            bg=self.COLORS["panel"],
            fg=self.COLORS["text"],
            activebackground=self.COLORS["accent_dark"],
            activeforeground=self.COLORS["text"],
        )
        session_menu = tk.Menu(menu, tearoff=False, bg=self.COLORS["panel"], fg=self.COLORS["text"])
        session_menu.add_command(label="New conversation", command=self.clear_chat)
        session_menu.add_separator()
        session_menu.add_command(label="Exit", command=self.master.destroy)
        menu.add_cascade(label="Conversation", menu=session_menu)

        help_menu = tk.Menu(menu, tearoff=False, bg=self.COLORS["panel"], fg=self.COLORS["text"])
        help_menu.add_command(label="About", command=self.show_about)
        menu.add_cascade(label="Help", menu=help_menu)
        self.master.config(menu=menu)

    def _build_header(self):
        header = tk.Frame(self, bg=self.COLORS["panel"], padx=24, pady=18)
        header.grid(row=0, column=0, sticky="ew")

        icon = tk.Label(
            header,
            text="✚",
            bg=self.COLORS["accent"],
            fg="#07151a",
            font=(self.font_family, 19, "bold"),
            width=2,
            pady=3,
        )
        icon.pack(side=tk.LEFT, padx=(0, 12))

        title_frame = tk.Frame(header, bg=self.COLORS["panel"])
        title_frame.pack(side=tk.LEFT)
        tk.Label(
            title_frame,
            text="HealthCare Assistant",
            bg=self.COLORS["panel"],
            fg=self.COLORS["text"],
            font=(self.font_family, 16, "bold"),
        ).pack(anchor="w")
        tk.Label(
            title_frame,
            text="General health information, whenever you need it",
            bg=self.COLORS["panel"],
            fg=self.COLORS["muted"],
            font=(self.font_family, 9),
        ).pack(anchor="w", pady=(2, 0))

        tk.Label(
            header,
            text="● Online",
            bg=self.COLORS["panel"],
            fg=self.COLORS["accent"],
            font=(self.font_family, 9, "bold"),
        ).pack(side=tk.RIGHT, anchor="n", pady=5)

    def _build_chat_area(self):
        area = tk.Frame(self, bg=self.COLORS["window"], padx=18)
        area.grid(row=1, column=0, sticky="nsew", pady=(16, 8))

        self.text_box = tk.Text(
            area,
            state=tk.DISABLED,
            wrap=tk.WORD,
            relief=tk.FLAT,
            borderwidth=0,
            padx=18,
            pady=16,
            spacing1=4,
            spacing3=12,
            bg=self.COLORS["window"],
            fg=self.COLORS["text"],
            insertbackground=self.COLORS["text"],
            font=(self.font_family, 10),
        )
        self.text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(
            area,
            command=self.text_box.yview,
            bg=self.COLORS["panel_light"],
            troughcolor=self.COLORS["window"],
            activebackground=self.COLORS["accent"],
            relief=tk.FLAT,
            width=10,
        )
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_box.configure(yscrollcommand=scrollbar.set)

        self.text_box.tag_configure(
            "user_label", foreground=self.COLORS["accent"], font=(self.font_family, 9, "bold")
        )
        self.text_box.tag_configure(
            "bot_label", foreground="#8fc8ff", font=(self.font_family, 9, "bold")
        )
        self.text_box.tag_configure("message", foreground=self.COLORS["text"], lmargin1=12, lmargin2=12)
        self.text_box.tag_configure("time", foreground=self.COLORS["muted"], font=(self.font_family, 8))

    def _build_input_area(self):
        input_panel = tk.Frame(self, bg=self.COLORS["panel"], padx=18, pady=14)
        input_panel.grid(row=2, column=0, sticky="ew")

        self.entry_field = tk.Entry(
            input_panel,
            bg=self.COLORS["input"],
            fg=self.COLORS["muted"],
            insertbackground=self.COLORS["text"],
            relief=tk.FLAT,
            borderwidth=0,
            font=(self.font_family, 10),
        )
        self.entry_field.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=10, padx=(0, 10))
        self.entry_field.insert(0, "Type your symptoms or question...")
        self.entry_field.bind("<FocusIn>", self._clear_placeholder)
        self.entry_field.bind("<FocusOut>", self._restore_placeholder)

        ttk.Button(input_panel, text="Send  ➤", style="Accent.TButton", command=self.send_message).pack(
            side=tk.RIGHT
        )

    def _build_status_bar(self):
        footer = tk.Frame(self, bg=self.COLORS["window"], padx=20)
        footer.grid(row=3, column=0, sticky="ew", pady=(4, 10))
        self.status_label = tk.Label(
            footer,
            text="Ready to help",
            bg=self.COLORS["window"],
            fg=self.COLORS["muted"],
            font=(self.font_family, 8),
        )
        self.status_label.pack(side=tk.LEFT)
        tk.Label(
            footer,
            text="For information only • Not a substitute for a doctor",
            bg=self.COLORS["window"],
            fg=self.COLORS["muted"],
            font=(self.font_family, 8),
        ).pack(side=tk.RIGHT)

    def _clear_placeholder(self, _event=None):
        if self.entry_field.get() == "Type your symptoms or question...":
            self.entry_field.delete(0, tk.END)
            self.entry_field.config(fg=self.COLORS["text"])

    def _restore_placeholder(self, _event=None):
        if not self.entry_field.get().strip():
            self.entry_field.insert(0, "Type your symptoms or question...")
            self.entry_field.config(fg=self.COLORS["muted"])

    def _add_message(self, speaker, message, label_tag):
        now = datetime.now().strftime("%I:%M %p")
        self.text_box.config(state=tk.NORMAL)
        self.text_box.insert(tk.END, f"{speaker}  ", label_tag)
        self.text_box.insert(tk.END, f"{now}\n", "time")
        self.text_box.insert(tk.END, f"{message}\n\n", "message")
        self.text_box.config(state=tk.DISABLED)
        self.text_box.see(tk.END)

    def _add_user_message(self, message):
        self._add_message("You", message, "user_label")

    def _add_bot_message(self, message):
        self._add_message("Assistant", message, "bot_label")

    def send_message(self, _event=None):
        self._clear_placeholder()
        user_input = self.entry_field.get().strip()
        if not user_input:
            self.status_label.config(text="Please enter a message")
            return "break"

        self._add_user_message(user_input)
        self.status_label.config(text="Thinking...")
        self.master.update_idletasks()

        try:
            response = chat(user_input) or "I’m not sure how to answer that."
        except Exception:
            response = "I’m unable to process that right now. Please try again or contact a healthcare professional."

        self._add_bot_message(response)
        self.status_label.config(text=f"Last message sent at {datetime.now().strftime('%I:%M %p')}")
        self.entry_field.delete(0, tk.END)
        self._restore_placeholder()
        return "break"

    def clear_chat(self):
        self.text_box.config(state=tk.NORMAL)
        self.text_box.delete("1.0", tk.END)
        self.text_box.config(state=tk.DISABLED)
        self._add_bot_message("New conversation started. How can I help you today?")
        self.status_label.config(text="Ready to help")
        self.entry_field.focus_set()

    def show_about(self):
        messagebox.showinfo(
            "About HealthCare Assistant",
            "HealthCare Assistant provides general, educational information.\n\n"
            "It cannot diagnose conditions or replace a qualified healthcare professional.\n"
            "For emergencies, contact your local emergency service immediately.",
        )


def main():
    root = tk.Tk()
    root.title("HealthCare Assistant")
    root.geometry("720x680")
    root.minsize(560, 500)
    root.configure(bg=HealthCareChatInterface.COLORS["window"])
    HealthCareChatInterface(root).pack(fill=tk.BOTH, expand=True)
    root.mainloop()


if __name__ == "__main__":
    main()
