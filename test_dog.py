import watchdog.events 
import watchdog.observers 
import time 
import json


class Handler(watchdog.events.PatternMatchingEventHandler): 
	def __init__(self): 
		# Set the patterns for PatternMatchingEventHandler 
		watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*.json'], ignore_directories=True, case_sensitive=False) 

	def on_created(self, event): 
		print(f"Watchdog received created event - {event.src_path}") 
		# Event is created, you can process it now 

	def on_modified(self, event): 
		print(f"Watchdog received modified event - {event.src_path}") 
		# Event is modified, you can process it now 

		with open (event.src_path, 'r') as time_file:
			time = time_file.read()
		print(json.loads(time))


if __name__ == "__main__": 
	src_path = "/home/alex/repos/python/alarmlamp/flask"
	event_handler = Handler() 
	observer = watchdog.observers.Observer() 
	observer.schedule(event_handler, path=src_path, recursive=True) 
	observer.start() 
	try: 
		while True: 
			time.sleep(1) 
	except KeyboardInterrupt: 
		observer.stop() 
	observer.join() 

