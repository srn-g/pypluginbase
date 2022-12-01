from src.PluginManager import PluginManager


def main():
    plugin_manager: PluginManager
    plugin_manager = PluginManager()
    plugin_manager.plugins_folder_path = 'plugins'
    plugin_manager.discover_plugins()
    
    plugin_manager.register_plugin('PluginA')
    plugin_manager.run_plugin('PluginA', name='main')

if __name__ == '__main__':
    main()