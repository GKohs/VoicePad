from PySide6.QtCore import QRunnable, QObject, Signal
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import subprocess
from tempfile import gettempdir


class TaskSignals(QObject):
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)

    def __init__(self):
        super().__init__()


class GetVoicesChoicesTask(QRunnable):
    signals = TaskSignals()

    def __init__(self):
        super(GetVoicesChoicesTask, self).__init__()

    def run(self):
        session = Session(profile_name="udemy-admin", region_name="eu-central-1")
        polly = session.client("polly")

        try:
            # Request speech synthesis
            response = polly.describe_voices()
            self.signals.result.emit(response)
        except (BotoCoreError, ClientError) as error:
            # The service returned an error, exit gracefully
            print(error)
            sys.exit(-1)


class GetSynthesizedVoiceTask(QRunnable):
    signals = TaskSignals()

    def __init__(self, data):
        super(GetSynthesizedVoiceTask, self).__init__()
        self.data = data

    def run(self):
        session = Session(profile_name="udemy-admin", region_name="eu-central-1")
        polly = session.client("polly")

        try:
            # Request speech synthesis
            response = polly.synthesize_speech(Text=self.data['text'],
                                               OutputFormat="mp3",
                                               VoiceId=self.data['voice'],
                                               Engine=self.data['engine'])
        except (BotoCoreError, ClientError) as error:
            # The service returned an error, exit gracefully
            print(error)
            sys.exit(-1)

        # Access the audio stream from the response
        if "AudioStream" in response:
            # Note: Closing the stream is important because the service throttles on the
            # number of parallel connections. Here we are using contextlib.closing to
            # ensure the close method of the stream object will be called automatically
            # at the end of the with statement's scope.
            with closing(response["AudioStream"]) as stream:
                output = os.path.join(gettempdir(), "speech.mp3")

                try:
                    # Open a file for writing the output as a binary stream
                    with open(output, "wb") as file:
                        file.write(stream.read())
                except IOError as error:
                    # Could not write to file, exit gracefully
                    print(error)
                    sys.exit(-1)

        else:
            # The response didn't contain audio data, exit gracefully
            print("Could not stream audio")
            sys.exit(-1)

        # Play the audio using the platform's default player
        if sys.platform == "win32":
            os.startfile(output)
        else:
            print("Flup")
            # The following works on macOS and Linux. (Darwin = mac, xdg-open = linux).
            # opener = "open" if sys.platform == "darwin" else "xdg-open"
            # subprocess.call([opener, output])


