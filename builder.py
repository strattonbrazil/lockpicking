import random

from os import listdir
from pydub import AudioSegment
from progress.bar import Bar

# returns a list of files to concatenate
def get_file_stream():
    paths = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    files = []

    files.append("intro.mp3")
    files.append("see_what_it_takes.mp3")
    files.append("tension.mp3")

    passes = 200
    for passNum in range(passes):
        for path in paths:
            file = random.choice(listdir(path))
            files.append(path + "/" + file)

            if "binding" in files[-1] and random.random() < 0.05:
                files.append("a_lot_of_core.mp3")

        files.append("backwards.mp3")

        for path in list(reversed(paths))[1:-1]:
            file = random.choice(listdir(path))
            files.append(path + "/" + file)

            if random.random() < 0.05:
                files.append("there_we_go.mp3")

    files.append("victory.mp3")
    files.append("a_few_minutes.mp3")
    files.append("closing.mp3")

    return files

def paths_to_mp3(paths, output_path):
    with Bar('Combining mp3 files', max=len(paths), suffix='%(percent)d%%  - %(eta)ds') as bar:
        first_sound = None
        for path in paths:
            sound = AudioSegment.from_mp3(path)
            if not first_sound:
                first_sound = sound
            else: # tack it on
                first_sound += sound
            bar.next()

    print("writing file to: " + output_path)
    first_sound.export(output_path, format="mp3")

files = get_file_stream()
print(files)
paths_to_mp3(files, "/tmp/out.mp3")