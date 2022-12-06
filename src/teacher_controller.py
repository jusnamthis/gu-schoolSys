from views import teacher_view as tv
import file_handler as fl


def on_user_authorized():
    act = tv.get_user_action()

    if act == tv.GIVE_A_GRADE_ACT_ID:
        on_grade_act_chosen()
    elif act == tv.ADD_A_STUDENT_ACT_ID:
        on_add_student_act_chosen()
    else:
        on_user_authorized()


def on_grade_act_chosen():
    class_id = tv.get_class(fl.get_classes())

    cl_info = fl.get_surnames(class_id)

    surnames = [surn for surn in cl_info.keys()]
    student_surname_id = tv.choose_student_by_surname(surnames)
    student_surname = surnames[student_surname_id]

    subjects = list(cl_info[student_surname].keys())
    subj_id = tv.choose_subj(subjects)
    subj = subjects[subj_id]

    mark = tv.get_mark(student_surname, subj)

    cl_info[student_surname][subj].append(mark)

    fl.dump_cl_info(class_id, cl_info)


def on_add_student_act_chosen():
    student_name = tv.get_student_surname().lower()
    student_class = tv.get_student_class_to_add()

    fl.dump_student(student_class, student_name)