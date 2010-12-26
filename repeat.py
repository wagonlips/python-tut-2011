#!/usr/bin/python
import sys

def main():
  print 'Hi'
  print repeat('Yes ', False), sys.argv[1]
  print repeat('Dynomite! ', True), sys.argv[2]

def repeat(s, exclaim):
  result = s + s + s
  if exclaim:
    result + "!!!"
  return result

if __name__ == '__main__':
  main()
