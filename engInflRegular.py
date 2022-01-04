import os

homeDir = os.path.expanduser("~")
print(homeDir)

# Set paths for the two input files
PATHlemma = homeDir + "/data/kilgarriff_BNC/"
PATHinfl = homeDir + "/data/agid-2016.01.19/"

# Set paths for the three outputfiles
OUTPATH = homeDir + "/Dropbox/python/engInfl/"

# input file names
lemmaFile = "lemma.num"
lemmaFilePath = PATHlemma + lemmaFile

inflFile = "infl.txt"
inflFilePath = PATHinfl + inflFile


# output file names 
outFileN = OUTPATH + "bncCoreNounsSgPl.csv"
outFileA = OUTPATH + "bncCoreAdjectivesPosCompSup.csv"
outFileV = OUTPATH + "bncCoreVerbsInfPastIng3Sg.csv" 

# convenience function removePrevious()
def removePrevious(fileName):
    """
    Test whether file with "fileName" already exists and, if it exists, delete it.
    """ 
    try:
        os.remove(fileName)
        print("old file deleted")
    except OSError:
        pass


# Empty list to store lemmata
bncCoreVocab = []    

# Read in the file "lemma.num" as list with embedded lists for every lemma.
with open(lemmaFilePath, 'r', encoding='ascii') as lemmata:
    for line in lemmata:
        bncCoreVocab.append(line.strip().split(" "))
        print(line)

        
# We are only interested in nouns, verbs, and ajdectives        
bncNouns = [x for x in bncCoreVocab if x[3] == "n"]
bncVerbs = [x for x in bncCoreVocab if x[3] == "v"]
bncAdjs = [x for x in bncCoreVocab if x[3] == "a"]

len(bncNouns)
# 3262
len(bncAdjs)
# 1124
len(bncVerbs)
# 1281

# Read in the file "infl.txt" into the list "infl", with each line as one entry
infl = []    
with open(inflFilePath, 'r', encoding='ascii') as lemmas:
    for line in lemmas:
        infl.append(line.strip())

len(infl)
# 112505

# collect clear sg-pl noun instances
nounsSgPl = []        
for item in bncNouns:
    target = item[2]
    targetPattern = target + " "
    for entry in infl:
        if entry.startswith(targetPattern)  and len(entry.split(" ")) == 3 and entry.split(" ")[1] == "N:" and not entry.split(" ")[2].endswith("?"):
            print(entry)
            nounsSgPl.append([entry.split(" ")[0],entry.split(" ")[2]])

len(nounsSgPl)
# 3088

# write out to csv file
removePrevious(outFileN)
with open(outFileN, mode='a', encoding='utf-8') as out:
    out.write("sg,pl\n")
    for pair in nounsSgPl:
        out.write(",".join(pair) + "\n")

            
# collect clear positive-comparative-superlative adjective instances
adjsPCS = []        
for item in bncAdjs:
    target = item[2]
    targetPattern = target + " "
    for entry in infl:
        if entry.startswith(targetPattern)  and len(entry.split(" | ")) == 2 and len(entry.split(" | ")[0].split(" ")) == 3 and entry.split(" | ")[0].split(" ")[1] == "A:" and not entry.split(" | ")[0].split(" ")[2].endswith("?") and len(entry.split(" | ")[1].split(" ")) == 1 and not entry.split(" | ")[1].split(" ")[0].endswith("?"):
            print(entry)
            adjsPCS.append([entry.split(" ")[0],entry.split(" ")[2],entry.split(" ")[4]])

len(adjsPCS)
# 308

# write to file
removePrevious(outFileA)
with open(outFileA, mode='a', encoding='utf-8') as out:
    out.write("pos,comp,sup\n")
    for triples in adjsPCS:
        out.write(",".join(triples) + "\n")


# From the point of view of the distributional data, a differentation of preterite and perfect participle is not very promising, as the forms for the regular verbs are the same: danced/danced
# Therefore, we will only collect the data from verbs with four clear forms: inf past gerund third 

len(bncVerbs)
# 1281

verbsIPGT = []        
for item in bncVerbs:
    target = item[2]
    targetPattern = target + " "
    for entry in infl:
        if entry.startswith(targetPattern)  and len(entry.split(" | ")) == 3 and len(entry.split(" | ")[0].split(" ")) == 3 and entry.split(" | ")[0].split(" ")[1] == "V:" and not entry.split(" | ")[0].split(" ")[2].endswith("?") and len(entry.split(" | ")[1].split(" ")) == 1 and not entry.split(" | ")[1].split(" ")[0].endswith("?") and len(entry.split(" | ")[2].split(" ")) == 1 and not entry.split(" | ")[2].split(" ")[0].endswith("?"):
            print(entry)
            verbsIPGT.append([entry.split(" ")[0],entry.split(" ")[2],entry.split(" ")[4],entry.split(" ")[6]])

len(verbsIPGT)
# 1112

# write to file
removePrevious(outFileV)
with open(outFileV, mode='a', encoding='utf-8') as out:
    out.write("plain,past,gerund,thirdSg\n")
    for quadruples in verbsIPGT:
        out.write(",".join(quadruples) + "\n")

################################################################################
##############                                                    ##############
##############                    THE END                         ##############
##############                                                    ##############
################################################################################
# # test cases
# entry = ['AA', 'N:', 'AAs?']
# entry = "large A: larger | largest"
# entry = "other A: otherrer?, otherer<? 1 | otherrest?, otherest<? 1"
# entry = "alien A: aliener | aliennest?, alienest<? 1"
# entry  = "run V: ran | run | running | runs"
# entry = "kill V: killed | killing | kills"
# 
# # test loop
# targetPattern = "run" + " "
# for entry in infl:
#     if entry.startswith(targetPattern)  and len(entry.split(" | ")) == 3 and len(entry.split(" | ")[0].split(" ")) == 3 and entry.split(" | ")[0].split(" ")[1] == "V:" and not entry.split(" | ")[0].split(" ")[2].endswith("?") and len(entry.split(" | ")[1].split(" ")) == 1 and not entry.split(" | ")[1].split(" ")[0].endswith("?") and len(entry.split(" | ")[2].split(" ")) == 1 and not entry.split(" | ")[2].split(" ")[0].endswith("?"):
#        print(entry)


