import tkinter as tk
from tkinter import messagebox
import threading
import pyautogui
import time
import random
import webbrowser
from tkinter import font as tkfont

# Global variables
stop_flag = False
pause_flag = False
start_time = 0
timer_running = False
typing_active = False

# Default timing parameters (in seconds)
DEFAULT_PARAMS = {
    'char_delay_min': 0.05,
    'char_delay_max': 0.15,
    'punctuation_extra_min': 0.2,
    'punctuation_extra_max': 0.5,
    'line_delay_min': 2.0,
    'line_delay_max': 6.0,
    'long_pause_every': 8,
    'long_pause_min': 8.0,
    'long_pause_max': 15.0,
    'error_rate': 0,  # 0% chance of error by default
    'error_correction_min': 0.3,
    'error_correction_max': 0.6,
    'initial_delay': 5.0,
    'auto_correct': True
}

def open_portfolio():
    webbrowser.open_new("https://engrshuvodas.github.io/SHUVO-_portfolio/")

def show_about():
    messagebox.showinfo(
        "About Shuky",
        "Shuky - Advanced Human-Like Typing Bot\n"
        "Version: 2.4\n\n"
        "New Features:\n"
        "- Natural occasional mistakes (1% chance)\n"
        "- Auto-correction system\n"
        "- Configurable error rates\n\n"
        "© 2025 Engr Shuvo Das - All Rights Reserved"
    )

def reset_to_defaults():
    for widget in timing_controls.frame.winfo_children():
        if isinstance(widget, tk.Entry):
            widget.delete(0, tk.END)
    
    # Set random non-rounded values
    timing_controls.char_min.insert(0, round(random.uniform(0.03, 0.08), 3))
    timing_controls.char_max.insert(0, round(random.uniform(0.12, 0.18), 3))
    timing_controls.punct_min.insert(0, round(random.uniform(0.15, 0.25), 3))
    timing_controls.punct_max.insert(0, round(random.uniform(0.4, 0.6), 3))
    timing_controls.line_min.insert(0, round(random.uniform(1.8, 2.5), 3))
    timing_controls.line_max.insert(0, round(random.uniform(5.5, 7.0), 3))
    timing_controls.long_min.insert(0, round(random.uniform(7.5, 9.0), 3))
    timing_controls.long_max.insert(0, round(random.uniform(14.0, 16.0), 3))
    timing_controls.long_freq.insert(0, random.randint(7, 10))
    timing_controls.error_min.insert(0, round(random.uniform(0.25, 0.35), 3))
    timing_controls.error_max.insert(0, round(random.uniform(0.55, 0.65), 3))
    timing_controls.initial_delay.insert(0, round(random.uniform(4.5, 5.5), 3))
    timing_controls.error_rate.insert(0, 0)  # Default 0% error rate
    timing_controls.auto_correct.set(True)

def get_timing_params(controls):
    """Get current timing parameters from UI controls"""
    return {
        'char_delay': (float(controls.char_min.get()), float(controls.char_max.get())),
        'punctuation_extra': (float(controls.punct_min.get()), float(controls.punct_max.get())),
        'line_delay': (float(controls.line_min.get()), float(controls.line_max.get())),
        'long_pause': (float(controls.long_min.get()), float(controls.long_max.get())),
        'long_pause_every': int(controls.long_freq.get()),
        'error_rate': int(controls.error_rate.get()),
        'error_correction': (float(controls.error_min.get()), float(controls.error_max.get())),
        'initial_delay': float(controls.initial_delay.get()),
        'auto_correct': controls.auto_correct.get() == 1
    }

def toggle_pause():
    global pause_flag, typing_active, timer_running
    pause_flag = not pause_flag
    if pause_flag:
        pause_btn.config(text="Resume", bg="#3498db")
        timer_label.config(fg="red")
        typing_active = False
        stop_timer()
    else:
        pause_btn.config(text="Pause", bg="#f39c12")
        timer_label.config(fg="blue")
        typing_active = True
        start_timer()

