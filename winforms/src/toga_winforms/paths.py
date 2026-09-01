from toga import App
from toga.paths import PlatformDirsPaths


class Paths(PlatformDirsPaths):
    def platformdirs_args(self):
        return {
            "appname": App.app.formal_name,
            "appauthor": "Unknown" if App.app.author is None else App.app.author,
        }
