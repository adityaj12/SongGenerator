import pysynth

song = []
while True:
  note = input("Enter a note to add to your song (Press 1 to quit): ")
  if note == '1':
    break
  dur = int(input("How long do you want this note to last? "))
  song.append((note, dur))

pysynth.make_wav(song, fn = "song.wav")