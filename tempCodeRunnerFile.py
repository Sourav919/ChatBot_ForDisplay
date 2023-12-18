import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
import speech_recognition as sr
import question
import os

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

        self.text_label = QLabel(self)
        self.layout.addWidget(self.text_label)

        self.speak_button = QPushButton("Speak", self)
        self.speak_button.clicked.connect(self.audio_to_text)
        self.layout.addWidget(self.speak_button)

        self.video_widget = QVideoWidget(self)
        self.layout.addWidget(self.video_widget)

        self.central_widget.setLayout(self.layout)

        self.media_player = QMediaPlayer()
        self.media_player.setVideoOutput(self.video_widget)
        self.media_player.mediaStatusChanged.connect(self.handle_media_status_changed)

        self.sample_video_url = main_video_path
        self.answer_video_url = None
        self.play_video(self.sample_video_url)

    def audio_to_text(self):
        init_rec = sr.Recognizer()
        print("Let's speak!!")
        try:
            with sr.Microphone() as source:
                audio_data = init_rec.record(source, duration=4)
                print("Recognizing your text.............")
                text = init_rec.recognize_google(audio_data)
                self.text_label.setText("Recognized Text: " + text.strip())
                self.get_response(text.strip())
                print(text)
        except sr.UnknownValueError:
            print("Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

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
            self.play_video(video_url)
            return
        matching_intent = None
        self.play_video(main_video_path)

    def play_video(self, video_url):
        media_content = QMediaContent(QUrl.fromLocalFile(video_url))
        self.media_player.setMedia(media_content)
        self.media_player.play()

    def handle_media_status_changed(self, status):
        if status == QMediaPlayer.EndOfMedia:
            print("Video finished playing.")
            self.play_video(main_video_path)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HospitalChatbotGUI()
    window.show()
    sys.exit(app.exec_())
