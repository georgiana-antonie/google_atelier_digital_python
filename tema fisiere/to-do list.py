import csv

def main():
    print("Comenzi: \n"
          "1.Crearea unui to-do list \n2.Adaugare de categorii noi \n"
          "3.Adaugare de task-uri noi\n4.Stergerea unui task \n"
          "5.Editarea detaliilor dintr-un task \n"
          "6.Listare date \n7.Soratre")

    while True:
        comanda = input("Alege nr. comenzii dorite: ")

        if comanda == "1":
            adaugare_categorii()
            adaugare_taskuri()
            break
        elif comanda == "2":
            categorii_noi()
            break
        elif comanda == "3":
            taskuri_noi()
            break
        elif comanda == "4":
            stergere_task()
            break
        elif comanda == "5":
            editare_detalii(2)
            break
        elif comanda == "6":
            listare_date()
            break
        elif comanda == "7":
            sortare()
            break
        else:
            print("Alege o optiune existenta!")
            continue

#ADAUGARE CATEGORII
def adaugare_categorii():
    categorii_file = open("categorii.txt", "w")

    nr_categorii = int(input("Introdu numarul de categorii: "))

    for i in range(0, nr_categorii):
        categorie = input(f"Introdu numele pentru categoria \"{i + 1}\" : ")
        categorii_file.write(categorie + '\n')

    categorii_file.close()
    print(f"Ai terminat de introdus categoriile.\n")

#ADAUGARE TASK-URI
def adaugare_taskuri():
    taskuri_file = open("taskuri.txt", "w")
    nume_task = input("Introdu task-ul: ")

    #Adaugare deadline si persoana
    deadline_task= input("Introdu data pentru finalizarea task-ului: ")
    persoana_task = input("Introdu numele persoanei responsabile de task: ")

    #Adaugare categorie din care face parte
    categorie_invalida = True
    while categorie_invalida:
        categorie_task = input("Introdu numele categoriei din care face parte task-ul: ")

        with open("categorii.txt", "r") as categorii_file:
            for categorie in categorii_file:
                if categorie.strip().lower() == categorie_task.strip().lower():
                    taskuri_file.write(
                        nume_task.strip() + "," + deadline_task.strip() + "," + persoana_task.strip() + "," + categorie_task.strip() + '\n')
                    categorie_invalida = False
                    break

    taskuri_file.close()

#ADAUGARE DE CATEGORII NOI
def categorii_noi():
    categorie_existenta = True
    categorii=[]
    with open("categorii.txt", "r") as categorii_file:
        for categorie in categorii_file:
            categorii.append(categorie.replace("\n", ""))
    while categorie_existenta:
        categorie_noua = str(input("Introdu categoria : "))
        if categorie_noua not in categorii:
            categorie_existenta = False
            with open("categorii.txt", "a") as categorii_file:
                categorii_file.write(f"\n{categorie_noua}")
            break
    categorii_file.close()
    print(f"Ai terminat de introdus categoriile.\n")
# ADAUGARE DE TASK-URI NOI
def taskuri_noi():

    #Adaugare task si verificare sa nu existe deja
    task_existent = True
    task_exist=[]
    with open("taskuri.txt", "r") as taskuri_file:
        for nume_task in taskuri_file:
            task = nume_task.split(',')[0].lower().replace(" ", "")
            task_exist.append(task)
    while task_existent:
        task_nou = str(input("Introdu task-ul: "))
        if task_nou.lower().replace(" ", "").lower() in task_exist:
            print("Taskul introdus exista deja")
        else:
            task_existent = False
    taskuri_file.close()
    #Adaugare deadline si persoana
    deadline_task= input("Introdu data pentru finalizarea task-ului: ")
    persoana_task = input("Introdu numele persoanei responsabile de task: ")

    #Adaugare categorie din care face parte
    categorie_invalida = True
    while categorie_invalida:
        categorie_task = input("Introdu numele categoriei din care face parte task-ul: ")
        with open("categorii.txt", "r") as categorii_file:
            for categorie in categorii_file:
                if categorie.lower().replace("\n","") == categorie_task.lower():
                    with open("taskuri.txt", "a") as taskuri_file:
                        taskuri_file.write(
                            task_nou + ", " + deadline_task + ", " + persoana_task + ", " + categorie_task + '\n')
                    categorie_invalida = False
                    break
    taskuri_file.close()
    categorii_file.close()

#STERGEREA UNUI TASK
def stergere_task():
    task_gasit = True
    taskuri=[]
    while task_gasit:
        stergere_task = input("Introdu numele task-ului pe care vrei sa il stergi:")
        with open("taskuri.txt", "r") as taskuri_file:
            updated_lines = []
            for nume_task in taskuri_file:
                task = nume_task.split(',')[0].lower().replace(" ", "")
                taskuri.append(task)
                if task != stergere_task.lower().replace(" ", ""):
                    updated_lines.append(nume_task)
            if stergere_task.lower().replace(" ", "") in taskuri:
                with open("taskuri.txt", "w") as taskuri_file:
                    taskuri_file.writelines(updated_lines)
                task_gasit = True
                print(f'Task-ul "{stergere_task}" a fost sters.')
                break
            taskuri = []
            print("Task-ul nu a fost gasit!")


