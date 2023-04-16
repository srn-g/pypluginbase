# pypluginbase
__Sample plugin architecture for python__
#### Design
The following diagram demonstrates how these concepts are implemented in this package.

![image](https://user-images.githubusercontent.com/68561885/210153327-45e45b6e-b507-46b5-9d99-4982f70f61ea.png)

### How to use
#### To make a new plguin 
In order to make a new plugin you just need to make a class that implements the IPlugin interface and place it in the plugin directory(You can change the default directory by changing ...). Then you can overide the following methods to customize your plugin.
#### **[Get info method](https://github.com/srn-g/pypluginbase/blob/663c85ece4d962cbf73f6b33eb5b5845a8be43bd/src/IPlugin.py#L12)**
This method is used by the application to show the plugin information.
```python
plugin_info = PluginInfo()
        plugin_info.name = __name__
        plugin_info.description = __name__
        plugin_info.version = '0.1.0'

        return 
```
#### **[Invoke method](https://github.com/srn-g/pypluginbase/blob/663c85ece4d962cbf73f6b33eb5b5845a8be43bd/src/IPlugin.py#L19)**
This is the method that gets called when the plugin is invoked by the application.

#### **[Dispose method](https://github.com/srn-g/pypluginbase/blob/663c85ece4d962cbf73f6b33eb5b5845a8be43bd/src/IPlugin.py#L26)**
This is the method gets called when the plugin is getting unloaded so you can dispose unused resources that were used by the plugin.
