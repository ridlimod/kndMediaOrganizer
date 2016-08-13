## batchprocess.py
from modules.FileProcess import batchprocess

def _archlinux_():
	# Source folder, this one will be walked recursively in search of your files
	sInd = "/media/BLACK/Work/PersonalMedia/FotosWork/src"

	# Target folder where the pictures will be copied, and renamed and organized.
	# Current Pattern: ./[Year]/[Month]/[Day]/[Year-Month-Day]/[HH.MM.SS-Take-Camera].[ext]
	sOutd = "/media/BLACK/Work/PersonalMedia/FotosWork/sources"

	# This script doesn't remove any file, but the pictures that were copied right in target folder will be moved here.
	# Files not in extensions list or already on Target Folder will be left in the source folder
	sProcd = "/media/BLACK/Work/PersonalMedia/FotosWork/proc"

	# list of search extensions.
	lext = [".jpg",".jpeg",".jpe",".tif",".nef",".cr2",".psd",".png",".gif"]

	# launch command
	batchprocess(sInd,sOutd,sProcd,lext)

## test code
if __name__ == "__main__":
	_archlinux_()
