from aiogram import Bot, types
from aiogram.types import CallbackQuery, Message
import sqlite3
from core.keyboards.inline import select_command2, select_command3
from core.keyboards.reply import reply_keyboard2, reply_keyboard, reply_keyboard3, reply_keyboard4


filter_bd = []
sp_pet = []
sp_pet2 = []
count2 = 0
count = 0


async def select_pet(call: CallbackQuery, bot: Bot):
    if call.data == "1_dog":
        answer = f"Вы выбрали собаку."
        filter_bd.append("dog")
    elif call.data == "1_cat":
        answer = f"Вы выбрали кошку."
        filter_bd.append("cat")
    await call.message.answer(f"{answer} Выберите:", reply_markup=select_command2)
    await call.message.edit_reply_markup()
    await call.answer()


async def select_pet2(call: CallbackQuery, bot: Bot):
    if call.data == "2_feature":
        answer = f"Вы выбрали питомца с особенностями."
        filter_bd.append(1)
    elif call.data == "2_nofeature":
        answer = f"Вы выбрали питомца без особенностей."
        filter_bd.append(0)
    elif call.data == "2_dt_matter":
        answer = f"Вы выбрали 'Не имеет значения'."
        filter_bd.append(2)
    await call.message.answer(f"{answer} Выберите пол питомца:", reply_markup=select_command3)
    await call.message.edit_reply_markup()
    await call.answer()


async def select_pet3(call: CallbackQuery, bot: Bot):
    if call.data == "3_women":
        answer = f"Вы выбрали питомца женского пола."
        filter_bd.append("девочка")
    elif call.data == "3_men":
        answer = f"Вы выбрали питомца мужского пола."
        filter_bd.append("мальчик")
    elif call.data == "3_dt_matter":
        answer = f"Вы выбрали 'Не имеет значения'."
        filter_bd.append(2)
    await call.message.answer(answer)
    await call.message.edit_reply_markup()
    await call.message.answer(f"<b>Мы поняли какого питомца вы хотите, сейчас выведем список животных"
                              f" </b>", parse_mode="HTML", reply_markup=reply_keyboard3)
    global sp_pet
    sp_pet = selekt()


def selekt():
    con = sqlite3.connect('./data/Vernost_db.db')
    cur = con.cursor()
    global filter_bd
    pet = filter_bd[0]
    id_an = 1
    if filter_bd[1] == 2:
        if filter_bd[2] == 2:
            sp_pet = cur.execute('''SELECT photo_id, name, gen, age, about FROM Animals WHERE id = ?
             AND Type = ?''', (id_an, pet)).fetchall()
            filter_bd = []
            return sp_pet

        else:
            gen = filter_bd[2]
            sp_pet = cur.execute('''SELECT photo_id, name, gen, age, about FROM Animals WHERE id = ? AND Type = ? AND 
            gen = ?''', (id_an, pet, gen)).fetchall()
            filter_bd = []
            return sp_pet

    else:
        osob = filter_bd[1]
        if filter_bd[2] == 2:
            sp_pet = cur.execute('''SELECT photo_id, name, gen, age, about FROM Animals WHERE id = ? AND Type = ? AND 
            osob = ?''', (id_an, pet, osob)).fetchall()
            filter_bd = []
            return sp_pet

        else:
            gen = filter_bd[2]
            sp_pet = cur.execute('''SELECT photo_id, name, gen, age, about FROM Animals WHERE id = ? AND Type = ? AND 
            osob = ? AND gen = ?''', (id_an, pet, osob, gen)).fetchall()
            filter_bd = []
            return sp_pet


def select_nayden():
    con = sqlite3.connect('./data/Vernost_db.db')
    cur = con.cursor()
    sp_pet_ = cur.execute('''SELECT photo_id, name FROM Animals WHERE id = ?''', "2").fetchall()
    #  Здесь выводится имя изображения и имя питомца
    return sp_pet_


async def output_pets(message: Message):
    global sp_pet
    global count
    global filter_bd
    prov = True
    if len(sp_pet) != 0:
        photo, name, gen, age, about = sp_pet[count]
        count += 1
        file_path = f"./data/{photo}"
        print(file_path)
        await message.answer_photo(photo=types.FSInputFile(path=file_path), caption=f"Кличка: {name}\nПол: {gen}\n"
                                   f"Возраст: {age}\nКраткая информация о питомце: {about}",
                                   reply_markup=reply_keyboard2)
    else:
        await message.answer("Простите, мы не нашли питомцев по вашим параметрам...", reply_markup=reply_keyboard)
        prov = False
    if count >= len(sp_pet) and prov:
        filter_bd = []
        sp_pet = []
        count = 0
        await message.answer("Вы пересмотрели всех питомцев.", reply_markup=reply_keyboard)


async def all_pets(message: Message):
    global sp_pet2
    global count2
    sp_pet2 = select_nayden()
    prov2 = True
    if len(sp_pet2) != 0:
        photo2, name2 = sp_pet2[count2]
        count2 += 1
        file_path2 = f"./data/{photo2}"
        print(file_path2)
        await message.answer_photo(photo=types.FSInputFile(path=file_path2), caption=f"{name2}",
                                   reply_markup=reply_keyboard4)
    else:
        prov2 = False
        await message.answer("Простите, найденных питомцев пока что нет.", reply_markup=reply_keyboard)
    if count2 >= len(sp_pet2) and prov2:
        sp_pet2 = []
        count2 = 0
        await message.answer("Это питомцы которые уже смогли обрести свой дом❤", reply_markup=reply_keyboard)
