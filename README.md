# MiddleOut Compressor
👨‍💻 Author
Yoshita Sharma &
Devangshu Singh
📧 singhdevangshu@gmail.com
📧 sharmayoshita7@gmail.com
![MiddleOut Logo](./assets/logo.png)  
*A next-generation lossless compression tool inspired by the Pied Piper concept — delivering high compression ratios without sacrificing speed or data integrity.*

---

## 📌 Overview
MiddleOut Compressor is a **cross-platform desktop application** designed to compress and decompress files of **any type** (text, images, audio, video, archives) using a **custom middle-out lossless algorithm**.  
The goal: **Outperform standard compression tools** like ZIP, RAR, and 7z in both **efficiency** and **compression ratio**.

---

## ✨ Features
- **Custom Lossless Compression Algorithm**  
  Achieves higher compression ratios by analyzing and optimizing middle segments of binary data.
- **Supports All File Types**  
  Works with documents, media files, executables, and more.
- **Cross-Platform GUI**  
  Built with a **modern dark theme** featuring green and white accents, inspired by the Pied Piper aesthetic.
- **Drag & Drop Support**  
  Simply drop your file into the app to start compression.
- **Fast & Lightweight**  
  Designed to operate with minimal CPU & RAM usage.

---

## 🖥️ Tech Stack
- **Language**: Python  
- **GUI Framework**: Tkinter / PyQt5 (custom dark theme)  
- **Compression Core**: Custom Middle-Out Algorithm (Python)
- **Platform**: Windows (initial release), cross-platform support planned

---

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/middleout-compressor.git
cd middleout-compressor
2. Install Python (3.8+)

Download from python.org and install.
Check installation:

python --version

🚀 How to Download & Run the Project
Step 1 — Clone the Repository
git clone https://github.com/<your-username>/middleout-compressor.git
cd middleout-compressor

Step 2 — Create Virtual Environment (Recommended)
python -m venv venv


Activate it:

Windows

venv\Scripts\activate


Mac/Linux

source venv/bin/activate

Step 3 — Install Dependencies
pip install -r requirements.txt

Step 4 — Run the Application
python app.py

📂 Usage

Open the application.

Select a file or drag & drop it.

Click Compress to save a .moc file.

To decompress, click Decompress and select a .moc file.

⚙️ How It Works

The Middle-Out algorithm:

Splits file data into start, middle, and end sections.

Compresses the middle section (high redundancy zone) using optimized lossless encoding.

Keeps start & end intact for file integrity.

Recombines with metadata to perfectly restore the original.

📊 Performance Targets

20–40% smaller than ZIP for most file types.

2× faster compression speed on mid-range hardware.

Zero data loss — perfect file restoration.

📅 Roadmap

 Multi-threaded compression

 Password-protected encryption

 MacOS & Linux versions

 Cloud API for compression

🤝 Contributing

We welcome contributions!

Fork the repo

Create a branch:

git checkout -b feature/YourFeature


Commit changes:

git commit -m "Add YourFeature"


Push and create a Pull Request.

📜 License

MIT License — free to use, modify, and distribute.



