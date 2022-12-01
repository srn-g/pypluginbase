class PluginInfo:
    """
    Information of the plugin
    """

    _name: str
    _description: str
    _version: str

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, value):
        self._version = value
