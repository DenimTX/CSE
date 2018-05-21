import winsound

notes = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}


def play_note(note, duration=250):
    winsound.Beep(int(256 * (2 ** (notes[note] / 12))), duration)


song = "A A A B A A E A A B B B A B A B A A"
for note in song.split():
    play_note(note)
