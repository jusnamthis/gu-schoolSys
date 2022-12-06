from views import view
import teacher_controller as tc
import student_controller as sc


def on_app_started():
    authorize_user(view.authenticate())


def authorize_user(role):
    if role == view.STUDENT_ROLE_ID:
        sc.on_user_authorized()
    else:
        tc.on_user_authorized()


if __name__ == '__main__':
    on_app_started()