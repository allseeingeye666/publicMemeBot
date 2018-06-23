import random

def SentenceGenerate():
  sentenceArr = ["","","","","",""]
  '''
  sentenceArr[0] is an article
  sentanceArr[1] is a noun
  sentenceArr[2] is a verb
  sentenceArr[3] is a proposition
  sentenceArr[4] is an article
  sentenceArr[5] is a noun
  '''
  articles = ["The","A","An"]
  nouns = ["NounExample1", "NounExample2"]
  verbs = ["VerbExample1", "VerbExample2"]
  propositions = ["on", "in", "at", "since", "for", "ago", "before", "to", "past", "by"]
  
  articleInt = random.randint(0,len(articles)-1)
  sentenceArr[0] =  articles[articleInt]
  str(sentenceArr[0])
  nounInt = random.randint(0,len(nouns)-1)
  sentenceArr[1] = nouns[nounInt]
  str(sentenceArr[1])
  verbInt = random.randint(0,len(verbs)-1)
  sentenceArr[2] = verbs[verbInt]
  str(sentenceArr[2])
  propositionInt = random.randint(0,len(propositions)-1)
  sentenceArr[3] = propositions[propositionInt]
  str(sentenceArr[3])
  articleInt = random.randint(0,len(articles)-1)
  sentenceArr[4] = articles[articleInt]
  str(sentenceArr[4])
  nounInt = random.randint(0,len(nouns)-1)
  sentenceArr[5] = nouns[nounInt]
  str(sentenceArr[5])
  
  FullSentence = sentenceArr[0] + " " + sentenceArr[1] + " " + sentenceArr[2] + " " + sentenceArr[3] + " " + sentenceArr[4] + " " + sentenceArr[5]
  print(FullSentence)
  
sentenceGenerate()
