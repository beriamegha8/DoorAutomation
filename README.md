# Face Recognition Door Access Control System

This project implements a face recognition-based door access control system using Python, OpenCV, Telegram Bot, and Arduino.

## Overview

The system captures video frames from a camera, performs face detection using OpenCV's Haar Cascade Classifier, and sends the detected face image to a Telegram bot. The Telegram bot then prompts the user for access approval, and based on the response, it sends a command to an Arduino to either open or keep the door closed.

## Requirements

- Python 3.x
- OpenCV
- telepot (Telegram Bot API wrapper)
- pyserial (Python Serial Library)
- [Arduino](https://www.arduino.cc/) with appropriate firmware
- [Telegram Bot](https://core.telegram.org/bots) (Bot Token and Chat ID required)

## Setup

1. Install the required Python packages:
   ```bash
   pip install opencv-python telepot pyserial python-dotenv
   
2. Connect the Arduino to the system and update the serial port in the Python script.

3. Create a .env file in the project root with the following content:
BOT_TOKEN=your_telegram_bot_token
CHAT_ID=your_chat_id

4. Run the Python script:
python face_recognition.py

## Project Structure

face_recognition.py: Main Python script for face detection and interaction with Telegram Bot and Arduino.
haarcascade_frontalface_default.xml: Haar Cascade Classifier for face detection.
face_detected.jpg: Image file saved when a face is detected.

## Usage

Run the Python script.
The camera captures frames and detects faces.
Detected faces are sent to a Telegram bot.
The Telegram bot prompts for access approval.
Based on the response, the Arduino is commanded to open or close the door.

## License

This project is closed to contributions. All rights reserved.
