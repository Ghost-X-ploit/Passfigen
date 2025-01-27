import random
import string
from colorama import Fore, Style, init

# Initialize colorama
init()

def display_pfg_logo():
    logo = f"""
    {Fore.RED}    
    ████████╗ ████████╗ █████████╗
    ██╔═══██║ ██╔═════╝ ██╔══════╝
    ████████║ ██████╗   ██║  █████╗   
    ██╔═════╝ ██╔═══╝   ██║     ██║ 
    ██║       ██║       ██████████║
    ╚═╝       ╚═╝       ╚═════════╝
    Password  File      Generator
    
    
    
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠶⠛⠉⠀⠀⠀⠀⠉⠙⠶⠦⣀⡀⠀⠀⠀⣀⣠⠴⠶⠞⠛⠛⠶⠤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠲⣞⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠞⠁⠀⠀⠀⠀⠀⣀⣠⡤⠤⠤⠤⣤⣄⡀⠀⠀⠹⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣴⠃⠀⠀⠀⠀⢠⠶⠛⠉⠁⠀⠀⠀⠀⠀⠈⠙⠓⠦⢤⣿⠤⠖⠒⠒⠒⠒⠒⠚⠒⠓⠲⠾⢧⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⡤⠤⠤⠤⠤⣭⣳⣤⡀⠀⠀⠀⢀⣀⣀⣠⣤⣤⣤⣬⣙⣳⣦⣄⠀⠀
⠀⠀⠀⠀⢀⣀⣿⣷⣦⣤⣄⣀⡀⠀⣀⣀⣤⣤⣤⣶⣯⣭⣥⣶⣶⣯⣭⣽⣶⣶⣬⣭⣙⣴⢖⣫⣭⣿⣿⣶⣶⣶⣶⣶⣾⣿⣿⣿⣷⣤
⠀⠀⠀⣤⠛⢹⡇⠈⠉⠙⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⡿⣿⣿⣿⣿⣿⣦
⠀⢀⡞⠁⠀⠸⠇⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡣⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿
⢀⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿P⣿F⣿G⣿⣿⣿⣿⣿⣿⣿⡁⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⡿⠛⠉⠉⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⣀⠀⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⣉⣩⡭⠿⠛⠉⠁⠀⠀⠀⠀⠀⠙⠛⢿⡒⠛⠛⠛⠋⠻⡭⡉⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠹⣦⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡾⠛⠉⠉⠉⠳⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⢀⣀⠀⠀⠀⠉⠙⠳⠦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣇⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⡄⠀⠈⠉⠛⠢⢤⣤⣀⠀⠀⠈⠉⠉⠑⠒⠒⠒⠢⠤⢤⣤⣤⣤⣤⣄⣠⣤⣤⡤⠔⠚⠋⠁⢀⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⢦⣄⡀⠀⠀⠀⠈⠉⠙⠓⠒⠦⢦⣤⣤⣄⣀⣀⣀⣀⣀⣀⠀⠀⠈⠁⠀⢀⣀⣀⣠⣤⠖⠉⠀⠀
⠛⣻⣶⣦⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠲⢤⣤⣀⣀⠀⠀⠀⠀⠀⠀⠁⠀⠈⠀⠉⠀⠉⠉⠉⠉⠉⣉⣉⣤⣥⣷⠾⠓⢲⣚⡟
⠈⣞⣷⣴⣌⣽⣫⣿⠷⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠛⠛⠛⠷⠶⠶⠶⠶⢶⢦⣤⣤⣴⢿⣯⡉⠉⣁⣞⠗⢂⠹⡝⠅
⠀⣻⣿⣷⢪⣿⣋⠀⠀⢀⡈⣽⡛⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡟⣛⣍⣿⢷⡆⣈⣻⣮⠀⣻⣧⢿⣷⣶⠾
⠿⣿⣿⠾⠿⣿⡿⣵⣿⡏⣿⠹⣿⣞⢷⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣴⠟⡾⣿⣹⣿⣿⢷⡽⣏⠛⠓⠒⠛⠛⠛⠛⠛
⡼⢭⠥⣴⠬⣿⠿⢯⡿⢥⡿⢧⡿⢿⡿⢯⠭⢭⡿⢿⡿⢿⡿⢶⡶⢶⡾⢾⡿⢿⡭⢿⣿⠼⣧⠍⣭⠭⣥⠬⣷⢻⣆⣀⣦⣀⣴⣀⣀⠀
⢱⡿⠶⠿⠶⠾⠶⠾⠶⠾⠷⠾⠶⠾⠷⠾⠶⠾⠷⠾⠷⠾⠷⠾⠷⠾⠟⠛⠻⠞⠛⠛⠛⠛⠛⠛⠛⠋⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⢹⡀
⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇
    {Style.RESET_ALL}
    """
    print(logo)

