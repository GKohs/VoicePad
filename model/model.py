from PySide6.QtCore import QObject, Signal
from enum import Enum


# What about program states?
# class State(Enum):
#     STARTING = 1
#     RUNNING = 2
#     CLOSING = 3
#     LOADING_DATA = 4
#     SAVING_DATA = 5
#     SYNTHESIZING_VOICE = 6


class Model(QObject):
    voices_response_changed = Signal(dict)
    voices_names_changed = Signal(list)
    voices_gender_changed = Signal(list)
    voices_languages_changed = Signal(list)
    voices_engines_changed = Signal(list)

    voice_push_button_disabled_status_changed = Signal(bool)

    text_edit_plaintext_changed = Signal(str)

    voices_names_current_changed = Signal(str)
    voices_gender_current_changed = Signal(str)
    voices_engines_current_changed = Signal(str)
    voices_languages_current_changed = Signal(str)

    settings_changed = Signal(dict)

    def __init__(self):
        super().__init__()

        self._voices_response = dict()

        self._voices_names = list()
        self._voices_gender = list()
        self._voices_engines = list()
        self._voices_languages = list()

        self._voice_push_button_disabled_status = False

        self._text_edit_plaintext = ""

        self._settings = {
            '_voices_names_current': "",
            '_voices_engines_current': "",
            '_voices_gender_current': "",
            '_voices_languages_current': "",
        }

    @property
    def voices_response(self):
        """
        API Response from AWS with data of possible voices
        :return:
        """
        return self._voices_response

    @voices_response.setter
    def voices_response(self, value):
        self._voices_response = value
        self.voices_response_changed.emit(self._voices_response)

    ##############
    # Voice filter
    ##############

    @property
    def voices_names(self):
        """
        comboBox Voices
        :return:
        """
        return self._voices_names

    @voices_names.setter
    def voices_names(self, value):
        self._voices_names = value
        self.voices_names_changed.emit(self._voices_names)

    @property
    def voices_gender(self):
        """
        comboBox Gender
        :return:
        """
        return self._voices_gender

    @voices_gender.setter
    def voices_gender(self, value):
        self._voices_gender = value
        self.voices_gender_changed.emit(self._voices_gender)

    @property
    def voices_engines(self):
        """
        comboBox Engines
        :return:
        """
        return self._voices_engines

    @voices_engines.setter
    def voices_engines(self, value):
        self._voices_engines = value
        self.voices_engines_changed.emit(self._voices_engines)

    @property
    def voices_languages(self):
        """
        comboBox Languages
        :return:
        """
        return self._voices_languages

    @voices_languages.setter
    def voices_languages(self, value):
        self._voices_languages = value
        self.voices_languages_changed.emit(self._voices_languages)

    ######################
    # Voice filter current
    ######################

    @property
    def voices_names_current(self):
        """
        comboBox voices - current choice
        :return:
        """
        return self._settings['_voices_names_current']

    @voices_names_current.setter
    def voices_names_current(self, value):
        self._settings['_voices_names_current'] = value
        self.voices_names_current_changed.emit(
            self._settings['_voices_names_current']
        )

    @property
    def voices_names_current_by_view(self):
        """
        comboBox voices - current choice
        :return:
        """
        return self._settings['_voices_names_current']

    @voices_names_current_by_view.setter
    def voices_names_current_by_view(self, value):
        self._settings['_voices_names_current'] = value

    @property
    def voices_gender_current(self):
        """
        comboBox gender - current choice
        :return:
        """
        return self._settings['_voices_gender_current']

    @voices_gender_current.setter
    def voices_gender_current(self, value):
        self._settings['_voices_gender_current'] = value
        self.voices_gender_current_changed.emit(
            self._settings['_voices_gender_current']
        )

    @property
    def voices_gender_current_by_view(self):
        """
        comboBox gender - current choice
        :return:
        """
        return self._settings['_voices_gender_current']

    @voices_gender_current_by_view.setter
    def voices_gender_current_by_view(self, value):
        self._settings['_voices_gender_current'] = value

    @property
    def voices_engines_current(self):
        """
        comboBox engines - current choice
        :return:
        """
        return self._settings['_voices_engines_current']

    @voices_engines_current.setter
    def voices_engines_current(self, value):
        self._settings['_voices_engines_current'] = value
        self.voices_engines_current_changed.emit(
            self._settings['_voices_engines_current']
        )

    @property
    def voices_engines_current_by_view(self):
        """
        comboBox engines - current choice
        :return:
        """
        return self._settings['_voices_engines_current']

    @voices_engines_current_by_view.setter
    def voices_engines_current_by_view(self, value):
        self._settings['_voices_engines_current'] = value
        self.voices_engines_current_changed.emit(
            self._settings['_voices_engines_current']
        )

    @property
    def voices_languages_current(self):
        """
        comboBox languages - current choice
        :return:
        """
        return self._settings['_voices_languages_current']

    @voices_languages_current.setter
    def voices_languages_current(self, value):
        self._settings['_voices_languages_current'] = value
        self.voices_languages_current_changed.emit(
            self._settings['_voices_languages_current']
        )

    @property
    def voices_languages_current_by_view(self):
        """
        comboBox languages - current choice
        :return:
        """
        return self._settings['_voices_languages_current']

    @voices_languages_current_by_view.setter
    def voices_languages_current_by_view(self, value):
        self._settings['_voices_languages_current'] = value

    #########################
    # Voice pushButton status
    #########################

    @property
    def voice_push_button_disabled_status(self):
        """
        pushButton 'Voice' -> Send text to synthesize voice
        :return:
        """
        return self._voice_push_button_disabled_status

    @voice_push_button_disabled_status.setter
    def voice_push_button_disabled_status(self, value):
        self._voice_push_button_disabled_status = value
        self.voice_push_button_disabled_status_changed.emit(
            self._voice_push_button_disabled_status
        )

    ##########
    # textEdit
    ##########

    @property
    def text_edit_plaintext(self):
        """
        textEdit field changed
        :return:
        """
        return self._text_edit_plaintext

    @text_edit_plaintext.setter
    def text_edit_plaintext(self, value):
        self._text_edit_plaintext = value
        self.text_edit_plaintext_changed.emit(self._text_edit_plaintext)

    @property
    def text_edit_plaintext_by_view(self):
        """
        textEdit field changed from view
        :return:
        """
        return self._text_edit_plaintext

    @text_edit_plaintext_by_view.setter
    def text_edit_plaintext_by_view(self, value):
        self._text_edit_plaintext = value

    ################
    # Voice settings
    ################

    @property
    def settings(self):
        """
        comboBox settings (current choices of comboBoxes)
        :return:
        """
        return self._settings

    @settings.setter
    def settings(self, value):
        self._settings = value
        self.settings_changed.emit(self._settings)

