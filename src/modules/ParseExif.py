# commodity function ( could be inline )
def badchar(s):
	return any(c in "\"" for c in s)

class ParseExif( object ):
	def __init__( self, p_tags, p_filename ):
		#print p_tags
		if "EXIF DateTimeOriginal" in p_tags and \
		not "0000" in p_tags["EXIF DateTimeOriginal"].values and p_tags["EXIF DateTimeOriginal"].values:
			p_str = p_tags["EXIF DateTimeOriginal"]
			lDatetime = p_str.values.replace(" ",":").split(":")
			print (lDatetime)
			self.year = lDatetime[0]
			self.month = lDatetime[1]
			self.day =lDatetime[2]
			self.timefs = ".".join(lDatetime[3:])
		elif "Image DateTime" in p_tags and \
		not "0000" in p_tags["Image DateTime"].values and p_tags["Image DateTime"].values:
			p_str = p_tags["Image DateTime"]
			lDatetime = p_str.values.replace(" ",":").split(":")
			print (lDatetime)
			self.year = lDatetime[0]
			self.month = lDatetime[1]
			self.day =lDatetime[2]
			self.timefs = ".".join(lDatetime[3:])
		else:
			mFstat = os.stat( p_filename )
			tstamp = datetime.fromtimestamp(mFstat.st_mtime)
			self.year = tstamp.strftime("%Y")
			self.month = tstamp.strftime("%m")
			self.day = tstamp.strftime("%d")
			self.timefs = tstamp.strftime("%H.%M.%S")

		if "Image Model" in p_tags and p_tags["Image Model"] != "":
			p_str = p_tags["Image Model"]
			test = p_str.values
			print (test,badchar(test))
			if badchar(test):
				test = "INVALID"
			self.model = test.replace(" ","_")
		else:
			self.model = "UNK"