#!/usr/bin/env python3

import argparse


def read_IOB_tags(infiles):
	a = dict()
	with open(infiles, "r", encoding="utf-8") as infile:
		contents = infile.readlines()
		i = 0
		for lines in contents:
			a[i] = lines.strip("\n").split()
			i+=1
	return a


def convert_to_IOBES(iob_Format):
	iobes_Format = dict()
	for id in iob_Format:
		data = iob_Format[id]
		new_data = []
		l = len(data)
		for i, tag in enumerate(data):
			if i+1 == l or data[i+1][0] != "I":
				if tag[0] == "B":
					new_data.append("S"+tag[1:])
				elif tag[0] == "I":
					new_data.append("E"+tag[1:])
				else:
					new_data.append(tag)
			else:
				new_data.append(tag)
		iobes_Format[id] = new_data
	return iobes_Format


train_tags = []
train_sentences = []
test_sentences = []
test_tags = []


def get_train_tags(infile):
	with open(infile, "r", encoding="utf-8") as ifile:
		contents = ifile.readlines()
		for lines in contents:
			if lines != "\n":
				sentence = []
				sent_tag = []
				data = lines.strip("\n").split("\t")[1:]
				for elements in data:
					form, upos, tag = elements.split()
					sentence.append(form)
					if tag == "0":
						sent_tag.append("O")
					else:
						sent_tag.append(tag)
				train_sentences.append(sentence)
				train_tags.append(sent_tag)

				
def get_test_tags(infile):
	with open(infile, "r", encoding="utf-8") as ifile:
		contents = ifile.readlines()
		sentence = []
		tags = []
		for lines in contents:
			if lines == "\n":
				test_sentences.append(sentence)
				test_tags.append(tags)
				sentence = []
				tags = []
			else:
				word, tag = lines.strip("\n").split("\t")
				sentence.append(word)
				tags.append(tag)
		test_sentences.append(sentence)
		test_tags.append(tags)

		
if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	group0 = parser.add_mutually_exclusive_group(required=True)
	group0.add_argument("--train", action='store_true', help="Generate the training data")
	group0.add_argument("--test", action='store_true', help="Generate the testing data")
	group0.add_argument("--convert", action='store_true', help="Convert to IOBES from IOB dataset")
	parser.add_argument("--input", type=str, help="Input file for the data")
	args = parser.parse_args()
	
	if args.test:
		get_test_tags(args.input)
		with open("test.words.txt", "w", encoding="utf-8") as wordsfile:
			for i in range(len(test_sentences)):
				wordsfile.write(" ".join(test_sentences[i])+"\n")
		with open("test.tags.txt", "w", encoding="utf-8") as tagsfile:
			for i in range(len(test_tags)):
				tagsfile.writelines(" ".join(test_tags[i])+"\n")
	elif args.train:
		get_train_tags(args.input)
		with open("train.words.txt", "w", encoding="utf-8") as wordsfile:
			for i in range(len(train_sentences)):
				wordsfile.write(" ".join(train_sentences[i])+"\n")
		with open("train.tags.txt", "w", encoding="utf-8") as tagsfile:
			for i in range(len(train_tags)):
				tagsfile.write(" ".join(train_tags[i])+"\n")
	else:
		iob_Format = read_IOB_tags(args.input)
		new_Data = convert_to_IOBES(iob_Format)
		with open(args.input.replace(".txt", "_IOBES.txt"), "w", encoding="utf-8") as outfile:
			for id in new_Data:
				outfile.write(" ".join(new_Data[id]) + "\n")
# testfile= senseval3.tsv
# trainfile = SEM.BI
