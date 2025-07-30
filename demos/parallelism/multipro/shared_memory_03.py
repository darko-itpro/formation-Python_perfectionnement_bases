"""
Usage de la SharedMemory avec un process.
Accès par identifiant.
"""

from multiprocessing import Process
from multiprocessing.shared_memory import SharedMemory

def job():
    shared_mem = SharedMemory(name="sm")
    shared_mem.buf[:12] = b'Hello World!'
    shared_mem.close()

if __name__ == '__main__':
    shared_mem = SharedMemory(name="sm", create=True, size=100)

    process = Process(target=job, args=())
    process.start()
    process.join()

    print(bytes(shared_mem.buf[:12]).decode())

    shared_mem.close()
    shared_mem.unlink()
