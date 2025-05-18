from flask import Flask, render_template, request, jsonify
import speech_recognition as sr
import os
from pydub import AudioSegment
from werkzeug.utils import secure_filename
import logging

app = Flask(__name__)

# Logging setup
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transcribe', methods=['POST'])
def transcribe():
    if 'audio' not in request.files:
        logger.error("No audio file provided")
        return jsonify({'error': 'No audio file provided'}), 400

    audio_file = request.files['audio']
    filename = secure_filename(audio_file.filename)
    webm_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    wav_path = webm_path.replace('.webm', '.wav')

    audio_file.save(webm_path)
    logger.info(f"📥 Received and saved file: {webm_path}")

    try:
        # Convert webm to wav
        audio = AudioSegment.from_file(webm_path, format="webm")
        audio.export(wav_path, format="wav")
        logger.info(f"✅ Converted to WAV: {wav_path}")

        # Transcribe with speech_recognition
        recognizer = sr.Recognizer()
        with sr.AudioFile(wav_path) as source:
            audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
        logger.info("✅ Transcription complete")

        return jsonify({'text': text})
    
    except sr.UnknownValueError:
        logger.warning("Speech was not understood")
        return jsonify({'error': 'Could not understand the audio'}), 400
    except sr.RequestError as e:
        logger.error(f"Speech recognition error: {e}")
        return jsonify({'error': f'Speech recognition error: {e}'}), 500
    except Exception as e:
        logger.exception("Unexpected error")
        return jsonify({'error': f'Unexpected error: {str(e)}'}), 500
    finally:
        # Cleanup
        for f in [webm_path, wav_path]:
            if os.path.exists(f):
                os.remove(f)
                logger.info(f"🧹 Deleted: {f}")

if __name__ == '__main__':
    app.run(debug=True)
