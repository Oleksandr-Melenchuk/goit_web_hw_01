from abc import ABC, abstractmethod
from objects import *


class AbstractView(ABC):
    
    @abstractmethod
    def user_input(self):
        pass
    
    @abstractmethod
    def greeting(self):
        pass
    
    @abstractmethod
    def message(self):
        pass
    
    @abstractmethod
    def show_phone(self):
        pass
    
    @abstractmethod
    def show_all_info(self):
        pass
    
    @abstractmethod
    def show_birthday(self):
        pass
    
    @abstractmethod
    def birthdays(self):
        pass
    
    @abstractmethod
    def show_command(self):
        pass
    
    

class ConsoleView(AbstractView):
    
    def __init__(self):
        self.book = AddresBook()
        
    def user_input(self):
        user_inp = str(input("Write command: "))
        return user_inp
        
    
    def greeting(self):
        print("Hello. How can i help you")
    
    def message(self, message):
        print(f"{message}")
    
    
    def show_phone(self, record: Record):
        numbers = "; ".join(str(phone.value) for phone in record.phones) 
        return f'Name: {record.name.value}, Phone : {numbers}'
    
    def show_all_info(self, record: Record):
        birthday = f'Birthday: {record.birthday.value}' if record.birthday is not None else ""
        numbers = '; '.join(phone.value for phone in record.phones)
        return f"Name: {record.name.value}, Phone(s): {numbers}, {birthday}"
    
    
    def show_birthday(self, contact) -> str :
        return f'{contact.name.value} : {contact.birthday.value}'
    
              
    def birthdays(self, contact: dict):
        return f'Name: {contact["name"]}. Birthday : {contact['birthday']}'

    def show_command(self, command_descriptions: list):
        print("\nДоступні команди:")
        print("-" * 80)
        for desc in command_descriptions:
            print(desc)
        print("-" * 80)

