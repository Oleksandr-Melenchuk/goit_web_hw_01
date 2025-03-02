from pathlib import Path
import re


path = Path('')


""" Функція аналізує файл і повертає загальну та середню суму з/п """
def total_salary(path):

    # Перевірка чи вказаний шлях до файлу або шлях веде до папки
    if not path.exists():
        raise FileNotFoundError(f"{path} Відсутній файл ")
    
    if path.is_dir():
        raise ValueError("Ви вказали шлях до папки")

    #Початкові значення для обчислення 
    sum_of_salary, index = 0, 0

    
    try:
        #Відкриття файлу з декодуванням
        with open(path, 'r', encoding='utf-8') as file:
            
            # Знаходимо цифрове значення
            for string in file:
                salarys = re.findall(r'\d+', string)

                # Обчислення суми та індексу
                for salary in salarys:
                    sum_of_salary = sum_of_salary + int(salary)
                    index += 1

        # Якщо у файлі немає валідних значень
        if index == 0:
            return (0,0)

        # Обчислення середньої зарплатні
        average_salary = sum_of_salary / index
        count_salary = (sum_of_salary, int(average_salary))

        return count_salary

    except FileNotFoundError:
        print("Вкажіть вірну назву файлу або перевірте шлях")

    except ZeroDivisionError:
        print("У файлі відсутні значення")

    except ValueError:
        print("Ви вказали шлях до папки")

    except TypeError:
        print("Невірні дані у файлі")

print(total_salary(path))