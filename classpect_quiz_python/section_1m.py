'''
Section 1 of the Classpect quiz.
'''

import random  # @UnusedImport
from random import shuffle  # @UnusedImport

import classpect_quiz
import section_2m  # @UnusedImport
import section_3m  # @UnusedImport
import section_4m  # @UnusedImport
import dictionaries  # @UnusedImport

def main():
	'''
	Tests section 1.
	'''
	
	print("Testing Section 1.")
	results = section_1()
	print(results)
	
def section_1(verbose):
	
	'''
	Finds the top 3 aspects.
	Returns a list of 3 aspects.
	In case of a tie, returns a longer list.
	
					Free	Limited
	Cardinal		Space   Time
	Energy/Change   Life	Doom
	Responsibility  Breath  Blood	
	People/Choice   Heart   Mind
	Information	 Void	Light
	Belief/Poss.	Hope	Rage

	'''
	
	
	# lists of free and limited aspects
	free = ['space', 'life', 'breath', 'heart', 'void', 'hope']
	limited = ['time', 'doom', 'blood', 'mind', 'light', 'rage']
	
	# Prints beginning part
	
	print("------------")
	print("This is Section 1 of the 4-part Class/Aspect Quiz.")
	print("There are 48 questions in this section.")
	print("Respond to these statements about yourself on a scale of 1 to 5,")
	print("with 1 meaning 'not at all' and 5 meaning 'very much'.")
	print("------------")
	
	# Questions, as q objects, with classpects listed
	
	questions = [0] * 48  # 48 questions
	
	questions[0] = classpect_quiz.q("I am patient.")
	questions[0].classpect = ['time']
	
	questions[1] = classpect_quiz.q("Even though all good things come to an end, there is always a new beginning.")
	questions[1].classpect = ['time']
	
	questions[2] = classpect_quiz.q("There is beauty in the fact that things change.")
	questions[2].classpect = ['time']
	
	questions[3] = classpect_quiz.q("I am good with my hands.")
	questions[3].classpect = ['space']
	
	questions[4] = classpect_quiz.q("I tend toward the physical rather than the abstract.")
	questions[4].classpect = ['space']
	
	questions[5] = classpect_quiz.q("I like to travel, and am a good navigator.")
	questions[5].classpect = ['space']
	
	questions[6] = classpect_quiz.q("With the proper movement and positioning, any trial can be overcome.")
	questions[6].classpect = ['time', 'space']
	
	questions[7] = classpect_quiz.q("I like the chaos of nature.")
	questions[7].classpect = ['life']
	
	questions[8] = classpect_quiz.q("I enjoy overcoming difficulties, and going outside normal rules to do it.")
	questions[8].classpect = ['life']
	
	questions[9] = classpect_quiz.q("Growth and change is absolutely necessary in life.")
	questions[9].classpect = ['life']
	
	questions[10] = classpect_quiz.q("I like figuring out how systems and patterns work, and using them to my advantage.")
	questions[10].classpect = ['doom']
	
	questions[11] = classpect_quiz.q("I always feel a strong sense of cause and effect.")
	questions[11].classpect = ['doom']
	
	questions[12] = classpect_quiz.q("I enjoy finding my limits and pushing them, even if it takes sacrifice to do so.")
	questions[12].classpect = ['doom']
	
	questions[13] = classpect_quiz.q("I use the energy inside myself to accomplish my goals.")
	questions[13].classpect = ['life', 'doom']
	
	questions[14] = classpect_quiz.q("I prefer to live a carefree lifestyle.")
	questions[14].classpect = ['breath']
	
	questions[15] = classpect_quiz.q("I don't like being bound or tied down to commitments.")
	questions[15].classpect = ['breath']
	
	questions[16] = classpect_quiz.q("Even if the end is certain, I will forge my own path to get there.")
	questions[16].classpect = ['breath']
	
	questions[17] = classpect_quiz.q("Bonds with family and friends are of utmost importance.")
	questions[17].classpect = ['blood']
	
	questions[18] = classpect_quiz.q("Societal restraints are necessary.")
	questions[18].classpect = ['blood']
	
	questions[19] = classpect_quiz.q("I prefer to make alliances and form strong allegiances with those I trust.")
	questions[19].classpect = ['blood']
	
	questions[20] = classpect_quiz.q("I often find my freedoms and responsibilities at odds.")
	questions[20].classpect = ['breath', 'blood']
	
	questions[21] = classpect_quiz.q("I believe in the soul.")
	questions[21].classpect = ['heart']
	
	questions[22] = classpect_quiz.q("Willpower and integrity will get me anywhere I need to be.")
	questions[22].classpect = ['heart']
	
	questions[23] = classpect_quiz.q("I know who I am and what I feel.")
	questions[23].classpect = ['heart']
	
	questions[24] = classpect_quiz.q("What people do is more important than what they feel inside.")
	questions[24].classpect = ['mind']
	
	questions[25] = classpect_quiz.q("I often put aside my feelings to make important decisions.")
	questions[25].classpect = ['mind']
	
	questions[26] = classpect_quiz.q("Sometimes I find myself putting on a mask.")
	questions[26].classpect = ['mind']
	
	questions[27] = classpect_quiz.q("I like to know what makes people tick.")
	questions[27].classpect = ['heart', 'mind']
	
	questions[28] = classpect_quiz.q("Sometimes it's better to keep it secret.")
	questions[28].classpect = ['void']
	
	questions[29] = classpect_quiz.q("I can pull something from nothing.")
	questions[29].classpect = ['void']
	
	questions[30] = classpect_quiz.q("I am good at hiding, and finding things that are hidden.")
	questions[30].classpect = ['void']
	
	questions[31] = classpect_quiz.q("I seek out knowledge and truth.")
	questions[31].classpect = ['light']
	
	questions[32] = classpect_quiz.q("I don't like it when secrets are kept from me.")
	questions[32].classpect = ['light']
	
	questions[33] = classpect_quiz.q("Often I find myself explaining how things work to others.")
	questions[33].classpect = ['light']
	
	questions[34] = classpect_quiz.q("I think luck plays a big role in how things turn out.")
	questions[34].classpect = ['void', 'light']
	
	questions[35] = classpect_quiz.q("At heart, I am optimistic.")
	questions[35].classpect = ['hope']
	
	questions[36] = classpect_quiz.q("The future is full of possibility.")
	questions[36].classpect = ['hope']
	
	questions[37] = classpect_quiz.q("I often find it hard to narrow down my options to make a decision.")
	questions[37].classpect = ['hope']
	
	questions[38] = classpect_quiz.q("I find it easy to eliminate choices until the best one remains.")
	questions[38].classpect = ['rage']
	
	questions[39] = classpect_quiz.q("Most of the time, my way is the best way.")
	questions[39].classpect = ['rage']
	
	questions[40] = classpect_quiz.q("Anger and fear are the best motivational force.")
	questions[40].classpect = ['rage']
	
	questions[41] = classpect_quiz.q("One's perception of the future strongly affects how the future actually unfolds.")
	questions[41].classpect = ['hope', 'rage']
	
	questions[42] = classpect_quiz.q("I prefer to leave my options open rather than settle down.")
	questions[42].classpect = free
	
	questions[43] = classpect_quiz.q("Making decisions is hard for me.")
	questions[43].classpect = free
	
	questions[44] = classpect_quiz.q("Sometimes a little chaos, mystery, and indecision is for the best.")
	questions[44].classpect = free
	
	questions[45] = classpect_quiz.q("I like to live a structured life.")
	questions[45].classpect = limited
	
	questions[46] = classpect_quiz.q("Having a plan for the future is for the best.")
	questions[46].classpect = limited
	
	questions[47] = classpect_quiz.q("Life would be better if everyone always followed the rules.")
	questions[47].classpect = limited
	
	
	shuffle(questions)
	
	# Ask Questions
	for question in questions:
		while True:
			answer = classpect_quiz.ask(question)
			if answer != False:  # If valid input
				question.answer = answer
				break
	
	# Tally results

	space = 0
	time = 0
	life = 0
	doom = 0
	breath = 0
	blood = 0
	heart = 0
	mind = 0
	void = 0
	light = 0
	hope = 0
	rage = 0
	
	for question in questions:
		if 'space' in question.classpect:
			space = space + question.answer
		if 'time' in question.classpect:
			time = time + question.answer
		if 'life' in question.classpect:
			life = life + question.answer
		if 'doom' in question.classpect:
			doom = doom + question.answer
		if 'breath' in question.classpect:
			breath = breath + question.answer
		if 'blood' in question.classpect:
			blood = blood + question.answer
		if 'heart' in question.classpect:
			heart = heart + question.answer
		if 'mind' in question.classpect:
			mind = mind + question.answer
		if 'void' in question.classpect:
			void = void + question.answer
		if 'light' in question.classpect:
			light = light + question.answer
		if 'hope' in question.classpect:
			hope = hope + question.answer
		if 'rage' in question.classpect:
			rage = rage + question.answer
		
	d = {'space':space, 'time':time,
		 'life':life, 'doom':doom,
		 'breath':breath, 'blood':blood,
		 'heart':heart, 'mind':mind,
		 'void':void, 'light':light,
		 'hope':hope, 'rage':rage,
		 'legit_key':0}
	
	if verbose == True:
		print(d)
	
		
	results = ['legit_key', 'legit_key', 'legit_key']
		
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
