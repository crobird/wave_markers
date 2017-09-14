#!/usr/bin/env python

"""
This script will take a wavefile and the labelfile output from Audacity as input 
and output a wavefile with the labels embedded as cue points.

Cue labels are written into the wavfile, but note that only the starting time is
used for the cue time. The ending time is ignored.
"""

import os.path
from math import floor
from wavelib import Wave


def get_wave_labels(bitrate, labelfile):
	labelfile_data = []
	with open(labelfile, "r") as fh:
		for line in fh:
			if not line.strip():
				continue
			start, end, *label = line.strip().split("\t")
			position = floor(bitrate * float(start))
			if label:
				labelfile_data.append({"position": position, "label": label[0]})
			else:
				labelfile_data.append(position)
	return labelfile_data


def main(args):
	w = Wave(args.wavefile)
	wave_labels = get_wave_labels(w.rate, args.labelfile)
	w.write(args.outfile, markers=wave_labels)


if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('-w', '--wavefile', help="Input wave file", required=True)
	parser.add_argument('-l', '--labelfile', help="Audacity label file", required=True)
	parser.add_argument('-o', '--outfile', help="Output file", required=True)

	args = parser.parse_args()

	if not os.path.isfile(args.wavefile):
		print("Error: '{}' isn't a file".format(args.wavefile))
		exit(1)

	if not os.path.isfile(args.labelfile):
		print("Error: '{}' isn't a file".format(args.labelfile))
		exit(1)

	main(args)