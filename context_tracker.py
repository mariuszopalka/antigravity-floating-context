import os
import glob
import time
import tkinter as tk
import json

# Automatically find the user's home directory to protect privacy and work on any PC
BRAIN_DIR = os.path.join(os.path.expanduser("~"), ".gemini", "antigravity-ide", "brain")
# Standard limit assumption for large models
LIMIT = 1_000_000 

def get_latest_transcript():
    pattern = os.path.join(BRAIN_DIR, "*", ".system_generated", "logs", "transcript_full.jsonl")
    files = glob.glob(pattern)
    if not files:
        return None
    latest_file = max(files, key=os.path.getmtime)
    return latest_file

def estimate_tokens(filepath):
    try:
        total_chars = 0
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                if not line.strip(): continue
                data = json.loads(line)
                content = data.get('content', '')
                if content:
                    total_chars += len(content)
        return total_chars // 4
    except Exception:
        return 0

def update_label(label, root):
    latest_file = get_latest_transcript()
    if not latest_file:
        label.config(text="Context: Waiting for data...")
    else:
        tokens = estimate_tokens(latest_file)
        percentage = (tokens / LIMIT) * 100
        label.config(text=f"Context: {tokens/1000:.1f}k / 1M ({percentage:.1f}%)")
    
    # Force the window to stay on top, even above the Windows taskbar
    root.lift()
    root.attributes("-topmost", True)
    
    label.after(3000, update_label, label, root)

def create_ui():
    root = tk.Tk()
    root.overrideredirect(True) 
    root.attributes("-topmost", True) 
    root.attributes("-alpha", 0.9) 
    root.configure(bg="#2d2d2d") 
    
    label = tk.Label(root, text="Context: Loading...", fg="#00ffcc", bg="#2d2d2d", font=("Consolas", 10, "bold"), padx=10, pady=5)
    label.pack()
    
    def start_move(event):
        root.x = event.x
        root.y = event.y
    def stop_move(event):
        root.x = None
        root.y = None
    def do_move(event):
        deltax = event.x - root.x
        deltay = event.y - root.y
        x = root.winfo_x() + deltax
        y = root.winfo_y() + deltay
        root.geometry(f"+{x}+{y}")
        
    label.bind("<ButtonPress-1>", start_move)
    label.bind("<ButtonRelease-1>", stop_move)
    label.bind("<B1-Motion>", do_move)
    
    label.bind("<Double-Button-1>", lambda e: root.destroy())
    
    root.geometry("+50+50")
    
    update_label(label, root)
    root.mainloop()

if __name__ == "__main__":
    create_ui()
