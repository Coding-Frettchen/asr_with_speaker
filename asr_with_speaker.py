import os
import shutil
import tempfile
import glob
import torch
import torchaudio
import json
from tqdm import tqdm
from pyannote.audio import Pipeline
import whisper

width = shutil.get_terminal_size().columns


def diarize_and_transcribe(audio_path):
    tmpdir = tempfile.mkdtemp()
    chunk_dir = os.path.join(tmpdir, "chunks")
    os.makedirs(chunk_dir, exist_ok=True)

    print("-" * width)
    print("[*] Audio wird in Stücke geteilt ...")
    print()
    os.system(f"ffmpeg -i '{audio_path}' -f segment -segment_time {CHUNK_DURATION} "
              f"-ar 16000 -ac 1 -sample_fmt s16 -c:a pcm_s16le '{chunk_dir}/chunk_%03d.wav'")

    # Sprecher-Diarisation vorbereiten
    print("-" * width)
    print("[*] Lade Sprecher-Diarisation...")
    print()
    diar_pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization", use_auth_token=HF_TOKEN)

    # Whisper-Modell laden
    model = whisper.load_model("large") # Other Models are 'medium', 'base', 'small'
    print("-" * width)
    print(f"[*] Lade Whisper-Modell...... {modle}")
    print()
    

    full_transcript = []
    json_output = []

    chunk_paths = sorted(glob.glob(f"{chunk_dir}/chunk_*.wav"))
    print(f"[*] Verarbeite {len(chunk_paths)} Chunks ...")

    for idx, chunk_path in enumerate(tqdm(chunk_paths, desc="Transkription")):
        diar_result = diar_pipeline(chunk_path)
        result = model.transcribe(chunk_path, fp16=torch.cuda.is_available())

        for turn in diar_result.itertracks(yield_label=True):
            segment, _, speaker = turn
            start = segment.start
            end = segment.end

            text = result['text'].strip()

            full_transcript.append(f"{speaker}: {text}")
            json_output.append({
                "speaker": speaker,
                "start": start,
                "end": end,
                "text": text
            })

    # Ergebnisse speichern
    with open(OUTPUT_TXT, "w", encoding="utf-8") as f:
        f.write("\n".join(full_transcript))

    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(json_output, f, indent=2, ensure_ascii=False)

    shutil.rmtree(tmpdir)
    
    print("-" * width)
    print(f"[*] Transkription abgeschlossen. Ergebnisse in '{OUTPUT_TXT}' und '{OUTPUT_JSON}' gespeichert.")

if __name__ == "__main__":
    path = input("File Path: ").strip()
    output_name = input("Name Output Files (empty for Input-Name): ")
    diarize_and_transcribe(path)

# Konfiguration
HF_TOKEN = "Hugging_Face_ReadToken" #Replace with your Hugging Face token
CHUNK_DURATION = 10  # in seconds 
OUTPUT_TXT = f"{output_name}.txt"
OUTPUT_JSON = f"{output_name}-1.json"
