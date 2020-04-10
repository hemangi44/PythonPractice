def double_char(txt):
	s=""
	for i in range(0,len(txt)):
		s+=txt[i]
		s+=txt[i]
	return s

print(double_char('hemangi'))