from abc import ABC, abstractmethod

from .PluginInfo import PluginInfo


class IPlugin(ABC):
    """
    Plugin interface
    """

    @abstractmethod
    def get_info(self) -> PluginInfo:
        """
        Get plugin information
        """
        pass

    @abstractmethod
    def invoke(self, **kwargs):
        """
        Invoke plugin
        """
        pass

    @abstractmethod
    def dispose(self):
        """
        Dispose unused resources
        """
        pass
