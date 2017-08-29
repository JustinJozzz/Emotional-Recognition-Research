import os
import glob

#anger-ANS, disgust-DIS, fear-AFS, happiness-HAS, neutral-NES, Sadness-SAS, Surprise-SUS
path = ''#your path to KDEF dataset

allFiles = {}

allFiles['Happiness'] = glob.glob(os.path.join(path, 'A*', '*HAS.jpg'))
allFiles['Anger'] = glob.glob(os.path.join(path, 'A*', '*ANS.jpg'))
allFiles['Fear'] = glob.glob(os.path.join(path, 'A*', '*AFS.jpg'))
allFiles['Disgust'] = glob.glob(os.path.join(path, 'A*', '*DIS.jpg'))
allFiles['Neutral'] = glob.glob(os.path.join(path, 'A*', '*NES.jpg'))
allFiles['Sadness'] = glob.glob(os.path.join(path, 'A*', '*SAS.jpg'))
allFiles['Surprise'] = glob.glob(os.path.join(path, 'A*', '*SUS.jpg'))


    