from __future__ import print_function
import sys

def gen_res_list(aspect_x, aspect_y, max_x_res, max_y_res=None):
    ratio = float(aspect_x) / float(aspect_y)
    if not max_y_res:
        max_y_res = max_x_res
    output = []
    for x in range(max_x_res + 1):
        y = float(x) / ratio
        if y % 1 == 0:
            output.append((x, int(y)))
        if y >= max_y_res:
            break
    return output

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('aspect.py usage: python aspect.py <aspect_x> <aspect_y> <max_x_res> <max_y_res>')
    else:
        a_x = int(sys.argv[1])
        a_y = int(sys.argv[2])
        mxr = int(sys.argv[3])
        myr = 0
        if not myr:
            myr = mxr
        if len(sys.argv) > 4:
            myr = sys.argv[4]
    result = gen_res_list(a_x, a_y, mxr, myr)
    print('Valid Resolutions for {}:{} up to {}x{}'.format(a_x, a_y, mxr, myr))
    for r in result:
        print('{},{}'.format(r[0], r[1]))
