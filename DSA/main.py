import os
import re

def clean_folder_name(name):

    cleaned_name = name.replace(' ', '_').lower()

    cleaned_name = re.sub(r'[^\w]', '', cleaned_name)
    return cleaned_name

def get_next_folder_number():
    existing_folders = [f for f in os.listdir() if os.path.isdir(f) and f[0].isdigit()]
    if not existing_folders:
        return 1
    max_number = max([int(f.split('.')[0]) for f in existing_folders])
    return max_number + 1

def create_folder_and_files(folder_name, num_files):
    cleaned_name = clean_folder_name(folder_name)
    folder_number = get_next_folder_number()
    full_folder_name = f"{folder_number}.{cleaned_name}"

    os.makedirs(full_folder_name)
    print(f"Created folder: {full_folder_name}")

    for i in range(1, num_files + 1):
        file_name = f"{i}.py"
        file_path = os.path.join(full_folder_name, file_name)
        with open(file_path, 'w') as f:
            f.write(f"# This is {file_name}")
        print(f"Created file: {file_path}")

def main():
    folder_name = input("Enter the folder name: ")
    num_files = int(input("Enter the number of Python files to create: "))

    create_folder_and_files(folder_name, num_files)

if __name__ == "__main__":
    main()