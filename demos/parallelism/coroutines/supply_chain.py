"""
Supply chain simulation using coroutines and asyncio.

Inspired by games such as Factorio or Satisfactory.
"""

import asyncio

async def mine(convoyeur):
    while True:
        await asyncio.sleep(1)
        await convoyeur.put("minerai")
        print("Minerai extrait")

async def fonderie(convoyeur):
    while True:
        minerai = await convoyeur.get()
        await asyncio.sleep(2)
        print(f"{minerai} transformé en lingot")

async def main():
    convoyeur = asyncio.Queue(maxsize=5)

    await asyncio.gather(
        mine(convoyeur),
        fonderie(convoyeur),
    )

asyncio.run(main())
