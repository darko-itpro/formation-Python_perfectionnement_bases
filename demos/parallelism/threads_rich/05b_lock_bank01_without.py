import time
from concurrent.futures import ThreadPoolExecutor

from rich.console import Console

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, amount):
        console.log(f"Will withdraw ${amount:.2f} 💸")
        if self.balance >= amount:
            new_balance = self.balance - amount
            time.sleep(0.1)  # Simulate a delay
            self.balance = new_balance
            console.log(f"New Balance ${self.balance:.2f} 💵")
        else:
            raise ValueError("Insufficient balance")

account = BankAccount(1000)

console = Console()
console.clear()

console.rule("Starting…")

with ThreadPoolExecutor(max_workers=2) as executor:
    executor.submit(account.withdraw, 500)
    executor.submit(account.withdraw, 700)

console.print(f"📈 Final account balance: {account.balance}")
