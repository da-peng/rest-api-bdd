import  os
import tkinter

def getCaseList(path):

    projectTestCasePath = {}
    projectNames = []

    for root,dirs,files in os.walk(path):
        projectNames.append([x for x in dirs if '_'  not in x and 'steps' not in x])
        for name in files:
            if "steps"  not in root:
                for key in projectNames[0]:
                    if key in root and "feature" in name:
                        if key not in projectTestCasePath.keys():
                            projectTestCasePath[key] = []
                        projectTestCasePath[key].append(os.path.join(root, name))

    return projectTestCasePath



def executeCmd(cmd):
    out = os.popen(cmd)
    return out.read()


if __name__ == "__main__":

    for i,j in  getCaseList("../features").items():
        print(i,j)
    files = []
    cmd  = "behave" + ' '.join(files)
    executeCmd(cmd)


