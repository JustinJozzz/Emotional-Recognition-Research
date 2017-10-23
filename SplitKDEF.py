import os
import glob
import shutil

#anger-ANS, disgust-DIS, fear-AFS, happiness-HAS, neutral-NES, Sadness-SAS, Surprise-SUS
path = 'path to KDEF Dataset'#your path to KDEF dataset

allFiles['Happiness'] = glob.glob(os.path.join(path, 'A*', '*HAS.jpg'))
allFiles['Anger'] = glob.glob(os.path.join(path, 'A*', '*ANS.jpg'))
allFiles['Fear'] = glob.glob(os.path.join(path, 'A*', '*AFS.jpg'))
allFiles['Disgust'] = glob.glob(os.path.join(path, 'A*', '*DIS.jpg'))
allFiles['Neutral'] = glob.glob(os.path.join(path, 'A*', '*NES.jpg'))
allFiles['Sadness'] = glob.glob(os.path.join(path, 'A*', '*SAS.jpg'))
allFiles['Surprise'] = glob.glob(os.path.join(path, 'A*', '*SUS.jpg'))


for e in allFiles:
    for f in allFiles[e]:
        targetPath = os.path.join(os.curdir, e)
        if not os.path.exists(targetPath):
            os.makedirs(targetPath, exist_ok = True)
        shutil.copy2(f, targetPath)