from os.path import join, getsize
import os
import shutil
import fnmatch
import sys

def splitdir(dir,pattern,slices):
   size = 0L
   dirdict={}
   cnt=0;
   
   for i in range(slices):
      if os.path.isdir(join(dir,'slice'+str(i+1))) != True:
          os.mkdir(join(dir,'slice'+str(i+1)))

   for root, dirs, files in os.walk(dir):
      for name in files:
        if fnmatch.fnmatch(name,pattern) :
	    dirdict[join(root,name)]=getsize(join(root,name))
   for file,size in sorted( dirdict.items(), key=lambda d: d[1],reverse=True):
       shutil.move(file,join(dir,'slice'+str(cnt%slices+1)))
       cnt+=1
      
      

if __name__ == '__main__':
   if len(sys.argv) != 4:
	print "Split files under some path into some slice"
	print "Usage:	dir  pattern slicenum"
	print "Example: /tmp 'test*' 5 [will split all files under /tmp/test* into slice[1-5] ]"
	exit(1)
   splitdir(sys.argv[1],sys.argv[2],int(sys.argv[3]))

