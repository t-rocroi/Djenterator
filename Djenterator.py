## Djent-erator

import itertools
import random

def tabHeader(measures,beats):
	#print the timing at the top
	timing = []
	print('   ', end = '')
	for m in range(1, measures + 1):
		for t in range(0,beats):
			if t < 3:
				temp = str(t + 1) + ' e + a '
				timing.append(temp)
			else:
				temp = str(t + 1) + ' e + a|'
				timing.append(temp)
	print(''.join(timing))

	#print all other strings tabs
	for j in range(1, len(tuning_select)):
		print(tuning_select[-j], '|', end = '')
		for k in range(1, measures + 1):
			print('--' * ((beats * 4) - 1) + '-|', end = '')
		print('')

# create list of each 4-space permunation of binary states
perms = ["-".join(seq) for seq in itertools.product('0-', repeat=4)]

# define the different tunings
tunings = {
		'std':['E', 'A', 'D', 'G', 'b', 'e'],
		'dropD':['D', 'A', 'D', 'G', 'B', 'e'],
		'std7':['B', 'E', 'A', 'D', 'G', 'b', 'e'],
		'dropA':['A', 'E', 'A', 'D', 'G', 'b', 'e']}

# data entry
print("please enter your tuning below.\n")
for k, v in tunings.items():
	print("type {} for {}".format(k,v))
choice = input("\nWhich tuning are you using? ")
if choice in tunings:
	tuning_select = tunings[choice]
else:
	print("\n\nPlease Check spelling. Choice not available.\n")

# how many riffs do you want?
RiffCount = int(input('\nhow many riffs do you want? '))

# how many measures long?
measures = int(input('\nwe are in 4/4. How many measures do you want? '))
beats = 4  # we are in 4/4

# to compile 4 measures, I need 16 sets of 16th notes
print('\n\n' + "On a {} string guitar, play:".format(len(tuning_select)))
for i in range(0, RiffCount):
	# initialize riff
	riff = []

	# this is for random riffs in random orders
	for r in range(0, 16):
		riff.append(perms[random.randint(0, 15)])
	print('\nriff #{}:'.format(i + 1))

	# print "header" of the tab notation
	tabHeader(measures,beats)

	# print the rhythm
	djent = []
	print(tuning_select[0],'|',end='')
	for mm in range(1, measures + 1):
		for tt in range(1,beats+1):
			if tt != 4:
				temp3 = riff[mm * tt - 1] + '-'
				djent.append(temp3)
			else:
				temp3 = riff[mm * tt - 1] + '|'
				djent.append(temp3)
	print(''.join(djent))
	print('')
