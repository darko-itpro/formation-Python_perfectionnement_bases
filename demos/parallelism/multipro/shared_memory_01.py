"""
Principe de base de l'objet SharedMemory
"""

from multiprocessing.shared_memory import SharedMemory

sh_mem = SharedMemory(size=1024, create=True)

sh_mem.buf[0] = 42

print(f"{sh_mem.buf[0]=}")

sh_mem.close()
sh_mem.unlink()
