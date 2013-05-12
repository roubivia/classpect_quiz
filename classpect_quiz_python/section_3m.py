'''
Section 3 of the Classpect quiz.
'''

import random
from random import shuffle

import classpect_quiz
import section_1m
import section_2m
import section_4m
import dictionaries

def main():
    '''
    Tests section 3.
    '''
    
    test_classes = ['prince', 'knight', 'thief']
    test_aspects = ['time', 'void', 'breath']
    
    print("Testing Section 3.")
    results = section_3(test_classes, test_aspects)
    print(results)

def section_3(list_of_classes, list_of_aspects, verbose):
    
    '''
    Randomly combines top 3 aspects and classes with active/passive distinctions.
    Returns the top 3+ combinations for further refinement in section 4.
    In case of a tie, asks more questions.
    Returns a list of 3+ complete titles.
    '''
    
    print("------------")
    print("This is Section 3 of the 4-part Class/Aspect Quiz.")
    print("There are at least 27 questions in this section,")
    print("but if you are especially conflicted, there may be many more.")
    print("Respond to these statements about yourself on a scale of 1 to 5,")
    print("with 1 meaning 'not at all' and 5 meaning 'very much'.")
    print("------------")
    
    # Lists of words for each of the classes and aspects
    
    active_classes = ['mage', 'witch', 'prince', 'thief', 'maid', 'knight']
    
    # Questions list
    
    questions = []
    
    # Types of questions
    
    # Active
    
    active = [0] * 6
    active[0] = "I <class> <aspect>"
    active[1] = "I <class> my personal <aspect>"
    active[2] = "My ability to <class> <aspect> has helped me in life"
    active[3] = "I often <class> <aspect> to get ahead"
    active[4] = "In my life, I try to <class> <aspect>"
    active[5] = "I <class> things through <aspect>"
    
    # Passive
    
    passive = [0] * 6
    passive[0] = "My <aspect> helps me <class>"
    passive[1] = "I use my <aspect> to <class> others"
    passive[2] = "I help others use their <aspect> to <class> things"
    passive[3] = "I <class> <aspect> to affect those around me"
    passive[4] = "I work through others in order to <class> <aspect>"
    passive[5] = "I find it easier to <class> with the help of <aspect>"
    
    # Starts putting questions into list
    
    for k in range(3):  # 3 questions for every classpect
        for element in list_of_classes:
            # If active
            if element in active_classes:
                for aspect in list_of_aspects:
                    sentence_list = active[random.randrange(5)].split(' ')
                    for k in range(len(sentence_list)):
                        if sentence_list[k] == '<class>':
                            word_list = dictionaries.words[element]
                            sentence_list[k] = word_list[random.randrange(len(word_list) - 1)]
                        if sentence_list[k] == '<aspect>':
                            word_list = dictionaries.words[aspect]
                            sentence_list[k] = word_list[random.randrange(len(word_list) - 1)]
                    sentence = ''
                    for k in range(len(sentence_list) - 1):
                        sentence = sentence + sentence_list[k] + ' '
                    sentence = sentence + sentence_list[len(sentence_list) - 1] + '.'
                    new_q = classpect_quiz.q(sentence)
                    new_q.classpect = [element, aspect]
                    questions = questions + [new_q]
            # If passive
            else:
                for aspect in list_of_aspects:
                    sentence_list = passive[random.randrange(5)].split(' ')
                    for k in range(len(sentence_list)):
                        if sentence_list[k] == '<class>':
                            word_list = dictionaries.words[element]
                            sentence_list[k] = word_list[random.randrange(len(word_list) - 1)]
                        if sentence_list[k] == '<aspect>':
                            word_list = dictionaries.words[aspect]
                            sentence_list[k] = word_list[random.randrange(len(word_list) - 1)]
                    sentence = ''
                    for k in range(len(sentence_list) - 1):
                        sentence = sentence + sentence_list[k] + ' '
                    sentence = sentence + sentence_list[len(sentence_list) - 1] + '.'
                    new_q = classpect_quiz.q(sentence)
                    new_q.classpect = [element, aspect]
                    questions = questions + [new_q]

    
    shuffle(questions)
    
    # Asks questions
    
    for question in questions:
        while True:
            answer = classpect_quiz.ask(question)
            if answer != False:  # If valid input
                question.answer = answer
                break
            
    # Tally answers
    
    d = {}
    # {'title':value}
    
    results = [questions[0].classpect[0] + ' of ' + questions[0].classpect[1]] * 3
    # List of top keys from question
    # Initialized to a valid key value, just the first one from questions
    
    for question in questions:
        title = str(question.classpect[0] + ' of ' + question.classpect[1])
        if title in d.keys():
            d[title] = d[title] + question.answer
        else:
            d[title] = question.answer
            
    if verbose == True:
        print(d)     
    
    # Find the highest 3 values, copy their keys to results list

    for key in d:
        if d[key] >= d[results[0]]:
            results[0] = key
    for key in d:
        if key != results[0]:
            if d[key] >= d[results[1]]:
                results[1] = key
    for key in d:
        if key != results[0] and key != results[1]:
            if d[key] >= d[results[2]]:
                results[2] = key
    
    # Check for duplicates, add any to list
    
    for key in d:
        if key != results[0] and key != results[1] and key != results[2]:
            if d[key] == d[results[2]]:  # If there is a tie, it is for last place
                results = results + [key]
    
    if verbose == True:
        print(results)
    
    return(results)

#------------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#------------------------------------------------------------------------
if __name__ == '__main__':
    main()
