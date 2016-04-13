# convert topic vectors to a clean format 'topic_no: words' for manualy matching the best tag with a topic from tags predcited by LDA
import re
topics = open('topics').read().split('\n')[:-1]
f = open('queries', 'w')
for i in range(len(topics)):
	m = re.search('topic.*', topics[i])
	if m:
    		topics[i] = m.group(0)

for i in range(len(topics)):
	temp = topics[i].split(' ')
	temp = 	[temp[i] for i in range(len(temp)) if i%2 != 0]
	temp[0] = temp[0][1:]
	for j in range(1,len(temp)):
		temp[j] = temp[j].split('*')[1]
	
	s = temp[0] + ':' + ' '.join(temp[1:]) + '\n'
	f.write(s)

f.close()

