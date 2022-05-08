import os

try:
    for f in os.scandir('sqls/'):
        if f.is_file() and f.path.split('.')[-1].lower() == 'sql':
            print(f.path)
except ValueError:
    print(1)

# for f in os.scandir('sql/'):
#     if f.is_file() and f.path.split('.')[-1].lower() == 'sql':
#         with open(f.path, 'r') as csvfile:
#             print(csvfile.read())

# import re
# import os
# import pprint
#
# if __name__ == "__main__":
#     path = 'sql/'
#     files = os.listdir(path)
#     reg_table = r'(?:from|join|apply)\s+' \
#                 r'(?!\w+\s*\()' \
#                 r'([\w\[\]`]*\.?[\w\[\]`]*\.?[\w\[\]`]*\.?[\w\[\]#`]+)' \
#                 r'((?:\s*\,\s*[\w\[\]`]*\.?[\w\[\]`]*\.?[\w\[\]`]*\.?[\w\[\]#`]+)*)'
#     reg_execute = r'exec\s+([\w\[\]`]*\.?[\w\[\]`]*\.?[\w\[\]`]*\.?[\w\[\]`]+)'
#     reg_procedure = r'(?:alter|create)\s+(?:procedure|proc)\s+' \
#                     r'([\w\[\]`]*\.?[\w\[\]`]*\.?[\w\[\]`]*\.?[\w\[\]`]+)'
#     reg_delete = r'[\s\[\]`]'
#
#     for file in files:
#         temp_tables = {
#             'file': file,
#             'tables': [],
#             'executes': [],
#             'procedures': []
#         }
#
#         file_text = open(path + file, 'r').read()
#
#         for i in re.findall(reg_table, file_text, re.IGNORECASE):
#             if i[0].find('#') == -1:
#                 temp_name = re.sub(reg_delete, '', i[0]).split('.')
#                 temp_dist = {
#                     'name_all': re.sub(reg_delete, '', i[0]),
#                     'server': temp_name[0] if len(temp_name) == 4 else None,
#                     'database': temp_name[1] if len(temp_name) == 4 else temp_name[0] if len(temp_name) == 3 else None,
#                     'schema': temp_name[2] if len(temp_name) == 4 else temp_name[1] if len(temp_name) == 3 else temp_name[
#                         0] if len(temp_name) == 2 else None,
#                     'table': temp_name[3] if len(temp_name) == 4 else temp_name[2] if len(temp_name) == 3 else temp_name[
#                         1] if len(temp_name) == 2 else temp_name[0]
#                 }
#                 temp_tables['tables'].append(temp_dist)
#             if i[1] != '':
#                 for j in re.sub(reg_delete, '', i[1]).split(','):
#                     if j != '' and j.find('#') == -1:
#                         temp_name = j.split('.')
#                         temp_dist = {
#                             'name_all': j,
#                             'server': temp_name[0] if len(temp_name) == 4 else None,
#                             'database': temp_name[1] if len(temp_name) == 4 else temp_name[0] if len(
#                                 temp_name) == 3 else None,
#                             'schema': temp_name[2] if len(temp_name) == 4 else temp_name[1] if len(temp_name) == 3 else
#                             temp_name[0] if len(temp_name) == 2 else None,
#                             'table': temp_name[3] if len(temp_name) == 4 else temp_name[2] if len(temp_name) == 3 else
#                             temp_name[1] if len(temp_name) == 2 else temp_name[0]
#                         }
#                         temp_tables['tables'].append(temp_dist)
#         for i in re.findall(reg_execute, file_text, re.IGNORECASE):
#             if i.find('#') == -1:
#                 temp_name = re.sub(reg_delete, '', i).split('.')
#                 temp_dist = {
#                     'name_all': re.sub(reg_delete, '', i),
#                     'server': temp_name[0] if len(temp_name) == 4 else None,
#                     'database': temp_name[1] if len(temp_name) == 4 else temp_name[0] if len(temp_name) == 3 else None,
#                     'schema': temp_name[2] if len(temp_name) == 4 else temp_name[1] if len(temp_name) == 3 else temp_name[
#                         0] if len(temp_name) == 2 else None,
#                     'execute': temp_name[3] if len(temp_name) == 4 else temp_name[2] if len(temp_name) == 3 else temp_name[
#                         1] if len(temp_name) == 2 else temp_name[0]
#                 }
#                 temp_tables['executes'].append(temp_dist)
#         for i in re.findall(reg_procedure, file_text, re.IGNORECASE):
#             if i.find('#') == -1:
#                 temp_name = re.sub(reg_delete, '', i).split('.')
#                 temp_dist = {
#                     'name_all': re.sub(reg_delete, '', i),
#                     'server': temp_name[0] if len(temp_name) == 4 else None,
#                     'database': temp_name[1] if len(temp_name) == 4 else temp_name[0] if len(temp_name) == 3 else None,
#                     'schema': temp_name[2] if len(temp_name) == 4 else temp_name[1] if len(temp_name) == 3 else temp_name[
#                         0] if len(temp_name) == 2 else None,
#                     'procedure': temp_name[3] if len(temp_name) == 4 else temp_name[2] if len(temp_name) == 3 else
#                     temp_name[1] if len(temp_name) == 2 else temp_name[0]
#                 }
#                 temp_tables['procedures'].append(temp_dist)
#
#     pprint.pprint(temp_tables)
