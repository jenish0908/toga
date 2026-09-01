import sys

from toga import App
from toga.paths import PlatformDirsPaths

if sys.platform == "darwin":

    class Paths(PlatformDirsPaths):
        def platformdirs_args(self):
            # macOS keys app-specific folders by bundle identifier.
            return {"appname": App.app.app_id}

elif sys.platform == "win32":

    class Paths(PlatformDirsPaths):
        def platformdirs_args(self):
            return {
                "appname": App.app.formal_name,
                "appauthor": "Unknown" if App.app.author is None else App.app.author,
            }

else:
    Paths = PlatformDirsPaths
