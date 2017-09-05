# wave_markers
Python3 script to add cue markers to a wave file

## Usage

1. Load a 32-bit 48000 wav file in Audacity.
2. Use Command-B in Audacity to add labels.
3. Export labels as file with File -> Export Labels
4. Create new wave file using original source and label file.

```
$ python add_markers.py -w foo.wav -l foo.txt -o mg4.wav
``` 

## Current limitations

I made this to dump wave files with cues to the [Make Noise Morphagene](http://makenoisemusic.com/modules/morphagene). It works for me, but it's not perfect....

- Some parts of the wave file aren't included in the output wave file. The WAV format includes varied chunk names and unrecognized chunks are discarded. 
- Generated wave file sounds distorted on a computer. It plays fine on my modular, but macOS plays the file poorly. This could be due to discarded wave file chunks (as mentioned earlier) that don't make it in the generated audio file, or due to some other aspect of how the file is rewritten through the wave library. Morphagene reads them OK, though.
- I have seen a few splices not make it out and I'm not sure why. Seems like it might be related to audio files that were too big for Morphagene, but this needs more testing. The splices that are lost seem to always be the at the end.

## Credit to others
I'm taking advantage of a repo from the github user josephernest's modifications to the scipy/io library for wave files. The only changes I made was to add support for python3.

https://github.com/josephernest/wavfile.py/blob/master/wavfile.py?utf8=✓

https://github.com/scipy/scipy/blob/master/scipy/io/wavfile.py

