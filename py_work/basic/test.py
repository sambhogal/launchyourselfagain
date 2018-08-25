
def verbing(s):
  # +++your code here+++
  if len(s) >= 3:
    if s[len(s)-3:] == "ing":
      return s + "ly"
    else:
      return s + "ing"
  else:
    return s


def test(got, expected):
	if got == expected:
		prefix = ' OK '
	else:
		prefix = '  X '
	print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
	print("Hello World")
	#print 'verbing'
	#test(verbing('hail'), 'hailing')


if __name__ == '__main__':
  main()