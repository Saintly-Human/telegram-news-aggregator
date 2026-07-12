from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

def categories_kb(categories_list):
    kb = InlineKeyboardBuilder()

    for category in categories_list:
        kb.add(InlineKeyboardButton(text=category['name'], callback_data=f'category:{category['name']}'))
    kb.adjust(2)
    return kb.as_markup()

def posts_paginated_kb(posts_list, category_name, page_number=1, start = 0, finish = 5):
    kb = InlineKeyboardBuilder()

    r = []
    for i, el in enumerate(posts_list):
        el['id'] = i
        r.append(el)
    total_pages = round(len(posts_list) / 5)

    for post in r[start:finish]:
        print(post)
        kb.add(InlineKeyboardButton(text=post['title'], callback_data=f'post:{post["id"]}:{category_name}'))

    kb.adjust(1)

    kb.row(
        InlineKeyboardButton(text='<', callback_data=f'prev:{page_number}:{start}:{finish}:{category_name}'),
        InlineKeyboardButton(text=f'{page_number}/{total_pages}', callback_data='pages'),
        InlineKeyboardButton(text='>', callback_data=f'next:{page_number}:{start}:{finish}:{total_pages}:{category_name}')
    )
    kb.row(InlineKeyboardButton(text='На гланую', callback_data='home'))
    return kb.as_markup()