from abc import ABC, abstractmethod
from collections import UserDict
from datetime import datetime, timedelta
import pickle


class Field(ABC):
    
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    
    def __init__(self, value):
        if isinstance(value, Phone):
            value = value.value
        
        if not self.number_check(value):
            raise ValueError("Not correct form of number")
        super().__init__(value)
    
    @staticmethod
    def number_check(value):
        return value.isdigit() and len(value) == 10

class Birthday(Field):
    
    def __init__(self, value: str):
        try:
            datetime.strptime(value, "%d.%m.%Y")
            self.value = value
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")


class Record:
    
    def __init__(self, name: Name, phone: Phone):
        self.name = Name(name)
        self.phones = [Phone(phone)]
        self.birthday = None
        
    def find_phone(self, phone) -> bool:
        for p in self.phones:
            if p.value == phone:
                return True
        return False
    
    def add_phone(self, phone: Phone):
        if not self.find_phone(phone):
            self.phones.append(Phone(phone))

            
    def change_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                self.phones.remove(phone)
                self.add_phone(Phone(new_phone))
                return True
        return False

    def remove_phone(self, phone):
        if self.find_phone(phone):
            self.phones.remove(phone)
                  
    def add_birthday(self, birthday: str):
        self.birthday = Birthday(birthday)

            
class AddresBook(UserDict):
    
    def add_user_in_contacts(self, record: Record):
        self.data[record.name.value] = record
        
    def find(self, name: str):
        return self.data.get(name)
        
    def get_upcoming_birthdays(self):
        today = datetime.today().date()
        upcoming_birthdays = []
        
        for record in self.data.values():
            if record.birthday:
                converted_record = datetime.strptime(record.birthday.value, "%d.%m.%Y").date()
                birthday_this_year = converted_record.replace(year=today.year)
                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)
                
                days_ahead = (birthday_this_year - today).days
                if days_ahead <= 7:
                    congrats_date = birthday_this_year
                    if congrats_date.weekday() in (5, 6):
                        congrats_date += timedelta(days=(7 - congrats_date.weekday()))
                    
                    upcoming_birthdays.append({
                        "name": record.name.value,
                        "birthday": congrats_date.strftime("%d.%m.%Y")
                    })
        
        return upcoming_birthdays                                   
    
    def save_data(self, filename="addressbook.pkl"):
            with open(filename, "wb") as f:
                pickle.dump(self, f)
                
    @classmethod        
    def load_data(self, filename="addressbook.pkl"):
            try:
                with open(filename, "rb") as f:
                    return pickle.load(f)
            except FileNotFoundError:
                return AddresBook()