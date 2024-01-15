import os

file_name = input("Ievadi faila nosaukumu: ")
file_extension = input("Ievadi faila formātu: ")
file_path = f"{file_name}.{file_extension}"

try:
    # Check if the file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"'{file_path}' neēksistēt.")

    # Check if the file extension is supported
    supported_extensions = ["txt", "csv"]
    if file_extension not in supported_extensions:
        raise ValueError("neatbalstīta faila formāta.")

    # Read the file contents
    with open(file_path, 'r') as file:
        contents = file.read()

    # Print the contents on the terminal
    print(f" Saturs: '{file_path}':\n{contents}")

except FileNotFoundError as fnf_error:
    print(fnf_error)
except ValueError as value_error:
    print(value_error)
except Exception as e:
    print(f"Negaidīts errors: {str(e)}")