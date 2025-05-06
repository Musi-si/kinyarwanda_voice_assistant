from asr import transcribe_audio
from nlp import get_response
from tts import speak

def choose_input_method():
    speak( 'Hitamo uburyo bwo kuganira.' )
    print( '1. Gukoresha amajwi abitse.' )
    print( '2. Gufata amajwi ukoresheje mikoro.' )
    choice = input( 'Andika 1 cyangwa 2: ' ).strip()
    return choice

audio_files = [
    'audio_samples/01.wav',
    'audio_samples/02.wav',
    'audio_samples/03.wav',
    'audio_samples/04.wav',
    'audio_samples/05.wav',
    'audio_samples/06.wav',
    'audio_samples/07.wav',
    'audio_samples/08.wav',
    'audio_samples/09.wav',
    'audio_samples/01.wav',
    'audio_samples/10.wav'
]

speak( 'Murakaza neza! Tangira kuganira. Vuga "rekera aho" kugira ngo uhagarike.' )

choice = choose_input_method()

if choice == '1':
    for audio in audio_files:
        text = transcribe_audio( audio )
        print( f'Transcription: { text }' )

        if 'rekera aho' in text.lower():
            speak( 'Sawa turasubira' )
            break

        response = get_response( text )
        speak( response )
        
elif choice == '2':
    while True:
        text = transcribe_audio()
        print( f'Transcription: { text }' )

        if 'rekera aho' in text.lower():
            speak( 'Sawa turasubira' )
            break

        response = get_response( text )
        speak( response )

else:
    speak( 'Ongera uhitemo neza hagati ya 1 na 2 gusa.' )