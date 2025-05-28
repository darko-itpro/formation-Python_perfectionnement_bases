from multiprocessing import Process
from multiprocessing.shared_memory import ShareableList

def task(sl):
    print(sl)
    for i in range(len(sl)):
        sl[i] = sl[i] * 10


if __name__ == '__main__':
    sl = ShareableList([1, 2, 3, 4, 5]) #  On peut la nommer avec `name=list_name`
    print(sl)

    process = Process(target=task, args=(sl,))
    process.start()
    process.join()

    print(sl)

    sl.shm.close()
    sl.shm.unlink()
