import cv2
import numpy as np
import telepot
import time
import serial
import os
from dotenv import load_dotenv


load_dotenv()

# Telegram Bot Token and Chat ID (Replace with your bot token and chat ID)
BOT_TOKEN = os.environ.get('BOT_TOKEN')
chat_id = os.environ.get('chat_id')
CHAT_ID = os.environ.get('CHAT_ID')
# Initialize the Telegram bot
bot = telepot.Bot(BOT_TOKEN)    
def handle(msg):
    chat_id = msg['chat']['id']
    content_type, chat_type, chat_id = telepot.glance(msg)
    
    if content_type == 'text':
        message = msg['text']
        if message.lower() == 'yes':
            # Send a message to Arduino for access granted
            ser.write(b'O')  # Send 'O' to Arduino to open the door
            send_telegram_message('face_detected.jpg', 'Access granted.')
        elif message.lower() == 'no':
            # Send a message to Arduino for access denied
            ser.write(b'C')  # Send 'C' to Arduino to keep the door closed
            send_telegram_message('face_detected.jpg', 'Access denied.')

# Function to send a message with a photo to Telegram
def send_telegram_message(image_path, message):
    with open(image_path, 'rb') as photo:
        bot.sendPhoto(CHAT_ID, photo, caption=message)

# Initialize the face detection model (you may need to install OpenCV and face detection model)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Open the camera (you may need to change the camera index)
cap = cv2.VideoCapture(0)

# Initialize the serial connection to the Arduino (change the port name)
ser = serial.Serial('COM7', 9600)  # Replace 'COM3' with your Arduino's port

while True:
    ret, frame = cap.read()

    if not ret:
        continue

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    if len(faces) > 0:
        # Face detected
        cv2.imwrite('face_detected.jpg', frame)  # Save the image with the face
        send_telegram_message('face_detected.jpg', 'Face detected. Access request received.')
        break
        # Prompt for access approval
        
        '''access_approval = input('Access granted? (yes/no): ')

        if access_approval.lower() == 'yes':
            # Send a message to Arduino for access granted
            ser.write(b'O')  # Send 'O' to Arduino to open the door
        else:
            # Send a message to Arduino for access denied
            ser.write(b'C')  # Send 'C' to Arduino to keep the door closed'''

    # Display the frame with rectangles around faces (optional)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('Face Detection', frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
bot.message_loop(handle)
cap.release()
cv2.destroyAllWindows()
