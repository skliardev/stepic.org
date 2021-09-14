import zipfile
import os
import shutil
with zipfile.ZipFile('main.zip', 'r') as inzip, open('out.txt', 'w') as ouf:
    inzip.extractall()
    lst = []
    for path, dirs, files in sorted(os.walk('main')):
        if any('.py' in string for string in files):
            ouf.write(path + '\n')
    ouf.flush()
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'main')
    shutil.rmtree(path)
