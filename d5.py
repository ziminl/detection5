


import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class FileChangeHandler(FileSystemEventHandler):
    def __init__(self):
        self.first_file_changed = False

    def on_any_event(self, event):
        if event.is_directory:
            return
        elif event.event_type == 'created':
            if not self.first_file_changed:
                self.save_file(event.src_path)
        elif event.event_type == 'modified':
            if not self.first_file_changed:
                self.save_file(event.src_path)

    def save_file(self, file_path):
        shutil.copy2(file_path, '/path/to/save/first_file')
        self.first_file_changed = True

def detect_file_change(path):
    event_handler = FileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


detect_file_change('/path/to/file_or_directory')



