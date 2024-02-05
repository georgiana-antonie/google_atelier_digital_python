import csv


def get_categories():
    categories_file = open("categories.txt", "a")

    no_categories = int(input("Introdu numarul de categorii: "))

    for i in range(0, no_categories):
        category = input(f"Introdu numele pentru categoria \"{i + 1}\" : ")
        categories_file.write(category + '\n')

    categories_file.close()
    print(f"Ai terminat de introdus categoriile.\n")


def get_tasks():
    tasks_file = open("tasks.txt", "a")

    task = input("Introdu task-ul: ")
    task_date = input("Introdu data pentru finalizarea task-ului: ")
    task_person = input("Introdu numele persoanei responsabile de task: ")

    invalid_category = True
    while invalid_category:
        task_category = input("Introdu numele categoriei din care face parte task-ul: ")

        with open("categories.txt", "r") as categories_file:
            for category in categories_file:
                if category.strip().lower() == task_category.strip().lower():
                    tasks_file.write(
                        task.strip() + "," + task_date.strip() + "," + task_person.strip() + "," + task_category.strip() + '\n')
                    invalid_category = False
                    break

    tasks_file.close()

#LISTARE DATE
def category_sort():
    with open("tasks.txt", "r", newline='') as tasks_file:
        tasks_list = []
        category = csv.reader(tasks_file, delimiter='\t')
        for line in category:
            if(line):
                tasks_list.append(line[0].split(','))
        tasks_list.sort(key=lambda x: x[3])
        for task in tasks_list:
            print(task)

        #for line in tasks_file.readlines():
        #    tasks_list.append(line.strip().split(","))
       # tasks_list.sort(key=lambda x: x[3])
        #for task in tasks_list:
        #    print(task)

#CRITERII DE SORTARE
#Sortare ascendentă task
def task_ascending_sort():
    with open("tasks.txt", "r", newline='') as tasks_file:
        tasks_list = []
        task = csv.reader(tasks_file, delimiter='\t')
        for line in task:
            if(line):
                tasks_list.append(line[0].split(','))
        tasks_list.sort(key=lambda x: x[0])
        for task in tasks_list:
            print(task)

#Sortare descendentă task
def task_descending_sort():
    with open("tasks.txt", "r", newline='') as tasks_file:
        tasks_list = []
        task = csv.reader(tasks_file, delimiter='\t')
        for line in task:
            if(line):
                tasks_list.append(line[0].split(','))
        tasks_list.sort(key=lambda x: x[0], reverse=True)
        for task in tasks_list:
            print(task)

#Sortare ascendentă deadline
def deadline_ascending_sort():
    with open("tasks.txt", "r", newline='') as tasks_file:
        tasks_list = []
        task = csv.reader(tasks_file, delimiter='\t')
        for line in task:
            if(line):
                tasks_list.append(line[0].split(','))
        tasks_list.sort(key=lambda x: x[1])
        for task in tasks_list:
            print(task)

#Sortare descendentă deadline
def deadline_descending_sort():
    with open("tasks.txt", "r", newline='') as tasks_file:
        tasks_list = []
        task = csv.reader(tasks_file, delimiter='\t')
        for line in task:
            if(line):
                tasks_list.append(line[0].split(','))
        tasks_list.sort(key=lambda x: x[1], reverse=True)
        for task in tasks_list:
            print(task)

#Sortare ascendentă persoana
def person_ascending_sort():
    with open("tasks.txt", "r", newline='') as tasks_file:
        tasks_list = []
        task = csv.reader(tasks_file, delimiter='\t')
        for line in task:
            if(line):
                tasks_list.append(line[0].split(','))
        tasks_list.sort(key=lambda x: x[2])
        for task in tasks_list:
            print(task)

#Sortare descendentă persoana
def person_descending_sort():
    with open("tasks.txt", "r", newline='') as tasks_file:
        tasks_list = []
        task = csv.reader(tasks_file, delimiter='\t')
        for line in task:
            if(line):
                tasks_list.append(line[0].split(','))
        tasks_list.sort(key=lambda x: x[2], reverse=True)
        for task in tasks_list:
            print(task)

#Sortare ascendentă categorie
def category_ascending_sort():
    with open("tasks.txt", "r", newline='') as tasks_file:
        tasks_list = []
        task = csv.reader(tasks_file, delimiter='\t')
        for line in task:
            if(line):
                tasks_list.append(line[0].split(','))
        tasks_list.sort(key=lambda x: x[3])
        for task in tasks_list:
            print(task)

#Sortare descendentă categorie
def category_descending_sort():
    with open("tasks.txt", "r", newline='') as tasks_file:
        tasks_list = []
        task = csv.reader(tasks_file, delimiter='\t')
        for line in task:
            if(line):
                tasks_list.append(line[0].split(','))
        tasks_list.sort(key=lambda x: x[3], reverse=True)
        for task in tasks_list:
            print(task)

def sort():

    print("Tipuri de sortare: \n"
          "1. sortare ascendentă task; \n2. sortare descendentă task; \n"
          "3. sortare ascendentă data; \n4. sortare descendentă data; \n"
          "5. sortare ascendentă persoana responsabilă; \n6. sortare descendentă persoană responsabilă; \n"
          "7. sortare ascendentă categorie; \n8. sortare descendentă categorie")

    sort_option = input("Alege sortarea dorita: ")
    if sort_option == 1:
        task_ascending_sort()
    if sort_option == 2:
        task_descending_sort()
    if sort_option == 3:
        deadline_ascending_sort()
    if sort_option == 4:
        deadline_descending_sort()
    if sort_option == 5:
        person_ascending_sort()
    if sort_option == 6:
        person_descending_sort()
    if sort_option == 7:
        category_ascending_sort()
    if sort_option == 8:
        category_descending_sort()

#FILTRARE DATE
def data_filter():
    print("Campuri: \n"
          "1.Task \n2.Data \n3.Persoana responsabila \n4.Categorie")
    filer = input("Introdu campul dupa care se realizeaza filtrarea: ")



#ADAUGAREA UNUI NOU TASK IN LISTA

#EDITAREA DETALIILOR REFERITOARE LA TASK


#STERGEREA UNUI TASK DIN LISTA INITIALA
def delete_task():
    invalid_task  = True
    while invalid_task:
        delete_task = input("Alege task-ul pe care doresti sa il stergi: ")

        with open("tasks.txt", "r") as tasks_file:
            for task in tasks_file:
                if task.strip()[0] == delete_task:
                    task_file.append(task)
                else:
                    invalid_task = False
                    break




#get_categories()
#get_tasks()
#sort()
delete_task()
