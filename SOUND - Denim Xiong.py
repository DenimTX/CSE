import winsound

notes = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}


def play_note(note, duration=500):
    winsound.Beep(int(256 * (2 ** (notes[note] / 12))), duration)


song = "E D E D E G D C A C E A B E A B C E D E D E B D C A C E A B E B C A B C D E G F E D"
for note in song.split():
    play_note(note)
