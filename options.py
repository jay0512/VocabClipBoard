import pymongo
import random
from nltk.corpus import wordnet
from nltk.corpus import wordnet


def createOption(var):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    try:
        mydb = myclient["VocabWord"]
        mycol = mydb["Words"]
        x = []
        for i in mycol.find():
            x.append(i['VocabWord'])
    except:
        print('An error occurred.')

    syn = wordnet.synsets(var)[0]


    if(syn.name()!=''):
        hyp = syn.hypernyms()
        if hyp :
            option1 = hyp[0]
            print("option1 ",option1.lemmas()[0].name())
        else:
            print('random1',random.choice(x))
        hypo = syn.hyponyms()
        if hypo:
            option2 = hypo[0]
            lemmas = [l.name() for l in option2.lemmas()]
            print("option2 ",lemmas[0])
        else:
            # random
            print('random2',random.choice(x))

        if syn.lemmas():
            print("lemmas",syn.lemmas())
            for j in syn.lemmas():
                if j.antonyms(): # If adj has antonym.
                    # Prints the adj-antonym pair.
                    print ("option3 ",j.antonyms()[0].name())
                    break
                else:
                    option3 = random.choice(x)
                    print("random3",option3)
        else:
            print("else")
        # anto = syn.antonyms()[0]
        # if anto:
        #     option3 = anto[0]
        # else:
        #     # random
        #     print('random3')
        
        # print(option1.lemmas()[0].name())
        # print('\n\n')
        # print(option2)
        # print('\n\n')
        # print(option3)
        # print('\n\n')

        return