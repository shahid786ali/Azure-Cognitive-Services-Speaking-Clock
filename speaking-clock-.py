from dotenv import load_dotenv
from datetime import datetime
import os

# Import namespaces
import azure.cognitiveservices.speech as speech_sdk
from playsound import playsound

def main():
    try:
        global speech_config

        # Get Configuration Settings
        load_dotenv()
        cog_key = os.getenv('COG_SERVICE_KEY')
        cog_region = os.getenv('COG_SERVICE_REGION')

        # Configure speech service
        speech_config = speech_sdk.SpeechConfig(cog_key, cog_region)
        print('Ready to use speech service in:', speech_config.region)

        # Get spoken input
        command = TranscribeCommand()
        if command.lower() == 'what time is it?':
            TellTime()
        elif command.lower() == 'your name':
            YourNameCall()  # Call your new function if the command is "your name"

    except Exception as ex:
        print(ex)

def TranscribeCommand():
    command = ''
    audioFile = "E:\\NUST Ai\\azure assigment\\intro.wav"
    playsound(audioFile)
    audio_config = speech_sdk.AudioConfig(filename=audioFile)
    speech_recognizer = speech_sdk.SpeechRecognizer(speech_config, audio_config)

    # Process speech input
    speech = speech_recognizer.recognize_once_async().get()
    if speech.reason == speech_sdk.ResultReason.RecognizedSpeech:
        command = speech.text
        print(command)
    else:
        print(speech.reason)
        if speech.reason == speech_sdk.ResultReason.Canceled:
            cancellation = speech.cancellation_details
            print(cancellation.reason)
            print(cancellation.error_details)

    # Return the command
    return command

def TellTime():
    now = datetime.now()
    response_text = 'The time is {}:{:02d}'.format(now.hour, now.minute)
    print(response_text)

def YourNameCall():
    try:
        # Configure speech recognition for your recorded audio
        audio_file_path = "intro.mp3"  # Update with your recorded audio file
        audio_config = speech_sdk.AudioConfig(filename=audio_file_path)
        speech_recognizer = speech_sdk.SpeechRecognizer(speech_config, audio_config)

        # Process speech input
        speech_result = speech_recognizer.recognize_once()

        if speech_result.reason == speech_sdk.ResultReason.RecognizedSpeech:
            recognized_text = speech_result.text
            print(f"Recognized: {recognized_text}")

            # Check if your name is in the recognized text
            if "Your Name" in recognized_text:  # Replace "Your Name" with your actual name
                # Configure speech synthesis
                speech_config.speech_synthesis_voice_name = "en-US-JessaNeural"  # Use an appropriate voice
                speech_synthesizer = speech_sdk.SpeechSynthesizer(speech_config)

                # Synthesize spoken output with your name
                response_text = f"Hello, {recognized_text}!"
                speech_synthesizer.speak_text(response_text)
                print(response_text)

        else:
            print(f"Recognition failed: {speech_result.reason}")

    except Exception as ex:
        print(f"An error occurred: {ex}")

    # Configure speech synthesis
    speech_config.speech_synthesis_voice_name = "en-GB-RyanNeural"  # Change voice as needed
    speech_synthesizer = speech_sdk.SpeechSynthesizer(speech_config)

    # Synthesize spoken output
    speak = speech_synthesizer.speak_text_async(response_text).get()
    if speak.reason != speech_sdk.ResultReason.SynthesizingAudioCompleted:
        print(speak.reason)

    # Print the response
    print(response_text)

if __name__ == "__main__":
    main()





from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.translation.document import DocumentTranslationClient
from azure.identity import DefaultAzureCredential

# Your Azure Translator service settings
translator_endpoint = "YOUR_TRANSLATOR_ENDPOINT"
translator_key = "YOUR_TRANSLATOR_KEY"
translator_resource_id = "YOUR_TRANSLATOR_RESOURCE_ID"

def YourNameCall():
    try:
        # Configure speech recognition for your recorded audio
        audio_file_path = "intro.wav"  # Update with your recorded audio file
        audio_config = speech_sdk.AudioConfig(filename=audio_file_path)
        speech_recognizer = speech_sdk.SpeechRecognizer(speech_config, audio_config)

        # Process speech input
        speech_result = speech_recognizer.recognize_once()

        if speech_result.reason == speech_sdk.ResultReason.RecognizedSpeech:
            recognized_text = speech_result.text
            print(f"Recognized: {recognized_text}")

            # Check if your name is in the recognized text
            if "Your Name" in recognized_text:  # Replace "Your Name" with your actual name
                # Configure speech synthesis
                speech_config.speech_synthesis_voice_name = "en-US-JessaNeural"  # Use an appropriate voice
                speech_synthesizer = speech_sdk.SpeechSynthesizer(speech_config)

                # Synthesize spoken output with your name
                response_text = f"Hello, {recognized_text}!"
                speech_synthesizer.speak_text(response_text)
                print(response_text)

                # Translate the recognized text to Urdu
                translated_text = translate_to_urdu(recognized_text)
                print(f"Translated to Urdu: {translated_text}")

                # Synthesize the translated text and play it
                speech_config.speech_synthesis_voice_name = "ur-PK-IsmatNeural"  # Change to a Urdu voice
                speech_synthesizer = speech_sdk.SpeechSynthesizer(speech_config)
                speech_synthesizer.speak_text(translated_text)

        else:
            print(f"Recognition failed: {speech_result.reason}")

    except Exception as ex:
        print(f"An error occurred: {ex}")

def translate_to_urdu(text_to_translate):
    # Initialize the translator client
    translation_client = DocumentTranslationClient(endpoint=translator_endpoint, credential=translator_key)

    # Translate the text to Urdu
    result = translation_client.begin_translation(source_language="en", target_languages=["ur"], texts=[text_to_translate])
    translated_texts = list(result.result())

    if len(translated_texts) > 0:
        return translated_texts[0]["translations"][0]["text"]
    else:
        return "Translation failed"

if __name__ == "__main__":
    main()
