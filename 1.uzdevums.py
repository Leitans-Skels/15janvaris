file_name = input("Ievadi faila nosaukumu: ")
file_path = f"{file_name}.txt"

try:

    with open(file_path, 'r') as file:
        contents = file.read()

   
    print(f"Saturs: '{file_path}':\n{contents}")

except FileNotFoundError:
    print(f"Fails '{file_path}' neēksistē.")
except Exception as e:
    print(f"Negaidīts errors: {str(e)}")