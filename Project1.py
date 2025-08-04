class MenuItem:
    def __init__(self, name,items, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self, table_number, items):
        self.table_number = table_number
        self.items = items

    def total_price(self):
        return sum(item.price * quantity for item, quantity in self.items.items())

menu = [
    MenuItem("Chicken Burger", "Burger με κοτόπουλο, bacon, τυρί edam, τομάτα, μαρούλι με μαγιονέζα", 4.20),
    MenuItem("Ham Burger", "Burger με μπιφτέκι, τυρί, κέτσαπ, μουστάρδα", 2.85),
    MenuItem("Green Burger", "Burger με ζουμερό μπιφτέκι, τυρί, φρέσκια τομάτα, μαρούλι, κρεμμύδι, πίκλες, κέτσαπ και dressing sauce", 4.20),
    MenuItem("Club Sandwich", "Club sandwich με 3 πλούσιες στρώσεις Philadelphia σε φρυγανισμένο ψωμί του τοστ με ζουμερό κοτόπουλο φιλέρο, bacon, τομάτα, μαρούλι και τηγανητές πατάτες", 10.90),
    MenuItem("Σαλάτα ceasars", "Δροσερή πράσινη σαλάτα με ζουμερό κοτόπουλου σε βάση μαρουλιού, με καλαμπόκι, κρουτόν, τριμμένο τυρί και vinaigrette ελαιόλαδου", 6.90),
    MenuItem("Κινόα με Λαχανικά", "Δροσερή σαλάτα με κινόα, κόκκινη πιπεριά, τοματίνια, αγγούρι, δυόσμο, φρέσκο μαϊντανό και sauce λαδολέμονο.", 6.30)

]

orders = []

while True:
    table_number = input("Enter table number: ")
    if table_number == "done":
        break

    items = {}
    for item in menu:
        quantity = int(input(f"How many {item.name}s? "))
        items[item] = quantity

    order = Order(table_number, items)
    print(f"Order for table {order.table_number}:")
    for item, quantity in order.items.items():
        print(f"{item.name} x {quantity}")
    print(f"Total price: {order.total_price():.2f}")

    orders.append(order)

print("All orders:")
for order in orders:
    print(f"Table {order.table_number}:")
    for item, quantity in order.items.items():
        print(f"{item.name} x {quantity}")
    print(f"Total price: {order.total_price():.2f}")



 #Ζητάμε από τον χρήστη να επιλέξει τον τρόπο πληρωμής
while True:
    payment_method = input("Πληρωμή με κάρτα ή μετρητά; Επιλέξτε 'Κ' για κάρτα ή 'Μ' για μετρητά: ")
    if payment_method.upper() == "Κ":
        print("Επιλέξατε πληρωμή με κάρτα.")
        break
    elif payment_method.upper() == "Μ":
        print("Επιλέξατε πληρωμή με μετρητά.")
        break
    else:
        print("Λανθασμένη επιλογή, παρακαλώ προσπαθήστε ξανά.")

# Ελέγχουμε αν ο πελάτης πλήρωσε με μετρητά και αν χρειάζεται να δώσουμε ρέστα
if payment_method.upper() == "Μ":
    while True:
        paid_amount = float(input("Πόσο πληρώσατε; "))
        if paid_amount >= order.total_price():
            change = round(paid_amount - order.total_price()) 
            print(f"Παρακαλώ πάρτε τα {change} ευρώ ρέστα.")
            break
        else:
            print("Λανθασμένο ποσό, παρακαλώ προσπαθήστε ξανά.")

