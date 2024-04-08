# offline_sttts (Speech to Text to Speech)

offline_sttts is a Python-based proof-of-concept (POC) tool designed to facilitate speech-to-text-to-speech conversion, primarily aimed at individuals with speaking disabilities or for online content creation, such as VTubers. This tool provides real-time speech recognition and synthesis capabilities, allowing users to convert spoken words into text and then into synthesized speech.

## Features

- **Real-time Speech Recognition:** Utilizes speech recognition technology to transcribe spoken words into text in real-time.
- **Text-to-Speech Synthesis:** Employs text-to-speech synthesis to convert the transcribed text into audible speech.
- **Offline Usage:** Designed to operate offline, ensuring privacy and accessibility without requiring an internet connection.

## Installation

To install offline_sttts and its dependencies, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/offline_sttts.git
    ```

2. Navigate to the project directory:

    ```bash
    cd offline_sttts
    ```

3. Install the required dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To use offline_sttts, follow these instructions:

1. Ensure that the required dependencies are installed (see Installation section).
3. Run the main script to start the speech-to-text-to-speech conversion process.
4. Speak into the microphone, and the tool will transcribe your speech into text and then synthesize it into audible speech in real-time.

## Acknowledgments

offline_sttts is based entirely on two projects by [KoljaB](https://github.com/KoljaB):
- [RealtimeSTT](https://github.com/KoljaB/RealtimeSTT)
- [RealtimeTTS](https://github.com/KoljaB/RealtimeTTS)

## Contributing

Contributions to offline_sttts are welcome! As this project is currently a proof-of-concept, it is highly likely to break. If you have any ideas for improvements, new features, or bug fixes, feel free to submit a pull request. Before contributing, please review the [contribution guidelines](CONTRIBUTING.md).

## License

offline_sttts is licensed under the [MIT License](LICENSE).
