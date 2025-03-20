# Face Recognition Attendance System

This project is a **Face Recognition Attendance System** that leverages Python, Firebase, and Google Sheets for real-time attendance tracking using face recognition. The system captures live video from a webcam, recognizes student faces, and updates their attendance records in Firebase. The attendance data can also be viewed and managed in Google Sheets.

## Features

- **Real-Time Face Recognition**: Detects and identifies student faces using the webcam.
- **Automatic Attendance Logging**: Updates attendance records in Firebase.
- **Data Integration**: Connects to Google Sheets for data visualization and management.
- **Conditional Formatting**: Google Sheets highlights updated attendance records.
- **Face Data Encoding**: Pre-encodes student faces for fast recognition.
- **Custom UI**: Displays student data including total attendance, major, year, and more on a custom background.

## Technology Stack

- **Python**
- **OpenCV**: For video capture and display.
- **Face Recognition**: Python library for face encoding and comparison.
- **CVZone**: For displaying bounding boxes and overlays.
- **Firebase**:
  - **Realtime Database**: For storing student records and attendance.
  - **Cloud Storage**: For storing and retrieving student images.
- **Google Sheets API**: For viewing and managing attendance data.
- **Numpy**: For efficient array operations.
- **Pickle**: For saving and loading face encodings.

## Setup and Installation

### Prerequisites

1. **Python 3.x** installed on your machine.
2. **Firebase Project** with:
   - Realtime Database enabled.
   - Cloud Storage enabled.
3. **Google Sheets API** access.
