# Antigravity Floating Context Tracker

A lightweight, frameless floating widget written in pure Python (`tkinter`) that displays the estimated context window usage for the Antigravity IDE in real-time.

## The Problem
The current version of Antigravity IDE lacks a built-in visual indicator for context window token usage in the default chat interface. While there are IDE extensions available (like `antigravity-context-window`), some users prefer not to install third-party plugins due to security concerns or because they prefer not to clutter their IDE with extensions that require deep access to local files.

## The Solution
This script provides a 100% transparent, standalone, and secure alternative. It is a tiny Python script (~60 lines) that runs entirely outside of the IDE. It creates a minimalist, frameless overlay that floats on top of all windows (even the Windows taskbar) and updates automatically.

### How it works under the hood
Antigravity IDE saves conversation histories locally in `~/.gemini/antigravity-ide/brain/`. 
This script automatically detects your **currently active session** by finding the most recently modified `transcript_full.jsonl` file. It then reads this file, counts the characters, and estimates the token usage (using a standard heuristic of ~4 characters per token). 

- **Zero dependencies**: No heavy frameworks required.
- **Zero network calls**: No data is sent over the internet.
- **Fully auditable**: It's a single, tiny file.

## Usage
Simply run the script using Python on Windows:

```bash
python context_tracker.py
```

- **Drag & Drop**: Click and hold the widget to move it anywhere on your screen (e.g., tuck it into the corner of your IDE).
- **Always on top**: It will remain visible over Antigravity IDE and your system taskbar.
- **Close**: Double-click the widget to terminate the script.

## Requirements
- Windows OS
- Python 3.x (Uses the built-in `tkinter` library, so no `pip install` is required)

## License
MIT
