#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from exile_ui.widgets import DatePickerWidget
import models


class OperarioForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(OperarioForm, self).__init__(*args, **kwargs)
        self.fields['password1'].label = "Contraseña"
        self.fields['password2'].label = "Confirmar contraseña"
    # end def

    class Meta:
        model = models.Operario
        exclude = ()
    # end class
# end class
