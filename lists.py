#!/usr/bin/python
import sys
def main():

  fruit = ['oranges', 'bananas', 'figs', 'hot house grapes']
  for i in fruit:
    print i

  print " "

  fruit.append('apples')
  for i in fruit:
    print i

  print " "

  fruity = []
  fruity.append('insectosaurus')
  fruity.append('frogosaur')
  fruity.append('penguidactyl')
  print fruity[2]
  for i in fruity:
    print i

  print ''
  print 'Check this...'
  mylist = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
  print len(mylist)
  i = 0
  while i < len(mylist):
    print i
    print mylist[i]
    i += 1
    print 'iterating ' + str(i)
  print 'Printing '
  print mylist


if __name__ == '__main__':
  main()
