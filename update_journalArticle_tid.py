#update the journal article collection in TW
__author__ = "Rahul Kashyap"
__maintainer__ = "Rahul Kashyap"
__email__ = "rahulkashyap411@gmail.com"

"""scans the directory _all_papers_Refs/<year> under each year and checks if this tiddler has already been created and exists in the directory old_all_papers_Refs_tiddlers and if it's new creates new tiddlers in new_all_papers_Refs_tiddlers. 
NOTE: it doesnot check if the tiddler has been already exported in the TW. So, after importing the tiddlers, copy them into old directory for next time succesful update
"""

import glob
import os
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-t", "--tags", dest="tag_list", nargs='+',help="tag list",required=False)

args = parser.parse_args()
tag_list=args.tag_list




papers=glob.glob("_all_papers_Refs/*/*.pdf")
print('total number of papers:',len(papers))

for f in papers:
    #print(f)
    os.rename(f, f.replace(' ', '_'))  #removes spaces from filenames

papers=glob.glob("_all_papers_Refs/*/*.pdf")
print('total number of papers:',len(papers))

for f in papers:
    #print(f)
    os.rename(f, f.replace(' ', '_'))  #removes spaces from filenames



for f in papers:
    #print(f)
    #os.rename(f, f.replace(' ', '_'))  #removes spaces from filenames
    filename = f.split('_all_papers_Refs/')[1].split('/')[1].split('.pdf')[0]
    #print("[ext[%s|%s]]\n"%(filename,f))

    year=f.split('_all_papers_Refs/')[1].split('/')[0]
    #print(year)
    if (os.path.isfile('old_all_papers_Refs_tiddlers/%s.tid'%filename) == False):
        print('---- creating tiddler for this file -----')
        print(filename)
        with open('new_all_papers_Refs_tiddlers/%s.tid'%filename, 'w+') as the_file:
                the_file.write('created: 20190906064520623\n')
                the_file.write('creator: rkashyap\n')
                the_file.write('modified: 20190906064638137\n')
                the_file.write('modifier: rkashyap\n')
                the_file.write('literaturetype: JournalArticle\n')
                the_file.write('year: %s\n'%year)
                the_file.write('tags: %s\n'%' '.join(tag_list))
                the_file.write('title: %s\n'%filename.split('.pdf')[0])
                the_file.write('type: text/vnd.tiddlywiki\n')
                the_file.write('\n')
                the_file.write('[ext[%s|%s]]'%(filename,f))
                the_file.write('(<$appear show=[[*,|%s]]myNotes Notes>'%filename)
                the_file.write('\n')
                the_file.write('\n')
                the_file.write('</$appear>)')

        print('copy this .tid files to your TW ONLY then move them to old_all_papers_Refs_tiddlers')
