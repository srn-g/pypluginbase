import os
from importlib import import_module
from multiprocessing import Process
from threading import Lock

from .IPlugin import IPlugin


class SingletonMeta(type):
    """
    This is a thread-safe implementation of Singleton.

    https://refactoring.guru/design-patterns/singleton/python/example#example-1
    """

    _instances = {}

    _lock: Lock = Lock()
    """
    We now have a lock object that will be used to synchronize threads during
    first access to the Singleton.
    """

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        # Now, imagine that the program has just been launched. Since there's no
        # Singleton instance yet, multiple threads can simultaneously pass the
        # previous conditional and reach this point almost at the same time. The
        # first of them will acquire lock and will proceed further, while the
        # rest will wait here.
        with cls._lock:
            # The first thread to acquire the lock, reaches this conditional,
            # goes inside and creates the Singleton instance. Once it leaves the
            # lock block, a thread that might have been waiting for the lock
            # release may then enter this section. But since the Singleton field
            # is already initialized, the thread won't create a new object.
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class PluginManager(metaclass=SingletonMeta):
    """
    Load and run plugin
    """

    _plugins_folder_path: str
    _plugins_list: list
    _registered_plugins: dict
    _running_plugins: dict

    def __init__(self):
        self._plugins_folder_path = 'plugins'
        self._plugins_list = []
        self._registered_plugins = {}
        self._running_plugins = {}

    @property
    def plugins_folder_path(self):
        return self._plugins_folder_path
    
    @plugins_folder_path.setter
    def plugins_folder_path(self, value):
        self._plugins_folder_path = value

    @property
    def plugins_list(self):
        return self._plugins_list

    @property
    def registered_plugins(self):
        return self._registered_plugins

    @property
    def running_plugins(self):
        return self._running_plugins

    def discover_plugins(self):
        """
        Find plugins and add them to list
        """

        for file_name in os.scandir(self._plugins_folder_path):
            if file_name.is_file():
                head, tail = os.path.split(file_name.path)
                plugin_name, extension = os.path.splitext(tail)

                if extension != '.py':
                    continue

                self._plugins_list.append(plugin_name)

    def register_plugin(self, plugin_name: str):
        """
        Load the plugin and get its information
        """

        if plugin_name in self._plugins_list:
            loaded_plugin: IPlugin

            module = import_module(
                f'{self._plugins_folder_path}.{plugin_name}')

            loaded_plugin = getattr(module, plugin_name)()
            self._registered_plugins[plugin_name] = loaded_plugin

    def run_plugin(self, plugin_name: str, **kwargs) -> str:
        """
        Run the plugin
        """

        output = 'The plugin is successfully run...'

        if plugin_name in self._running_plugins:
            output = 'The plugin is already run...'

            return output

        if plugin_name not in self._registered_plugins:
            output = 'The plugin is not registered...'

            return output

        plugin: IPlugin
        plugin = self._registered_plugins[plugin_name]

        proc = Process(target=plugin.invoke, kwargs=kwargs)
        proc.start()
        
        self._running_plugins[plugin_name] = proc

        return output

    def stop_plugin(self, plugin_name: str) -> str:
        """
        Stop and end the plugin
        """

        output = 'The plugin is successfully end...'

        if plugin_name not in self._running_plugins:
            output = 'The plugin is not already run...'

            return output

        if plugin_name not in self._registered_plugins:
            output = 'The plugin is not registered...'

            return output

        plugin = self._registered_plugins[plugin_name]
        plugin.dispose()

        proc = self._running_plugins[plugin_name]
        proc.terminate()

        self._running_plugins.pop(plugin_name)

        return output
