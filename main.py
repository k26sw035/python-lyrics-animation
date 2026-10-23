import sys
import time


def typewriter_line(text, char_delay=0.07):
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(char_delay)
  print()


def play_lyrics():
  lyrics = [
      ("Tu hai kahan...", 0.08, 0.8),
      ("Khwaabon ke iss jahan mein...", 0.07, 0.6),
      ("Main dhoondoon tujhe har jagah...", 0.07, 0.7),
      ("Kya tum sun rahe ho?", 0.08, 1.0),
  ]

  print("\n--- 🎵 Python Lyrics Animation 🎵 ---\n")
  time.sleep(1)

  for line, speed, pause in lyrics:
    typewriter_line(line, char_delay=speed)
    time.sleep(pause)

  print("\n-------------------------------------\n")


if __name__ == "__main__":
  play_lyrics()
