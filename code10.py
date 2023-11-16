import tkinter as tk
import pyautogui
import time
import threading
import webbrowser  # Required for opening the browser

class AutoTyperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto Typerr")
        
        self.text_box = tk.Text(root, height=10, width=40)
        self.text_box.pack(padx=10, pady=10)
        
        self.speed_label = tk.Label(root, text="Typing Speed (characters per second):")
        self.speed_label.pack()
        
        self.speed_entry = tk.Entry(root)
        self.speed_entry.pack(padx=10, pady=5)
        self.speed_entry.insert(tk.END, "5")  # Default speed
        
        self.start_button = tk.Button(root, text="Start Typing", command=self.start_typing)
        self.start_button.pack(pady=10)

        self.credits_label = tk.Label(root, text="made by anasy", fg="blue")  # Set text color to blue
        self.credits_label.pack(pady=(35, 10))  # Adjusting padding
        
        # Binding the label to open the GitHub profile in a browser when clicked
        self.credits_label.bind("<Button-1>", lambda event: self.open_github_profile())

    def start_typing(self):
        text_to_type = self.text_box.get("1.0", tk.END)
        speed = float(self.speed_entry.get())
        
        def type_text():
            time.sleep(3)  # Adding a delay before typing starts
            pyautogui.typewrite(text_to_type, interval=1/speed)
        
        # Create a thread to type the text
        threading.Thread(target=type_text).start()

    def open_github_profile(self):
        webbrowser.open_new_tab("https://github.com/anas-yunus/auto-typerr")

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoTyperApp(root)
    root.mainloop()
