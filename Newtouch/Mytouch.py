#!/usr/bin/env python
# coding:utf-8
import os
import argparse

print 'current dir ====> {0}\n{1}'.format(os.getcwd(), '*'*40)

parser = argparse.ArgumentParser(description='A script for add script header message')
parser.add_argument('newfile')

args = parser.parse_args()

header_msg = {
    'py': '#!/usr/bin/env python\n# coding:utf-8\n',
    'c': '#include <stdio.h>\n'
}

if os.path.isfile(os.getcwd()+'/'+args.newfile):
    print '\tfile already exists...'
else:
    if len(args.newfile.split('.')) == 2:
        newfile_type = args.newfile.split('.')[-1]

        if newfile_type in header_msg:
            with open(args.newfile, 'w') as f:
                print '\tadding header msg...'
                f.write(header_msg[newfile_type])
            msg = 'created %s' % args.newfile
            print msg.center(40, '*')
        else:
            os.system('touch %s' % args.newfile)
            print '\tcreated ', args.newfile
    else:
        temp = open(args.newfile, 'w')
        temp.close()
        print '\tcreated ', args.newfile
