# 🚀 PyOS

> An extensible terminal operating system simulation, featuring a modular command system, users, applications, persistent data, and more — built from scratch in Python.

PyOS is a long-term software development and learning project that simulates operating-system concepts inside a terminal environment.

It is being developed from scratch to strengthen Python programming, software architecture, modular design, data persistence, authentication, problem-solving, and general software-engineering skills while gradually building a feature-rich terminal environment.

---

## 🎯 Project Goals

- Build a modular terminal-based operating system simulation.
- Learn Python through a real, continuously evolving software project.
- Practice software architecture and separation of responsibilities.
- Learn how to design systems that can grow without becoming difficult to maintain.
- Practice persistent data storage and user management.
- Improve debugging, problem-solving, and development workflow.
- Continuously improve PyOS as new concepts and technologies are learned.

---

## ✨ Current Features

PyOS has evolved beyond its original basic terminal prototype.

### 🖥️ Core System

- Boot screen and startup sequence
- Interactive command-line shell
- Modular command architecture
- Dynamic command discovery and loading
- Command aliases
- Automatic command help system
- Built-in system commands
- Rich terminal interface

### 🔐 User System

- User account creation
- Username validation
- Duplicate username detection
- Password confirmation
- Persistent user data
- Login system
- Current-user/session handling

### 💾 Data Storage

PyOS currently uses JSON-based storage for persistent data.

Current data includes:

- User accounts
- System settings

The storage system will continue to evolve as PyOS develops.

### 🧩 Dynamic Commands

PyOS uses a modular command system where commands can be placed inside the command directory and discovered by the system automatically.

Seee **[ROADMAP.md](ROADMAP.md)**

A command can define information such as:

```python
TRIGGERS = ("example", "ex")
DESCRIPTION = "Example command"