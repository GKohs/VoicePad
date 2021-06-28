from PySide6.QtCore import QObject, Signal
from enum import Enum

from pathlib import Path

# What about program states?
# class State(Enum):
#     STARTING = 1
#     RUNNING = 2
#     CLOSING = 3
#     LOADING_DATA = 4
#     SAVING_DATA = 5
#     SYNTHESIZING_VOICE = 6


class Model(QObject):
    # voice filter choices signals
    voices_response_changed = Signal(dict)
    voices_names_changed = Signal(list)
    voices_gender_changed = Signal(list)
    voices_languages_changed = Signal(list)
    voices_engines_changed = Signal(list)

    # current voice filter choice signals
    voices_names_current_changed = Signal(str)
    voices_gender_current_changed = Signal(str)
    voices_engines_current_changed = Signal(str)
    voices_languages_current_changed = Signal(str)

    # voice pushButton status signal
    voice_push_button_disabled_status_changed = Signal(bool)

    # textEdit signal
    text_edit_plaintext_changed = Signal(str)

    # voice settings signal
    settings_changed = Signal(dict)

    # collection of data results signals
    collection_data_results_replace_changed = Signal(list)
    collection_data_results_append_changed = Signal(dict)
    collection_data_results_header_changed = Signal(list)

    # debug signal
    debug_signal = Signal()

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

        self._folder_data = "voicePadData"
        self._folder_settings = "settings"
        self._folder_results = "results"
        self._filename_voice_result_base = "voice."
        self._filename_collection_result_base = "collection_results."
        self._filename_settings_voices = "settingsVoices."
        self._base = Path().resolve()

        self._collection_data_results = list()

        self._collection_data_results_header = ["Datei", "Text", "Name",
                                                "Sprache", "Zeit"]

        self._switcher_collection_data_results_header = {
            'Datei': 'filename',
            'Text': 'text',
            'Name': 'voice',
            'Sprache': 'language',
            'Zeit': 'timestamp',
        }

    #############################
    # Path and filename variables
    #############################

    @property
    def folder_data(self):
        """
        Folder name for created content
        :return:
        """
        return self._folder_data

    @folder_data.setter
    def folder_data(self, value):
        self._folder_data = value

    @property
    def folder_settings(self):
        """
        Folder name for settings
        :return:
        """
        return self._folder_settings

    @folder_settings.setter
    def folder_settings(self, value):
        self._folder_settings = value

    @property
    def folder_results(self):
        """
        Folder name for results of synthesized text
        :return:
        """
        return self._folder_results

    @folder_results.setter
    def folder_results(self, value):
        self._folder_results = value

    @property
    def filename_settings_voices(self):
        """
        Filename for voices settings
        :return:
        """
        return self._filename_settings_voices

    @filename_settings_voices.setter
    def filename_settings_voices(self, value):
        self._filename_settings_voices = value

    @property
    def filename_voice_results_base(self):
        """
        Base of filename for results.
        Will be incremented
        :return:
        """
        return self._filename_voice_result_base

    @filename_voice_results_base.setter
    def filename_voice_results_base(self, value):
        self._filename_voice_result_base = value

    @property
    def filename_collection_result_base(self):
        """
        Base of filename for results.
        Will be incremented
        :return:
        """
        return self._filename_collection_result_base

    @filename_collection_result_base.setter
    def filename_collection_result_base(self, value):
        self._filename_collection_result_base = value

    def get_path_settings_voices(self):
        settings_path = self._base.joinpath(self.folder_data).joinpath(
            self.folder_settings)
        settings_filename = self.filename_settings_voices
        return settings_path.joinpath(settings_filename)

    def get_path_voice_results(self):
        voice_result_path = self._base.joinpath(self.folder_data).joinpath(
            self.folder_results)
        voice_result_filename = self.filename_voice_results_base
        return voice_result_path.joinpath(voice_result_filename)

    def get_path_collection_results(self):
        collection_result_path = self._base.joinpath(
            self.folder_data).joinpath(
            self.folder_results)
        collection_result_filename = self.filename_collection_result_base
        return collection_result_path.joinpath(collection_result_filename)

    ##############
    # API response
    ##############

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

    def set_voices_filter_to_name(self):
        """
        loads name of voice from result table into filter
        TBD: engine has to be handled differently
        :return:
        """
        # self._settings = {
        #     '_voices_names_current': "",
        #     '_voices_engines_current': "",
        #     '_voices_gender_current': "",
        #     '_voices_languages_current': "",
        # }
        pass

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

    ##################################
    # Task for synthesizing voice data
    ##################################

    def get_voice_task_data(self):
        data = {'voice': self.voices_names_current,
                'engine': self.voices_engines_current,
                'text': self.text_edit_plaintext,
                'language': self.voices_languages_current}
        return data

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

    ##################
    # Data collections
    ##################

    @property
    def collection_data_results_append(self):
        """
        Collection of data results is a list of dictionaries with keywords:
        - text
        - path
        - filename
        - timestamp
        - voice
        - engine
        :return: last dict in list
        """
        return self._collection_data_results[-1]

    @collection_data_results_append.setter
    def collection_data_results_append(self, value):
        self._collection_data_results.append(value)
        self.collection_data_results_append_changed.emit(
            self._collection_data_results[-1])

    @property
    def collection_data_results_replace(self):
        """
        Collection of data results is a list of dictionaries with keywords:
        - text
        - path
        - filename
        - timestamp
        - voice
        - engine
        :return: list of dicts
        """
        return self._collection_data_results

    @collection_data_results_replace.setter
    def collection_data_results_replace(self, value):
        self._collection_data_results = value
        self.collection_data_results_replace_changed.emit(
            self._collection_data_results)

    @property
    def collection_data_results_header(self):
        """
        Header of table for data results
        :return: list of strings
        """
        return self._collection_data_results_header

    @collection_data_results_header.setter
    def collection_data_results_header(self, value):
        self._collection_data_results_header = value
        self.collection_data_results_header_changed.emit(
            self._collection_data_results_header)

    @property
    def switcher_collection_data_results_header(self):
        """
        Header of table for data results
        :return: list of strings
        """
        return self._switcher_collection_data_results_header

    @switcher_collection_data_results_header.setter
    def switcher_collection_data_results_header(self, value):
        self._collection_data_results_header = value

    #######
    # Debug
    #######

    def debug(self):
        self.debug_signal.emit()
