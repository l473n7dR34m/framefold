# framefold

*Fold your image sequences into clean animated loops.*

---

## 🌀 What is it?

**framefold** is a lightweight Python tool that compiles a folder of image frames into animated **GIF** or **MOV** files — or both.  
Perfect for generative artists, coders, and motion designers working with frame exports.

---

## ✨ Features

- Convert sequences of images into `.gif`, `.mov`, or both
- Supports common formats: `.png`, `.jpg`, `.jpeg`, `.bmp`, `.gif`
- Auto-generates poetic, timestamped filenames
- Simple folder selection via GUI dialogs
- Cross-platform (macOS & Windows)
- Output to any folder you choose

---

## 🛠 Requirements

- Python 3.7 or higher
- [Pillow](https://pypi.org/project/Pillow/)
- [OpenCV](https://pypi.org/project/opencv-python/)

Install dependencies with:

```bash
pip install -r requirements.txt



How to Use:
Clone or download this repo.

Run the script:

bash
Copy
Edit
python framefold.py
Select your input folder containing image sequences (frames).

Select your output folder where the rendered file(s) will be saved.

When prompted, choose:

gif for a looping animated GIF

mov for a .mov video file

both to export both formats

Output file will be named using the current timestamp and a randomly generated poetic name like:

2025-04-03_17-42-19_kaleidoscope_sentinel.mov

Tips
Frame order is based on filename sorting. Use consistent naming like frame_001.png, frame_002.png, etc.

If you want to hardcode a default save location, you can modify the script where the output folder is selected.
