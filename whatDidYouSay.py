import os
import whisper
import json
import time
startTime = time.time()
model = whisper.load_model("base.en")
# assign directory
directory = 'C://users/moult/documents/making gold/audio/untranscribed'
newPath = 'C://users/moult/documents/making gold/audio/transcribed'
for filename in os.listdir(directory):
    #if the proper file type then process it
    if filename.lower().endswith(('.wav', '.mp3')):
        f = os.path.join(directory, filename)
        print('processing: ', filename)
        result = model.transcribe(f)
        print('transcription complete')
        extensionlessFilename = filename.split('.')[0]
        transcriptionFilePath = 'C://users/moult/documents/making gold/audio/_transcriptions/'+ extensionlessFilename + '.json'
        with open(transcriptionFilePath, "w") as tf:
            json.dump(result,tf)
        tf.close()
        print('transcription saved, moving file now')
        print(f)
        os.rename(f, os.path.join(newPath,filename))
        print('time elapsed: ', time.time() - startTime)
    else:
        print('skipping: ', filename)
stopTime = time.time()
print('total time elapsed: ', stopTime - startTime)
