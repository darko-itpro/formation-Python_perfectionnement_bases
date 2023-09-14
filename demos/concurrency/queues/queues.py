import threading
import queue
import time

q = queue.Queue(4)

def worker():
    while True:
        print("looping")
        item = q.get()
        print(f'Working on {item}')
        time.sleep(1)
        print(f'Finished {item}')
        q.task_done()

# Turn-on the worker thread.
threading.Thread(target=worker, daemon=True).start()

print("Starting queue")
# Send thirty task requests to the worker.
for item in range(30):
    q.put(item)

# Block until all tasks are done.
q.join()
print('All work completed')