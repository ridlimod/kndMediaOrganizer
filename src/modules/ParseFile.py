import os
import exifread
from modules.FileCompare import filecmp
from modules.ParseExif import ParseExif
import fnmatch

class ParseFile( object ):
	def __init__(self, p_filename, p_outtree = "out" ):
		extension=os.path.splitext( p_filename )[1].lower()
		fh = open( p_filename,"rb" )
		tags = exifread.process_file( fh, details=False )
		fh.close()
		data = ParseExif( tags, p_filename )
		self.path = os.path.join( p_outtree, data.year, data.month, "-".join([data.year,data.month,data.day]) )
		partname = "{0}-{1}-{2}{3}".format(data.timefs,"*", data.model, extension)
		self.exist = False
		cardinal = self._calccardinal( p_filename, partname )
		self.name = partname.replace("*",cardinal)

	def _isin(self, p_filename, l_files):
		isin = False
		for file in l_files:
			if filecmp(p_filename,file):
				isin = True
				break
		return isin

	def _calccardinal(self, p_filename, p_wildcard):
		if os.path.exists(self.path):
			files = os.listdir( self.path )
			conflictFiles = fnmatch.filter(files, p_wildcard)
			if len(conflictFiles)==0 or not self._isin(p_filename, \
							  map(lambda x : os.path.join(self.path,x), \
							  conflictFiles)):
				cardinal = len(conflictFiles)
			else:
				self.exist = True
				return "*"
		else:
			cardinal = 0
		return "{0:02d}".format(cardinal)