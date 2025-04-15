from objects import *
from view import ConsoleView

def input_error(func):
    def inner(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except(ValueError,KeyError,IndexError, AttributeError) as error:
            return f'Error {error}'
    
    return inner


class Controller:
    def __init__(self, view: ConsoleView, book: AddresBook):
        self.book = book
        self.view = view

        self.commands = {
            
            'hello': (self.do_greeting, 'hello - Привітання з користувачем'),
            'add': (self.add_contact, 'add - Додати користувача(Якщо контакт є додати номер)'),
            'change': (self.change_contact, 'change - Змінити номер формат(Контакт Старий номер Новий номер)'),
            'all': (self.show_all, 'all - Вивести усю інформацію про контакти'),
            'phone': (self.show_contact, 'phone - Вивести номер(а) телефону контакта'),
            'add-birthday': (self.add_birthday_to_contact, 'add-birthday - Додати дату народження контакту'),
            'show-birthday': (self.show_contact_birthday, 'show-birthday - Вивести дату народження контакта'),
            'birthdays': (self.show_contacts_birthdays, 'birthdays - Вивести усі дні народження у продовж наступних 7 робочих днів'),
            'command': (self.show_commands, 'command - Вивести список команд'),
            }
        
    @input_error
    def parse_input(self):
        user_inp = self.view.user_input()
        inp = user_inp.strip().split()
        if len(inp) < 1:
            raise ValueError("Write command")
        cmd = inp[0].lower()
        args = inp[1:] if len(inp) >= 2 else ''
        return cmd, args

    @input_error
    def run(self):
        while True:
            cmd, args = self.parse_input()
            if cmd in ['exit', 'close']:
                self.view.message("Good Bye!")
                self.book.save_data()
                break
            self.handler_command(cmd, args)
    
    @input_error
    def handler_command(self, cmd, args):
        entry = self.commands.get(cmd)
        if entry:
            handler, _= entry
            handler(args)
        else:
            self.view.message(f"Unknown command: {cmd}")
            

    

    def do_greeting(self, args= None):
        self.view.greeting()

    def add_contact(self, args): 
        name, phone = args
        contact = self.book.find(name)
        if contact:
            contact.add_phone(phone)
        elif contact is None:
            self.book.add_user_in_contacts(Record(name, phone))
        
        self.view.message("Contact Added")
        
    def change_contact(self, args):
        name, old_phone, new_phone = args
        contact = self.book.find(name)
        if contact is None:
            self.view.message(f"Contact '{name}' not found")
            return
        contact.change_phone(old_phone, new_phone)
        self.view.message("Contact Changed")
        
    def show_all(self, args= None):
        for record in self.book.values():
            self.view.message(self.view.show_all_info(record))
                
    def show_contact(self, args):
        name = args[0]
        contact = self.book.find(name)
        if contact:
            self.view.message(self.view.show_phone(contact))
        
    def add_birthday_to_contact(self, args):
        name, birthday = args
        contact = self.book.find(name)
        if contact:
            contact.add_birthday(birthday)
            self.view.message('Birthday Added')
            
    def show_contact_birthday(self, args):
        name = args[0]
        contact = self.book.find(name)
        if contact:
            self.view.message(self.view.show_birthday(contact))
            
    def show_contacts_birthdays(self, args=None):
        upcoming_birthdays = self.book.get_upcoming_birthdays()
        for birthday in upcoming_birthdays:
            self.view.message(self.view.birthdays(birthday))
            
    def show_commands(self, args=None):
        for _, description in self.commands.values():
            self.view.message(description)
            
                    
