import os
import shutil
from modules.ParseFile import ParseFile


def getImgFiles( p_basedir, p_lext ):
	return [ os.path.join(d[0],f) \
			for d in os.walk(p_basedir) \
			for f in d[2]
			if os.path.splitext(f.lower())[1] in p_lext ]

def movetree(p_fpfile,p_dest,p_base):
	if p_fpfile.startswith(p_base):
		fpfile = p_fpfile[len(p_base)+1:]
		relpath = os.path.dirname(fpfile)
		despath = os.path.join(p_dest,relpath)
		if not(os.path.exists(despath)):
			os.makedirs(despath)
		shutil.move(p_fpfile, despath)
	else:
		return False

def batchprocess(p_in, p_out, p_proc, p_lext):
	print ("Retrieving image files from {0}".format(p_in))
	files = getImgFiles(p_in, p_lext)
	for filename in files:
		print ("Processing {0}".format(filename))
		filep = ParseFile(filename,p_out)
		if not filep.exist:
			if not os.path.exists(filep.path):
				print ("Making path {0}".format(filep.path))
				os.makedirs(filep.path)
			source = os.path.join(p_in, filename)
			target = os.path.join(filep.path,filep.name)
			print ("Copyng {0} to {1}".format(source, target))
			shutil.copy2(source, target)
		else:
			print ("File {0} already exists".format(os.path.join(filep.path,filep.name)))

		print ("Moving tree {0} to {1} with base {2}".format( \
			   filename, p_proc, p_in))
		movetree(filename,p_proc,p_in)

