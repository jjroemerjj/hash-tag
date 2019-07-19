from my_directory.json_iris import *


if __name__ == '__main__':

    file_path = "data/iris.data"

    with open(file_path, 'r', encoding="utf-8") as f:
        working_data_set: list = [edit_line(line) for line in f]
    working_data_set: list = [to_good_type(line) for line in working_data_set]

    print(working_data_set)

    data = working_data_set
    attributes = ['petal length', 'petal width', 'sepal length', 'sepal width', 'species']
    save_file_path = 'data/iris.json'
    serialize_json(data, save_file_path, attributes)

