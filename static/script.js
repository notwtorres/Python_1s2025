let isRecording = false;
let mediaRecorder = null;
let audioChunks = [];

const recordButton = document.getElementById('recordButton');
const transcriptionDiv = document.getElementById('transcription');

recordButton.addEventListener('click', async () => {
    if (!isRecording) {
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
            mediaRecorder = new MediaRecorder(stream); // default to audio/webm

            audioChunks = [];

            mediaRecorder.ondataavailable = (event) => {
                if (event.data.size > 0) {
                    audioChunks.push(event.data);
                }
            };

            mediaRecorder.onstop = async () => {
                const webmBlob = new Blob(audioChunks, { type: 'audio/webm' });
                const formData = new FormData();
                formData.append('audio', webmBlob, 'recording.webm');

                try {
                    const response = await fetch('/transcribe', {
                        method: 'POST',
                        body: formData
                    });

                    const result = await response.json();
                    transcriptionDiv.textContent = result.text || `Error: ${result.error}`;
                    console.log("✅ Transcription result:", result);
                } catch (error) {
                    transcriptionDiv.textContent = 'Request failed: ' + error.message;
                }
            };

            mediaRecorder.start();
            recordButton.textContent = 'Stop Recording';
            recordButton.classList.add('recording');
            isRecording = true;
        } catch (err) {
            transcriptionDiv.textContent = 'Microphone access error: ' + err.message;
        }
    } else {
        mediaRecorder.stop();
        recordButton.textContent = 'Start Recording';
        recordButton.classList.remove('recording');
        isRecording = false;
    }
});


