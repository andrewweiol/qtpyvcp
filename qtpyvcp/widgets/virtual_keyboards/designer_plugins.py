#!/usr/bin/env python

from qtpyvcp.widgets.qtdesigner import _DesignerPlugin, _PluginExtension

from vkb_key import VKBKey
class VirtualKeyPlugin(_DesignerPlugin):
    def pluginClass(self):
        return VKBKey

from vkb_modifier_key import VBKModifierKey
class VBKModifierKeyPlugin(_DesignerPlugin):
    def pluginClass(self):
        return VBKModifierKey
