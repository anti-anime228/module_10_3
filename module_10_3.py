import threading
import time
import random


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        transactions_plus = 10
        random_number1 = random.randint(50, 500)
        with self.lock:
            while transactions_plus > 0:
                if self.balance >= 500 and self.lock.locked():
                    self.lock.release()
                self.balance += random_number1
            print(f"Пополнение: {random_number1}. Баланс: {self.balance}")
            transactions_plus -= 1
            time.sleep(0.1)

    def take(self):
        transactions_minus = 10
        random_number2 = random.randint(50, 500)
        print(f"Запрос на {random_number2}")
        with self.lock:
            while transactions_minus > 0:
                if random_number2 <= self.balance:
                    self.balance -= random_number2
                    print(f"Снятие: {random_number2}. Баланс: {self.balance}")
                    transactions_minus -= 1
                else:
                    print("Запрос отклонён, недостаточно средств")
                    if not self.lock.locked():
                        self.lock.acquire()
                time.sleep(0.1)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
print(f'Итоговый баланс: {bk.balance}')

