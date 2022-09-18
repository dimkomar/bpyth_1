import os
import time

# 1. files that need to copy added to list
source = ['"/Users/dmitriyko/Documents/files/A_EDU/python/folder_1"',
          '"/Users/dmitriyko/Documents/files/A_EDU/python/folder_2"']

# 2. Dump copies should be saved in main catalog
target_dit = '/Users/dmitriyko/Documents/files/A_EDU/python/main_dir'

# 3. Files goes to archive
# 4. Current date is used for name of sub_folder in main catalog
today = target_dit + os.sep + time.strftime('%Y%m%d')
# time name for zip
now = time.strftime('%H%M%S')

# ask user comment for name file
comment = input('Input comment -->')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '.zip' + \
             comment.replace(' ', '_') + '.zip'

# create catalog if nit exist
if not os.path.exists(today):
    os.makedirs(today)
    print('Catalog crated')

# 5. used zip_command to move file to zip-archive
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))


