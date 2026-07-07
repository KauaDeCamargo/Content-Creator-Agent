from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
import groq
import json

load_dotenv()

def transcribe_video():
    videos_dir = Path('videos')
    client = Groq()
    transcriptions = {}

    for creator_dir in videos_dir.iterdir():
        creator_name = creator_dir.name

        transcriptions[creator_name] = []

        for video_file in creator_dir.glob('*.mp4'):
            print(f'Processando: {video_file}')

            try:
                response = client.audio.transcriptions.create(
                    model='whisper-large-v3',
                    file=Path(video_file),
                    response_format='text'
                )
                transcriptions[creator_name].append({
                    'video': video_file.name,
                    'transcription': response
                })
            except groq.APIError as e:
                print(f'Erro ao processar {video_file}: {e}')
    
    with open('transcriptions.json', 'w', encoding='utf-8') as f:
        json.dump(transcriptions, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    transcribe_video()