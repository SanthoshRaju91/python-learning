import threading
import time

processing_lock = False


def embed():
    global processing_lock

    processing_lock = True
    threading.Thread(target=scheduler).start()

    time.sleep(10)
    processing_lock = False


def scheduler():
    time.sleep(5)
    if processing_lock == True:
        print("Process is hung")


embed()
