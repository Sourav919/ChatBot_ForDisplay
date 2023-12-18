import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QLabel, QScrollArea, QVBoxLayout, QFrame, QComboBox
from PyQt5.QtGui import QPixmap
import firebase_admin
from firebase_admin import credentials, auth, db, initialize_app

import os



current_directory = os.path.dirname(os.path.realpath(__file__))

json_path = os.path.join(current_directory, 'chatbot.json')

#cred = credentials.Certificate('/home/knight/ChatBot_UI/chatbot.json')
cred = credentials.Certificate(json_path)
firebase_admin.initialize_app(cred, {'databaseURL': 'https://chatbot-402717-default-rtdb.firebaseio.com/'})



class RoundedVBoxLayout(QVBoxLayout):

    def __init__(self):

        super().__init__()

        self.rounded_frame = QFrame()

        self.rounded_frame.setStyleSheet("QFrame {border-radius: 50px; background-color: lightgray;}")
        self.rounded_frame.setLayout(self)
    

    def addWidget(self, widget):
        # Add widgets to the rounded frame
        super().addWidget(widget)


        

class LoginScreen(QDialog):

    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi("login.ui",self)
        
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)

        self.loginButton.clicked.connect(self.loginfunction)
        #self.loginButton.clicked.connect(self.gotoDashboard)

    def loginfunction(self):
        username = self.emailfield.text()
        password = self.passwordfield.text()

        if len(username)==0 or len(password)==0:
            self.labelError.setText("Please input all fields.")

        else:

            try:
                user = auth.get_user_by_email(username)
                
                if user:
                    self.gotoDashboard()
            
            except:
                print("Login Failed !")
                self.labelError.setText("Login Failed Invalid Username or Password")
    

    def gotoDashboard(self):

        dashBoard = DashBoard()
        widget.addWidget(dashBoard)
        widget.setCurrentIndex(widget.currentIndex()+1)


class DashBoard(QDialog):

    def __init__(self):
        super(DashBoard, self).__init__()
        loadUi('dashboard.ui', self)

        self.ref = db.reference('/intents_and_questions')

        self.layout = self.questionLayout
        self.show_intents_questions()

        
        
        self.get_intents()

        

    def update_intent(self):

        pass


    def update_question(self):

        pass


    def get_intents(self):

        

        self.intentCombo.setContentsMargins(40, 140, 0, 0)

        data = self.ref.get()

        if data:
            self.intentCombo.addItems(list(data.keys()))
        
        else:
            self.intentCombo.addItems([])


    def show_intents_questions(self):
        
        

        data = self.ref.get()

        if data:
            # Assuming data is a dictionary
            for intent, questions in data.items():
                questions_text = '\n'.join(questions)
                #label_text = f"Intent: {intent}\nQuestions:{questions_text}\n{'-'*50}"
                label_text = f"INTENT :  {intent}\n\nQUESTIONS : \n{questions_text}\n{'-'*50}"
                label = QLabel(label_text)
                label.setContentsMargins(20,20,20,20)
                self.layout.addWidget(label)
        

        
            
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        scroll_widget = QWidget()
        scroll_widget.setLayout(self.layout)
        scroll_area.setWidget(scroll_widget)

        #main_layout = QVBoxLayout()
        main_layout = RoundedVBoxLayout()
        main_layout.addWidget(scroll_area)

        main_layout.setContentsMargins(20, 120, 800, 30)
        

        self.setLayout(main_layout)
        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle('Dashboard')
        self.show()


      
app = QApplication(sys.argv)
welcome = LoginScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()


try:
    sys.exit(app.exec_())
except:
    print("Exiting")