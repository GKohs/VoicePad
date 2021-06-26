from PySide6.QtCore import QObject, Slot
from PySide6.QtCore import QThreadPool

import time
import json
from pathlib import Path

from model.model import Model

from controllers.task_voice import GetVoicesChoicesTask, GetSynthesizedVoiceTask


class MainController(QObject):
    def __init__(self, model: Model):
        super().__init__()

        self._model = model

        self.base = Path().parent.absolute()

        QThreadPool.globalInstance().setMaxThreadCount(1)
        self.load_voices()

        self.set_voice_button_status()

    def load_voices(self):
        """
        Synthesizes text to voice
        Started by pushButton "Voice"
        :return:
        """
        getVoicesChoicesTask = GetVoicesChoicesTask()
        getVoicesChoicesTask.signals.result.connect(self.set_voices_response)
        QThreadPool.globalInstance().tryStart(getVoicesChoicesTask)

    @Slot(dict)
    def set_voices_response(self, response):
        """
        Reads AWS API response and creates content for comboBoxes
        :param response: API response from AWS with voice data
        :return:
        """
        self._model.voices_response = response

        self._model.voices_languages = self.get_language_choices()
        self._model.voices_gender = self.get_gender_choices()
        self._model.voices_engines = self.get_engine_choices()
        self._model.voices_names = self.get_voices_choices()

        self.load_settings()

    @Slot(str)
    def set_text_edit_plaintext_by_view(self, value):
        self._model.text_edit_plaintext_by_view = value

    @Slot()
    def update_voices_choices(self):
        # ToDo: Show number of voices for each selection beneath name
        # necessary: what is intuitive?
        language_selected = self._model.voices_languages_current
        gender_selected = self._model.voices_gender_current
        engine_selected = self._model.voices_engines_current

        filtered_names = list()
        if (type(engine_selected) is str and
            type(gender_selected) is str and
                type(language_selected) is str):

            for each in self._model.voices_response['Voices']:
                if ((language_selected == "Alle" or
                        each['LanguageName'] in language_selected) and
                    (gender_selected == "Alle" or
                     each['Gender'] in gender_selected) and
                    (engine_selected == "Alle" or
                     any([True for tmp_engine in each['SupportedEngines'] if
                          tmp_engine in engine_selected]))):
                    filtered_names.append(each['Name'])

        self._model.voices_names = filtered_names

    @Slot(str)
    def update_voices_names(self, value):
        self._model.voices_names_current = value

    @Slot(str)
    def update_voices_names_by_view(self, value):
        self._model.voices_names_current = value

    @Slot(str)
    def update_voices_language(self, value):
        self._model.voices_languages_current = value
        self.update_voices_choices()

    @Slot(str)
    def update_voices_language_by_view(self, value):
        self._model.voices_languages_current = value
        self.update_voices_choices()

    @Slot(str)
    def update_voices_gender(self, value):
        self._model.voices_gender_current = value
        self.update_voices_choices()

    @Slot(str)
    def update_voices_gender_by_view(self, value):
        self._model.voices_gender_current = value
        self.update_voices_choices()

    @Slot(str)
    def update_voices_engines(self, value):
        self._model.voices_engines_current = value
        self.update_voices_choices()

    @Slot(str)
    def update_voices_engines_by_view(self, value):
        self._model.voices_engines_current = value
        self.update_voices_choices()

    @Slot()
    def set_voice_button_status(self):
        if (len(self._model.text_edit_plaintext) == 0 or
                self._model.voices_names_current == ""):
            self._model.voice_push_button_disabled_status = True
        else:
            self._model.voice_push_button_disabled_status = False

    @Slot()
    def synthesize_voice(self):
        self.save_settings()
        data = {'voice': self._model.voices_names_current,
                'engine': self._model.voices_engines_current,
                'text': self._model.text_edit_plaintext}
        synthesize_task = GetSynthesizedVoiceTask(data)
        QThreadPool.globalInstance().tryStart(synthesize_task)

    @Slot()
    def debug(self):
        print(self._model.settings)

    def load_settings(self):
        with open('settings', 'r') as f:
            self._model.settings = json.load(f)

    def save_settings(self):
        with open('settings', 'w') as f:
            json.dump(self._model.settings, f)

    def get_language_choices(self):
        return ["Alle"] + sorted(set([each['LanguageName'] for each in self._model.voices_response['Voices']]))

    def get_gender_choices(self):
        return ["Alle"] + sorted(set([each['Gender'] for each in self._model.voices_response['Voices']]))

    def get_engine_choices(self):
        engine_choices = []
        for each in self._model.voices_response['Voices']:
            for engine in each['SupportedEngines']:
                if engine not in engine_choices:
                    engine_choices.append(engine)
        return sorted(engine_choices)

    def get_voices_choices(self):
        return sorted(set([each['Name'] for each in self._model.voices_response['Voices']]))


