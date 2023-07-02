def help() -> str:
    return "Available commands:\n" \
           "- hello\n" \
           "- add [name] [phone]\n" \
           "- change [name] [phone]\n" \
           "- phone [name]\n" \
           "- show all\n" \
           "- help \n" \
           "- good bye, close, exit"

def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except KeyError:
            return "contact not found"
        except ValueError:
            return "invalid input"
        except IndexError:
            return "Invalid input"
        except Exception:
            return help()
    return wrapper

phonebook = {}

@input_error
def add(name:str, phone:str) -> str:
    phonebook[name] = phone
    return "add success"

@input_error
def find(name:str)->str:
    if name in phonebook:
        return phonebook[name]
    else:
        raise KeyError("Contact not found")

@input_error
def change(name:str, new_phone:str)->str:
    if name in phonebook:
        phonebook[name] = new_phone
        return "phone number updated"
    else: 
        raise KeyError("not found")

@input_error
def show_all()->str:
    if len(phonebook) == 0:
        return "no contacts found"
    else: 
        output = ""
        for name, phone in phonebook.items():
            output += f"{name}: {phone} \n"
        return output.strip()

@input_error
def no_command(*args):
    return " - not valid command entered\n" \
           " - type 'help' for commands"

@input_error
def hello() -> str:
    return "How can I help you?"

@input_error
def close() -> str:
    return "Good bye!"

@input_error
def parser(text: str) -> tuple[callable, tuple[str]]:
    text_lower = text.lower()
    if text_lower == "hello":
        return hello, ()
    elif text_lower.startswith("add"):
        command, args = add, text_lower.replace("add", "").strip().split()
        if len(args) != 2:
            raise ValueError
        return command, tuple(args)
    elif text_lower.startswith("change"):
        command, args = change, text_lower.replace("change", "").strip().split()
        if len(args) != 2:
            raise ValueError
        return command, tuple(args)
    elif text_lower.startswith("find"):
        command, args = find, (text_lower.replace("find", "").strip(),)
        if len(args[0]) == 0:
            raise ValueError
        return command, args
    elif text_lower == "show all":
        return show_all, ()
    elif text_lower == "help":
        return help, ()
    elif text_lower in ["good bye", "close", "exit"]:
        return close, ()
    else:
        return no_command, ()
        
def main(): 
    while True: 
        user_input = input (">>>")
        command, data = parser(user_input)
        
        if command == close:
            break 
        
        result = command(*data)   
        print (result)
        

if __name__ == "__main__": 
    main()
