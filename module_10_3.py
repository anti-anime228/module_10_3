import threading
import time
import random


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        transactions_plus = 100
        while transactions_plus > 0:
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
                time.sleep(0.1)
            self.balance += random.randint(50, 500)
            print(f"Пополнение: {random.randint(50, 500)}. Баланс: {self.balance}")
            transactions_plus -= 1
            time.sleep(0.1)

    def take(self):
        transactions_minus = 100
        print(f"Запрос на {random.randint(50, 500)}")
        while transactions_minus > 0:
            if random.randint(50, 500) <= self.balance:
                self.balance -= random.randint(50, 500)
                print(f"Снятие: {random.randint(50, 500)}. Баланс: {self.balance}")
                transactions_minus -= 1
                time.sleep(0.1)
            else:
                print("Запрос отклонён, недостаточно средств")
                if not self.lock.locked():
                    self.lock.acquire()
                transactions_minus -= 1
                time.sleep(0.1)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
