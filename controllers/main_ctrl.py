from PySide6.QtCore import QObject, Slot, QThreadPool, Qt
from PySide6.QtWidgets import QTableWidgetItem

import time
import json
from pathlib import Path
import os
import sys
from datetime import datetime

from model.model import Model
from controllers.task_voice import GetVoicesChoicesTask, GetSynthesizedVoiceTask


class MainController(QObject):
    def __init__(self, model: Model):
        super().__init__()

        self._model = model
        self.list_of_tasks = list()

        # only one thread at a time is executed, the rest is queued
        QThreadPool.globalInstance().setMaxThreadCount(1)

    def view_initialized(self):
        self.load_voices()
        self.load_collection_results()
        self.set_voice_button_status()
        self.load_table_header()

    def load_voices(self):
        """
        Synthesizes text to voice
        Started by pushButton "Voice"
        :return:
        """
        getVoicesChoicesTask = GetVoicesChoicesTask()
        getVoicesChoicesTask.signals.result.connect(self.set_voices_response)
        QThreadPool.globalInstance().tryStart(getVoicesChoicesTask)

    def load_table_header(self):
        self._model.collection_data_results_header = self._model.collection_data_results_header

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
        voice_selected = self._model.voices_names_current
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

        self._model.voices_names = [filtered_names, voice_selected]

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
        data = self._model.get_voice_task_data()

        data['path'], data['filename'] = self.create_path_result_voice()
        data['timestamp'] = f"{datetime.now():%d.%m.%Y %H:%M:%S}"

        synthesize_task = GetSynthesizedVoiceTask(data)
        # synthesize_task.signals.finished_with_data.disconnect(self.update_result)
        synthesize_task.signals.finished_with_data.connect(self.update_result)
        self.list_of_tasks.append(synthesize_task)
        QThreadPool.globalInstance().tryStart(synthesize_task)

    @Slot(dict)
    def update_result(self, value):
        value['path'] = str(value['path'])
        self._model.collection_data_results_append = value

    def create_path_result_voice(self):
        """
        Creates folder structure and incrementing filename for voice results
        :return:
        """
        path_result = self._model.get_path_voice_results()
        filename_result = self._model.filename_voice_results_base

        new_filename = ""
        for i in range(1, 1000):
            new_filename = filename_result.replace('.', str(i).zfill(3) + '.mp3')
            if not path_result.parent.joinpath(new_filename).exists():
                break

        path_result = path_result.parent.joinpath(new_filename)
        path_result.parent.mkdir(parents=True, exist_ok=True)

        return path_result, new_filename

    @Slot(int, int)
    def double_click_result_table_field(self, row, column):
        # print("Debug hi:", self._model.collection_data_results_replace[row])
        result = self._model.collection_data_results_replace[row]
        if column == 0:
            # Datei -> play audio in standard player
            if sys.platform == "win32":
                os.startfile(result['path'])
            else:
                print("Flup")
                # The following works on macOS and Linux. (Darwin = mac, xdg-open = linux).
                # opener = "open" if sys.platform == "darwin" else "xdg-open"
                # subprocess.call([opener, output])
        elif column == 1:
            # Text -> copy text to textEdit
            self._model.text_edit_plaintext = result['text']
        elif column == 2:
            # Name -> Set setting to this name
            # TODO: engine has to be handled differently for that
            # -> "Alle" should be possible with automatic detection and
            # standard as default if both is possible
            # self._model.set_voices_filter_to_name = resut['voice']
            pass

    @Slot(int, Qt.SortOrder)
    def click_result_table_header_sort(self, column: int, order: Qt.SortOrder):
        """
        Sorting the list of results in model
        :param column: which column will be used for sorting
        :param order: ascending or descending
        :return:
        """
        header_text = self._model.collection_data_results_header[column]
        collection_key = self._model.switcher_collection_data_results_header[header_text]
        reverse = order == Qt.SortOrder.DescendingOrder

        self._model.collection_data_results_replace = sorted(
            self._model.collection_data_results_replace,
            key=lambda k: k[collection_key].lower(),
            reverse=reverse)

    @Slot()
    def debug(self):
        print("Debug hi:")
        # print(f"{value1 = }")
        # print(f"{value2 = }")
        # self._model.debug() # emits Signal for view

    def load_settings(self):
        if Path.exists(self._model.get_path_settings_voices()):
            with open(self._model.get_path_settings_voices(), 'r') as f:
                self._model.settings = json.load(f)

    def save_settings(self):
        path_settings_voices = self._model.get_path_settings_voices()

        # creates settings folder if it does not exist yet
        path_settings_voices.parent.mkdir(parents=True, exist_ok=True)

        with open(path_settings_voices, 'w') as f:
            json.dump(self._model.settings, f)

    def load_collection_results(self):
        if Path.exists(self._model.get_path_collection_results()):
            with open(self._model.get_path_collection_results(), 'r') as f:
                self._model.collection_data_results_replace = json.load(f)

    def save_collection_results(self):
        path_results = self._model.get_path_collection_results()

        # creates settings folder if it does not exist yet
        path_results.parent.mkdir(parents=True, exist_ok=True)

        with open(path_results, 'w') as f:
            json.dump(self._model.collection_data_results_replace, f)

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


