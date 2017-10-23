import os
import glob
import shutil

emotions = {0.0: 'Neutral', 1.0: 'Anger', 3.0: 'Disgust', 4.0: 'Fear', 5.0: 'Happiness', 6.0: 'Sadness', 7.0: 'Surprise'}
labelPath = 'path to CK+ labels'
imagePath = 'path to CK+ images'
datasetPath = 'path where you want to put the images'

allLabels = glob.glob(os.path.join(labelPath, '*', '*', '*.txt'))

for txtFile in allLabels:
	with open(txtFile) as file:
		number = float(file.readline())
		if(number != 2.0):
			base = os.path.basename(txtFile)
			imgName = base.split("_emotion")[0]
			neutralName = base.split('000000')[0]
			shutil.copy2(os.path.join(imagePath, txtFile.split("\\")[6], txtFile.split("\\")[7], imgName+'.png'), os.path.join(datasetPath, emotions[number]))
			if len(glob.glob(os.path.join(datasetPath, 'Neutral', neutralName[0:5]+'*.png'))) <= 0:
				shutil.copy2(os.path.join(imagePath, txtFile.split("\\")[6], txtFile.split("\\")[7], neutralName+'00000001.png'), os.path.join(datasetPath, 'Neutral'))