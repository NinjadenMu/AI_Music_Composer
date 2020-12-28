from mido import MidiFile
import random
import mido
import copy
import pygame

mid = MidiFile('river_flows_in_you.mid')

tracks = [[] for track in enumerate(mid.tracks)]

for i, track in enumerate(mid.tracks):
    for message in track:
        tracks[i].append(message)

tracks_original = copy.deepcopy(tracks)
tracks[1] = tracks[1][7:]

parsed_notes = []

i = 0

while i < len(tracks[1]):
    if tracks[1][i].type != 'note_on':
        tracks[1].pop(i)
        i -= 1

    i += 1

for i in range(len(tracks[1]) - 1):
    if tracks[1][i].type == 'note_on':
        parsed_notes.append([tracks[1][i].note])
        parsed_notes[-1].append(round(tracks[1][i].velocity, -1))
        parsed_notes[-1].append(round(tracks[1][i + 1].time, -1))

#print(parsed_notes)

no_duplicates = []
future_notes = []

for i in range(len(parsed_notes)):  
    if parsed_notes[i] not in no_duplicates:
        no_duplicates.append(parsed_notes[i])
        future_notes.append([])

for i in range(len(parsed_notes) - 1):
    for j in range(len(no_duplicates)):
        if parsed_notes[i] == no_duplicates[j]:
            future_notes[j].append(parsed_notes[i + 1])

future_notes.pop(-1)
prev_note = random.choice(parsed_notes)
length = int(input('\nHow long do you want the composition to be? \n'))
composition_parsed = []

cap_index = len(future_notes)

for i in range(length + 1):
    composition_parsed.append(prev_note)
    index = no_duplicates.index(prev_note)
    if index == cap_index:
        prev_note = random.choice(no_duplicates)
    else:
        prev_note = random.choice(future_notes[index])

composition_parsed[0][2] = 10

with MidiFile() as output:
    track = mido.MidiTrack()

    for i in range(len(composition_parsed)):
        if composition_parsed[i][1] > 127:
            composition_parsed[i][1] = 127 # prevent invalid values
        
        if composition_parsed[i][0] > 75:
            track.append(mido.Message('note_on', note = composition_parsed[i][0], velocity = composition_parsed[i][1], time = 1))
        
        else:
            track.append(mido.Message('note_on', note = composition_parsed[i][0], velocity = composition_parsed[i][1], time = 1))

        if composition_parsed[i][2] < 100:
            track.append(mido.Message('note_off', note = composition_parsed[i][0], velocity=0, time = composition_parsed[i][2] * 10))
        
        elif composition_parsed[i][2] < 250:
            track.append(mido.Message('note_off', note = composition_parsed[i][0], velocity=0, time = composition_parsed[i][2] * 5)) 
        
        else:
           track.append(mido.Message('note_off', note = composition_parsed[i][0], velocity=0, time = composition_parsed[i][2] * 2)) 

    output.tracks.append(track)
    output.save('output.mid')

pygame.init()
pygame.mixer.music.load("output.mid")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.wait(pygame.time.get_ticks() + 10)
















