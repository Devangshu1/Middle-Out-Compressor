import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image, ImageTk
import os
import threading
from utils import compressor

class MiddleOutGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("MiddleOut Compressor")
        self.root.geometry("600x550")
        self.root.configure(bg="#1e1e1e")

        self.logo_img = None
        self.file_path = None

        self.setup_ui()

    def setup_ui(self):
        # Try to load logo
        try:
            logo_path = os.path.join(os.path.dirname(__file__), "logo.png")
            logo = Image.open(logo_path).resize((80, 80))
            self.logo_img = ImageTk.PhotoImage(logo)
            tk.Label(self.root, image=self.logo_img, bg="#1e1e1e").place(x=20, y=20)
        except Exception as e:
            print("Logo not loaded:", e)

        # Header
        tk.Label(self.root, text="MiddleOut Compressor", font=("Segoe UI", 20, "bold"), 
                 bg="#1e1e1e", fg="#00ff88").pack(pady=20)

        # File selection button
        self.select_button = tk.Button(self.root, text="Select File", command=self.select_file,
                                       bg="#00ff88", fg="#1e1e1e", font=("Segoe UI", 12), bd=0, width=15)
        self.select_button.pack(pady=10)

        # Compress button
        self.compress_button = tk.Button(self.root, text="Compress", command=self.start_compression,
                                         bg="#00aa66", fg="white", font=("Segoe UI", 12), bd=0, width=15)
        self.compress_button.pack(pady=10)

        # Custom progress bar style
        style = ttk.Style(self.root)
        style.theme_use('clam')
        style.configure("green.Horizontal.TProgressbar", 
                        foreground="#00ff88", 
                        background="#00ff88", 
                        troughcolor="#2a2a2a", 
                        bordercolor="#2a2a2a", 
                        lightcolor="#00ff88", 
                        darkcolor="#00ff88")

        # Progress bar
        self.progress = ttk.Progressbar(self.root, orient=tk.HORIZONTAL, length=400, mode='indeterminate',
                                        style="green.Horizontal.TProgressbar")
        self.progress.pack(pady=20)

        # Message Label
        self.message_label = tk.Label(self.root, text="", font=("Segoe UI", 11),
                                      bg="#1e1e1e", fg="#ffffff", wraplength=500, justify="center")
        self.message_label.pack(pady=10)

        # Footer
        tk.Label(self.root, text="Powered by MiddleOut Tech", font=("Segoe UI", 10),
                 bg="#1e1e1e", fg="#888").pack(side=tk.BOTTOM, pady=10)

    def select_file(self):
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            self.message_label.config(text=f"Selected: {os.path.basename(self.file_path)}", fg="#ffffff")

    def start_compression(self):
        if not self.file_path:
            self.message_label.config(text="Please select a file first.", fg="#ff4444")
            return

        self.progress.start(100)  # start with interval
        self.message_label.config(text="Compressing...", fg="#00ff88")

        thread = threading.Thread(target=self.compress_file)
        thread.start()

    def compress_file(self):
        try:
            output_path, warning = compressor.compress_file(self.file_path)
            self.root.after(0, self.on_compression_done, output_path, warning)
        except Exception as e:
            self.root.after(0, self.on_compression_error, str(e))

    def on_compression_done(self, output_path, warning):
        self.progress.stop()
        msg = f"✅ File compressed to: {os.path.basename(output_path)}"
        if warning:
            msg += f"\n⚠️ {warning}"
        self.message_label.config(text=msg, fg="#00ff88")

    def on_compression_error(self, error_msg):
        self.progress.stop()
        self.message_label.config(text=f"❌ Error: {error_msg}", fg="#ff4444")

if __name__ == '__main__':
    root = tk.Tk()
    app = MiddleOutGUI(root)
    root.mainloop()
