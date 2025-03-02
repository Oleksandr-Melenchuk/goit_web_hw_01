def hello() -> None:
    print('How i can help you?')

#Додає новий словник якщо name не збігається
def add_contact(contact, args):
    
    if len(args) != 2:
        return "Invalid number of arguments"
    
    name, phone = args
    
    if name in contact:
        return "User already added"
    
    contact[name] = phone
    
    return 'Contact added.'
    
#Змінює значення phone якщо name у списку
def change_contact(contact, args):
    if len(args) != 2:
        return "invalid number of arguments"
    
    name, phone = args
    
    if name not in contact:
        return "User not found"
    
    contact[name] = phone
    return "Сontact updated"

        
#Повертає номер якщо name у списку
def show_phone(contacts, users_request):
    name = users_request[0]
    if name in contacts:
        return contacts[name]
    
    return "Contact not found"

#Повертає усі збереженні контакти
def show_all(contacts):
    return '\n'.join(f'{key}: {value}' for key, value in contacts.items())

