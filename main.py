import sys

from PySide6.QtCore import QThreadPool
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_main import Ui_MainWindow
from pynput import mouse
from pynput.mouse import Button, Controller
from Monitor import Monitor
import json
import time
from datetime import datetime
import pyautogui

from buttons_threads.start_button_class import StartButtonThread
from buttons_threads.record_button_class import RecordButtonThread



class Clicker(QMainWindow):

    def __init__(self):
        super(Clicker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.FLAG = True
        self.TIME = ""
        

        self.ui.start_button.pressed.connect(self.starting)
        self.ui.record_button.pressed.connect(self.recording)
        self.ui.save_time_button.pressed.connect(self.set_timer)

        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())    

    def closeEvent(self, event):

        yes = QMessageBox.StandardButton.Yes
        no = QMessageBox.StandardButton.No
        
        reply = QMessageBox.question(self, "Закрыть?", "Уверены, что хотите закрыть приложение?\nВсе операции будут прерваны.", yes, no)
        if reply == QMessageBox.StandardButton.Yes:
            Monitor.flag = False
            self.FLAG = False
            event.accept()
        else:
            event.ignore()
    
    def started_app_record_info(self):
        self.ui.status_info.setText("Запись запущена!")

    def set_app_record(self):
        self.monitoring_mouse = Monitor()

        mouse_listener = mouse.Listener(on_click=self.monitoring_mouse.on_click,
                                        on_scroll=self.monitoring_mouse.on_scroll,
                                        on_move=self.monitoring_mouse.on_move)
        
        mouse_listener.start()
        mouse_listener.join()

        return self.monitoring_mouse.status

    def finished_app_record_info(self, result):
        
        if self.FLAG:
            if result == "Successful":
                self.ui.status_info.setText("Запись прошла успешно!")
            else:
                self.ui.status_info.setText("Запись прекращена!")

    def started_app_info(self):
        self.ui.status_info.setText(f"Программа будет запущена {self.TIME}!")

    def set_app_start(self):
        
        time_now = datetime.now()

        try:
            start = datetime.strptime(self.TIME, "%d.%m.%Y %H:%M")
        except ValueError:
            return ValueError
        
        try:
            with open("main_record.txt") as main_file:
                main_data = json.load(main_file)
        except FileNotFoundError:
            return FileExistsError
        

        while time_now < start:
            if self.FLAG:
                time_now = datetime.now()
                time.sleep(0.1)
            else:
                return
        
        mouse = Controller()


        for index, obj in enumerate(main_data):

            if self.FLAG is False:
                return
            
            action, _time = obj["action"], obj["_time"]
            
            try:
                next_movement = main_data[index+1]["_time"]
                pause_time = next_movement - _time
            except IndexError as e:
                pause_time = 0.1
            
            
            x, y = obj["x"], obj["y"]

            mouse.position = (x, y)   

            if action == "scroll":

                horizontal_direction, vertical_direction = obj["horizontal_direction"], obj["vertical_direction"]
                mouse.scroll(horizontal_direction, vertical_direction)
            
            time.sleep(pause_time)
            
            # and obj["button"] == "Button.left"
            if action is True and obj["button"] == "Button.left":
                if obj["_counter"] in (3, 4): # (3, 4)
                    time.sleep(0.5)
                    mouse.click(Button.left)
                    
                    
                elif obj["_counter"] > 4: # 4
                    mouse.position = (x, y)
                    mouse.click(Button.left)
                    time.sleep(0.5)

                    if pyautogui.locateOnScreen("accept.png", confidence=0.99):
                        accept = pyautogui.locateOnScreen("accept.png", confidence=0.99)
                        center = pyautogui.center(accept)
                        mouse.position = (center.x, center.y)
                        time.sleep(0.5)
                        mouse.click(Button.left)
                        time.sleep(3)
                    else:
                        cancel = pyautogui.locateOnScreen("cancel.png", confidence=0.9)
                        center = pyautogui.center(cancel)
                        mouse.position = (center.x, center.y)
                        mouse.click(Button.left)

                    time.sleep(0.5)

                elif obj["_counter"] in (1, 2): # (1, 2)
                    time.sleep(0.5)
                    mouse.click(Button.left)
                    time.sleep(7)

            
            

    def finished_app_info(self, event):        
        if event is FileExistsError:
            self.ui.status_info.setText("Файл с записью не найден.")
        elif event is ValueError:
            self.ui.status_info.setText("Ошибка! Укажите время начала работы кликера!")
        else:
            self.ui.status_info.setText("Программа завершена успешно!")

    def recording(self):

        record_button_thread = RecordButtonThread(self.set_app_record)
        record_button_thread.signals.started.connect(self.started_app_record_info)
        record_button_thread.signals.finished.connect(self.finished_app_record_info)

        self.threadpool.start(record_button_thread)

    def starting(self):

        start_button_thread = StartButtonThread(self.set_app_start)
        start_button_thread.signals.started.connect(self.started_app_info)
        start_button_thread.signals.finished.connect(self.finished_app_info)

        self.threadpool.start(start_button_thread)

    def set_timer(self):
        self.TIME = self.ui.time_edit.text()

        self.ui.status_info.setText("Время сохранено.")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Clicker()
    window.show()

    sys.exit(app.exec())
    
