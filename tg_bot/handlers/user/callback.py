from aiogram import Router, F, types
from tg_bot.utils import read_json
from tg_bot.keyboards.inline import posts_paginated_kb

router = Router()

@router.callback_query(F.data.startswith('category'))
async def choose_category(callback: types.CallbackQuery):
    print(callback.data)
    _, category_name = callback.data.split(':')
    posts = read_json('tg_bot/data/posts.json')[category_name.strip()]
    print(posts)

    await callback.message.edit_text(f'''
        Выбранная категория: {category_name}
        Кол-во постов: {len(posts)}
    ''', reply_markup=posts_paginated_kb(posts, category_name))

@router.callback_query(F.data.startswith('post'))
async def choose_post(callback: types.CallbackQuery):
    _, post_id, category_name = callback.data.split(':')
    posts = read_json('tg_bot/data/posts.json')[category_name.strip()]
    post = posts[int(post_id)]
    await callback.message.delete()
    try:
        await callback.message.answer_photo(post['img'])
    finally:
        await callback.message.answer(f'''
{post['title']}
{post['full_description']}
{post['date']}
''')

@router.callback_query(F.data.startswith('prev'))
async def prev(callback: types.CallbackQuery):
    _, page_number, start, finish, category_name = callback.data.split(':')

    if int(page_number) == 1:
        return await callback.answer('Вы уже на первой странице', show_alert=True)

    posts = read_json('tg_bot/data/posts.json')[category_name.strip()]

    return await callback.message.edit_reply_markup(
        reply_markup=posts_paginated_kb(
            posts_list=posts,
            category_name=category_name,
            start=int(start) - 5,
            finish=int(finish) - 5,
            page_number=int(page_number) - 1
        )
    )

@router.callback_query(F.data.startswith('next'))
async def next_page(callback: types.CallbackQuery):
    _, page_number, start, finish, total_pages, category_name = callback.data.split(':')

    if int(page_number) == int(total_pages):
        return await callback.answer('Вы уже на последней странице', show_alert=True)

    posts = read_json('tg_bot/data/posts.json')[category_name.strip()]

    return await callback.message.edit_reply_markup(
        reply_markup=posts_paginated_kb(
            posts_list=posts,
            category_name=category_name,
            start=int(start) + 5,
            finish=int(finish) + 5,
            page_number=int(page_number) + 1
        )
    )