from objectpack.ui import BaseEditWindow, make_combo_box, TabbedWindow, ComboBoxWithStore, model_fields_to_controls
from m3_ext.ui import all_components as ext
from m3 import actions

from m3_ext.ui.windows.window import ExtWindow
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User, Group, Permission

from objectpack.ui import TabbedWindow

ext.ExtGridColumn

class PermissionMyWindow(BaseEditWindow):

    def _init_components(self):
        """
        Здесь следует инициализировать компоненты окна и складывать их в
        :attr:`self`.
        """
        self.grid = ext.ExtObjectGrid()
        super(PermissionMyWindow, self)._init_components()

        self.field__name = ext.ExtStringField(
            label=u'name',
            name='name',
            allow_blank=False,
            anchor='100%')

        self.field__gender = model_fields_to_controls(
            model=Permission,
            window=ExtWindow,
            # field_list=['name', 'content_type'],
            model_register={'content_type': Permission.content_type})

        self.field__code_name = ext.ExtStringField(
            label='code name',
            name='code name',
            allow_blank=False,
            anchor='100%',
        )

    def _do_layout(self):
        """
        Здесь размещаем компоненты в окне
        """
        super(PermissionMyWindow, self)._do_layout()
        self.form.items.extend((
            self.field__name,
            self.field__gender,
            self.field__code_name,
            self.items.append(self.grid)
        ))

    def set_params(self, params):
        """
        Установка параметров окна

        :params: Словарь с параметрами, передается из пака
        """
        super(PermissionMyWindow, self).set_params(params)
        self.height = 'auto'
