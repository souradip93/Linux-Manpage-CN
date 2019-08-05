import re

regex = re.compile('^(\d+\.\d+) \((.*?);(.*?);(.*?)\)$')

with open('output.txt') as f:
	for line in f:
		line = line.strip()
		res = regex.search(line)
		if res is not None and res.group(4).strip() != '' and float(res.group(1)) > 0.90:
			if '(' not in res.group(2) and '(' not in res.group(3) and '(' not in res.group(4):
				print res.group(1)+': ('+res.group(2)+';'+res.group(3)+';'+res.group(4)+')'
		
