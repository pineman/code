"""
Generate icon caches on linux.
"""


import os


icon_path = '/home/pineman/.icons/'
icon_dirs = [f for f in os.listdir(icon_path) if os.path.isdir(icon_path + f)]

for d in icon_dirs:
    os.system('gtk-update-icon-cache -f -t ' + os.path.join(icon_path, d))
