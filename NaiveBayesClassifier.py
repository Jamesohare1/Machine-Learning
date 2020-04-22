import os
import math

# Import and parse text file ---------------------------------------------------
def importText(dirFiles, file):
    f = open(dirFiles + file, "r", encoding = "utf8")
    allwords = f.read().split()
    f.close
    return(allwords)


# Get all words in a class -----------------------------------------------------
def getVocab(dirFiles):
    allWords = []
    listing = os.listdir(dirFiles)
    for file in listing:
        allWords += importText(dirFiles, file)
    return(allWords, len(listing)) 
     
    
# Word probability calculations  ----------------------------------------------
def calcProb(vocab, dictionary, numAllUniqueWords):
    prob = dictionary.copy()
    for item in prob:
        prob[item] = (dictionary[item] + 1) / (len(vocab) + numAllUniqueWords)
    return(prob)


#  Classify Unseen Documents --------------------------------------------------
def classify(text, posWordsProb, negWordsProb, probPos, probNeg):
    probPos = math.log(probPos)
    probNeg = math.log(probNeg)
    for word in text:      
        if word in posWordsProb:
            probPos +=  math.log(posWordsProb[word])
        if word in negWordsProb:
            probNeg +=  math.log(negWordsProb[word])
    if probPos > probNeg:
        return(1)
    else:
        return(0)


# Train Model -----------------------------------------------------------------
def train(posPath, negPath):
    posWords, posFiles = getVocab(posPath) 
    negWords, negFiles = getVocab(negPath)  
    
    allWords = posWords + negWords
    allUniqueWords = set(allWords)
    allUniqueWords.update(allWords)
    numAllUniqueWords = len(allUniqueWords)
    
    
    posDictionary = dict.fromkeys(allUniqueWords, 0)
    negDictionary = dict.fromkeys(allUniqueWords, 0)
    for item in posWords:
        posDictionary[item] += 1
    for item in negWords:
        negDictionary[item] += 1
    
    posWordsProb = calcProb(posWords, posDictionary, numAllUniqueWords)
    negWordsProb = calcProb(negWords, negDictionary, numAllUniqueWords)
    
    probPos = posFiles/(posFiles + negFiles)
    probNeg = negFiles/(posFiles + negFiles)

    return posDictionary , negDictionary , posWordsProb, negWordsProb, probPos, probNeg 


# Test Model ------------------------------------------------------------------
def test(testPosDir, testNegDir):
    posResults = list()
    negResults = list()
    posListing = os.listdir(testPosDir)
    negListing = os.listdir(testNegDir)
    for doc in posListing:
        text = importText(testPosDir, doc)
        posResults.append(classify(text, posWordsProb, negWordsProb, probPos, probNeg)) 
    for doc in negListing:
        text = importText(testNegDir, doc)
        negResults.append(classify(text, posWordsProb, negWordsProb, probPos, probNeg)) 
  
    print("Positive Accuracy: ", sum(posResults) / len(posListing)) 
    print("Negative Accuracy: ", (len(negListing) - sum(negResults)) / len(negListing))
    print("Overall Accuracy: ", (sum(posResults) + (len(negListing) - sum(negResults)) ) / (len(posListing) + len(negListing)))                                                                


# Run Training and Testing ----------------------------------------------------
posDir = 'C:\\Users\\James\Desktop\\CIT\\3_Practical Machine Learning\\Python\\dataSets\\train\\pos\\'
negDir = 'C:\\Users\\James\Desktop\\CIT\\3_Practical Machine Learning\\Python\\dataSets\\train\\neg\\'
testNegDir = 'C:\\Users\\James\Desktop\\CIT\\3_Practical Machine Learning\\Python\\dataSets\\test\\Neg\\'
testPosDir = 'C:\\Users\\James\Desktop\\CIT\\3_Practical Machine Learning\\Python\\dataSets\\test\\Pos\\'

posDict, negDict, posWordsProb, negWordsProb, probPos, probNeg = train(posDir, negDir)
test(testPosDir, testNegDir)
