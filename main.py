import board
import audiomp3
import audioio

data = open("cplay-16bit-16khz-64kbps.mp3", "rb")
mp3 = audiomp3.MP3Decoder(data)
a = audioio.AudioOut(board.A0)

print("playing")
a.play(mp3)
while a.playing:
    pass
print("stopped")
