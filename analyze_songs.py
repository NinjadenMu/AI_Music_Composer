from mido import MidiFile
import pandas as pd
import time
import mido

mid = MidiFile('composition.mid')

tracks = [[] for track in enumerate(mid.tracks)]

for i, track in enumerate(mid.tracks):
    for message in track:
        tracks[i].append(message)

tracks[0] = tracks[0][10:-1]

parsed_notes = []

i = 0

for i in range(len(tracks[0]) - 1):
    if tracks[0][i].type == 'note_on' and tracks[0][i].velocity != 0:
        print(i)
        parsed_notes.append([tracks[0][i].note])
        parsed_notes[int(i / 2)].append(tracks[0][i].velocity)
        parsed_notes[int(i / 2)].append(tracks[0][i + 1].time)

print(parsed_notes)







