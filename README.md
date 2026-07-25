<div align="center">

<img src="./assets/images/logo.png" alt="Shuky Logo" width="80"/>

# 🤖 Shuky — Advanced Human-Like Typing Bot

**v3.0.1** · Python 3.x · Windows · MIT License

[![GitHub](https://img.shields.io/badge/GitHub-engrshuvodas-181717?logo=github)](https://github.com/engrshuvodas)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-blue?logo=internet-explorer)](https://engrshuvodas.github.io/SHUVO-_portfolio/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Shuky** is a sophisticated typing automation bot that simulates human typing with realistic delays, visible error simulation, smart auto-correction, and fully configurable timing — perfect for bypassing copy-paste restrictions while keeping output 100% accurate.

</div>

---

## 📋 Table of Contents

- [Features](#-features)
- [What's New in v2.5](#-whats-new-in-v25)
- [Version History](#-version-history)
- [Requirements](#-requirements)
- [Installation & Run (Python)](#-installation--run-python)
- [Run as Executable (No Python Needed)](#-run-as-executable-no-python-needed)
- [Build EXE Yourself](#️-build-exe-yourself)
- [Timing Controls Reference](#️-timing-controls-reference)
- [How the Typing Engine Works](#-how-the-typing-engine-works)
- [Project Structure](#-project-structure)
- [Developer](#-developer)
- [License](#-license)

---

## ✨ Features

| Feature | Description |
|---|---|
| ⏱️ **Realistic Character Delays** | Per-character delay randomized between configurable min/max |
| ✍️ **Human-Like Mistakes** | Randomly types a wrong character, then backspaces and corrects it |
| 🧠 **Smart Punctuation Pauses** | Extra delay after `.`, `!`, `?`, `,`, `;`, `:` |
| 🔁 **Long Pauses** | Simulates "thinking breaks" after every N lines |
| 🛑 **Start / Pause / Resume / Stop** | Full control during typing session |
| 📊 **Active Typing Timer** | Counts only real typing time (paused time excluded) |
| ⚙️ **Fully Configurable Timing** | All delays adjustable live from the GUI |
| ✅ **One-Click Reset** | Restores randomized but realistic default values |
| 🖥️ **Clean Tkinter GUI** | User-friendly interface, no terminal needed |
| 📦 **Standalone EXE** | Available as a single `.exe` — no Python required |

---

## 🆕 What's New in v3.0.1

- 🏷️ **Version label updated to v3.0.1** across GUI, title bar, and about dialog
- 🖼️ **Consistent icon everywhere** — same `shukylogo.ico` in title bar, taskbar, and EXE file via `AppUserModelID` + `resource_path` fix
- 📦 **Standalone EXE release** bundled with PyInstaller (`Shuky_v3.0.1.exe`) including icon as embedded data
- 🐛 **Taskbar icon fix** — Windows `SetCurrentProcessExplicitAppUserModelID` called before Tk window creation so taskbar always shows the correct icon
- 📝 **README fully overhauled** — more informative, better structured for developers

---

## 📜 Version History

| Version | Highlights |
|---|---|
| **v3.0.1** | Taskbar icon fix, consistent `shukylogo.ico` everywhere, EXE release |
| **v2.4** | Performance improvements, stability fixes |
| **v2.3** | Auto-correction toggle, accurate timer, improved pause/resume |
| **v2.0** | Long pause logic, line delay system |
| **v1.0** | Initial release — basic typing simulation |

---

## 📦 Requirements

### To run from source (Python)

| Requirement | Version |
|---|---|
| Python | 3.8 or higher |
| `pyautogui` | `pip install pyautogui` |
| `tkinter` | Built-in with Python (no install needed) |

### To run the EXE

- ✅ **Nothing to install** — just download `Shuky_v3.0.1.exe` and run it
- Windows 10/11 recommended

---

## 💻 Installation & Run (Python)

```bash
# Clone the repository
git clone https://github.com/engrshuvodas/Shuky.git
cd Shuky

# Install dependencies
pip install -r requirements.txt

# Launch the app (run from project root, not from src/)
python src/Shuky.py
```

**Usage steps after launching:**
1. Paste or type your text into the text box
2. Adjust timing sliders, or click **Reset Timing** for smart defaults
3. Click **Start Typing**
4. Switch to the target window within the initial delay countdown
5. Watch Shuky type naturally — use **Pause/Stop** anytime

---

## 📦 Run as Executable (No Python Needed)

Download `Shuky_v3.0.1.exe` from the `v3.0.1/` folder and double-click it. No installation required.

> ⚠️ **Windows Defender / Antivirus Note:** PyInstaller-built executables are sometimes flagged as false positives. This is a known PyInstaller behavior. The source code is fully open — you can review it and build the EXE yourself (see below).

---

## 🛠️ Build EXE Yourself

If you prefer to compile from source:

```bash
# Install PyInstaller
pip install pyinstaller

# Run from the src/ directory
cd src

# Build single-file windowed EXE with custom icon (icon also bundled inside via --add-data)
pyinstaller --onefile --windowed \
  --icon="../assets/icons/shukylogo.ico" \
  --add-data "../assets/icons/shukylogo.ico;assets/icons" \
  --name="Shuky_v3.0.1" \
  --distpath="../releases/v3.0.1" \
  Shuky.py
```

| Flag | Purpose |
|---|---|
| `--onefile` | Bundle everything into a single `.exe` |
| `--windowed` | No console/terminal window |
| `--icon` | Embed custom icon |
| `--name` | Output filename |
| `--add-data "shukylogo.ico;."` | Bundle the icon file inside the EXE so `root.iconbitmap()` can find it at runtime |

---

## ⚙️ Timing Controls Reference

| Control | Default | Description |
|---|---|---|
| **Char Delay** | 0.665 – 1.258 s | Delay between each typed character |
| **Punctuation+** | 0.15 – 0.25 s (min) / 0.4 – 0.6 s (max) | Extra pause after punctuation marks |
| **Line Delay** | 1.8 – 2.5 s (min) / 5.5 – 7.0 s (max) | Pause before typing a new line |
| **Long Pause** | 7.5 – 9.0 s (min) / 14 – 16 s (max) | Long "thinking" break every N lines |
| **Long Pause Freq** | Every 7–10 lines | How often long pauses occur |
| **Error Rate** | 0% | % of mistakes to intentionally leave uncorrected |
| **Correction Delay** | 0.25 – 0.35 s (min) / 0.55 – 0.65 s (max) | Time before backspacing a wrong char |
| **Start Delay** | 5.0 s | Countdown before typing begins (time to switch windows) |
| **Auto-Correct** | ✅ Enabled | Backspaces and reypes on simulated errors |

---

## 🧠 How the Typing Engine Works

```
Input Text
    │
    ▼
For each character:
    ├── 10% chance: generate "visible wrong char"
    │       ├── error_rate == 0%  → backspace + retype correct char  (auto-corrected)
    │       └── error_rate  > 0%  → randomly keep mistake in output
    │
    ├── Apply char_delay (random between min/max)
    ├── If punctuation → apply extra punctuation pause
    └── If end of line:
            ├── Press Enter
            └── Every N lines → apply long_pause (thinking break)
```

**Key behavior:**
- `error_rate = 0%` → final output is always **100% correct**, but visually looks human (mistakes happen but are corrected)
- `error_rate > 0%` → some mistakes are intentionally left in the output at the configured percentage

---

## 📁 Project Structure

```
Shuky/                          ← project root
├── .github/
│   └── ISSUE_TEMPLATE/
│       └── bug_report.md       ← GitHub issue template
├── assets/
│   ├── icons/
│   │   └── shukylogo.ico       ← app icon (title bar, taskbar & EXE)
│   └── images/
│       ├── logo.png             ← logo
│       └── Shuky Preview.png   ← UI screenshot
├── releases/
│   ├── v2.4/
│   │   └── Shuky_v2.4.exe      ← previous release
│   └── v3.0.1/
│       └── Shuky_v3.0.1.exe    ← current release ✅
├── src/
│   └── Shuky.py                ← main application source
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

## 👨‍💻 Developer

<div align="center">

Made with ❤️ by **Engr Shuvo Das**

| Platform | Link |
|:---|:---|
| 🌐 **Portfolio** | [engrshuvodas.github.io](https://engrshuvodas.github.io/SHUVO-_portfolio/) |
| 💼 **LinkedIn** | [engrshuvoda](https://www.linkedin.com/in/engrshuvoda/) |
| 💻 **GitHub** | [engrshuvodas](https://github.com/engrshuvodas) |
| 📺 **YouTube** | [Channel](https://www.youtube.com/channel/UCEJ0R871tF2PLT27q9azYWg) |
| 💰 **Fiverr** | [Hire Me](https://www.fiverr.com/shuvo_das74886) |
| 💬 **WhatsApp** | [Chat Now](https://wa.me/+8801765245872) |
| 🐦 **X (Twitter)** | [@engrshuvodas](https://x.com/engrshuvodas) |
| 📘 **Facebook** | [Engr Shuvo](https://www.facebook.com/engr.shuvo74886/) |
| 📧 **Email** | [engrshuvoda@gmail.com](mailto:engrshuvoda@gmail.com) |

</div>

---

## 📄 License

This project is licensed under the **MIT License** — free to use, modify, and distribute with attribution.

```
MIT License © 2025 Engr Shuvo Das
```

---

<div align="center">
⭐ If you find Shuky useful, please <strong>star this repo</strong> — it helps a lot!
</div>
