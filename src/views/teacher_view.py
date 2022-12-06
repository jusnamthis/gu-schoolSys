GIVE_A_GRADE_ACT_ID = 1
ADD_A_STUDENT_ACT_ID = 2

CLASS_REQUEST_MSG = 'Enter students class by index: '


def get_user_action():
    act = input('Choose the action:\n\t1. give a grade;\n\t2. add a student.: ')
    return validate_action(act)


def validate_action(act):
    if not act.isdigit():
        return get_user_action()
    else:
        act_id = int(act)
        if act_id != GIVE_A_GRADE_ACT_ID and act_id != ADD_A_STUDENT_ACT_ID:
            return get_user_action()

    act = int(act)
    
    if act == GIVE_A_GRADE_ACT_ID:
        return GIVE_A_GRADE_ACT_ID

    if act == ADD_A_STUDENT_ACT_ID:
        return ADD_A_STUDENT_ACT_ID


def get_student_class_to_add():
    return input('Enter student class: ')


def get_student_surname():
    return input('Enter student surname: ')


def get_class(cls):
    """
    cls = List
    shows the classes contains in cls list
    get index of class and returns it
    """
    for i in range(len(cls)):
        index = cls[i].index('.')
        print('{}. {}'.format(i + 1, cls[i][:index]))
    return int(input(CLASS_REQUEST_MSG)) - 1


def choose_student_by_surname(surnames):
    for i in range(len(surnames)):
        print('{}. {}'.format(i + 1, surnames[i].capitalize()))
    return int(input('Choose the student from the list above: ')) - 1


def choose_subj(subjs):
    for i in range(len(subjs)):
        print('{}. {}'.format(i + 1, subjs[i].capitalize()))
    return int(input('Choose the subj from the list above: ')) - 1


def get_mark(name, subj):
    return int(input(f'Enter the grade of {name.capitalize()} in {subj.capitalize()}: '))
