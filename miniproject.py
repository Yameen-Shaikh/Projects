class ATM:
    def __init__(self, name, pin, balance):
        self.name = name
        self.pin = pin
        self.__balance = balance

    def check_balance(self, pin):
        if self.pin == pin:
            print(f"Current balance: ₹{self.__balance}")
        else:
            print("❌ Invalid PIN!")

    def deposit(self, amt):
        if amt > 0:
            self.__balance += amt
            print(f"₹{amt} deposited. New balance = ₹{self.__balance}")
        else:
            print("❌ Invalid amount!")

    def withdraw(self, pin, amt):
        if self.pin == pin:
            if 0 < amt <= self.__balance:
                self.__balance -= amt
                print(f"₹{amt} withdrawn. New balance = ₹{self.__balance}")
            else:
                print("❌ Insufficient balance or invalid amount!")
        else:
            print("❌ Invalid PIN!")

    def change_pin(self, old_pin, new_pin):
        if self.pin == old_pin:
            self.pin = new_pin
            print("✅ PIN updated successfully.")
        else:
            print("❌ Old PIN is incorrect!")

# Create account
acc = ATM("Lala", 1234, 50000)

# Menu
while True:
    print("\n=== ATM MENU ===")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Change PIN")
    print("5. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        pin = int(input("Enter PIN: "))
        acc.check_balance(pin)

    elif choice == "2":
        amt = int(input("Enter amount to deposit: "))
        acc.deposit(amt)

    elif choice == "3":
        pin = int(input("Enter PIN: "))
        amt = int(input("Enter amount to withdraw: "))
        acc.withdraw(pin, amt)

    elif choice == "4":
        old_pin = int(input("Enter current PIN: "))
        new_pin = int(input("Enter new PIN: "))
        acc.change_pin(old_pin, new_pin)

    elif choice == "5":
        print("👋 Thank you for using the ATM. Goodbye!")
        break

    else:
        print("❌ Invalid option. Try again.")
