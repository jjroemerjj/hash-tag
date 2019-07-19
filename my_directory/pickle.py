from my_directory.employe import Employee

import pickle, json


def serialize_pickle(data_to_serialize, file_path):
    with open(file_path, 'wb') as f:
        pickle.dump(data_to_serialize, f)


def deserialize_pickle(file_path):
    with open(file_path, 'rb') as f:
        employees = pickle.load(f)
        return employees


def try_serialize_json():
    kowalska = Employee("Magdalena", "Kowalska")
    kowalski = Employee('Jan', 'Kowalski')
    employees = [kowalska, kowalski]
    with open('employees.json', 'w') as f:
        json.dump(employees, f)


def serialize_json():
    employees = {
        'kowalska': {"first_name": "magdalena", "Last_name": "kowalska"},
        'kowalski': {'first_name': 'jan', 'last_name': 'kowalski'}}
    with open ('data/employees.json', 'w') as f:
        json.dump(employees, f)
