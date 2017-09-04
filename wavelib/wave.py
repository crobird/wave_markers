#!/usr/bin/env python

"""
Simple interface to wavfile's read function, printing out the details of a wav file
"""

from . import wavfile


class Wave(object):

	def __init__(self, filename, readmarkers=False, readmarkerlabels=False, readmarkerslist=False,
								 readloops=False, readpitch=False, normalized=False, forcestereo=False):
		self.filename         = filename
		self.readmarkers      = readmarkers
		self.readmarkerlabels = readmarkerlabels
		self.readmarkerslist  = readmarkerslist
		self.readloops        = readloops
		self.readpitch        = readpitch
		self.normalized       = normalized
		self.forcestereo      = forcestereo
		self.rate             = None
		self.data             = None
		self.bits             = None
		self.markers          = None
		self.markerlabels     = None
		self.markerslist      = None
		self.loops            = None
		self.pitch            = None

		self.rate, self.data, self.bits, *all_else = wavfile.read(filename, 
			readmarkers=readmarkers, readmarkerlabels=readmarkerlabels, readmarkerslist=readmarkerslist, 
			readloops=readloops, readpitch=readpitch)

		# Set self vars for wavfile output
		for name in ["readmarkers", "readmarkerlabels", "readmarkerslist", "readloops", "readpitch"]:
			if getattr(self, name):
				setattr(self, name[4:], all_else.pop(0))

	def __repr__(self):
		outlines = []
		for name in ["rate", "data", "bits", "markers", "markerlabels", "markerslist", "loops", "pitch"]:
			item = getattr(self, name)
			if (hasattr(item, "size") and item.size) or item:
				outlines.append("{}: {}".format(name, item))
		return "\n".join(outlines)

	def write(self, filename, markers=None, loops=None, pitch=None, normalized=False):
		# wavfile.write(filename, self.rate, self.data, self.bits, markers=markers, loops=loops, pitch=pitch, normalized=normalized)
		wavfile.write(filename, self.rate, self.data, markers=markers)


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

