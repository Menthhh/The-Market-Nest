from PySide6.QtCore import QSettings

def get_token():
    settings = QSettings("se_project", "the_market_nest")
    token = settings.value("auth/token", defaultValue=None)
    return token

print(get_token())