'''
Section 2 of the Classpect quiz.
'''

import random  # @UnusedImport
from random import shuffle

import classpect_quiz
import section_1m  # @UnusedImport
import section_3m  # @UnusedImport
import section_4m  # @UnusedImport
import dictionaries  # @UnusedImport

def main():
    '''
    Tests section 2.
    '''
    
    print("Testing Section 2.")
    results = section_2()
    print(results)
    
def section_2(verbose):
    
    '''
    Finds the top 3 classes.
    Returns a list of 3 class words.
    In case of a tie, returns a longer list.
    
             Active    Passive
    Know     Mage      Seer
    Change   Witch     Heir
    Destroy  Prince    Bard
    Steal    Thief     Rogue
    Create   Maid      Sylph
    Exploit  Knight    Page

    Know    vs. Change
    Create  vs. Destroy
    Steal   vs. Exploit
    '''
    
    # lists of active and passive classes
    active = ['mage', 'witch', 'prince', 'thief', 'maid', 'knight']
    passive = ['seer', 'heir', 'bard', 'rogue', 'sylph', 'page']
    
    # Prints beginning part
    
    print("------------")
    print("This is Section 2 of the 4-part Class/Aspect Quiz.")
    print("There are 48 questions in this section.")
    print("Respond to these statements about yourself on a scale of 1 to 5,")
    print("with 1 meaning 'not at all' and 5 meaning 'very much'.")
    print("------------")
    
    # Questions, as q objects, with classpects listed
    
    questions = [0] * 48  # 48 questions
    
    questions[0] = classpect_quiz.q("Information can be a powerful tool, and I know how to use it.")
    questions[0].classpect = ['mage']
    
    questions[1] = classpect_quiz.q("I decide what to do for myself.")
    questions[1].classpect = ['mage']
    
    questions[2] = classpect_quiz.q("As long as I understand what I'm doing, it doesn't matter if others do.")
    questions[2].classpect = ['mage']
    
    questions[3] = classpect_quiz.q("I try to see patterns and the flow of things.")
    questions[3].classpect = ['seer']
    
    questions[4] = classpect_quiz.q("I find others come to me when they want to learn about something.")
    questions[4].classpect = ['seer']
    
    questions[5] = classpect_quiz.q("While I generally have a good understanding of the situation, I don't like to take control.")
    questions[5].classpect = ['seer']
    
    questions[6] = classpect_quiz.q("I have always had an intuitive understanding of the world.")
    questions[6].classpect = ['mage', 'seer']
    
    questions[7] = classpect_quiz.q("I shape the situation around me to get the change I desire.")
    questions[7].classpect = ['witch']
    
    questions[8] = classpect_quiz.q("If something needs doing, I am the one who gets it done.")
    questions[8].classpect = ['witch']
    
    questions[9] = classpect_quiz.q("I don't like standing back when exciting things are happening.")
    questions[9].classpect = ['witch']
    
    questions[10] = classpect_quiz.q("I find myself inspiring others.")
    questions[10].classpect = ['heir']
    
    questions[11] = classpect_quiz.q("While I don't often take the wheel, I like to help others do so.")
    questions[11].classpect = ['heir']
    
    questions[12] = classpect_quiz.q("I find that the things I change often change me as well.")
    questions[12].classpect = ['heir']
    
    questions[13] = classpect_quiz.q("I am afraid of stagnation.")
    questions[13].classpect = ['witch', 'heir']
    
    questions[14] = classpect_quiz.q("Sometimes I find myself burning more bridges than necessary.")
    questions[14].classpect = ['prince']
    
    questions[15] = classpect_quiz.q("I have trouble controlling my destructive impulses.")
    questions[15].classpect = ['prince']
    
    questions[16] = classpect_quiz.q("I can get things done, but often let it fail afterwards.")
    questions[16].classpect = ['prince']
    
    questions[17] = classpect_quiz.q("I can find the flaws in just about anything.")
    questions[17].classpect = ['bard']
    
    questions[18] = classpect_quiz.q("I am an expert at ferreting out weakness and using that as an advantage.")
    questions[18].classpect = ['bard']
    
    questions[19] = classpect_quiz.q("Jokes that have a little bite are the best kind.")
    questions[19].classpect = ['bard']
    
    questions[20] = classpect_quiz.q("I tear down challenges like they are paper.")
    questions[20].classpect = ['prince', 'bard']
    
    questions[21] = classpect_quiz.q("I often find myself hoarding things.")
    questions[21].classpect = ['thief']
    
    questions[22] = classpect_quiz.q("I like to dominate resources, so I can allocate a little extra to myself.")
    questions[22].classpect = ['thief']
    
    questions[23] = classpect_quiz.q("If I want something, I will have it by any means necessary.")
    questions[23].classpect = ['thief']
    
    questions[24] = classpect_quiz.q("I prefer to get things moving with a light touch rather than a shove.")
    questions[24].classpect = ['rogue']
    
    questions[25] = classpect_quiz.q("I like to keep the good things flowing, and my friends thank me for it.")
    questions[25].classpect = ['rogue']
    
    questions[26] = classpect_quiz.q("I often sneakily manipulate events to help those that need it most.")
    questions[26].classpect = ['rogue']
    
    questions[27] = classpect_quiz.q("It's not always wrong to take something that isn't yours.")
    questions[27].classpect = ['thief', 'rogue']
    
    questions[28] = classpect_quiz.q("When I see something going wrong, I try to step in and fix the problem.")
    questions[28].classpect = ['maid']
    
    questions[29] = classpect_quiz.q("I like to create new things; I hate seeing things around me fall to pieces.")
    questions[29].classpect = ['maid']
    
    questions[30] = classpect_quiz.q("If there is a problem, I can usually create a solution.")
    questions[30].classpect = ['maid']
    
    questions[31] = classpect_quiz.q("People often come to me for help with their problems.")
    questions[31].classpect = ['sylph']
    
    questions[32] = classpect_quiz.q("I would rather give advice than deal with my own issues.")
    questions[32].classpect = ['sylph']
    
    questions[33] = classpect_quiz.q("I use my talents to smooth things over quietly.")
    questions[33].classpect = ['sylph']
    
    questions[34] = classpect_quiz.q("I can't stand the thought of tossing things aside just because they are broken.")
    questions[34].classpect = ['maid', 'sylph']
    
    questions[35] = classpect_quiz.q("I find creative and elegant solutions using minimal resources.")
    questions[35].classpect = ['knight']
    
    questions[36] = classpect_quiz.q("I find myself exploiting loopholes to make things work.")
    questions[36].classpect = ['knight']
    
    questions[37] = classpect_quiz.q("I use what I have on-hand to solve problems and get things done.")
    questions[37].classpect = ['knight']
    
    questions[38] = classpect_quiz.q("I might be lacking now, but I am working hard to be the best I can be.")
    questions[38].classpect = ['page']
    
    questions[39] = classpect_quiz.q("I would prefer to help others fight rather than fight myself.")
    questions[39].classpect = ['page']
    
    questions[40] = classpect_quiz.q("I often find myself lending others the strength they need to push on.")
    questions[40].classpect = ['page']
    
    questions[41] = classpect_quiz.q("I don't have much; but what I do have, I use very well.")
    questions[41].classpect = ['knight', 'page']
    
    questions[42] = classpect_quiz.q("I get shit done.")
    questions[42].classpect = active
    
    questions[43] = classpect_quiz.q("If you want it done right, you must do it yourself.")
    questions[43].classpect = active
    
    questions[44] = classpect_quiz.q("Nothing gets done if you expect others to do it for you.")
    questions[44].classpect = active
    
    questions[45] = classpect_quiz.q("I would rather help others than help myself.")
    questions[45].classpect = passive
    
    questions[46] = classpect_quiz.q("Being in the limelight isn't for me.")
    questions[46].classpect = passive
    
    questions[47] = classpect_quiz.q("Sometimes, it's more effective to delegate than to micromanage.")
    questions[47].classpect = passive
    
    shuffle(questions)
    
    # Ask Questions
    for question in questions:
        while True:
            answer = classpect_quiz.ask(question)
            if answer != False:  # If valid input
                question.answer = answer
                break
    
    # Tally results

    mage = 0
    witch = 0
    prince = 0
    thief = 0
    maid = 0
    knight = 0
    seer = 0
    heir = 0
    bard = 0
    rogue = 0
    sylph = 0
    page = 0
    
    for question in questions:
        if 'mage' in question.classpect:
            mage = mage + question.answer
        if 'witch' in question.classpect:
            witch = witch + question.answer
        if 'prince' in question.classpect:
            prince = prince + question.answer
        if 'thief' in question.classpect:
            thief = thief + question.answer
        if 'maid' in question.classpect:
            maid = maid + question.answer
        if 'knight' in question.classpect:
            knight = knight + question.answer
        if 'seer' in question.classpect:
            seer = seer + question.answer
        if 'heir' in question.classpect:
            heir = heir + question.answer
        if 'bard' in question.classpect:
            bard = bard + question.answer
        if 'rogue' in question.classpect:
            rogue = rogue + question.answer
        if 'sylph' in question.classpect:
            sylph = sylph + question.answer
        if 'page' in question.classpect:
            page = page + question.answer
         
    d = {'mage':mage, 'witch':witch,
         'prince':prince, 'thief':thief,
         'maid':maid, 'knight':knight,
         'seer':seer, 'heir':heir,
         'bard':bard, 'rogue':rogue,
         'sylph':sylph, 'page':page,
         'legit_key':0}
    
    if verbose == True:
        print(d)
    
        
    results = ['legit_key', 'legit_key', 'legit_key']  # Initial values must be legit keys for d
        
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
