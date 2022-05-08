import re#s
import os
from pprint import pprint


class SqlParsing:
    files = []
    reg_table = r'(?:from|join|apply)\s+' \
                r'(?!\w+\s*\()' \
                r'([\w\[\]`]*\.?[\w\[\]`]*\.?[\w\[\]`]*\.?[\w\[\]#`]+)' \
                r'((?:\s*\,\s*[\w\[\]`]*\.?[\w\[\]`]*\.?[\w\[\]`]*\.?[\w\[\]#`]+)*)'
    reg_execute = r'exec\s+([\w\[\]`]*\.?[\w\[\]`]*\.?[\w\[\]`]*\.?[\w\[\]`]+)'
    reg_procedure = r'(?:alter|create)\s+(?:procedure|proc)\s+' \
                    r'([\w\[\]`]*\.?[\w\[\]`]*\.?[\w\[\]`]*\.?[\w\[\]`]+)'
    reg_delete = r'[\s\[\]`]'

    temp_arr = {
        'file': '',
        'tables': [],
        'executes': [],
        'procedures': []
    }

    def __init__(self, path):
        self.path = path
        self.start()

    def list_files(self):
        if os.path.exists(self.path):
            files = os.listdir(self.path)
            for file in files:
                if file.endswith('.sql'):
                    self.files.append(file)
            if len(self.files) > 0:
                return self.files
            else:
                return -2
        else:
            return -1

    def append_temp_tables(self, typ, arr_name, name):
        self.temp_arr[typ + 's'].append({
            'name_all': re.sub(self.reg_delete, '', name),
            'server': arr_name[0] if len(arr_name) == 4 else None,
            'database': arr_name[1] if len(arr_name) == 4 else arr_name[0] if len(arr_name) == 3 else None,
            'schema': arr_name[2] if len(arr_name) == 4 else arr_name[1] if len(arr_name) == 3 else arr_name[0] if len(
                arr_name) == 2 else None,
            typ: arr_name[3] if len(arr_name) == 4 else arr_name[2] if len(arr_name) == 3 else arr_name[1] if len(
                arr_name) == 2 else arr_name[0]
        })

    def asd(self, i, typ):
        if i.find('#') == -1:
            temp_name = re.sub(self.reg_delete, '', i).split('.')
            self.append_temp_tables(typ, temp_name, i)

    def start(self):
        files = self.list_files()
        if files != -1 and files != -2:

            for file in self.files:
                self.temp_arr = {
                    'file': file,
                    'tables': [],
                    'executes': [],
                    'procedures': []
                }

                file_text = open(self.path + file, 'r').read()
                for i in re.findall(self.reg_table, file_text, re.IGNORECASE):
                    self.asd(i[0], 'table')
                    if i[1] != '':
                        for j in re.sub(self.reg_delete, '', i[1]).split(','):
                            self.asd(j, 'table')
                for i in re.findall(self.reg_execute, file_text, re.IGNORECASE):
                    self.asd(i, 'execute')
                for i in re.findall(self.reg_procedure, file_text, re.IGNORECASE):
                    self.asd(i, 'procedure')
        elif files == -1:
            print('Нет папки')
        elif files == -2:
            print('Нет файлов расширения SQL')

    def show_all(self, typ):
        if typ == 'arr':
            pprint(self.temp_arr)

    def show_tables(self, typ):
        if typ == 'arr':
            pprint(self.temp_arr)


if __name__ == "__main__":
    sql = SqlParsing("sql/")
    sql.show_tables('arr')
