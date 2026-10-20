# HealthCare Assistant

HealthCare Assistant is a desktop healthcare information chatbot built with Python, Tkinter, Natural Language Toolkit (NLTK), and TensorFlow. It recognises common health-related questions and returns educational responses through a simple graphical interface.

> **Important:** This project is for educational and informational purposes only. It does not diagnose medical conditions, prescribe treatment, or replace a qualified healthcare professional. In an emergency, contact your local emergency service immediately.

## Features

- Desktop chat interface built with Tkinter
- Intent-based natural language classification
- Pattern matching for commonly asked questions
- Responses for general health topics, prevention, greetings, and basic FAQs
- Conversation timestamps and chat history within the current session
- New conversation and clear-chat controls
- Input through the Send button or the Enter key
- Pre-trained TensorFlow/Keras model included in the repository
- Separate dataset analysis notebook for exploratory work

## How It Works

The chatbot follows this workflow:

```text
User message
     |
Text tokenisation and lemmatisation
     |
Pattern matching and bag-of-words generation
     |
TensorFlow intent classification model
     |
Response selection from intents.json
     |
Response displayed in the Tkinter interface
```

The application first attempts to match the message with known intent patterns. If no reliable pattern match is found, the trained neural network predicts the most likely intent and selects a response from `intents.json`.

## Project Structure

| File | Description |
| --- | --- |
| `gui.py` | Tkinter desktop application and chat interface |
| `chatbot_py.py` | Text preprocessing, intent prediction, and response generation |
| `training_py.py` | Script used to train the TensorFlow/Keras intent model |
| `intents.json` | Intent tags, example patterns, and chatbot responses |
| `chatbotmodel.h5` | Saved trained Keras model |
| `words.pkl` | Processed vocabulary used by the model |
| `classes.pkl` | Saved intent labels |
| `heart-disease.csv` | Dataset used for exploratory analysis |
| `Data_Analysis.ipynb` | Notebook for dataset exploration and analysis |
| `LICENSE` | Project license |

## Requirements

- Python 3.10 or newer
- TensorFlow
- NLTK
- NumPy
- Pandas
- Tkinter

Tkinter is included with most standard Python installations on Windows. On Linux, it may need to be installed separately through the operating system package manager.

## Installation

Clone or download the repository, then create and activate a virtual environment:

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the Python dependencies:

```powershell
pip install tensorflow nltk numpy pandas
```

The application downloads the required NLTK resources automatically on first use.

## Run the Application

Start the desktop application with:

```powershell
python gui.py
```

Type a question in the input field and press **Enter** or select **Send**.

Example questions:

- `What are the symptoms of a common cold?`
- `How can I prevent fever?`
- `What is your name?`

## Retraining the Model

To update the chatbot's vocabulary, intent classes, and model, edit `intents.json` and run:

```powershell
python training_py.py
```

This regenerates `words.pkl`, `classes.pkl`, and `chatbotmodel.h5`. Make a backup of the existing model files before retraining if you want to preserve the current version.

## Safety and Limitations

The chatbot provides general educational information based on its predefined intents. Its responses may be incomplete or inaccurate, and it cannot understand every medical situation. Users should not use the application for self-diagnosis, emergency decisions, or medication changes without professional guidance.

## Future Improvements

- Hindi and English language support
- Emergency-symptom detection with prominent safety guidance
- Conversation export and feedback collection
- Improved multi-turn conversation context
- Confidence-aware fallback responses
- Automated model evaluation and test coverage

## License

See the [LICENSE](LICENSE) file for licensing information.
