"""
Usage de la SharedMemory avec liste d'entiers
"""

from multiprocessing.shared_memory import SharedMemory
from multiprocessing import Process


def task(shared_mem):
    shared_mem.buf[:5] = bytearray([1, 2, 3, 4, 5])
    shared_mem.close()


if __name__ == '__main__':
    shared_mem = SharedMemory(create=True, size=100)

    process = Process(target=task, args=(shared_mem,))
    process.start()
    process.join()

    data = [int(shared_mem.buf[i]) for i in range(5)]

    print(data)

    shared_mem.close()
    shared_mem.unlink()
