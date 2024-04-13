import os
import time
import zipfile

source = ['C:\\Users\\Dgl\\Desktop\\НАТАША', 'C:\\Users\\Dgl\\Desktop\\edik']

target_dir = "D:\\Edo`s Projects\\python"

target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.rar'



zip_command = "rar a {0} {1}".format(target, ' '.join(source))

if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')