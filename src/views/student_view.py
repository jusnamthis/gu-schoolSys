GET_STUDENT_INFO_ACT_ID = 1
MIN_CLASS = 1
MAX_CLASS = 11


def get_class(cls):
    for i in range(len(cls)):
        index = cls[i].index('.')
        print('{}. {}'. format(i + 1, cls[i][:index]))
    cl = int(input('Enter your class: ')) - 1
    return cl


def validate_class_input(cl):
    if not cl.isdigit():
        return get_class()
    elif not MIN_CLASS <= int(cl) <= MAX_CLASS:
        return get_class()
    return int(cl)


def get_surname():
    return input('Enter your surname: ')


def show_marks(student_info):
    for key, value in student_info.items():
        print(key, *value)
