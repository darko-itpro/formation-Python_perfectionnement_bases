from multiprocessing import Process
from multiprocessing.managers import SharedMemoryManager


def task(sl):
    for i in range(len(sl)):
        sl[i] = sl[i] * 10


if __name__ == '__main__':
    manager = SharedMemoryManager()
    manager.start()

    sl = manager.ShareableList([1, 2, 3, 4, 5])
    print(sl)

    process = Process(target=task, args=(sl,))
    process.start()
    process.join()

    print(sl)

    manager.shutdown()