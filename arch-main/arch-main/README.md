<p>
    <img src="https://github.com/Hsinchu-Side-project-team/arch/blob/main/Screenshot%202025-05-25%20001756.png" alt="Architecture" width="100%"/>
   
</p>
## 🧠 Fall Detection System (YOLO + FallNet)

This project aims to improve safety in long-term care facilities by providing real-time fall detection and alerting. The system integrates object detection (YOLO) and a deep learning-based sequence model (FallNet) to recognize and respond to fall incidents.

### 📷 Real-Time Monitoring
- A camera captures live video streams from the care environment.
- The system processes the video in real time to detect falls using human pose estimation and a CNN-LSTM-based FallNet model.

### 🚨 Immediate Alert System
- When a fall is detected, the system sends an alert to the backend server.
- The server instantly sends an email notification to designated caregivers via Gmail.

### 💾 Data Storage
- Relevant video clips are automatically saved to the server's database for later review and analysis.

### 🌐 Web-Based User Interface
- Users can log in through a web interface to:
  - View event records
  - Replay historical video clips
  - Read and manage data stored in the database

### 🛡️ Impact
- The system enhances safety in elderly care environments.
- It reduces risks for patients by enabling rapid response to fall incidents.
