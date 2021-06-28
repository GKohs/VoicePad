import time

from PySide6.QtWidgets import QMainWindow, QTableWidgetItem
from PySide6.QtCore import Slot
from views.main_view_ui import Ui_MainWindow

from model.model import Model
from controllers.main_ctrl import MainController


class MainView(QMainWindow):
    def __init__(self, model: Model, main_controller: MainController):
        super().__init__()

        self._model = model
        self._main_controller = main_controller
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        ###############################
        # connect widgets to controller
        ###############################

        # update textEdit
        self._ui.textEdit.textChanged.connect(
            lambda: self._main_controller.set_text_edit_plaintext_by_view(
                self._ui.textEdit.toPlainText()))

        # update by change of current filter choice
        self.connect_signals_voice_filter()

        # update of voice button disabled status
        self._ui.voicesComboBox.currentTextChanged.connect(
            self._main_controller.set_voice_button_status)
        self._ui.textEdit.textChanged.connect(
            self._main_controller.set_voice_button_status)

        # voice button pushed
        self._ui.voicePushButton.clicked.connect(
            self._main_controller.synthesize_voice)
        self._ui.debugPushButton.clicked.connect(self._main_controller.debug)

        # related to result table
        self._ui.resultTableWidget.cellDoubleClicked.connect(
            self._main_controller.double_click_result_table_field)
        self._ui.resultTableWidget.setSortingEnabled(False)
        self._ui.resultTableWidget.horizontalHeader().sortIndicatorChanged.connect(
            self._main_controller.click_result_table_header_sort)

        ################################
        # listen for model event signals
        ################################

        # self._model.voices_response_changed.connect(
        #     self.on_voices_response_changed)
        self._model.voices_names_changed.connect(self.on_voices_names_changed)
        self._model.voices_gender_changed.connect(
            self.on_voices_gender_changed)
        self._model.voices_languages_changed.connect(
            self.on_voices_languages_changed)
        self._model.voices_engines_changed.connect(
            self.on_voices_engines_changed)

        self._model.text_edit_plaintext_changed.connect(
            self.on_text_edit_plaintext_changed)

        self._model.voice_push_button_disabled_status_changed.connect(
            self.on_voice_push_button_disabled_status_changed)

        self._model.voices_names_current_changed.connect(
            self.on_voices_names_current_changed)
        self._model.voices_gender_current_changed.connect(
            self.on_voices_gender_current_changed)
        self._model.voices_engines_current_changed.connect(
            self.on_voices_engines_current_changed)
        self._model.voices_languages_current_changed.connect(
            self.on_voices_languages_current_changed)

        self._model.settings_changed.connect(
            self.on_settings_changed)

        self._model.collection_data_results_append_changed.connect(
            self.on_voice_result_append_changed)
        self._model.collection_data_results_replace_changed.connect(
            self.on_voice_result_replace_changed)

        self._model.collection_data_results_header_changed.connect(
            self.on_collection_data_results_header_changed
        )

        self._model.debug_signal.connect(self.on_debug_signal)

        self._main_controller.view_initialized()

        # set a default value
        # self._ui.voicePushButton.setDisabled(self._model.voice_push_button_status)

    ######################################
    # Dis-/connecting voice filter signals
    ######################################

    def connect_signals_voice_filter(self):
        self._ui.voicesComboBox.currentTextChanged.connect(
            lambda: self._main_controller.update_voices_names_by_view(
                self._ui.voicesComboBox.currentText()))
        self._ui.languageComboBox.currentTextChanged.connect(
            lambda: self._main_controller.update_voices_language_by_view(self._ui.languageComboBox.currentText()))
        self._ui.genderComboBox.currentTextChanged.connect(
            lambda: self._main_controller.update_voices_gender_by_view(self._ui.genderComboBox.currentText()))
        self._ui.enginesComboBox.currentTextChanged.connect(
            lambda: self._main_controller.update_voices_engines_by_view(self._ui.enginesComboBox.currentText()))

    def disconnect_signals_voice_filter(self):
        self._ui.voicesComboBox.currentTextChanged.disconnect()
        self._ui.languageComboBox.currentTextChanged.disconnect()
        self._ui.genderComboBox.currentTextChanged.disconnect()
        self._ui.enginesComboBox.currentTextChanged.disconnect()

    ########################
    # Voice Settings changed
    ########################

    @Slot(str)
    def on_voices_names_current_changed(self, value):
        self._ui.voicesComboBox.setCurrentText(value)

    @Slot(str)
    def on_voices_gender_current_changed(self, value):
        self._ui.genderComboBox.setCurrentText(value)

    @Slot(str)
    def on_voices_engines_current_changed(self, value):
        self._ui.enginesComboBox.setCurrentText(value)

    @Slot(str)
    def on_voices_languages_current_changed(self, value):
        self._ui.languageComboBox.setCurrentText(value)

    @Slot(list)
    def on_voices_languages_changed(self, value):
        self._ui.languageComboBox.clear()
        self._ui.languageComboBox.addItems(value)

    @Slot(list)
    def on_voices_gender_changed(self, value):
        self._ui.genderComboBox.clear()
        self._ui.genderComboBox.addItems(value)

    @Slot(list)
    def on_voices_engines_changed(self, value):
        self._ui.enginesComboBox.clear()
        self._ui.enginesComboBox.addItems(value)

    @Slot(list)
    def on_voices_names_changed(self, value):
        self._ui.voicesComboBox.clear()
        self._ui.voicesComboBox.addItems(value[0])
        self._ui.voicesComboBox.setCurrentText(value[1])

        if self._ui.voicesComboBox.count() == 0:
            self._ui.voicesComboBox.setDisabled(True)
        else:
            self._ui.voicesComboBox.setDisabled(False)

    ##################
    # textEdit changed
    ##################

    @Slot(str)
    def on_text_edit_plaintext_changed(self, value):
        self._ui.textEdit.setText(value)

    ##########################
    # voice Btn status changed
    ##########################

    @Slot(str)
    def on_voice_push_button_disabled_status_changed(self, value):
        self._ui.voicePushButton.setDisabled(value)

    ##################
    # Settings changed
    ##################

    @Slot(dict)
    def on_settings_changed(self, value):
        self._ui.languageComboBox.setCurrentText(
            value['_voices_languages_current'])
        self._ui.genderComboBox.setCurrentText(value['_voices_gender_current'])
        self._ui.enginesComboBox.setCurrentText(value['_voices_engines_current'])
        self._ui.voicesComboBox.setCurrentText(value['_voices_names_current'])

    ############################
    # Voice results were changed
    ############################

    @Slot(dict)
    def on_voice_result_append_changed(self, value, save=True):
        voice_filename = QTableWidgetItem(value['filename'])
        voice_text = QTableWidgetItem(value['text'])
        voice_name = QTableWidgetItem(value['voice'])
        voice_language = QTableWidgetItem(value['language'])
        voice_date = QTableWidgetItem(value['timestamp'])
        # another column with engine?

        # add to the bottom
        add_below = self._ui.resultTableWidget.rowCount()
        self._ui.resultTableWidget.insertRow(add_below)
        self._ui.resultTableWidget.setItem(add_below, 0, voice_filename)
        self._ui.resultTableWidget.setItem(add_below, 1, voice_text)
        self._ui.resultTableWidget.setItem(add_below, 2, voice_name)
        self._ui.resultTableWidget.setItem(add_below, 3, voice_language)
        self._ui.resultTableWidget.setItem(add_below, 4, voice_date)

        if save:
            self._main_controller.save_collection_results()

    @Slot(list)
    def on_voice_result_replace_changed(self, value):
        self._ui.resultTableWidget.setRowCount(0)
        for result in value:
            self.on_voice_result_append_changed(result, save=False)
        self._main_controller.save_collection_results()

    ###############################
    # Change appearance of elements
    ###############################

    def on_collection_data_results_header_changed(self, value):
        self._ui.resultTableWidget.setHorizontalHeaderLabels(value)

    #################
    # Debug activated
    #################

    @Slot()
    def on_debug_signal(self):
        self._ui.resultTableWidget.setHorizontalHeaderLabels(["Datei", "Text", "Name", "Sprache", "Zeit"])
