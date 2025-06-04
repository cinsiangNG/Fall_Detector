![FFmpeg-Logo svg](https://github.com/user-attachments/assets/470cc8ce-987e-4641-8f0f-66a3bf39a235)

# 🎬 Video Splitting Tool (with FFmpeg)

This Python script allows you to split a video into smaller segments using FFmpeg.  
You can customize the duration of each output segment.

---

## ✅ Prerequisites

1. **Download FFmpeg**  
   -Window: [🔗 https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)
   -Linux: 
    ```bash
    sudo apt update
    sudo apt install ffmpeg
    ```

2. **Install & Add FFmpeg to Environment Variables**  
   - Decompress the downloaded file.  
   - Locate the `bin` folder inside (e.g., `C:\ffmpeg\bin`).  
   - Add this path to your system environment variable:

     **Steps:**
     - Press `Win + S`, search for **"Environment Variables"**.
     - Click **"Environment Variables..."**.
     - Under **System Variables**, find `Path` and click **Edit**.
     - Add a new line:  
       ```
       C:\ffmpeg\bin
       ```
     - Click **OK → OK** to confirm.

3. **Verify FFmpeg Installation**
   - Open **Command Prompt** and type:
     ```bash
     ffmpeg -version
     ```
   - If installed correctly, you’ll see something like:
     ```
     ffmpeg version 5.x ...
     ```

---

## 🚀 How to Use

1. Make sure your video file is accessible and note its path.
2. Edit the script `Video_splitting.py` if needed (e.g., segment duration).
3. Run the script with Python:
   ```bash
   python Video_splitting.py
