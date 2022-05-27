import input_functions
import recording_functions

def surname():
    data = input_functions.get_surname()
    recording_functions.write_surname(data)
    return data

def name():
    data = input_functions.get_name()
    recording_functions.write_name(data)
    return data

def number():
    data = input_functions.get_number()
    recording_functions.write_namber(data)
    return data

def description():
    data = input_functions.get_description()
    recording_functions.write_description(data)
    return data
