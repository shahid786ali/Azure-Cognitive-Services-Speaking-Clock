# Azure Cognitive Services Speaking Clock

## Overview

This Python script demonstrates the integration of Azure Cognitive Services for speech recognition, text-to-speech synthesis, and translation. It recognizes spoken commands and responds accordingly, providing the current time and optionally translating responses into other languages. Use this code as a sample application for implementing voice-based interactions with Azure Cognitive Services.

## Prerequisites

Before running the script, you need to set up the following prerequisites:

- An Azure Cognitive Services account with the necessary keys and endpoints for the Speech Service and Translator Service.

## Getting Started

1. Clone the repository or download the script to your local machine.

2. Create a virtual environment (optional but recommended) for isolating dependencies:

    ```bash
    python -m venv myenv
    ```

    Activate the virtual environment:

    - On Windows:
      ```bash
      myenv\Scripts\activate
      ```

    - On macOS and Linux:
      ```bash
      source myenv/bin/activate
      ```

3. Install required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Open the script and update the Azure Cognitive Services configuration settings:

    - Replace 'YOUR_TRANSLATOR_ENDPOINT', 'YOUR_TRANSLATOR_KEY', and 'YOUR_TRANSLATOR_RESOURCE_ID' with your Azure Translator Service settings.
    - Ensure that the audio files and speech recognition models are set up correctly.

5. Run the script:

    ```bash
    python speaking-clock.py
    ```

6. Follow the on-screen prompts to interact with the Speaking Clock.

## Additional Notes

- The script can recognize specific commands such as "What time is it?" and "Your Name." Customize the recognized commands and responses as needed.

- This script is designed as a sample application to showcase Azure Cognitive Services capabilities. You can extend and adapt it for your specific use case.

- To play audio, the script uses either the 'playsound' or 'pygame' library for audio playback. If you encounter issues with 'playsound,' you can use 'pygame' as an alternative. Install 'pygame' using `pip install pygame`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Feedback and Contributions

Feedback and contributions are welcome! If you have any suggestions or encounter issues, please open an issue or create a pull request.

---

Enjoy using the Azure Cognitive Services Speaking Clock!

