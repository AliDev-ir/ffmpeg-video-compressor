# ffmpeg-video-compressor

# 🎬 Video Compressor

A simple and efficient video compression tool using **FFmpeg** to reduce file size while maintaining good quality. 🚀

## 📌 Features

- Compresses videos without significant quality loss.
- Uses **FFmpeg** for encoding with `libx264`.
- Adjustable quality and speed settings.
- Easy to use in **CLI (Command Line Interface)**.

## 🛠️ Requirements

Make sure you have the following installed:
- **Python 3.x** 🐍
- **FFmpeg** 🎥 (Install it from [here](https://ffmpeg.org/download.html))

## 📥 Installation

Clone the repository and navigate to the project folder:
```bash
git clone https://github.com/yourusername/video-compressor.git
cd video-compressor
```

## ▶️ Usage

Run the script in the terminal:
```bash
python compress_video.py input.mp4 output.mp4 [crf] [preset]
```

### ✅ Parameters:
- **`input.mp4`** → The original video file.
- **`output.mp4`** → The compressed output file.
- **`crf` (optional)** → Controls quality (lower is better, default is `23`).
  - `18` → High quality
  - `23` → Default (good balance)
  - `28` → Lower quality (smaller size)
- **`preset` (optional)** → Controls compression speed.
  - `ultrafast`, `superfast`, `veryfast`, `faster`, `fast`, `medium`, `slow`, `slower`, `veryslow`
  - Default is `slow` (better compression, slightly slower)

### Example:
```bash
python compress_video.py sample.mp4 compressed.mp4 24 fast
```

## 💡 Notes
- FFmpeg must be installed and accessible from the command line.
- The **CRF** setting affects both quality and file size.
- Faster presets reduce compression time but may result in larger file sizes.

## 📜 License
This project is licensed under the **MIT License**. Feel free to use and modify it! 🎉

---
🎬  Keywords: video compression, FFmpeg, Python, reduce video size, video optimizer
Made with ❤️ by **Ali Vaez** 🚀

