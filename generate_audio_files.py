import os
import sounddevice as sd
import soundfile as sf

# Phrases and filenames
transcriptions = {
    '01.wav': 'amakuru',
    '02.wav': 'mwaramutse',
    '03.wav': 'sawa',
    '04.wav': 'umeze ute',
    '05.wav': 'ndarwaye',
    '06.wav': 'ndishimye',
    '07.wav': 'witwa nde',
    '08.wav': 'ukora iki',
    '09.wav': 'nkeneye ubufasha',
    '10.wav': 'Rwanda Coding Academy iherereye he?',
}

# Output folder
os.makedirs( 'audio_samples', exist_ok = True )

def record_audio( file, duration = 3, sample_rate = 16000 ):
    print( f'🎙️ Vuga: "{ transcriptions[ file ] }"' )
    print( '👉 Turimo gufata amajwi... tangira kuvuga!' )
    
    recording = sd.rec( int( duration * sample_rate ), samplerate = sample_rate, channels = 1, dtype = 'int16' )
    sd.wait()  # Wait until recording is finished

    filepath = f'audio_samples/{ file }'
    sf.write( filepath, recording, sample_rate )
    print( f'✅ Amajwi abitswe nka: { filepath }\n' )

for file in transcriptions:
    input( '>> Kanda "Enter" igihe witeguye gufata ijwi...' )
    record_audio( file )

print( '🎉 Amajwi yose yafashwe, abitswe muri "audio_samples/"' )