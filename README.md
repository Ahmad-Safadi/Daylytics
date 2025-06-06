# 🧭 Daily Activity Tracker (Terminal-Based)

A simple and interactive terminal-based Python tool that helps you reflect on how you spend your 24 hours in a day. You log your **bad** and **good** activities, and the script provides a clear summary and progress bar visualization to help you stay mindful and balanced.

---

## 📌 Features

- 🚫 Track **bad activities** (distractions, time-wasters).
- ✅ Track **good activities** (productive, healthy, spiritual).
- 📊 Analyze the percentage of time spent on each activity.
- 📉 Visual progress bars with **Colorama** for easy visualization.
- 🧠 Helps you reflect and improve your daily routine.

---

## 🎮 How It Works

1. You'll first enter your **bad activities** (name + hours).
2. Then, you'll enter your **good activities**.
3. The script will automatically:
   - Ensure total hours don’t exceed 24.
   - Show remaining hours as you go.
   - Display a clear summary of both categories.
   - Show progress bars for time distribution.
   - Warn you if distractions outweigh productivity.

---

## 📦 Requirements

- Python 3.6+
- [`colorama`](https://pypi.org/project/colorama/)

You can install `colorama` via pip:

```bash
pip install colorama
