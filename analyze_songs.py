from mido import MidiFile
import pandas as pd
import time
import mido

mid = MidiFile('river_flows_in_you.mid')

tracks = [[] for track in enumerate(mid.tracks)]

for i, track in enumerate(mid.tracks):
    for message in track:
        tracks[i].append(message)

tracks[1] = tracks[1][8:]

parsed_notes = []

i = 0

for i in range(len(tracks[1]) - 1):
    if tracks[1][i].type == 'note_on':
        print(i)
        parsed_notes.append([tracks[1][i].note])
        parsed_notes[int(i / 2)].append(tracks[1][i].velocity)
        parsed_notes[int(i / 2)].append(tracks[1][i + 1].time)

print(parsed_notes)







