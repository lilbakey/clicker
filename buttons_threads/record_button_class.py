import sys
from PySide6.QtCore import (QObject, Signal, QRunnable, Slot)
import traceback



class RecordButtonSignal(QObject):
    
    started = Signal()
    finished = Signal(object)
    error = Signal(tuple)
    result = Signal(object)



class RecordButtonThread(QRunnable):

    def __init__(self, fn, *args, **kwargs) -> None:
        super(RecordButtonThread, self).__init__()
        
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = RecordButtonSignal()


    @Slot()
    def run(self):
        try:
            self.signals.started.emit()
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit(result)
