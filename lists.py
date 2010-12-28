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

if __name__ == '__main__':
  main()
