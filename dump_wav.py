#!/usr/bin/env python

"""
Simple interface to wavfile's read function, printing out the details of a wav file
"""

from wavelib import Wave


def dump_wav(filename, args):
	# Build options list to send to wavfile
	optnames = ["readmarkers", "readmarkerlabels", "readmarkerslist", "readloops", "readpitch", "normalized", "forcestereo"]
	opts = {x:True for x in filter(args.__getattribute__, optnames)}

	w = Wave(filename, **opts)
	print(w)


if __name__ == '__main__':
	import argparse

	parser = argparse.ArgumentParser()
	parser.add_argument('file', nargs=1, help="WAV file to debug")
	parser.add_argument('--readmarkers', default=False, action="store_true", help="Read markers")
	parser.add_argument('--readmarkerlabels', default=False, action="store_true", help="Read marker labels")
	parser.add_argument('--readmarkerslist', default=False, action="store_true", help="Read markers list")
	parser.add_argument('--readloops', default=False, action="store_true", help="Read loops")
	parser.add_argument('--readpitch', default=False, action="store_true", help="Read pitch")
	parser.add_argument('--normalized', default=False, action="store_true", help="Normalized")
	parser.add_argument('--forcestereo', default=False, action="store_true", help="Force stereo")

	args = parser.parse_args()
	w = Wave(args.file[0], readmarkers=args.readmarkers, readmarkerlabels=args.readmarkerlabels, readmarkerslist=args.readmarkerslist,
		readloops=args.readloops, readpitch=args.readpitch, normalized=args.normalized, forcestereo=args.forcestereo)

	print(w)

	# dump_wav(args.file[0], args)