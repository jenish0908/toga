from toga import App
from toga.paths import PlatformDirsPaths


class Paths(PlatformDirsPaths):
    def platformdirs_args(self):
        # macOS keys app-specific folders by bundle identifier.
        return {"appname": App.app.app_id}
