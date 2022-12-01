from src.IPlugin import IPlugin
from src.PluginInfo import PluginInfo

class PluginA(IPlugin):

    def get_info(self) -> PluginInfo:
        """
        Get plugin information
        """

        plugin_info = PluginInfo()
        plugin_info.name = __name__
        plugin_info.description = __name__
        plugin_info.version = '0.1.0'

        return plugin_info

    def invoke(self, **kwargs):
        print(kwargs['name'])

    def dispose(self):
        pass