# HealthCare Assistant

HealthCare Assistant is a Python desktop chatbot that provides general health information through a Tkinter interface. It combines simple pattern matching with a TensorFlow/Keras intent-classification model and chooses responses from `intents.json`.

> **Medical disclaimer:** This project is for educational and informational purposes only. It does not diagnose conditions, prescribe treatment, or replace a qualified healthcare professional. For an emergency, contact your local emergency service immediately.

## Features

- Dark-themed Tkinter desktop interface
- Intent recognition using pattern matching and a trained TensorFlow/Keras model
- Text tokenisation, lemmatisation, and bag-of-words processing with NLTK
- General responses for greetings, symptoms, prevention, and consultation-related questions
- Timestamps for messages and session chat history
- New conversation, clear-chat, Enter-key, and Send-button controls
- Optional terminal mode through `chatbot_py.py`
- Included trained model and preprocessing files
- Exploratory healthcare dataset notebook

## How It Works

```text
User message
    ↓
NLTK tokenisation and lemmatisation
    ↓
Known-pattern matching
    ↓ (if no reliable match)
Bag-of-words + TensorFlow intent prediction
    ↓
Response selected from intents.json
    ↓
Displayed in the Tkinter interface
```

Pattern matching handles close matches first. If it cannot find a reliable match, the neural-network model predicts the most likely intent.

## Project Structure

| File | Purpose |
| --- | --- |
| `gui.py` | Tkinter desktop application and chat interface |
| `chatbot_py.py` | Preprocessing, intent prediction, pattern matching, and response generation |
| `training_py.py` | Trains the TensorFlow/Keras intent model |
| `intents.json` | Intent tags, example patterns, and response text |
| `chatbotmodel.h5` | Pre-trained Keras model used by the application |
| `words.pkl` | Saved model vocabulary |
| `classes.pkl` | Saved intent labels |
| `Data_Analysis.ipynb` | Exploratory analysis notebook |
| `heart-disease.csv` | Dataset used by the analysis notebook |
| `chat.txt` | Project/chat notes |
| `LICENSE` | License information |

## Requirements

- Python 3.10 or newer
- TensorFlow
- NLTK
- NumPy
- Pandas
- Tkinter (usually included with Python on Windows)

On Linux, install Tkinter through your distribution's package manager if it is not already available.

## Installation

Open PowerShell in the project directory and create a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the dependencies:

```powershell
python -m pip install --upgrade pip
python -m pip install tensorflow nltk numpy pandas
```

The chatbot downloads the required NLTK resources (`punkt`, `punkt_tab`, `wordnet`, and `omw-1.4`) automatically the first time it starts. An internet connection may be required during that first run.

## Run the Desktop App

```powershell
python gui.py
```

Type a health-related question and press **Enter** or click **Send**. For example:

- `What are the symptoms of a common cold?`
- `How can I prevent fever?`
- `What is your name?`

## Run in Terminal Mode

For a simple command-line conversation, run:

```powershell
python chatbot_py.py
```

Type a message and press **Enter** to receive a response. Stop the program with `Ctrl+C`.

## Retrain the Model

1. Add or edit intent patterns and responses in `intents.json`.
2. Run the training script from the project directory:

   ```powershell
   python training_py.py
   ```

The script regenerates `words.pkl`, `classes.pkl`, and `chatbotmodel.h5`. Back up the existing model files first if you want to keep the current model. After training, run `gui.py` to test the updated model.

## Limitations and Safety

The chatbot only knows the intents and responses defined in `intents.json`. Its answers may be incomplete or inaccurate, and it does not maintain medical context across conversations. Do not use it for self-diagnosis, emergency decisions, or medication changes without professional guidance.

## Future Improvements

- Hindi and English language support
- Emergency-symptom detection with prominent safety guidance
- Conversation export and user feedback
- Multi-turn conversation context
- Confidence-aware fallback responses
- Automated tests and model evaluation

## License

See [LICENSE](LICENSE) for licensing information.
