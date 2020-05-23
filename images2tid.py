
#Converting set of images in a directory to .tid file
__author__ = "Rahul Kashyap"
__maintainer__ = "Rahul Kashyap"
__email__ = "rahulkashyap411@gmail.com"

"""makes a tiddler with links to all images in a directory and tags as given"""
import re, os, glob, codecs

from argparse import ArgumentParser
import numpy as np
from natsort import natsorted, ns
#import html2text

parser = ArgumentParser()
parser.add_argument("-o", "--out_file", dest="out_file",help="write report to FILE", metavar="FILE")
parser.add_argument("-t", "--tags", dest="tag_list", nargs='+',help="tag list")
parser.add_argument("-d", "--import_date", dest="import_date",help="import date")
#parser.add_argument("-w", "--image_width", dest="image_width",help="image width")
parser.add_argument("-l", "--img_loc", dest="img_loc",
                    help="new image location directory wrt TW file", default="images", required=True)
parser.add_argument("-q", "--quiet",
                    action="store_false", dest="verbose", default=True,
                    help="don't print status messages to stdout")

args = parser.parse_args()
#html_file=args.html_file
out_file=args.out_file
img_loc=args.img_loc
tag_list=args.tag_list
#image_width=args.image_width
import_date=args.import_date

print(img_loc)
types = ('*.png', '*.jpg', '.gif') # the tuple of file types
files = []
for t in types:
    files.extend(glob.glob(img_loc+'/'+t))
    
print(files)

files=natsorted(files, alg=ns.IGNORECASE)
print(len(files))
image_width="100%"

filename=out_file+'.tid'
with open(filename, 'w+') as the_file:
    the_file.write('created: 20190410063109351\n')
    the_file.write('modified: 20190412110038283\n')
    the_file.write('tags: %s\n'%' '.join(tag_list))
    the_file.write('import_date: %s\n'%import_date)
    the_file.write('title: %s\n'%out_file)
    the_file.write('type: text/vnd.tiddlywiki\n')

    for f in files:
        os.rename(f, f.replace(' ', '_'))

        the_file.write('\n')
        the_file.write("[img[%s]]\n"%f)
        the_file.write("[ext[%s|%s]]([ext[loc|%s]])"%(f,f,img_loc))
        the_file.write('\n')
    
