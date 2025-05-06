from speechbrain.inference.ASR import EncoderDecoderASR
import torchaudio
import speech_recognition as sr

torchaudio.set_audio_backend( 'soundfile' )

asr_model = EncoderDecoderASR.from_hparams(
    source = 'speechbrain/asr-wav2vec2-commonvoice-rw',
    savedir = 'pretrained_models/asr-wav2vec2-commonvoice-rw'
)

def transcribe_audio( audio_path = None ):
    if audio_path:
        return asr_model.transcribe_file( audio_path )
    else:
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print( 'Gira icyo uvuga ...' )
            audio = recognizer.listen( source )

        try:
            with open( 'input.wav', 'wb' ) as f:
                f.write( audio.get_wav_data() )
            
            return asr_model.transcribe_file( 'input.wav' )
        except Exception as e:
            return 'Simbashije kukumva neza.'