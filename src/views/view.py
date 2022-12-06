STUDENT_ROLE_ID = 1
TEACHER_ROLE_ID = 2


def authenticate():
    user_auth_data = input('Welcome! Are you student(s/student) or teacher(t/teacher): ')
    return validate_authenticate(user_auth_data)


def validate_authenticate(role):
    if role[0] == 's':
        return STUDENT_ROLE_ID
    elif role[0] == 't':
        return TEACHER_ROLE_ID
    else:
        return authenticate()