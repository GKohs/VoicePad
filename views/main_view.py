from PySide6.QtWidgets import QMainWindow
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
        self._ui.voicesComboBox.currentTextChanged.connect(
            lambda: self._main_controller.update_voices_names_by_view(
                self._ui.voicesComboBox.currentText()))
        self._ui.languageComboBox.currentTextChanged.connect(
            lambda: self._main_controller.update_voices_language_by_view(self._ui.languageComboBox.currentText()))
        self._ui.genderComboBox.currentTextChanged.connect(
            lambda: self._main_controller.update_voices_gender_by_view(self._ui.genderComboBox.currentText()))
        self._ui.enginesComboBox.currentTextChanged.connect(
            lambda: self._main_controller.update_voices_engines_by_view(self._ui.enginesComboBox.currentText()))

        # update of voice button disabled status
        self._ui.voicesComboBox.currentTextChanged.connect(
            self._main_controller.set_voice_button_status)
        self._ui.textEdit.textChanged.connect(
            self._main_controller.set_voice_button_status)

        self._ui.voicePushButton.clicked.connect(
            self._main_controller.synthesize_voice)
        self._ui.debugPushButton.clicked.connect(self._main_controller.debug)

        ################################
        # listen for model event signals
        ################################

        self._model.voices_response_changed.connect(
            self.on_voices_response_changed)
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

        # set a default value
        # self._ui.voicePushButton.setDisabled(self._model.voice_push_button_status)

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

    @Slot(dict)
    def on_voices_response_changed(self, value):
        pass

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
        self._ui.voicesComboBox.addItems(value)

        if self._ui.voicesComboBox.count() == 0:
            self._ui.voicesComboBox.setDisabled(True)
        else:
            self._ui.voicesComboBox.setDisabled(False)

    @Slot(str)
    def on_text_edit_plaintext_changed(self, value):
        self._ui.textEdit.setText(value)

    @Slot(str)
    def on_voice_push_button_disabled_status_changed(self, value):
        self._ui.voicePushButton.setDisabled(value)

    @Slot(dict)
    def on_settings_changed(self, value):
        self._ui.genderComboBox.setCurrentText(value['_voices_gender_current'])
        self._ui.enginesComboBox.setCurrentText(value['_voices_engines_current'])
        self._ui.languageComboBox.setCurrentText(value['_voices_languages_current'])
        self._ui.voicesComboBox.setCurrentText(value['_voices_names_current'])
