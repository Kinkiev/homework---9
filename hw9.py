def help() -> str:
    return "Available commands:\n" \
           "- hello\n" \
           "- add [name] [phone]\n" \
           "- change [name] [phone]\n" \
           "- find [name]\n" \
           "- show_all\n" \
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

commands = {
    "hello": hello,
    "add": add,
    "change": change,
    "find": find,
    "show_all": show_all,
    "help": help,
    "good bye": close,
    "close": close,
    "exit": close
}

@input_error
def parser(text: str) -> tuple[callable, tuple[str]]:
    text_lower = text.lower()
    words = text_lower.split()
    
    if words[0] in commands:
        command = commands[words[0]]
        args = tuple(words[1:])
        return command, args
    
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