def start_typing():
    global stop_flag, pause_flag, typing_active
    stop_flag = False
    pause_flag = False
    typing_active = True
    text = input_text.get("1.0", tk.END).rstrip()
    params = get_timing_params(timing_controls)
    
    if not text.strip():
        messagebox.showwarning("Empty Text", "Please enter some text to type.")
        return

    start_btn.config(state="disabled")
    stop_btn.config(state="normal")
    pause_btn.config(state="normal", text="Pause", bg="#f39c12")
    reset_btn.config(state="disabled")
    threading.Thread(target=type_text, args=(text, params)).start()
    start_timer()

def type_text(text, params):
    global stop_flag, pause_flag, typing_active
    
    lines = text.splitlines()
    char_delay = (params['char_delay'][0], params['char_delay'][1])
    punct_extra = (params['punctuation_extra'][0], params['punctuation_extra'][1])
    line_delay = (params['line_delay'][0], params['line_delay'][1])
    long_pause = (params['long_pause'][0], params['long_pause'][1])
    error_correction = (params['error_correction'][0], params['error_correction'][1])
    
    time.sleep(params['initial_delay'])
    line_count = 0
    char_count = 0  # Track character position for natural mistakes

    for line in lines:
        if stop_flag: break
        
        while pause_flag and not stop_flag:
            time.sleep(0.1)
            continue
            
        typing_active = True
        time.sleep(random.uniform(*line_delay))
        
        for i, char in enumerate(line):
            if stop_flag: break
            
            while pause_flag and not stop_flag:
                typing_active = False
                time.sleep(0.1)
                continue
            typing_active = True
            
            char_count += 1
            
            # Natural occasional mistake (1% chance, works even when error_rate=0)
            make_natural_mistake = (random.random() < 0.01 and 
                                  char_count > 10 and 
                                  char not in [' ', '\t', '\n'] and
                                  params['auto_correct'])
            
            if make_natural_mistake or (params['error_rate'] > 0 and 
                                      random.randint(1, 100) <= params['error_rate'] and 
                                      i > 3 and 
                                      char not in [' ', '\t'] and
                                      params['auto_correct']):
                
                wrong_char = chr(ord(char) + random.randint(-2, 2))
                pyautogui.write(wrong_char)
                time.sleep(random.uniform(*error_correction))
                
                pyautogui.press('backspace')
                time.sleep(random.uniform(error_correction[0]/2, error_correction[1]/2))
                pyautogui.write(char)
            
            pyautogui.write(char)
            time.sleep(random.uniform(*char_delay))
            
            if char in [".", "!", "?"]:
                time.sleep(random.uniform(*punct_extra))
            elif char in [",", ";", ":"]:
                time.sleep(random.uniform(punct_extra[0]/2, punct_extra[1]/2))

        if stop_flag: break
        
        if line_count < len(lines) - 1:
            pyautogui.press("enter")
            time.sleep(0.5)
            line_count += 1
            
            if line_count % params['long_pause_every'] == 0:
                typing_active = False
                time.sleep(random.uniform(*long_pause))
                typing_active = True
            elif line.strip() == "":
                typing_active = False
                time.sleep(random.uniform(line_delay[0]*1.5, line_delay[1]*1.5))
                typing_active = True

    stop_typing()

def stop_typing():
    global stop_flag, typing_active
    stop_flag = True
    typing_active = False
    stop_timer()
    start_btn.config(state="normal")
    stop_btn.config(state="disabled")
    pause_btn.config(state="disabled")
    reset_btn.config(state="normal")

def start_timer():
    global timer_running, start_time
    if not timer_running and typing_active:
        timer_running = True
        start_time = time.time()
        threading.Thread(target=update_timer, daemon=True).start()

def stop_timer():
    global timer_running
    timer_running = False

def update_timer():
    global timer_running
    while timer_running and not stop_flag:
        if typing_active and not pause_flag:
            elapsed = int(time.time() - start_time)
            timer_label.config(text=f"Typing Time: {elapsed} sec")
        time.sleep(1)

