'''
Section 4 of the Classpect quiz.
'''

import random
from random import shuffle

import classpect_quiz
import section_1m
import section_2m
import section_3m
import dictionaries

def main():
    '''
    Tests section 4.
    '''
    
    test_classpects = ['mage of space', 'mage of time', 'mage of life']
    
    print("Testing Section 4.")
    results = section_4(test_classpects)
    print(results)

def section_4(list_of_classpects, verbose):
    
    '''
    Takes the top 3 combinations of title and determines the best one.
    Returns the top title.
    '''
    
    print("------------")
    print("This is Section 4 of the 4-part Class/Aspect Quiz.")
    print("There are 4 questions in this section;")
    print("Choose the answer that best suits you.")
    print("Reply with the number that corresponds to your answer.")
    print("------------")
    
    # Build questions list
    
    questions = [0] * 4  # 4 questions
    
    questions[0] = classpect_quiz.q("What is your ideal occupation?")
    questions[0].classpect = list_of_classpects
    questions[0].dictionary = dictionaries.s4_q1
    
    questions[1] = classpect_quiz.q("Question 2")
    questions[1].classpect = list_of_classpects
    questions[1].dictionary = dictionaries.s4_q2
    
    questions[2] = classpect_quiz.q("Question 3")
    questions[2].classpect = list_of_classpects
    questions[2].dictionary = dictionaries.s4_q3
    
    questions[3] = classpect_quiz.q("Question 4")
    questions[3].classpect = list_of_classpects
    questions[3].dictionary = dictionaries.s4_q4
    

    # Asks questions
    
    for question in questions:
        while True:
            answer = classpect_quiz.long_ask(question)
            if answer != False:  # If valid input
                question.answer = answer  # answers will be classpects
                break
            
    # Tally answers
    
    d = {'legit key':0}
    
    for classpect in list_of_classpects:
        d[classpect] = 0
    
    for question in questions:
        d[question.answer] = d[question.answer] + 1
            
    if verbose == True:
        print(d)
    
    # Find top answer
    
    top_classpect = 'legit key'  # just needs to be a valid value
    for classpect in d:
        if d[classpect] > d[top_classpect]:
            top_classpect = classpect
    
    # Check for duplicates
    
    dupelist = []
    for classpect in d:
        if d[classpect] == d[top_classpect]:
            dupelist.append(classpect)
    
    if len(dupelist) > 1:
        top_classpect = tiebreak(dupelist) 
        
    return top_classpect
        
def tiebreak(dupelist):
    '''
    Breaks a tie between two or more classpects.
    '''
    
    question = classpect_quiz.q("Last question. Which do you feel describes you best?")
    question.classpect = dupelist
    question.dictionary = dictionaries.classpects_short
    
    while True:
            answer = classpect_quiz.long_ask(question)
            if answer != False:  # If valid input
                question.answer = answer  # answers will be classpects
                break
            
    return question.answer


#------------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#------------------------------------------------------------------------
if __name__ == '__main__':
    main()
