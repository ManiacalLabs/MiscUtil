from __future__ import print_function
import sys
import os
import shutil
import time
from datetime import datetime

print(sys.argv)
if len(sys.argv) < 3:
    print('Not enough arguments! Usage: imgport.py <in_dir> <out_dir>')
    sys.exit(1)

in_dir = sys.argv[1]
out_dir = sys.argv[2]

if not os.path.isdir(in_dir):
    print('{} is not a directory!'.format(in_dir))

if not os.path.isdir(out_dir):
    print('{} is not a directory!'.format(out_dir))

img_ext = ('BMP', 'GIF', 'JPEG', 'JPG', 'PNG', 'NEF', 'DNG')
vid_ext = ('WEBM', 'MKV', 'AVI', 'WMV', 'MOV', 'MP4', 'M4P', 'MPG', 'MP2', 'MPEG', 'M4V')
exts = img_ext + vid_ext

copy_total = 0

def ensure_dir_exists(mon, day, year):
    base = os.path.join(out_dir, year)
    if not os.path.isdir(base):
        print('Creating directory: ' + base)
        os.mkdir(base)
    sub = os.path.join(base, mon + '-' + day)
    if not os.path.isdir(sub):
        print('Creating directory: ' + sub)
        os.mkdir(sub)
    return sub

def copy_file(root, filename):
    global copy_total
    src = os.path.join(root, filename)
    mtime = datetime.fromtimestamp(os.path.getmtime(src))
    dst_dir = ensure_dir_exists(str(mtime.month).zfill(2),
                                str(mtime.day).zfill(2),
                                str(mtime.year).zfill(4))
    dst = os.path.join(dst_dir, filename)
    if os.path.exists(dst):
        print('{} exists. Skipping...'.format(dst.replace(out_dir, '')))
    else:
        stat = os.stat(src)
        size = round(float(stat.st_size) / (1024*1024), 1)
        print('({} MB) {} > {}'.format(size, src.replace(in_dir, ''), dst.replace(out_dir, '')))
        shutil.copy(src, dst)
        copy_total += stat.st_size

for root, _, files in os.walk(in_dir):
    for f in files:
        if f.upper().endswith(exts):
            copy_file(root, f)

print('\nComplete!\n{} MB in total copied'.format(round(float(copy_total) / (1024*1024), 1)))
