from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User, Group, Permission
from objectpack.actions import ObjectPack
from objectpack.ui import ModelEditWindow
from . import controller
from . import ui


class ContentTypePak(ObjectPack):
    model = ContentType
    add_window = edit_window = ModelEditWindow.fabricate(model)
    add_to_menu = True
    add_to_desktop = True


class UserObjectPack(ObjectPack):
    model = User
    add_window = edit_window = ui.UserAddWindow
    add_to_menu = True
    add_to_desktop = True


class GroupObjectPack(ObjectPack):
    model = Group
    add_window = edit_window = ModelEditWindow.fabricate(model)
    add_to_menu = True
    add_to_desktop = True


class PermissionObjectPack(ObjectPack):
    model = Permission
    add_window = edit_window = ModelEditWindow.fabricate(model, model_register=controller.observer)
    add_to_menu = True
    add_to_desktop = True
