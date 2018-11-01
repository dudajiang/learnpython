import pypinyin

def hp(word):    
	s = ''
	for i in pypinyin.pinyin(word, style=pypinyin.NORMAL):
		print(i[0])
		s += ''.join(i)
	return s

if __name__ == "__main__":
  print(hp("数学cc1"))