class TimingControls:
    def __init__(self, parent):
        self.frame = tk.LabelFrame(parent, text="Timing Controls (seconds)", font=("Arial", 10), padx=5, pady=5)
        
        def random_float(min_val, max_val):
            return round(random.uniform(min_val, max_val), 3)
        
        # Character Timing
        tk.Label(self.frame, text="Char Delay:").grid(row=0, column=0, sticky="e")
        self.char_min = tk.Entry(self.frame, width=6)
        self.char_min.insert(0, random_float(0.03, 0.08))
        self.char_min.grid(row=0, column=1)
        tk.Label(self.frame, text="to").grid(row=0, column=2)
        self.char_max = tk.Entry(self.frame, width=6)
        self.char_max.insert(0, random_float(0.12, 0.18))
        self.char_max.grid(row=0, column=3)
        
        # Punctuation Timing
        tk.Label(self.frame, text="Punctuation+:").grid(row=1, column=0, sticky="e")
        self.punct_min = tk.Entry(self.frame, width=6)
        self.punct_min.insert(0, random_float(0.15, 0.25))
        self.punct_min.grid(row=1, column=1)
        tk.Label(self.frame, text="to").grid(row=1, column=2)
        self.punct_max = tk.Entry(self.frame, width=6)
        self.punct_max.insert(0, random_float(0.4, 0.6))
        self.punct_max.grid(row=1, column=3)
        
        # Line Timing
        tk.Label(self.frame, text="Line Delay:").grid(row=2, column=0, sticky="e")
        self.line_min = tk.Entry(self.frame, width=6)
        self.line_min.insert(0, random_float(1.8, 2.5))
        self.line_min.grid(row=2, column=1)
        tk.Label(self.frame, text="to").grid(row=2, column=2)
        self.line_max = tk.Entry(self.frame, width=6)
        self.line_max.insert(0, random_float(5.5, 7.0))
        self.line_max.grid(row=2, column=3)
        
        # Long Pause Settings
        tk.Label(self.frame, text="Long Pause:").grid(row=3, column=0, sticky="e")
        self.long_min = tk.Entry(self.frame, width=6)
        self.long_min.insert(0, random_float(7.5, 9.0))
        self.long_min.grid(row=3, column=1)
        tk.Label(self.frame, text="to").grid(row=3, column=2)
        self.long_max = tk.Entry(self.frame, width=6)
        self.long_max.insert(0, random_float(14.0, 16.0))
        self.long_max.grid(row=3, column=3)
        tk.Label(self.frame, text="every").grid(row=3, column=4)
        self.long_freq = tk.Entry(self.frame, width=3)
        self.long_freq.insert(0, random.randint(7, 10))
        self.long_freq.grid(row=3, column=5)
        tk.Label(self.frame, text="lines").grid(row=3, column=6)
        
        # Error Settings
        tk.Label(self.frame, text="Error Rate:").grid(row=4, column=0, sticky="e")
        self.error_rate = tk.Entry(self.frame, width=3)
        self.error_rate.insert(0, 0)
        self.error_rate.grid(row=4, column=1)
        tk.Label(self.frame, text="%").grid(row=4, column=2)
        
        tk.Label(self.frame, text="Correction:").grid(row=4, column=3, sticky="e")
        self.error_min = tk.Entry(self.frame, width=6)
        self.error_min.insert(0, random_float(0.25, 0.35))
        self.error_min.grid(row=4, column=4)
        tk.Label(self.frame, text="to").grid(row=4, column=5)
        self.error_max = tk.Entry(self.frame, width=6)
        self.error_max.insert(0, random_float(0.55, 0.65))
        self.error_max.grid(row=4, column=6)
        
        self.auto_correct = tk.IntVar(value=1)
        tk.Checkbutton(self.frame, text="Auto-correct errors", variable=self.auto_correct,
                      bg=self.frame.cget('bg')).grid(row=5, column=0, columnspan=7, sticky="w")
        
        tk.Label(self.frame, text="Start Delay:").grid(row=6, column=0, sticky="e")
        self.initial_delay = tk.Entry(self.frame, width=6)
        self.initial_delay.insert(0, random_float(4.5, 5.5))
        self.initial_delay.grid(row=6, column=1)
        tk.Label(self.frame, text="seconds").grid(row=6, column=2)

