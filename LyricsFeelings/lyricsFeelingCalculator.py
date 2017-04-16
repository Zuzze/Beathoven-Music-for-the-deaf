#change lyricsfile manually
with open ("lyrics2.txt", "r") as lyricsfile:
    lyricsData=lyricsfile.read().replace('\n', ' ')
    lyricsData=lyricsData.replace('"', '')
    lyricsData=lyricsData.replace(',', '')
    lyricsData=lyricsData.replace('.', '')
    lyricsData=lyricsData.replace('!', '')
    lyricsData=lyricsData.replace('?', '')
    lyricsData=lyricsData.split(" ")
    print("LYRICS: ")
    print(lyricsData)

    #neutral factor
    neutralWordCount = 0
    with open ("neutral.txt", "r") as neutralWordsFile:
        neutralData=neutralWordsFile.read()
        neutralData=neutralData.split("\n")
        neutralData = list(filter(None, neutralData))#remove empty strings
        neutralWords = []
        for lyricsWord in lyricsData:
            for neutralWord in neutralData:
                if lyricsWord.lower() == neutralWord.lower():
                    neutralWordCount+=1
                    neutralWords.append(neutralWord)
        print("=== Neutral [0-1]===:" )
        print(neutralWordCount/(len(lyricsData) - 1.0))
        print("neutral words: " + str(neutralWordCount))
        print(neutralWords)
        print("all words: " + str(len(lyricsData)))


    #positive words factor
    with open ("positive.txt", "r") as positiveWordsFile:
        posData=positiveWordsFile.read()
        posData=posData.split("\n")
        posData = list(filter(None, posData))#remove empty strings
        posWordCount = 0
        posWords = []
        for lyricsWord in lyricsData:
            for posWord in posData:
                if lyricsWord.lower() == posWord.lower():
                    posWordCount+=1
                    posWords.append(posWord)
        print("=== Positive [0-1]===:" )
        print(posWordCount/(len(lyricsData) - 1.0 - neutralWordCount))
        print("positive words: " + str(posWordCount))
        print(posWords)
        print("all words: " + str(len(lyricsData)-neutralWordCount))

    #negative words factor
    with open ("negative.txt", "r") as negativeWordsFile:
        negData=negativeWordsFile.read()
        negData=negData.split("\n")
        negData = list(filter(None, negData))#remove empty
        negWordCount = 0
        negWords = []
        for lyricsWord in lyricsData:
            for negWord in negData:
                if lyricsWord .lower()== negWord.lower():
                    negWordCount+=1
                    negWords.append(negWord)
        print("=== Negative [0-1]===:" )
        print(negWordCount/(len(lyricsData) - 1.0 - neutralWordCount))
        print("negative words: " + str(negWordCount))
        print(negWords)
        print("all words: " + str(len(lyricsData)-neutralWordCount))
   
