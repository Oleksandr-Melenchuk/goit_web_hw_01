from func import *
from input_data import parse_input, correct_number


def main():

    contacts = {}
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ").strip().lower()
        command, *args = parse_input(user_input)
        

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        
        elif command == "hello":
            print("How can I help you?")
        
        elif command == 'add' and len(args) == 2:

            if correct_number(args[1]):
                print(add_contact(contacts, args))
            else:
                print("Invalid symbol in number ")

        elif command == 'change' and len(args) == 2:
            
            if correct_number(args[1]):
                print(change_contact(contacts, args))
            else:
                print("Invalid symbol in number ")

        elif command == 'phone' and len(args) == 1:
            print(show_phone(contacts, args))

        elif command == 'all':
            print(show_all(contacts))
        

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()