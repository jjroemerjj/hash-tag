import json


def edit_line(line: str) -> list:
    """ Removes '\n' character from the end of each line

    Splits string into list
    """
    line = line.replace('\n', '')
    line = line.split(',')
    return line


def to_good_type(line: list) -> list:
    """Changes strings from columns 0 - 3 into float numbers

    Last column (flower name) remains unchanged
    """
    for i in range(len(line) - 1):
        line[i] = float(line[i])
    return line


def serialize_json(data: list, file_path: str, attributes: list):
    with open(file_path, 'w') as f:
        for i in range(len(data)-1):
            employees = {
                attributes[0]: data[i][0],
                attributes[1]: data[i][1],
                attributes[2]: data[i][2],
                attributes[3]: data[i][3],
                attributes[4]: data[i][4]
            }
            json.dump(employees, f)
            f.write(',')
            f.write('\n')


