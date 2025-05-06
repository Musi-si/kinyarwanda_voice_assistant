from gtts import gTTS
from pydub import AudioSegment
import os

# Mapping of filenames to Kinyarwanda transcriptions
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

for filename, text in transcriptions.items():
    print( f'Generating { filename } for text: { text }' )

    # gTTS generates mp3
    tts = gTTS( text = text, lang = 'sw' )
    mp3_path = f'audio_samples/{ filename.replace( '.wav', '.mp3' ) }'
    wav_path = f'audio_samples/{ filename }'

    tts.save( mp3_path )

    # Convert mp3 to wav
    sound = AudioSegment.from_mp3( mp3_path )
    sound.export( wav_path, format = 'wav' )

    # Optional: remove intermediate mp3
    os.remove( mp3_path )

print( '✅ All WAV files generated in "audio_samples/"' )