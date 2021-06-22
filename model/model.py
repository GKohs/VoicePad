from PySide6.QtCore import QObject, Signal


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

    @property
    def voices_response(self):
        return self._voices_response

    @voices_response.setter
    def voices_response(self, value):
        self._voices_response = value
        self.voices_response_changed.emit(value)

    @property
    def voices_names(self):
        return self._voices_names

    @voices_names.setter
    def voices_names(self, value):
        self._voices_names = value
        self.voices_names_changed.emit(value)

    @property
    def voices_gender(self):
        return self._voices_gender

    @voices_gender.setter
    def voices_gender(self, value):
        self._voices_gender = value
        self.voices_gender_changed.emit(value)

    @property
    def voices_engines(self):
        return self._voices_engines

    @voices_engines.setter
    def voices_engines(self, value):
        self._voices_engines = value
        self.voices_engines_changed.emit(value)

    @property
    def voices_languages(self):
        return self._voices_languages

    @voices_languages.setter
    def voices_languages(self, value):
        self._voices_languages = value
        self.voices_languages_changed.emit(value)

    @property
    def voice_push_button_disabled_status(self):
        return self._voice_push_button_disabled_status

    @voice_push_button_disabled_status.setter
    def voice_push_button_disabled_status(self, value):
        self._voice_push_button_disabled_status = value
        self.voice_push_button_disabled_status_changed.emit(value)

    @property
    def text_edit_plaintext(self):
        return self._text_edit_plaintext

    @text_edit_plaintext.setter
    def text_edit_plaintext(self, value):
        self._text_edit_plaintext = value
        self.text_edit_plaintext_changed.emit(value)

    @property
    def voices_names_current(self):
        return self._voices_names_current

    @voices_names_current.setter
    def voices_names_current(self, value):
        self._voices_names_current = value
        self.voices_names_current_changed.emit(value)

    @property
    def voices_gender_current(self):
        return self._voices_gender_current

    @voices_gender_current.setter
    def voices_gender_current(self, value):
        self._voices_gender_current = value
        self.voices_gender_current_changed.emit(value)

    @property
    def voices_engines_current(self):
        return self._voices_engines_current

    @voices_engines_current.setter
    def voices_engines_current(self, value):
        self._voices_engines_current = value
        self.voices_engines_current_changed.emit(value)

    @property
    def voices_languages_current(self):
        return self._voices_languages_current

    @voices_languages_current.setter
    def voices_languages_current(self, value):
        self._voices_languages_current = value
        self.voices_languages_current_changed.emit(value)

    def __init__(self):
        super().__init__()

        self._voices_response = dict()

        self._voices_names = list()
        self._voices_gender = list()
        self._voices_engines = list()
        self._voices_languages = list()

        self._voices_names_current = str
        self._voices_gender_current = str
        self._voices_engines_current = str
        self._voices_languages_current = str

        self._voice_push_button_disabled_status = False
        self._text_edit_plaintext = ""
