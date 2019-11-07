import os
import functools

def getFoldersNames(path):
    folders = []
    for item in os.listdir(path):
        if not os.path.isfile(item) and item not in ('.git', '.idea'):
            folders.append(item)
    return folders

def getFilesNames(path):
    files = os.listdir(path)
    return files

def getProblemURLandScore(path):
    inFile = open(path, 'r')
    url = inFile.readline().split()[-1]
    difficulty = inFile.readline().split()[-1]
    score = inFile.readline().split()[-1]
    inFile.close()
    return url, difficulty, score

def getTotalNumberOfProblems():
    totalNumber = 0
    folders = getFoldersNames(os.getcwd())
    for folder in folders:
        subfolders = getFoldersNames(os.path.join(os.getcwd(), folder))
        for subfolder in subfolders:
            totalNumber += len(getFilesNames(os.path.join(os.getcwd(), folder, subfolder)))
    return totalNumber

readmeFile = open('README.md', 'w')
readmeFile.write('# Solutions to Hackerrank practice problems\n')
readmeFile.write('This repository contains ' + str(getTotalNumberOfProblems()) + ' solutions to Hackerrank practice problems with Python 3.\n')
readmeFile.write('\n')
readmeFile.write('If it was helpful please press a star.\n')
readmeFile.write('\n')
readmeFile.write('[![GitHub last commit](https://img.shields.io/github/last-commit/dispe1/Hackerrank-Solutions.svg)](https://github.com/dispe1/Hackerrank-Solutions)\n')
readmeFile.write('[![GitHub commit activity the past week, 4 weeks, year](https://img.shields.io/github/commit-activity/y/dispe1/Hackerrank-Solutions.svg)](https://github.com/dispe1/Hackerrank-Solutions)\n')
readmeFile.write('[![GitHub repo size in bytes](https://img.shields.io/github/repo-size/dispe1/Hackerrank-Solutions.svg)](https://github.com/dispe1/Hackerrank-Solutions)\n')
readmeFile.write('[![GitHub stars](https://img.shields.io/github/stars/dispe1/Hackerrank-Solutions.svg)](https://github.com/dispe1/Hackerrank-Solutions)\n')
readmeFile.write('\n')

folders = getFoldersNames(os.getcwd())
for folder in folders:
    readmeFile.write('- ' + folder + '\n')
    subfolders = getFoldersNames(os.path.join(os.getcwd(), folder))
    for subfolder in subfolders:
        readmeFile.write('    ' + subfolder + '\n')
        files = getFilesNames(os.path.join(os.getcwd(), folder, subfolder))
        for file in files:
            url, difficulty, score = getProblemURLandScore(os.path.join(os.getcwd(), folder, subfolder, file))
            readmeFile.write('        - ' + "".join(file.split(".")[1:-1])[1:]
                  + ' | [Problem](' + url
                  + ')'
                  + ' | [Solution]'
                  + '(https://github.com/dispe1/Hackerrank-Solutions/blob/master/'
                  + folder.replace(' ', '%20') + '/' + subfolder.replace(' ', '%20') + '/'
                  + file.replace(' ', '%20') + ')'
                  + ' | Difficulty: ' + difficulty
                  + ' | Score: ' + str(score) + '\n')

readmeFile.close()
