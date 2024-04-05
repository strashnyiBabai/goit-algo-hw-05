def input_error(func):
    """Decorator, caches ValueError, IndexError, KeyError
        and gives informative message to user acording to error"""
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter name"
        except KeyError:
            return "No user with this name found"

    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_username_phone(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated"
    return "Contact isn't found"

@input_error
def phone_username(args, contacts):
    name = args[0]
    return contacts[name]
    

@input_error
def show_all_phones(contacts):
    return contacts

def main():
    """Main starts the bot for saving phone numbers"""
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)


        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_username_phone(args, contacts))
        elif command == "phone":
            print(phone_username(args, contacts))
        elif command == "all":
            print(show_all_phones(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()