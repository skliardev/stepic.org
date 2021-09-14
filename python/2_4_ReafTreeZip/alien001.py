import os
import zipfile

pydirs = list()

with zipfile.ZipFile('main.zip', 'r') as zip:
    for zip_path in zip.namelist():
        if os.path.dirname(zip_path) not in pydirs and os.path.basename(zip_path).endswith('.py'):
            pydirs.append(os.path.dirname(zip_path))

print('\n'.join(sorted(pydirs)))
