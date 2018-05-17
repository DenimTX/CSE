import winsound

notes = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}


def play_note(note, duration=250):
    winsound.Beep(int(256 * (2 ** (notes[note] / 12))), duration)


song = "E D C D E E E D D D C C C"
for note in song.split():
    play_note(note)

song1 = "E D C D E E E E D D E D C"
for note in song1.split():
    play_note(note)
