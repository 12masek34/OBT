import objectpack
from django.contrib.auth.models import User, Group, Permission

from objectpack.actions import ObjectPack
from django.contrib.contenttypes.models import ContentType

from .controller import observer
from .ui import UserAddWindow


class ContentTypeAction(ObjectPack):
    model = ContentType

    add_to_menu = True
    add_to_desktop = True
    add_window = edit_window = objectpack.ui.ModelEditWindow.fabricate(model)


class UserAction(ObjectPack):
    model = User

    add_to_menu = True
    add_to_desktop = True
    add_window = edit_window = UserAddWindow


class GroupAction(ObjectPack):
    model = Group

    add_to_menu = True
    add_to_desktop = True
    add_window = edit_window = objectpack.ui.ModelEditWindow.fabricate(model)


class PermissionAction(ObjectPack):
    model = Permission
    add_to_menu = True
    add_to_desktop = True
    add_window = edit_window = objectpack.ui.ModelEditWindow.fabricate(model, model_register=observer)