def get_input(prompt, default=None):
    try:
        user_input = input(prompt)
        return user_input.strip() if user_input.strip() else default
    except EOFError:
        return default

def read_common_passwords(file_name):
    try:
        with open(file_name, 'r') as file:
            common_passwords = file.readlines()
        return [password.strip() for password in common_passwords]
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        return []

def add_special_characters(password, max_special_chars=2):
    special_chars = ['!', '@', '#', '$', '%', '&', '*']
    count = 0
    result = []
    for char in password:
        result.append(char)
        if char.isalpha() and count < max_special_chars:  # Add special characters after letters
            result.append(random.choice(special_chars))
            count += 1
    return ''.join(result)

def random_number():
    return str(random.randint(0, 9999))

def replace_s_and_a(password, probability=0.02):
    if random.random() < probability:
        password = password.replace('s', '$').replace('a', '@')
    return password

def reverse_string(s):
    return s[::-1]

def generate_variations_with_special_and_numbers(base):
    passwords = set()
    special_chars = ['!', '@', '#', '$', '%', '&', '*']
    for char in special_chars:
        for num in range(10):
            passwords.add(f"{base}{char}{num}")
    return passwords

def generate_strong_password(name, phone_no=None):
    if name:
        name = name.strip()
        name = random.choice([name.capitalize(), name.lower()])
        password = name + random.choice(string.digits)
        password += random.choice(string.ascii_uppercase)
        password += random.choice(string.ascii_lowercase)

        if phone_no:
            password += phone_no

        password = add_special_characters(password, max_special_chars=2)
        password = replace_s_and_a(password, 0.05)

        return password
    return None

