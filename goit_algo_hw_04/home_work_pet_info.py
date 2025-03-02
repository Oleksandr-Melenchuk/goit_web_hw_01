from pathlib import Path

path = Path('')

"""Функція зчитує файл та виводить список словників з інформацією про тварин.
   Якщо у файлі пропущене одне зі значень або значення не є коректним
   виводить повідомлення про відсутність не добавляючи у список словників """
def get_cats_info(path):

    cats_list = []
    id_list = set()

    # Перевірка чи вказаний шлях до файлу або шлях веде до папки
    if not path.exists():
        raise FileNotFoundError(f"{path} Відсутній файл ")
    
    if path.is_dir():
        raise ValueError("Введіть коректний шлях")
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for info in file:
                # Розділення рядка
                cat = info.strip().split(',')
                
                # Пропускає ітерацію якщо строка є пустою
                if not cat:
                    continue
                
                # У випадку відсутності одного з значень виводить загальну помилку
                if len(cat) != 3:
                    print(f"Неправильний формат рядка {info}")
                    continue
                
                cat_id, cat_name, cat_age = cat[0].strip(), cat[1].strip(), cat[2].strip()

                # Перевірка на відсутність ID
                if not cat_id:
                    print(f"Відсутній ID {cat_name}")
                    continue
                
                # Перевірка на унікальність ID
                if cat_id in id_list:
                    print(f'{info}ID не є унікальним')
                    continue
                id_list.add(cat_id)

                # Перевірка на валідність name
                if not cat_name or not cat_name.isalpha():
                    print(f"{info} І'мя повино складатись лише з букв")
                    continue
                
                # Перевірка на відсутність age
                if not cat_age:
                    print(f"{info} Відсутній вік ")
                    continue

                # Перевірка на валідність age
                elif not cat_age.isdigit():
                    print(f"{info} Вік має бути числом")
                    continue


                cats_dict = {'id': cat_id, 'name': cat_name, 'age': cat_age.strip()}
                cats_list.append(cats_dict)
                
    except FileNotFoundError:
        print(f"{path} Файл не знайдено")

    
    return cats_list

    



print(get_cats_info(path))