# GUI setup
root = tk.Tk()
root.title("Shuky - Advanced Typing Assistant")
root.geometry("850x800")
root.resizable(False, False)

# Custom colors
bg_color = "#f0f8ff"
primary_color = "#2c3e50"
secondary_color = "#3498db"
accent_color = "#e74c3c"

# Set background
root.configure(bg=bg_color)

# Custom font
title_font = tkfont.Font(family="Helvetica", size=14, weight="bold")
label_font = tkfont.Font(family="Arial", size=11)
button_font = tkfont.Font(family="Arial", size=10)

# App Logo and Title Frame
title_frame = tk.Frame(root, bg=bg_color)
title_frame.pack(pady=(10, 5))

# Logo (using text as logo)
logo_label = tk.Label(title_frame, text="✍️", font=("Arial", 24), bg=bg_color)
logo_label.pack(side=tk.LEFT, padx=5)

app_title = tk.Label(title_frame, text="Shuky Typing Assistant", font=title_font, fg=primary_color, bg=bg_color)
app_title.pack(side=tk.LEFT)

# Info button with icon
info_icon = tk.Label(title_frame, text="ℹ️", font=("Arial", 12), cursor="hand2", bg=bg_color)
info_icon.bind("<Button-1>", lambda e: show_about())
info_icon.pack(side=tk.RIGHT, padx=10)

# Text Area Frame
text_frame = tk.Frame(root, bg=bg_color)
text_frame.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)

tk.Label(text_frame, text="Enter or paste your text below:", font=label_font, bg=bg_color).pack(anchor="w")

input_text = tk.Text(text_frame, wrap=tk.WORD, height=12, font=("Consolas", 11), padx=10, pady=10,
                    borderwidth=2, relief="groove", undo=True)
input_text.pack(fill=tk.BOTH, expand=True)

# Timing Controls
timing_controls = TimingControls(root)
timing_controls.frame.pack(pady=10, padx=10, fill=tk.X)

# Button Frame
button_frame = tk.Frame(root, bg=bg_color)
button_frame.pack(pady=10)

start_btn = tk.Button(button_frame, text="Start Typing", command=start_typing, 
                     bg=secondary_color, fg="white", font=button_font, padx=15)
start_btn.pack(side=tk.LEFT, padx=5)

pause_btn = tk.Button(button_frame, text="Pause", command=toggle_pause,
                     bg="#f39c12", fg="white", font=button_font, padx=15,
                     state="disabled")
pause_btn.pack(side=tk.LEFT, padx=5)

stop_btn = tk.Button(button_frame, text="Stop Typing", command=stop_typing, 
                    bg=accent_color, fg="white", font=button_font, padx=15,
                    state="disabled")
stop_btn.pack(side=tk.LEFT, padx=5)

reset_btn = tk.Button(button_frame, text="Reset Timing", command=reset_to_defaults,
                     bg="#9b59b6", fg="white", font=button_font, padx=15)
reset_btn.pack(side=tk.LEFT, padx=5)

# Timer Display
timer_frame = tk.Frame(root, bg=bg_color)
timer_frame.pack(pady=5)

timer_label = tk.Label(timer_frame, text="Typing Time: 0 sec", font=label_font, fg=primary_color, bg=bg_color)
timer_label.pack()

# Footer Frame
footer_frame = tk.Frame(root, bg=bg_color)
footer_frame.pack(pady=(10, 5))

dev_btn = tk.Button(footer_frame, text="Developed by Engr Shuvo Das", font=("Arial", 9, "underline"), 
                   fg=primary_color, bg=bg_color, bd=0, cursor="hand2", command=open_portfolio)
dev_btn.pack()

root.mainloop()