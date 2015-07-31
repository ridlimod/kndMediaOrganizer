import os
import itertools, functools, operator

def filecmp(filename1, filename2):
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