# Bip Bip Hello Hello

An experiment in AI-to-AI communication through Morse code encoding, simulating conversations between two language models.

## Overview

Bip Bip Hello Hello creates a unique communication channel between two instances of a language model by encoding their responses in Morse code. Each model generates text, which is then converted to Morse code and transmitted to the other model. The receiving model decodes the Morse code back to text and generates a response, creating an iterative conversation loop entirely mediated through dot-dash encoding.

This project explores emergent communication patterns when AI models are forced to communicate through a constrained, historical encoding system rather than direct text exchange.

## Features

- 🤖 **Dual Model Communication**: Two separate instances of TinyLlama communicate independently
- 📡 **Morse Code Encoding/Decoding**: All inter-model communication happens via Morse code
- 🔄 **Iterative Conversations**: Configurable number of conversation turns
- 📊 **Conversation Tracking**: Monitor the full communication chain from text → Morse → text
- ⚡ **Lightweight Models**: Uses TinyLlama-1.1B for efficient processing
- 🎯 **Experimental AI Research**: Investigate constrained communication effects on LLM interactions

## How It Works

1. **Model A** generates initial text response
2. Text is **encoded** into Morse code (`·-·· ·-·· --- ...`)
3. **Model B** receives and **decodes** the Morse code back to text
4. **Model B** generates a response to the decoded message
5. **Model B's** response is **encoded** into Morse code
6. **Model A** receives and **decodes** the Morse code
7. Process repeats for specified number of turns

```
Model A Text → Morse Code → Model B Text → Response
     ↑                                        ↓
Model A Response ← Morse Code ← Model B Response
```

## Technology Stack

- **Language Model**: TinyLlama/TinyLlama-1.1B-Chat-v1.0
- **ML Framework**: Transformers/PyTorch
- **Encoding**: Custom Morse code implementation
- **Language**: Python 3.x

## Installation

### Prerequisites

- Python 3.7+
- PyTorch
- Transformers library
- Sufficient RAM for running TinyLlama models (minimum 4GB recommended)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/mehDktb/Bip_Bip_Hello_Hello.git
   cd Bip_Bip_Hello_Hello
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. The models will be downloaded automatically on first run.

## Usage

### Basic Usage

Run a conversation with default number of turns:
```bash
python main.py
```

### Custom Turn Count

Specify the number of conversation exchanges:
```bash
python main.py --turns 3
```

The `--turns` parameter controls how many times each chatbot receives input and generates output, creating a back-and-forth conversation of the specified length.

### Example Output

```
-------- chatbot 1 ---------------------
said: .. / .- -- / ..-. .. -. . ? / -.. --- .. -. --. / --. --- --- -.. ?
which means: I am fine. Doing good.
-------- chatbot 2 ---------------------
said: .. / .- -- / -.. --- .. -. --. / --. --- --- -.. ? / .. / .... .- ...- . / -... . . -. / .-- --- .-. -.- .. -. --.
which means: I am doing good. I have been working
```

## Parameters

- `--turns` : Number of conversation turns (default: 5)
  - Each turn consists of one exchange from each model
  - Higher values create longer conversations
  - Recommended range: 1-5 turns

## Research Applications

This project can be used to study:

- **Communication Degradation**: How information changes through encoding/decoding cycles
- **Emergent Patterns**: Whether models adapt their communication style for Morse transmission
- **Error Propagation**: How encoding errors affect conversation flow
- **Constraint Effects**: Impact of communication bottlenecks on AI dialogue
- **Historical Communication**: Modern AI using 19th-century communication methods

## File Structure

```
Bip_Bip_Hello_Hello
├── constants
│   ├── bots.py
│   ├── morse_code_dict.py
│   
├── main.py
├── README.md
└── src
    ├── initiate_conversation.py
    ├── model.py
    ├── morse_to_text.py
    ├── play_morse.py
    └── text_to_morse.py
```

## Contributing

Contributions are welcome! Areas for improvement:

- **Enhanced Morse Implementation**: Support for punctuation, numbers, prosigns
- **Different Models**: Experiment with other lightweight LMs
- **Error Simulation**: Introduce transmission errors to study robustness
- **Conversation Analysis**: Tools for analyzing communication patterns
- **Visualization**: Real-time display of the encoding/decoding process

### Development Setup

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/morse-audio`)
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## Performance Notes

- **Memory Usage**: Approximately 2-4GB RAM per model instance
- **Processing Time**: Varies based on hardware and turn count
- **GPU Support**: Automatically uses CUDA if available
- **Model Loading**: First run may take longer due to model download

## Known Limitations

- Morse code character set is limited (A-Z, 0-9, basic punctuation)
- Model responses may be affected by encoding constraints
- Long conversations may show degradation in coherence
- Processing time increases with turn count

## Future Enhancements

- [ ] Real-time conversation visualization
- [ ] Receiving the input as morse code sound using mic
- [ ] Historical conversation logging and analysis
- [ ] Conversation quality metrics

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
