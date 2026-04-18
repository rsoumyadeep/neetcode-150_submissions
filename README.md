# 🧠 NeetCode Revision Scheduler

## 🚀 Overview

This project automates **spaced repetition for coding problems** by converting a Markdown log of solved problems into scheduled revision tasks in Google Calendar.

Instead of manually tracking revisions, this system ensures consistent reinforcement of problem-solving patterns using an automated pipeline.

---

## 🔄 How It Works

```
problems.md → Python script → Google Calendar API → Scheduled reminders
```

1. You log solved problems in `problems.md`
2. The script parses the file and extracts problems
3. Applies spaced repetition intervals: **0, 1, 3, 7 days + weekly**
4. Creates events in Google Calendar with email reminders
5. Tracks processed entries to avoid duplicates

---

## ✨ Features

* 📄 **Markdown-based logging** (simple and human-readable)
* 🔁 **Spaced repetition scheduling**
* 📅 **Google Calendar integration**
* 🔐 **OAuth 2.0 authentication**
* ♻️ **Idempotent execution** (safe to rerun, no duplicate events)
* 🧠 **Automated learning reinforcement system**

---

## 🧰 Tech Stack

* Python
* Google Calendar API
* OAuth 2.0
* Markdown (.md)
* Git & GitHub

---

## 📁 Project Structure

```
neetcode-150_submissions/
│
├── Data Structures & Algorithms/
├── problems.md
├── README.md
│
└── automation/
    ├── sync_calendar.py
    ├── processed.json
    ├── credentials.json   (ignored)
    └── token.json         (ignored)
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone <your-repo-url>
cd neetcode-150_submissions
```

---

### 2. Install dependencies

```
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

---

### 3. Configure Google Calendar API

* Create a project in Google Cloud Console
* Enable Google Calendar API
* Create OAuth Client ID (Desktop App)
* Download and rename file to:

```
credentials.json
```

* Place it inside:

```
automation/
```

---

### 4. Add problems

Edit `problems.md`:

```
## 18-04-2026
- Two Sum
- Binary Search
```

---

### 5. Run the script

```
cd automation
python sync_calendar.py
```

---

## 📅 Example Output

The script creates:

* Day 0 (same day)
* Day +1
* Day +3
* Day +7
* Weekly recurring revision

All with email reminders.

---

## 🧠 Key Concepts Implemented

* API Integration (Google Calendar)
* OAuth Authentication Flow
* Idempotent System Design
* Data Parsing (Markdown → Structured Data)
* Automation Pipeline Design
* Spaced Repetition Strategy

---

## 🎯 Motivation

Most people solve coding problems and forget them.

This project enforces:

> Solve → Schedule → Revise → Retain

It transforms problem-solving into a **long-term learning system**.

---

## 🚀 Future Improvements

* CLI-based problem logging (`add_problem.py`)
* Difficulty-based scheduling (adaptive repetition)
* Dashboard visualization (GitHub Pages)
* Integration with LeetCode/NeetCode APIs
* WhatsApp/SMS reminders

---

## 📌 Notes

* `credentials.json` and `token.json` are excluded via `.gitignore`
* Script must be run locally (not on GitHub)

---

## 🤝 Contribution

Feel free to fork and extend the system with smarter scheduling or integrations.


## ⭐ Acknowledgment

Built as a personal tool to improve coding retention and learning efficiency.
