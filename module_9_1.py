def apply_all_func(int_list, *functions):
    
    print('*' * 20)
    
    results = dict()
    
    for func in functions:
        try:
            results[func.__name__] = func(int_list)
        except Exception as exc:
            print(f'Ошибка при вызове функции {func.__name__}: '
                  f'класс ошибки - {exc.__class__}; '
                  f'описание ошибки - {exc.args}')
        
    return results


print(f'Результат функции {apply_all_func.__name__}: '
      f'{apply_all_func([6, 20, 15, 9], max, min)}')
print(f'Результат функции {apply_all_func.__name__}: '
      f'{apply_all_func([6, 20, 15, 9], len, sum, sorted)}')
