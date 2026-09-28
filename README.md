# 📂 File Organizer with Python

A Python project designed to automatically organize files in a folder by sorting them into subfolders based on their file extensions.

The application uses a graphical folder selection window, allowing the user to choose the folder they want to organize. The program then identifies the files and automatically moves them into their respective categories.

## 🚀 Features

* 📁 Select a folder through a graphical interface.
* 🔍 Automatically identify file extensions.
* 🖼️ Organize image files.
* 📊 Organize spreadsheet files.
* 🌐 Organize HTML files.
* 📄 Organize PDF files.
* 📂 Automatically create destination folders.
* 🔄 Automatically move files into their respective folders.

## 🛠️ Technologies Used

* **Python 3**
* **OS** — file and directory management.
* **Tkinter** — graphical folder selection interface.

## 📋 How It Works

The user runs the program and selects the folder they want to organize.

The program then:

1. Lists all files in the selected folder.
2. Identifies the name and extension of each file.
3. Checks whether the extension belongs to a specific category.
4. Creates the category folder if it does not already exist.
5. Moves the file into the corresponding folder.

### Example

Before running the program:

```text
📁 Downloads
├── photo.jpg
├── document.pdf
├── spreadsheet.xlsx
├── website.html
└── image.png
```

After running the program:

```text
📁 Downloads
├── 📁 images
│   ├── photo.jpg
│   └── image.png
│
├── 📁 pdf
│   └── document.pdf
│
├── 📁 spreadsheets
│   └── spreadsheet.xlsx
│
└── 📁 internet
    └── website.html
```

## 💻 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repository.git
```

### 2. Navigate to the project folder

```bash
cd your-repository
```

### 3. Run the program

```bash
python main.py
```

A window will open, allowing you to select the folder you want to organize.

## 📦 Dependencies

The project only uses libraries included in the standard Python installation:

```python
import os
from tkinter.filedialog import askdirectory
```

Therefore, **no external packages need to be installed using `pip`**.

## 🧠 Concepts Practiced

This project was developed to practice important Python concepts, including:

* Module imports.
* File and directory manipulation.
* Lists and dictionaries.
* `for` loops.
* `if` statements.
* String manipulation.
* Functions.
* Checking whether files and directories exist.
* Creating directories.
* Moving and organizing files.
* Using `tkinter` for user interaction.

## 🔧 File Categories

The program currently organizes the following file types:

| Category        | Extensions     |
| --------------- | -------------- |
| 🖼️ Images      | `.png`, `.jpg` |
| 📊 Spreadsheets | `.xlsx`        |
| 🌐 Internet     | `.html`        |
| 📄 PDF          | `.pdf`         |
| 📑 CSV          | `.csv`         |

## 📈 Future Improvements

Some features that could be added in the future:

* [ ] Add more file extensions.
* [ ] Add support for `.jpeg`, `.gif`, `.webp`, and other image formats.
* [ ] Add support for `.docx` and `.txt` files.
* [ ] Create a more complete graphical interface.
* [ ] Display a message when the organization process is completed.
* [ ] Add an option to undo the organization.
* [ ] Handle files with duplicate names.
* [ ] Add a logging system.
* [ ] Allow users to customize file categories.
* [ ] Create a Windows `.exe` executable.

## 🎯 Purpose

This project was created as a practical **Python automation exercise**, using file and directory manipulation to solve a common everyday task.

The goal is to transform a manual and repetitive task into an automated process, making file organization faster and more convenient.

## 👨‍💻 Author

**Giliarde Rodrigues**

A project developed for learning and practicing **Python and task automation**.
