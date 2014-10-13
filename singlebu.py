import os
import shutil

def createPathing(newFile='.myvcs'):
	holderList = []
	for subdir, dirs, files in os.walk('.'):
	    for fileItem in files:
	    	# skip the .myvcs directory, don't need it
	    	if not newFile in subdir:
	        	holderList.append(os.path.join(subdir, fileItem))
	return holderList

def checkOrMakeDir(newFile='.myvcs'):
	# check if the file does exist presently
	if not os.path.exists(newFile):
		os.makedirs(newFile)
	else:
		# behave the same for now, by deleting and replacing old version
		shutil.rmtree(newFile)
		os.makedirs(newFile)

def singleBackup(newFile='.myvcs'):
	print('Copying files to ' + newFile + ' from directory at ' + os.getcwd() + '...')
	locationList = createPathing()
	checkOrMakeDir()
	for item in locationList:
		try:
			shutil.copyfile(item, newFile + item[1:])
		except IOError:
			filepath = item.split('/')[1:-1]
			filepathGrower = newFile
			for filepathPoint in filepath:
				if not os.path.exists(filepathGrower + '/' + filepathPoint):
					os.makedirs(filepathGrower + '/' + filepathPoint)
				filepathGrower = filepathGrower + '/' + filepathPoint
			shutil.copyfile(item, newFile + item[1:])
	print('Finished copying files to ' + newFile + '...')