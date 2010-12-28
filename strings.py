#!/usr/bin/python
import sys
def main():
  s = 'howdy'

  print s[2]
  print len(s)
  print s + ' fartknocker'

  pi = 3.14
  print 'The value of pi is ' + str(pi)

  value = 5
  print value
  value += 1
  print value
  half = value//2
  print half

  raw = r'my\back\slashes"heart"\n'
  print raw
  raw = 'my\back\slashes"heart"\n'
  print raw
  multi = 'This as a long line \
a really long line.'
  print multi
  multi = """This is also a really long
sort of a line thingy called a
line that just goes and goes."""
  print multi
  caps = "I'M NOT SHOUTING!!!"
  print caps
  print caps.lower()
  print caps.lower().capitalize()
  print caps.lower().capitalize().count('o')
  print caps.replace('SHOUT','YELL')
  swapped = caps.replace('SHOUT','YELL')
  print swapped.swapcase().capitalize()
  shorty = 'This short text has spaces between the words.'
  print shorty
  shorter = 'This short text has no spaces between the words.'.translate(None,' ')
  print shorter
  splits = shorty.split(' ')
  print splits
  print splits[5]

if __name__ == '__main__':
  main()
