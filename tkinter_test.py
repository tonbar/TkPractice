import logging
import os
import sys
import time
import tkinter as tk


class Tester:

    def __init__(self):
        # Initialise an instance of the module logger
        self.ml = ModuleLogger()
        self.log = self.ml.module_logger
        self.popup = self.ml.my_message
        # Create dictionary to hold information extracted from the sources
        self.info_dict = {}
        self.status = ""
        self.authoriser = ""
        self.worksheet = ""
        self.sample = ""

    def handle_exception(self, exc_type, exc_value, exc_traceback):
        # Debug is used as this type of error cannot be attempted to be passed to the popup as will happen with
        # use of critical or error level
        self.log.debug("An exception occurred", exc_info=(exc_type, exc_value, exc_traceback))
        # Pass write-out of error to popup
        self.log.critical(f"[CRITICAL ERROR]: {exc_value}. See bioinformatics team for support [CRITICAL ERROR]")
        self.log.critical("\n")
        self.log.critical("****[ERROR] PDF AND XML FILE HAVE NOT BEEN CORRECTLY GENERATED [ERROR]****")
        self.popup.mainloop()

    def test_stuff(self):
        print("starting")
        time.sleep(1)
        self.log.info("hiya")
        time.sleep(2)
        #raise Exception("Huge problemo")
        self.popup.mainloop()

class ModuleLogger:

    def __init__(self):
        # Create pop-up box
        from message_box import MessageBox, MyHandlerText, MyEntryWindow
        self.my_message = MessageBox(None)
        self.my_message.wm_title("CRUK Generator")
        self.module_logger = logging.getLogger(__name__)
        self.module_logger.setLevel(logging.DEBUG)

        # Create handler to route messages to popup
        gui_handler = MyHandlerText(self.my_message.popup_text)
        gui_handler.setLevel(logging.INFO)
        self.module_logger.addHandler(gui_handler)

        # Create handler to route debug messages to file
        #stdout_handler = logging.StreamHandler(sys.stdout)
        #stdout_handler.setLevel(logging.DEBUG)
        #self.module_logger.addHandler(stdout_handler)

        # Create handler to route messages to file
        file_handler = logging.FileHandler(os.path.join(os.getcwd(),"log.log"))
        file_handler.setLevel(logging.DEBUG)
        self.module_logger.addHandler(file_handler)

        # TODO Placed weirdly for testing
        m = MyEntryWindow(self.my_message)
        #self.my_message.wait_window(m.top)


def main():
    t = Tester()
    sys.excepthook = t.handle_exception
    t.test_stuff()


if __name__ == '__main__':
    main()