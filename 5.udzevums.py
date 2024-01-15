import PySimpleGUI as Sg

file_path = "lietotājs.txt"

try:
    name = input("Ievadi savu vārdu: ")

    with open(file_path, 'w') as file:
        file.write(name)

    print("Vārds piereģistrēts!")
        
except IOError:
    print(f"Errors failā '{file_path}'. pārbaudiet vai ievadītā informācija ir pareiza.")
except Exception as e:
    print(f"Negaidīts errors: {str(e)}")