# Instructions
* run the python script to generate the mp3

* run the following to convert it to a video
```
ffmpeg -loop 1 -framerate 1 -i locksmith.png -i /tmp/out.mp3 -c:v libx264 -preset veryslow -crf 0 -c:a copy -shortest /tmp/out.mkv
```