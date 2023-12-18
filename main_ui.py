import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget, QLabel
from PyQt5.QtCore import Qt, QCoreApplication
import speech_recognition as sr
import question
import os
import cv2
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QImage, QPixmap


current_directory = os.path.dirname(os.path.realpath(__file__))
main_video_path = os.path.join(current_directory, 'Friendly_new.mp4')

class HospitalChatbotGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hospital Chatbot")
        self.setGeometry(100, 100, 800, 600)
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()

        self.text_edit = QTextEdit(self)
        self.layout.addWidget(self.text_edit)

        self.speak_button = QPushButton("Speak", self)
        self.speak_button.clicked.connect(self.audio_to_text)
        self.layout.addWidget(self.speak_button)

        self.video_label = QLabel(self)
        self.video_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.video_label)

        self.central_widget.setLayout(self.layout)

        self.sample_video_url = main_video_path
        self.answer_video_url = None
        self.play_video(self.sample_video_url)

    def audio_to_text(self):
        init_rec = sr.Recognizer()
        self.text_edit.setPlainText("Let's speak!!")
        QCoreApplication.processEvents()

        try:
            with sr.Microphone() as source:
                audio_data = init_rec.record(source, duration=4)
                self.text_edit.setPlainText("Recognizing your text.............")
                QCoreApplication.processEvents()

                text = init_rec.recognize_google(audio_data)
                self.text_edit.setPlainText("Recognized Text: " + text.strip())
                QCoreApplication.processEvents()

                self.get_response(text.strip())
                print(text)
        except sr.UnknownValueError:
            self.text_edit.setPlainText("Speech Recognition could not understand audio")
        except sr.RequestError as e:
            self.text_edit.setPlainText(f"Could not request results from Google Speech Recognition service; {e}")

    def get_response(self, text):
        video_url = None
        print("Response Text: ", text)

        user_input = text.strip()
        lowercase_text = user_input.lower()

        matching_intent = [intent for intent, questions in question.intents_and_question.items() if any(q in lowercase_text for q in questions)]

        if matching_intent:
            print("Intent: ", matching_intent[0])
            video_url = question.get_video_response(matching_intent[0])
        else:
            print("No matching intent found.")
        if video_url:
            print("hello World")
            self.play_video(video_url)
            return
        matching_intent = None
        self.play_video(main_video_path)

    def play_video(self, video_url):
      cap = cv2.VideoCapture(video_url)

    # Get the frames per second (fps) of the video
      fps = cap.get(cv2.CAP_PROP_FPS)

    # Calculate delay between frames to achieve desired playback speed
      delay = int(1000 / (2 * fps))  # Change '2' to adjust the playback speed (e.g., '1' for normal speed)

      while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        height, width, channel = frame.shape
        bytes_per_line = 3 * width
        q_image = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        pixmap = QPixmap(q_image)
        pixmap = pixmap.scaledToWidth(self.video_label.width())
        self.video_label.setPixmap(pixmap)
        self.video_label.show()

        QCoreApplication.processEvents()

        # Introduce delay to control playback speed
        cv2.waitKey(delay)

      cap.release()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HospitalChatbotGUI()
    window.show()
    sys.exit(app.exec_())
