import sqlite3


def db_table_val(id: int, name: str, pet: str, osob: int, photo_id: str, age: str, gen: str, about: str):
    cur.execute('INSERT INTO Animals (id, name, osob, photo_id, age, gen, about) VALUES (?, ?, ?, ?, ?, ?, ?)',
                (id, name, pet, osob, photo_id, age, gen, about))
    con.commit()
    if gen == 'мальчик':
        print(f'{name} успешно добавлен!')
    elif gen == 'девочка':
        print(f'{name} успешно добавлена!')
    print()


if __name__ == '__main__':
    con = sqlite3.connect('Vernost_db.db', check_same_thread=False)
    cur = con.cursor()
    running = True
    while running:
        print(
            'Введите "." чтобы выйти, "+" если хотите добавить анкету, или "=" если хотите поменять статус на "нашёл '
            'хозяина".')
        comm = input('>>> ')
        if comm == ".":
            running = False

        elif comm == "+":
            id = 1
            name = input('Введите имя:  ')
            pet = input('Введите вид питомца(Собака/Кот):  ')
            osob = input('Имеются ли особенности? (Да/Нет): ')
            if osob.lower() == 'да':
                osob = 1
            elif osob.lower() == 'нет':
                osob = 0
            print('Расположите файл питомца в папке "Data"')
            photo_id = input('Введите название файла с изображением питомца(Пример: Lera.png | Gleb.jpg): ')
            age = input('Введите возраст(Пример: 3 года | 6 месяцев): ')
            gen = input('Введите пол (мальчик/девочка): ')
            about = input('Расскажите немного о питомце: ')
            print('Анкета будет выглядеть так:')
            print(f'<{photo_id}>', f'Имя: {name}', f'{gen}', f'Возраст: {age}', f'Характер: {about}', sep='\n')
            print()
            x = input('Добавить питомца? (Да/Нет): ')
            if x.lower() == 'да':
                db_table_val(id=id, name=name, pet=pet, osob=osob, photo_id=photo_id, age=age, gen=gen, about=about)
                print(f'Питомец {name} успешно добавлен.', '', '', sep='\n')

        elif comm == "=":
            name_an = input('Введите имя:  ')
            id_an = 2
            cur.execute('''UPDATE Animals SET id = ? WHERE name = ?''', (id_an, name_an))
            con.commit()
            print(f'Статус питомца {name_an} изменён на "нашёл хозяина".')
            print()
