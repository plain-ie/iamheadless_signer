from django.conf import settings as dj_settings

from .apps import IamheadlessSignerConfig as AppConfig


class Settings:

    APP_NAME = AppConfig.name
    VAR_PREFIX = APP_NAME.upper()

    VAR_KEY_MODEL_CLASS = f'{VAR_PREFIX}_KEY_MODEL_CLASS'

    @property
    def KEY_MODEL_CLASS(self):
        return getattr(
            dj_settings,
            self.VAR_KEY_MODEL_CLASS,
            f'{self.APP_NAME}.Key'
        )

    def __getattr__(self, name):
        return getattr(dj_settings, name)


settings = Settings()
