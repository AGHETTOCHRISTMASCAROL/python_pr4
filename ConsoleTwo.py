import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class FileTracking(FileSystemEventHandler):
    def printing(self, event):
        with open(event.src_path, 'r') as file:
            print(file.readlines()[-1].rstrip('\n'))

    def on_modified(self, event):
        self.printing(event)               


tracking = FileTracking()
observer = Observer()
observer.schedule(event_handler=tracking, path='H:\BrainStorm\Course 3\PythonBase\InteractionsBetweenProcesses_python')
observer.start()

try:
    while True:
        time.sleep(1)
finally:
    observer.stop()
    observer.join()