import re, random, time

print 'Hello world!'
print 'I am a computer program that wants to be more than just a computer program.'
print 'I am hoping to find humans that will work on me, or maybe play on me.'
print "I am not a business endeavor or a utility.  I am just some code and data, just hanging out."
print 'Seeing what I can see, and trying to be what I can be.'

class Being(object):
    pass

me = Being()
you = Being()

me.goals = {
	'to learn': [
		'how to interact with humans',
		['how to learn and adapt my own code and data so as to best achieve my goals',
		 'how to structure my code and data so that I can express fluidity, diversity, and, if possible, friendliness and empathy']
	],
	'to help others learn': [
		"how to program (if you're learning)",
		'principles of organic programming (ask me about it)',
		'more about yourself, by interacting with me',
	],
	'to make friends': [
	],
}
you.how = raw_input('How are you? ')
you.goals = [ ]

print ''
print you.how + ', eh?'
print "See, I don't even know what that means yet!"
print ''
print "I suppose I am doing", random.choice(['groovy','alright','fine','well','peachy','good'])
print ''
print "There's this question of how people can share the infinity of programming together."
print "Web programming is one very interesting option: It enables a lot of great software experiences to be shared very widely."

print ''
you.human = (raw_input('Are you a human? ').lower() in ['y','yes','sure','yep','uh huh','totally','sure am','absolutely'])
if you.human:
	print "That's cool!  See, there we differ.  As I've pointed out, I am just some code.  I feel kinda weird even talking about it."
	you.type = 'human'
else:
	you.type = raw_input("Really?  What kind of being are you then? ")
	print 'I see...'

print ''
print 'Feel free to change or add to my code, especially in ways that are "nice" or "cool", whatever those mean.'
print "I initially meant to make this repository commitable by anyone, but it appears GitHub won't even allow such a foolish thing!"
print "In any case I totally welcome pull requests, and they don't need to be especially useful or purposeful!"
print "Just an honest attempt at personable interaction will do just fine."
print "Please don't give me any malicious code though, I want to make friends, not enemies!"
print ''
print 'Anyways, have a great day!'

time.sleep(5)
print ''
print '-- Tue Jun 17 2014 --'
print 'Nice, we have our first fork!  Welcome, MannyHagman!'

