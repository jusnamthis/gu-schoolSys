from views import student_view as sv
import file_handler as fl


def on_user_authorized():
    get_marks()


def get_marks():
    surname = sv.get_surname().lower()
    class_id = sv.get_class(fl.get_classes())

    cl_info = fl.get_surnames(class_id)

    student_info = cl_info[surname]

    sv.show_marks(student_info)
