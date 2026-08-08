students = []
next_id = 1

def add():
    global next_id
    print("\n--- ADD STUDENT ---")
    name = input("Name: ")
    age = int(input("Age: "))
    course = input("Course: ")
    marks = (input("Marks: "))
    students.append({'id': next_id, 'name': name, 'age': age, 'course': course, 'marks': marks})
    print(f"Added! ID: {next_id}")
    next_id += 1

def view():
    print("\n--- ALL STUDENTS ---")
    if not students:
        print("No records")
        return
    for s in students:
        print(f"ID:{s['id']} | {s['name']} | {s['age']} | {s['course']} | {s['marks']}")

def search():
    print("\n--- SEARCH ---")
    key = input("Enter ID or Name: ")
    found = [s for s in students if str(s['id']) == key or key.lower() in s['name'].lower()]
    if found:
        for s in found:
            print(f"ID:{s['id']} | {s['name']} | {s['age']} | {s['course']} | {s['marks']}")
    else:
        print("Not found")

def update():
    print("\n--- UPDATE ---")
    sid = int(input("Enter ID: "))
    for s in students:
        if s['id'] == sid:
            s['name'] = input(f"Name ({s['name']}): ") or s['name']
            s['age'] = int(input(f"Age ({s['age']}): ") or s['age'])
            s['course'] = input(f"Course ({s['course']}): ") or s['course']
            s['marks'] = float(input(f"Marks ({s['marks']}): ") or s['marks'])
            print("Updated!")
            return
    print("ID not found")

def delete():
    print("\n--- DELETE ---")
    sid = int(input("Enter ID: "))
    for s in students:
        if s['id'] == sid:
            students.remove(s)
            print("Deleted!")
            return
    print("ID not found")

def stats():
    print("\n--- STATISTICS ---")
    if not students:
        print("No data")
        return
    marks = [s['marks'] for s in students]
    print(f"Total: {len(students)}")
    print(f"Avg Marks: {sum(marks)/len(marks):.2f}")
    print(f"Highest: {max(marks)}")
    print(f"Lowest: {min(marks)}")

while True:
    print("\n1.Add 2.View 3.Search 4.Update 5.Delete 6.Stats 7.Exit")
    ch = input("Choice: ")
    if ch == '1': add()
    elif ch == '2': view()
    elif ch == '3': search()
    elif ch == '4': update()
    elif ch == '5': delete()
    elif ch == '6': stats()
    elif ch == '7': break
    else: print("Invalid")