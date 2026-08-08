import csv
from datetime import datetime

FILE = "expenses.csv"

if not __import__('os').path.exists(FILE):
    csv.writer(open(FILE, 'w', newline='')).writerow(['Date','Category','Amount','Note'])

def add():
    print("\n--- ADD EXPENSE ---")
    d = input("Date (YYYY-MM-DD) or Enter for today: ")
    d = d if d else datetime.now().strftime("%Y-%m-%d")
    try: datetime.strptime(d, "%Y-%m-%d")
    except: print("Invalid date, using today"); d = datetime.now().strftime("%Y-%m-%d")
    
    c = input("Category: ")
    if not c: print("Category required!"); return
    
    try: a = float(input("Amount (in Rs.): ")); 
    except: print("Invalid amount!"); return
    if a <= 0: print("Amount must be positive!"); return
    
    n = input("Note (optional): ")
    csv.writer(open(FILE, 'a', newline='')).writerow([d, c, a, n])
    print("Added!")

def view():
    print("\n--- ALL EXPENSES ---")
    try:
        rows = list(csv.reader(open(FILE)))
        if len(rows) <= 1: print("No expenses"); return
        total = 0
        for r in rows[1:]:
            print(f"{r[0]:<12} {r[1]:<15} Rs.{r[2]:<10} {r[3]:<20}")
            total += float(r[2])
        print("-"*60)
        print(f"TOTAL: Rs.{total:.2f}")
    except: print("Error reading file")

def summary():
    print("\n--- CATEGORY SUMMARY ---")
    try:
        rows = list(csv.reader(open(FILE)))
        if len(rows) <= 1: print("No expenses"); return
        categories = {}
        for r in rows[1:]:
            categories[r[1]] = categories.get(r[1], 0) + float(r[2])
        total = 0
        for c, a in categories.items():
            print(f"{c:<15} Rs.{a:<10.2f}")
            total += a
        print("-"*30)
        print(f"{'TOTAL':<15} Rs.{total:<10.2f}")
    except: print("Error reading file")

while True:
    print("\n1.Add 2.View 3.Summary 4.Exit")
    ch = input("Choice: ")
    if ch == '1': add()
    elif ch == '2': view()
    elif ch == '3': summary()
    elif ch == '4': break
    else: print("Invalid")