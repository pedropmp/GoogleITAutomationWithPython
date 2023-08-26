#!/usr/bin/env python3
file = open("spider.txt")
print(file.readline())
print(file.read())

file.close()

'''closes the file automatically, but constraints it to a single block of code'''
with open("spider.txt") as file:
    print()
    for line in file:
        print(line.strip().upper())

'''open and close the file while storing the lines in a list'''
print()
file = open("spider.txt")
lines = file.readlines()
file.close()
lines.sort()
print(lines)

'''create a file while deleting its old contents'''
with open("novel.txt", "w") as file:
    file.write("It was a dark and stormy night")
    