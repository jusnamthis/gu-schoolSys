from os import listdir
import pickle

classes = []


def get_classes():
    """
    Check 'school_classes' dir and returns the names of files inside.
    """
    for cl in listdir("school_classes"):
        index = cl.index('.')
        classes.append(cl)
    return classes


def get_surnames(cl_id):
    cl_file_name = classes[cl_id]
    with open(f'school_classes/{cl_file_name}', 'rb') as file:
        cl_data = pickle.load(file)
    return cl_data


def dump_cl_info(cl_id, cl_info):
    cl_file_name = classes[cl_id]
    with open(f'school_classes/{cl_file_name}', 'wb') as file:
        cl_data = pickle.dump(cl_info, file)
    return cl_data


def dump_student(cl_name, student_name):
    with open(f'school_classes/{cl_name}.pickle', 'rb') as file:
        cl_data = pickle.load(file)

    cl_data[student_name] = {}

    with open(f'school_classes/{cl_name}.pickle', 'wb') as file:
        pickle.dump(cl_data, file)