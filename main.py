import time
def expression(tokens):
    if not tokens:
        raise ValueError("Пустое выражение")
    if tokens[0].isalpha():  # Проверка на букву
        term(tokens)
        if tokens and tokens[0] in ('-', '+'):  # Проверка на оператор
            operator = tokens.pop(0)  # Сохраняем оператор
            expression(tokens)  # Рекурсивно вызываем выражение
    elif tokens[0] == '(':
        term(tokens)
    else:
        raise ValueError("Ошибка в выражении")


def term(tokens):
    if not tokens:
        raise ValueError("Пустое терм")
    if tokens[0].isalpha():  # Проверка на букву
        atom(tokens)
    elif tokens[0] == '(':  # Проверка на открывающую скобку
        tokens.pop(0)  # Убираем '('
        expression(tokens)
        if tokens and tokens[0] == ')':  # Проверка на закрывающую скобку
            tokens.pop(0)
        else:
            raise ValueError("Ожидалась ')'")
    else:
        raise ValueError("Ошибка в терме")


def atom(tokens):
    if not tokens:
        raise ValueError("Пустое атом")
    if tokens[0].isalpha():  # Проверка на букву
        tokens.pop(0)  # Убираем текущий символ
    else:
        raise ValueError("Ожидался атом")


def parse_expression(input_str):
    tokens = list(input_str.replace(" ", ""))  # Разбиваем строку на символы
    try:
        expression(tokens)
        if tokens:  # Если остались непрочитанные символы
            raise ValueError("Лишние символы в выражении")
        print("Выражение корректно")
    except ValueError as e:
        print(f"Ошибка: {e}")


# Пример работы программы
if __name__ == "__main__":
    input_str = input("Введите выражение: ")
    parse_expression(input_str)
    time.sleep(5)