#EDITAREA DETALIILOR DINTR-UN TASK
def editare_detalii(id_rand):
    with open("taskuri.txt", "r") as taskuri_file:
        taskuri_list = []
        task = csv.reader(taskuri_file, delimiter='\t')
        for line in task:
            taskuri_list.append(line[0].split(","))

        for i in range(len(taskuri_list)):
            if i == id_rand:
                print(taskuri_list[i])
                while True:
                    print("1. Editare nume task \n2. Editare deadline task \n"
                          "3. Editare persoana responsabila \n4. Editare categorie \n")
                    optiune_editare = input("Introduceti optiunea: ")

                    if optiune_editare == "1":
                        nume_task = input("Introduceti numele task-ului: ")
                        nume_vechi = taskuri_list[i][0]
                        taskuri_list[i][0] = nume_task
                        print(f"Task-ul '{nume_vechi}' a fost modificat in '{nume_task}'")
                        break
                    elif optiune_editare == "2":
                        deadline_task = input("Introduceti deadline-ul task-ului: ")
                        deadline_vechi = taskuri_list[i][1]
                        taskuri_list[i][1] = deadline_task
                        print(f"Deadline-ul '{deadline_vechi}' a fost modificat in '{deadline_task}'")
                        break
                    elif optiune_editare == "3":
                        persoana_task = input("Introduceti persoana responsabila pentru task: ")
                        persoana_veche = taskuri_list[i][2]
                        taskuri_list[i][2] = persoana_task
                        print(f"Persoana responsabila '{persoana_veche}' a fost modificata in '{persoana_task}'")
                        break
                    elif optiune_editare == "4":
                        categorie_task = input("Introduceti categoria task-ului: ")
                        categorie_veche = taskuri_list[i][3]
                        taskuri_list[i][3] = categorie_task
                        print(f"Categoria '{categorie_veche}' a fost modificata in '{categorie_task}'")

    with open("taskuri.txt", "w") as taskuri_file:
        for task in taskuri_list:
            taskuri_file.write(f"{task[0]},{task[1]},{task[2]},{task[3]}\n")



#LISTARE DATE
def listare_date():
    with open("taskuri.txt", "r", newline='') as taskuri_file:
        taskuri_list = []
        categorie = csv.reader(taskuri_file, delimiter='\t')
        for line in categorie:
            if(line):
                taskuri_list.append(line[0].split(','))
        taskuri_list.sort(key=lambda x: x[3])
        for task in taskuri_list:
            print(task[3].upper())
            print(task)


#SORTARE
def sortare():
    print("Tipuri de sortare: \n"
          "1. sortare task;\n2. sortare deadline; \n"
          "3. sortare persoana responsabilă; \n4. sortare categorie; \n")

    while True:
        sort_option = input("Alege nr. sortarii dorite: ")

        if sort_option == "1":
            sortare_task()
            break
        elif sort_option == "2":
            sortare_deadline()
            break
        elif sort_option == "3":
            sortare_persoana()
            break
        elif sort_option == "4":
            sortare_categorie()
            break
        else:
            print("Alege o optiune existenta!")
            continue

# Sortare task
def sortare_task():
    tip_sortare = input("ascendenta/descendenta: ")
    with open("taskuri.txt", "r", newline='') as taskuri_file:
        taskuri_list = []
        task = csv.reader(taskuri_file, delimiter='\t')
        for line in task:
            if (line):
                taskuri_list.append(line[0].split(','))
        if tip_sortare == "ascendenta":
            taskuri_list.sort(key=lambda x: x[0])
        elif tip_sortare == "descendenta":
            taskuri_list.sort(key=lambda x: x[0], reverse=True)
    with open("taskuri.txt", "w") as taskuri_file:
        for task in taskuri_list:
            taskuri_file.write(f"{task[0]},{task[1]},{task[2]},{task[3]}\n")
    print("S-a finalizat sortarea")

# Sortare deadline
def sortare_deadline():
    tip_sortare = input("ascendenta/descendenta: ")
    with open("taskuri.txt", "r", newline='') as taskuri_file:
        taskuri_list = []
        task = csv.reader(taskuri_file, delimiter='\t')
        for line in task:
            if (line):
                taskuri_list.append(line[0].split(','))
        if tip_sortare == "ascendenta":
            taskuri_list.sort(key=lambda x: x[1])
        elif tip_sortare == "descendenta":
            taskuri_list.sort(key=lambda x: x[1], reverse=True)
    with open("taskuri.txt", "w") as taskuri_file:
        for task in taskuri_list:
            taskuri_file.write(f"{task[0]},{task[1]},{task[2]},{task[3]}\n")
    print("S-a finalizat sortarea")

# Sortare persoana responsabila
def sortare_persoana():
    tip_sortare = input("ascendenta/descendenta: ")
    with open("taskuri.txt", "r", newline='') as taskuri_file:
        taskuri_list = []
        task = csv.reader(taskuri_file, delimiter='\t')
        for line in task:
            if (line):
                taskuri_list.append(line[0].split(','))
        if tip_sortare == "ascendenta":
            taskuri_list.sort(key=lambda x: x[2])
        elif tip_sortare == "descendenta":
            taskuri_list.sort(key=lambda x: x[2], reverse=True)
    with open("taskuri.txt", "w") as taskuri_file:
        for task in taskuri_list:
            taskuri_file.write(f"{task[0]},{task[1]},{task[2]},{task[3]}\n")
    print("S-a finalizat sortarea")

# Sortare categorie
def sortare_categorie():
    tip_sortare = input("ascendenta/descendenta: ")
    with open("taskuri.txt", "r", newline='') as taskuri_file:
        taskuri_list = []
        task = csv.reader(taskuri_file, delimiter='\t')
        for line in task:
            if (line):
                taskuri_list.append(line[0].split(','))
        if tip_sortare == "ascendenta":
            taskuri_list.sort(key=lambda x: x[3])
        elif tip_sortare == "descendenta":
            taskuri_list.sort(key=lambda x: x[3], reverse=True)
    with open("taskuri.txt", "w") as taskuri_file:
        for task in taskuri_list:
            taskuri_file.write(f"{task[0]},{task[1]},{task[2]},{task[3]}\n")
    print("S-a finalizat sortarea")



if __name__ == "__main__":
    main()