def generate_passwords(user_details, num_passwords, common_passwords):
    passwords = set()

    if not user_details:
        for password in common_passwords:
            passwords.add(password)
            passwords.add(password + random_number())
            passwords.add(add_special_characters(password))
            passwords.add(reverse_string(password))
        return list(passwords)

    for _ in range(num_passwords):
        temp_passwords = set()

        if user_details.get("username"):
            username = user_details["username"]
            username = replace_s_and_a(username, 0.05)
            temp_passwords.add(generate_strong_password(username, user_details.get("phone_no")))
            temp_passwords.add(username + random_number())
            temp_passwords.add(reverse_string(username))

        if user_details.get("phone_no"):
            phone_no = user_details["phone_no"]
            temp_passwords.add(generate_strong_password(phone_no))
            temp_passwords.add(phone_no + random_number())
            temp_passwords.add(reverse_string(phone_no))

        if user_details.get("name"):
            name = user_details["name"]
            temp_passwords.add(generate_strong_password(name, user_details.get("phone_no")))

            if len(name) > 8:
                half1 = name[:len(name)//2]
                half2 = name[len(name)//2:]
                temp_passwords.add(generate_strong_password(half1))
                temp_passwords.add(generate_strong_password(half2))

            temp_passwords.add(name + random_number())
            temp_passwords.add(reverse_string(name))
            temp_passwords.update(generate_variations_with_special_and_numbers(name))

        passwords.update(temp_passwords)

    return list(passwords)

def create_password_file(password_file_name, passwords):
    try:
        with open(password_file_name, "w") as file:
            for password in passwords:
                file.write(password + "\n")
        print(f"Password file '{password_file_name}' has been created successfully.")
       

    except OSError as e:
        print(f"Error: Unable to create file '{password_file_name}'. {e}")

def main():
    display_pfg_logo()
    print(f"{Fore.GREEN}Welcome to the Password Generator for Brute Forcing{Style.RESET_ALL}")

    # print("SELECT AN OPTION TO BEGIN: ")

    user_details = {}
    common_passwords_file = "common.txt"
    common_passwords = read_common_passwords(common_passwords_file)

    if not common_passwords:
        print("No common passwords loaded, proceeding with generation.")

    while True:
        print(f"\n\t{Style.BRIGHT}{Fore.GREEN}SELECT AN OPTION TO BEGIN:{Style.BRIGHT}{Fore.GREEN}\n")
        print(f"\t[1] {Style.BRIGHT}{Fore.GREEN}Enter username{Style.BRIGHT}{Fore.GREEN}")
        print(f"\t[2] {Style.BRIGHT}{Fore.GREEN}Enter phone number{Style.BRIGHT}{Fore.GREEN}")
        print(f"\t[3] {Style.BRIGHT}{Fore.GREEN}Enter name{Style.BRIGHT}{Fore.GREEN}")
        print(f"\t[4] {Style.BRIGHT}{Fore.GREEN}Generate password file{Style.BRIGHT}{Fore.GREEN}{Style.RESET_ALL}")
        print(f"\t[5] {Style.BRIGHT}{Fore.RED}Exit{Style.BRIGHT}{Style.RESET_ALL}")

        try:
            option = get_input("\n\tEnter your choice : ", default="5")
        except EOFError:
            option = "5"

     

        if option == "1":
            username = get_input("\tEnter username: ")
            if username:
                user_details["username"] = username
            print("\tUsername Saved! \n")
        elif option == "2":
            phone_no = get_input("\tEnter phone number: ")
            if phone_no:
                user_details["phone_no"] = phone_no
            print("\tPhone no Saved! \n")
        elif option == "3":
            name = get_input("\tEnter your name: ")
            if name:
                user_details["name"] = name
            print("\tName Saved! \n")
        elif option == "4":
            password_file_name = get_input("\tEnter the password file name (e.g., passwords.txt): ", default="passwords.txt")
            try:
                num_passwords = int(get_input("\tHow many passwords do you want to generate in the file? ", default="100"))
                if user_details.get("username", "") == "" and user_details.get("name", "") == "" and user_details.get("phone_no", "") == "":
                    try:

                        # Open common.txt to read passwords
                        with open("common.txt", "r") as common_file:
                            passwords = common_file.readlines()

                        # Ensure there are enough passwords in the file
                        if num_passwords > len(passwords):
                            print(f"Error: Requested {num_passwords} passwords, but only {len(passwords)} available.")
                        else:
                            # Write the specified number of passwords to passwords.txt
                            with open("passwords.txt", "w") as password_file:
                                for i in range(num_passwords):
                                    password_file.write(passwords[i])

                            print(f"{num_passwords} passwords have been saved to 'passwords.txt'.")

                    except FileNotFoundError:
                        print("Error: 'common.txt' not found. Please ensure the file exists.")
                    except ValueError:
                        print("Error: Please enter a valid number.")
                else:
                    # print("Error: username, name, or phone_no is not empty.")
                    passwords = generate_passwords(user_details, num_passwords, common_passwords)
                    create_password_file(password_file_name, passwords)
                
            except ValueError:
                print("\tPlease enter a valid number for passwords.")

            break


                            
        elif option == "5":
            print("\tExiting the program.")
            break
        else:
            print("\tInvalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
