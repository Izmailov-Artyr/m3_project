from django.conf.urls import url
from objectpack import desktop
from .controller import controller
from . import actions


def register_urlpatterns():
    """
    Регистрация конфигурации урлов для приложения
    """
    return [url(*controller.urlpattern)]


def register_actions():
    """
    Регистрация экшен-паков
    """
    return controller.packs.extend([
        actions.ContentTypePak(),
        actions.UserObjectPack(),
        actions.GroupObjectPack(),
        actions.PermissionObjectPack(),
    ])


def register_desktop_menu():
    """
    Регистрация элементов рабочего стола
    """
    desktop.uificate_the_controller(
        controller,
        menu_root=desktop.MainMenu.SubMenu('Demo')
    )
