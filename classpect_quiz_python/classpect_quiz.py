'''
Gives class and aspect.

Four sections: 
1. Determine Top 3+ Aspects
    - Questions are statements about self, answer on 1-5 scale
2. Determine Top 3+ Class-Words
    - Questions are statements about self, answer on 1-5 scale
3. Find best 3+ combo-titles (incl. active and passive)
    - Questions are statements about self, randomly customized (1-5 scale)
4. Refine to find best title
    - Questions are "choose the best answer" from 3+ options
    
    
    Author: roubivia (cesiumtea@gmail.com)
    
'''

import random
from random import shuffle

import section_1m
import section_2m
import section_3m
import section_4m
import dictionaries

class q:
    '''
    The question class.
    Returns answer (int with value 1-5) if it is valid;
    Otherwise, returns False.
    '''
    def __init__(self, question):
        self.question = question
    description = "A question."
    author = "cesiumtea"    
    classpect = []
    answer = 0 
    dictionary = None  
    
def long_ask(question):
    '''
    For section 4.
    '''
    
    print(question.question)
    
    for k in range(len(question.classpect)):
        print((k), ':', question.dictionary[question.classpect[k]])
        
    while True:
        try: 
            answer = int(input("> "))
            break
        except:
            print("Please enter an integer corresponding to your answer.")
            return False
        
    if answer >= 0 and answer <= len(question.classpect) - 1:
        question.answer = answer
        return question.classpect[answer]  # RETURNS CLASSPECT INSTEAD OF INTEGER
    else:
        return False
        print("Your answer wasn't in range! Please try again.")
    
def ask(question):
    '''
    For sections 1-3.
    '''
    
    print(question.question)
    
    while True:
        try: 
            answer = int(input("> "))
            break
        except:
            print("Try again, smartass!")
            return False
    
    if answer >= 1 and answer <= 5:
        return answer  # RETURNS INTEGER BETWEEN 1 AND 5
    else:
        return False
    
    
    
def main():
    
    '''
    Calls the sections of the quiz.
    '''
    
    verbose = False
    
    while True:
        print("------------")
        print("Welcome to cesiumtea's Class/Aspect Quiz.")
        print("There are 4 sections to complete.")
        print("Enter 1 to continue to the quiz;")
        print("Enter 2 to view results and definitions;")
        print("Or enter 3 to view additional quiz data, credits, etc.")
        print("4 is for verbose/debug mode.")
        print("------------")
        
        answer = int(input("> "))
        if answer == 1:
            break
        elif answer == 2:
            view_all_results()
        elif answer == 3:
            view_additional_data()
        elif answer == 4:
            verbose = True
            break
        else:
            print("Try again, smartass!")
    
    list_of_aspects = section_1m.section_1(verbose)
    list_of_classes = section_2m.section_2(verbose)

#     Test code
#    list_of_aspects = ['breath', 'void', 'time']
#    list_of_classes = ['knight', 'prince', 'sylph', 'bard']


    list_of_classpects = section_3m.section_3(list_of_classes, list_of_aspects, verbose)
    top_classpect = section_4m.section_4(list_of_classpects, verbose)
    
#    test code
#    list_of_classpects = ['mage of light', 'prince of time', 'bard of hope']
#    top_classpect = 'mage of light'

    display_results(top_classpect, list_of_classpects)
    
#    print(list_of_classes)
#    print(list_of_aspects)
#    print(top_classpect)
    
def display_results(top_classpect, list_of_classpects):
    
    '''
    Displays the results prettily.
    '''

    title = top_classpect
    title_list = title.split(" ")
    
    title_string = title.upper() + '.'
    
    print("Your title is", title_string)
    
    print(dictionaries.class_descriptions[title_list[0]])
    
    print(dictionaries.aspect_descriptions[title_list[2]])
    
    print(dictionaries.classpects_long[top_classpect])
    
    print("Some of your other possible results include...")
    
    other_results = []
    for k in range(len(list_of_classpects)):
        if list_of_classpects[k] != top_classpect:
            other_results.append(list_of_classpects[k])
    
    for k in range(len(other_results)):
        print(dictionaries.classpects_short[other_results[k]])

    print("Hit any key to exit.")
    input()
    exit()
    
def view_all_results():
    '''
    Allows user to type a title and view its classpect.
    '''
    
    print("------------")
    print("Herein are all possible titles this quiz can give.")
    print("Type the class, aspect, or title you wish to see.")
    print("Possible classes: ")
    print("\tMage, Seer, Witch, Heir, Prince, Bard, ")
    print("\tThief, Rogue, Maid, Sylph, Knight, Page")
    print("Possible aspects: ")
    print("\tSpace, Time, Life, Doom, Breath, Blood,")    
    print("\tHeart, Mind, Void, Light, Hope, Rage")
    print("Or type 'exit' to go back to the main menu.")
    print("------------")
    
    while True:
        classpect = input("> ")
            
        if classpect == 'exit':
            return
        for title in dictionaries.class_descriptions:
            if classpect == title:
                print(dictionaries.class_descriptions[classpect])
        for title in dictionaries.aspect_descriptions:
            if classpect == title:
                print(dictionaries.aspect_descriptions[classpect])
        for title in dictionaries.classpects_long:
            if classpect == title:
                print(dictionaries.classpects_long[classpect])
        if classpect not in dictionaries.class_descriptions and classpect not in dictionaries.aspect_descriptions and classpect not in dictionaries.classpects_long:
            print("Title not recognized. Try again, smartass!")
    
def view_additional_data():
    '''
    Some stuff about the quiz that isn't necessarily apparent.
    '''
    
    print("------------")
    print("This quiz was developed by cesiumtea (cesiumtea@gmail.com, roubivia.tumblr.com).")
    print("Definitions of class and aspect based on posts by infinitywhale and bladekindeyewear on tumblr.")
    print("Special thanks to glilimith and captainatitat for their help with the quiz!")
    print("------------")
    

        
    


#------------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#------------------------------------------------------------------------
if __name__ == '__main__':
    main()
