task_list = ["test"]

def add_task():
    new_task = input("Geben Sie eine Aufgabe ein: ")
    task_list.append(new_task)

def show_task_list():
    for index in range(len(task_list)):
        number = index + 1
        print(str(number) + ". : " + task_list[index])
        print("\n")

def delete_task():
    remove_task = input("Welche Aufgabe wollen Sie entfernen: ")
    index_of_list = int(remove_task) - 1
    task_list.remove(task_list[index_of_list])

while True:
    print("""Willkommen zur To-Do-List
Was möchten Sie machen?
1. Aufgabe hinzufügen
2. Liste anzeigen
3. Aufgabe entfernen
4. Beenden""")

    choice = input("Wählen Sie aus: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_task_list()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Auf Wiedersehen")
        break



