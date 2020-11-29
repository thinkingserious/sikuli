from sikuli import *

# Sample text: https://en.m.wikipedia.org/wiki/File:AMS_Euler_sample_text.svg
r = selectRegion()
words = r.text()
print(words)