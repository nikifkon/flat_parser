import csv


class DataCleaner:
    """
    Transform values in csv file to specific type.

    Usage:
    cleaner = DataCleaner(path='test.csv', file_type='csv')
    cleaner.clean_price()
    cleaner.write_result()
    """
    def __init__(self, path: str = None, file_type: str = 'csv'):
        if path is None:
            raise FileNotFoundError('You must provide path to file')
        self.path = path
        self.file_type = file_type
        with open(path, encoding='utf-8') as file:
            reader = csv.DictReader(file)
            self.keys = set(reader.fieldnames)
            if self.keys is None:
                print(f'{path} is not valid or empty csv file')
                self.keys = set()
            self.row = list(reader)

    def write_result(self, path: str = None) -> str:
        if path is None:
            path_without_ext = ''.join(self.path.split('.')[:-1])
            path = f'{path_without_ext}_cleaned.{self.file_type}'
        with open(path, 'w', encoding='utf-8') as file:
            writter = csv.DictWriter(file, fieldnames=self.keys)
            writter.writeheader()
            writter.writerows(self.row)
        return path

    def clean_price(self):
        for row in self.row:
            if 'price' in row:
                row['price'] = row['price'].replace('.', '')

    def clean_floors(self):
        for row in self.row:
            if 'floors' in row:
                try:
                    row['floor'] = row['floors'].split('/')[0].strip()
                    row['floor_count'] = row['floors'].split('/')[1].strip()
                    self.keys.update(('floor', 'floor_count'))
                except IndexError:
                    pass
                finally:
                    row.pop('floors', None)
        self.keys.remove('floors')