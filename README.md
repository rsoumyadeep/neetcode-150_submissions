# 🧠 NeetCode Revision Scheduler

## 🚀 Overview

This project automates **spaced repetition for coding problems** by converting a Markdown log of solved problems into scheduled revision tasks using Google Calendar.

It eliminates manual tracking and ensures consistent revision through an automated pipeline.

---

## 🔄 How It Works

```text
problems.md → CLI (add_problem.py) → sync_calendar.py → Google Calendar
```

1. Add a solved problem via CLI
2. The problem is logged in `problems.md`
3. The scheduler parses the file
4. Revision events are created automatically in Google Calendar
5. Duplicate scheduling is prevented using persistent state

---

## ✨ Features

* 📄 Markdown-based problem logging
* ⚡ CLI tool for quick entry (`add_problem.py`)
* 🔁 Spaced repetition scheduling
* 📅 Google Calendar integration
* 🔐 OAuth 2.0 authentication
* ♻️ Idempotent execution (no duplicate events)
* 🔗 Clickable problem links in calendar
* 🏷️ Difficulty-based scheduling
* 🧠 Topic tracking support

---

## 🧰 Tech Stack

* Python
* Google Calendar API
* OAuth 2.0
* Markdown (.md)
* Git & GitHub

---

## 📁 Project Structure

```text
neetcode-150_submissions/
│
├── Data Structures & Algorithms/
├── problems.md
├── add_problem.py
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

```bash
git clone <your-repo-url>
cd neetcode-150_submissions
```

---

### 2. Install dependencies

```bash
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

---

### 3. Configure Google Calendar API

* Create a project in Google Cloud Console
* Enable Google Calendar API
* Create OAuth Client ID (Desktop App)
* Download and rename file to:

```text
credentials.json
```

* Place it inside:

```text
automation/
```

---

## 🧪 Usage

### 🔹 Add a new problem (interactive mode)

```bash
python add_problem.py
```

Follow prompts:

```
Problem name:
Link:
Difficulty (optional):
Topic (optional):
```

---

### 🔹 CLI mode (optional)

```bash
python add_problem.py "Two Sum" https://leetcode.com/problems/two-sum/ easy array
```

---

### 🔹 Automatic behavior

* Problem is added to `problems.md`
* Calendar events are scheduled automatically
* Email reminders are set

---

## 📄 Example `problems.md`

```md
## 17-04-2026
- Search a 2D Matrix | https://neetcode.io/problems/search-2d-matrix/question | medium | binary-search
- Binary Search | https://neetcode.io/problems/binary-search/question?list=neetcode150 | easy | binary-search
```

---

## 📅 Example Output

Each problem generates:

* Day 0 (same day)
* Day +1
* Day +3
* Day +7
* Weekly recurring revision

Calendar events include:

* Problem name
* Clickable link
* Difficulty
* Topic

---

## 🧠 Scheduling Logic

| Difficulty | Intervals         |
| ---------- | ----------------- |
| easy       | 0, 3, 7           |
| medium     | 0, 1, 3, 7        |
| hard       | 0, 1, 2, 3, 7, 14 |

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

Most developers solve problems and forget them.

This project enforces:

> Solve → Schedule → Revise → Retain

It transforms coding practice into a **long-term learning system**.

---

## 🚀 Future Improvements

* Auto-extract problem name from URL
* Adaptive scheduling based on recall success
* Dashboard visualization (GitHub Pages)
* Integration with LeetCode APIs
* WhatsApp/SMS reminders

---

## 📌 Notes

* `credentials.json` and `token.json` are excluded via `.gitignore`
* Script must be run locally (not on GitHub)

---

## 🤝 Contribution

Feel free to fork and extend the system.

---

## ⭐ Acknowledgment

Built as a personal system to improve coding retention and learning efficiency.
