MiniOS 

A lightweight terminal-based Mini Operating System simulation built with Python for the Operating Systems Laboratory course.
This project simulates core Linux terminal functionalities, user management, process handling, and terminal games.

---

Project Overview

MiniOS is a simplified operating system simulation that provides a Linux-like terminal environment.
The system supports common shell commands, custom user management commands, process management using Python’s `subprocess` library, and built-in terminal games.

When the program starts:

1. A welcome message is displayed.
2. Required packages/tools are automatically installed.
3. The terminal interface appears in the following format:

```bash
MiniOS v0.3
$Username@$Hostname:$PWD
```

---

Features

Linux-like Command Support

The system supports execution of common Linux commands such as:

* `ls`
* `grep`
* `find`
* `tar`
* `cd`
* `cat`
* `echo`
* `mkdir`
* `mv`
* `rm`
* `chmod`
* `wc`
* `pip`
* `apt-get`
* `dpkg`

---

Custom Implemented Commands

The following commands are fully implemented by the project and managed using JSON storage:

* `hostname`
* `passwd`
* `groupadd`
* `useradd`
* `userdel`

These commands store and manage user/system information inside JSON files.

---

Process Management System

The project includes a process management module implemented using Python’s `subprocess` library.

Supported features:

* Process creation
* PID management
* Running / Terminated process states
* Sequential vs Concurrent execution
* Zombie process simulation

---

Built-in Terminal Games

MiniOS contains two terminal-based games that can be executed directly inside the shell environment.

---

Technologies Used

* Python 3
* `subprocess`
* JSON
* OS / Sys libraries
* Terminal-based UI

---

How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/sonia-heidary/Mini_OS_Simulation.git
cd minios
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the System

```bash
python start.py
```

---

Example Usage

```bash
MiniOS v0.3
user@MiniOS:/home/user

$ ls
$ mkdir test
$ useradd ali
$ passwd ali
$ hostname
```

---

Process Management Example

```bash
$ process run app.py
$ process list
$ process state 1024
```

---

Zombie Process Concept

A zombie process is a process that has completed execution but still exists in the process table because the parent process has not yet read its exit status.

This concept is simulated in MiniOS for educational purposes.

---

Educational Goals

This project was developed to better understand:

* Operating System fundamentals
* Shell command execution
* Process lifecycle management
* User and group management
* Linux terminal behavior
* Concurrent processing

---

Author

Developed for the Operating Systems Laboratory Course by Sonia Heidary.
