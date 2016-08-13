import os
import itertools, functools, operator
import hashlib

# this method is exact but lacks of an early unmatch detection exit
# and it's very slow. It could be implemented with the takewhile function of
# the itertools module but it would be still very slow for equal files
def filecmp_deprecated(filename1, filename2):
	"Do the two files have exactly the same contents?"
	with open(filename1, "rb") as fp1:
		with open(filename2, "rb") as fp2:
			if os.fstat(fp1.fileno()).st_size != os.fstat(fp2.fileno()).st_size:
				return False # different sizes is not equal
			fp1_reader= functools.partial(fp1.read, 4096)
			fp2_reader= functools.partial(fp2.read, 4096)
			cmp_pairs= itertools.izip(iter(fp1_reader, ''), iter(fp2_reader, ''))
			inequalities= itertools.starmap(operator.ne, cmp_pairs)
			return not any(inequalities)

# this method is reliable enough and much faster
def filecmp_md5(filename1, filename2):
	"Do the two files have exactly the same contents?"
	with open(filename1, "rb") as fp1:
		with open(filename2, "rb") as fp2:
			if os.fstat(fp1.fileno()).st_size != os.fstat(fp2.fileno()).st_size:
				return False # different sizes is not equal

			m1 = hashlib.md5()
			m2 = hashlib.md5()
			m1.update(fp1.read())
			m2.update(fp2.read())

			if m1.digest()!=m2.digest():
				return False
	return True

def filecmp(filename1, filename2):
	return filecmp_md5(filename1, filename2)

if __name__=="__main__":
	print(os.getcwd())
	print(filecmp("./src/modules/ParseFile.py","./src/modules/ParseExif.py"))
	print(filecmp("./src/modules/ParseFile.py","./src/modules/ParseFile.py"))
