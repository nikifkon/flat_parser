import csv


def binarized(input_file, output_file=None, variables=None):
    if variables is None:
        print('vars for binarized is empty')
    binary = Binarized(input_file, file_type='csv')
    binary.set_vars(variables)
    result_path = binary.write_result(output_file)
    return result_path


class Binarized:
    """
    For each nominal variables(in csv file) that taking more then
    two value, create new binary variable.

    Usage:
    binary = Binarized(path='test.csv', file_type='csv')
    list = ['var1', 'var2']
    binary.set_vars(list)
    binary.write_result(path='output.csv')
    """
    def __init__(self, path: str = None, file_type: str = 'csv'):
        if path is None:
            raise FileNotFoundError('You must pass input_file to Binarized')
        self.path = path
        self.file_type = file_type
        self.vars = None
        with open(path, encoding='utf-8') as file:
            reader = csv.DictReader(file)
            if reader.fieldnames is None:
                print(f'{path} is not valid or empty csv file')
                self.keys = set()
            else:
                self.keys = set(reader.fieldnames)
            self.data = list(reader)

    def set_vars(self, _vars: list):
        self.vars = _vars

    def write_result(self, path: str = None) -> str:
        if path is None:
            path_without_ext = ''.join(self.path.split('.')[:-1])
            path = f'{path_without_ext}_binarized.{self.file_type}'
        new_keys = self.binary_data()
        self.keys.update(new_keys)
        with open(path, 'w', encoding='utf-8') as file:
            writter = csv.DictWriter(file, fieldnames=self.keys, restval=0)
            writter.writeheader()
            writter.writerows(self.data)
        return path

    def binary_data(self) -> set:
        new_keys = set()
        for flat in self.data:
            for var in self.vars:
                if var in flat:
                    value = flat[var]
                    if value == '':
                        continue
                    new_keys.add(value)
                    flat[value] = 1
        return new_keys
