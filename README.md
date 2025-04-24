
# 🗣️ asr_with_speaker

**Transcription with speaker diarization using Whisper – runs locally and is GDPR-compliant.**

---

## 📋 Features

- Automatic speech recognition (ASR) with [Whisper](https://github.com/openai/whisper)
- Speaker diarization using [pyannote.audio](https://github.com/pyannote/pyannote-audio)
- Works entirely offline (after initial model download)
- Saves output in both `.txt` and `.json`
- Temporary audio chunks are automatically cleaned up

---

## ✅ Requirements

- Python 3.10
- `ffmpeg`
- Compatible OS: Linux, Windows, macOS

---

## 🛠️ Installation

### 1. Clone this repository

```bash
git clone https://github.com/Coding-Frettchen/asr_with_speaker.git
cd asr_with_speaker
```

### 2. Install Python

#### Windows:

- Download the installer from [python.org/downloads](https://www.python.org/downloads/windows/)
- During installation, make sure to check: ✅ *Add Python to PATH*
- Recommended: Install Python 3.10.x (not higher)

#### Linux (Ubuntu/Debian):

```bash
sudo apt update
sudo apt install python3.10 python3.10-venv python3-pip
```

### 3. Install `ffmpeg`

#### Windows:

- Download from [ffmpeg.org/download](https://ffmpeg.org/download.html) → Windows builds by Gyan.dev
- Extract the ZIP to `C:\ffmpeg`
- Add `C:\ffmpeg\bin` to your **System PATH**:
  - Open "Environment Variables"
  - Under "System variables", find "Path", click "Edit", and add the full path to `ffmpeg\bin`

To verify, open a terminal (cmd or PowerShell) and run:

```bash
ffmpeg -version
```

#### Linux (Ubuntu/Debian):

```bash
sudo apt update
sudo apt install ffmpeg
```

To verify:

```bash
ffmpeg -version
```

---

### 4. Install Python packages

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

Start the script by running:

```bash
python asr_with_speaker.py
```

When prompted, enter the path to your Audio-file (mp3; wav).

---

## 🗂️ Output

You will get:

- `transcript.txt` – readable transcript with speaker labels
- `transcript.json` – structured version with timestamps and speaker metadata

---

## 🔐 GDPR Notice

All processing is done **locally**. No data is sent to external servers.

---

## 🧪 Tested With

- Python 3.10
- Whisper 20231117
- pyannote.audio 3.1.1
- ffmpeg 6.1.1

---

## 📄 License

MIT – see [LICENSE](LICENSE)
```

---

Sag Bescheid, wenn du zusätzlich:
- Beispiel-Screenshots,
- eine Demo-Datei,
- oder Schritt-für-Schritt-Bildanleitungen willst.
