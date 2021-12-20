import random
import os

base_filename = "file_"
word_file = "/usr/share/dict/words"
words = open(word_file).read().splitlines()
symbols = ["°", "'", "\""]

for i in range(6):
	os.mkdir("test" + str(i))
	for j in range(100):
		f = open("test" + str(i) + "/" + base_filename + str(j) + ".txt", "w")
		f.write(random.choice(words) + " ")
		f.write(str(random.randint(3,120)) + "." + str(random.randint(0,99)))
		f.write(random.choice(symbols))
		f.write("\n")
		f.close()
