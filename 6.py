def int_func(user_word):
    '''
    Принимает текст из маленьких букв
    Возвращает с первой прописной

    'text' → 'Text'
    '''
    user_word = user_word[0].upper() + user_word[1:]
    return user_word


word_list = ['text', 'text', 'text']
print(int_func('text '))
print(*list(map(lambda x: int_func(x), word_list)))