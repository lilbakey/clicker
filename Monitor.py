import time
import json


class Monitor:

    flag = True

    def __init__(self) -> None:
        self.storage = []
        self.status = ""
        self.counter_click = 0
        self.counter_scroll = 0

    def on_move(self, x, y):

        if self.flag is False:
             return False
        
        if len(self.storage) >= 1:

            if self.storage[-1]['action'] != "moved":
                
                    json_obj = {'action':'moved', 'x':x, 'y':y, '_time':time.time(), "_counter": self.counter_click}
                    self.storage.append(json_obj)

            elif self.storage[-1]['action'] == "moved" and time.time() - self.storage[-1]['_time'] > 0.02:
                
                    json_obj = {'action':'moved', 'x':x, 'y':y, '_time':time.time(), "_counter": self.counter_click}
                    self.storage.append(json_obj)

        else:
            
            json_obj = {"action": "moved", "x": x, "y": y, "_time": time.time(), "_counter": self.counter_click}
            self.storage.append(json_obj)


    def on_click(self, x, y, button, pressed):
        
        if self.flag is False:
             return False
        
        if pressed:
            self.counter_click += 1
        
        json_obj = {"action": pressed if pressed else "released", 
                    "button": str(button), "x": x, "y": y, "_time": time.time(), "_counter": self.counter_click}

        self.storage.append(json_obj)

        if len(self.storage) > 1:
            if self.storage[-1]["action"] == "released" and self.storage[-1]["button"] == "Button.right" and self.storage[-1]["_time"] - self.storage[-2]["_time"] > 2:
                    self.status = "Successful"
                    with open("main_record.txt", "w+") as outfile:
                        json.dump(self.storage, outfile)
                        
                    return False
            
            elif self.storage[-1]["action"] == "released" and self.storage[-1]["button"] == "Button.right" and self.storage[-3]["action"] == "released" and self.storage[-3]["button"] == "Button.right" and self.storage[-1]["_time"] - self.storage[-3]["_time"] < 1:
                self.status = "Cansel"
                return False

    def on_scroll(self, x, y, dx, dy):

        if self.flag is False:
             return False
        
        json_obj = {"action": "scroll", "vertical_direction": int(dy), "horizontal_direction": int(dx), 
                    "x": x, "y": y, "_time": time.time(), "_counter": self.counter_click}
        self.storage.append(json_obj)

