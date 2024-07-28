from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton
import sys
from backend import Chatbot
import threading

class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.chatbot = Chatbot()


        self.setMinimumSize(700, 500)

        # ADD chat area widget
        self.chat_Area = QTextEdit(self)
        self.chat_Area.setGeometry(10, 10, 480, 320)
        self.chat_Area.setReadOnly(True)

        # Add the input field widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 40)
        self.input_field.returnPressed.connect(self.send_message)

        # Add the button
        self.button = QPushButton("send", self)
        self.button.setGeometry(500, 340, 100, 40)
        self.button.clicked.connect(self.send_message)


        self.show()
    def send_message(self):
        user_input = self.input_field.text().strip()
        self.chat_Area.append(f"Me: {user_input}")
        self.input_field.clear()

        thread = threading.Thread(target=self.get_bot_response, args=(user_input, ))
        thread.start()

    def get_bot_response(self, user_input):
        response = self.chatbot.get_response(user_input)
        self.chat_Area.append(f"Bot: {response}")


app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())
