from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from supra import views as supra
import models
from usuarios import models as usuarios
import forms
from django.contrib.auth.decorators import login_required


class TipoActividadFormView(supra.SupraFormView):
    model = models.TipoActividad
    form_class = forms.TipoActividadForm

# end class


class TipoActividadListView(supra.SupraListView):
    model = models.TipoActividad
    list_display = ('nombre', )
    serarch_fields = list_display
# end class


class ActividadFormView(supra.SupraFormView):
    model = models.Actividad
    form_class = forms.ActividadForm

# end class


class ActividadListView(supra.SupraListView):
    model = models.Actividad
    list_display = ('nombre', 'descripacion', 'cliente',
                    'tipo_de_actividad', 'fecha_de_ejecucion', 'fecha_de_notificacion')
    list_filter = ['piscina__piscinero']
    serarch_fields = list_display
# end class



@login_required(login_url="/dashboard/login/")
def schedule(request):

    menu_list = admin_site.get_app_list(request)
    tipos = actividades.TipoActividad.objects.all()
    piscinas = usuarios.Piscina.objects.all()
    piscineros = usuarios.Piscinero.objects.all()
    clientes = usuarios.Cliente.objects.all()
    obj = {
        'menu_list': menu_list,
        'user': request.user,
        'funcname': 'Calendario',
        'model': 'Actividades',
        'tipos': tipos,
        'piscinas': piscinas,
        'piscineros': piscineros,
        'clientes': clientes,
        'data': dict(request.GET.iterlists())
    }
    extra_context = dict(dict(obj).items() + EXILE_UI['media'].items())
    return render(request, 'schedule.html', extra_context)
# edn def

def calendar(request):

    start = request.GET.get('start', False)
    end = request.GET.get('end', False)
    novedad_select = request.GET.get('novedad_select', '0')

    dates = []
    now = datetime.now()

    if start and isinstance(start, unicode) and start.isdigit():
        start = datetime.fromtimestamp(int(start))
    else:
        try:
            print start
            parts = start.split('-')
            start = datetime(int(parts[0]), int(parts[1]) + 1, int(parts[2]))
        except Exception as e:
            print e
        # end try
    # end if
    if end and isinstance(end, unicode) and end.isdigit():
        end = datetime.fromtimestamp(int(end))
    else:
        try:
            parts = end.split('-')
            end = datetime(int(parts[0]), int(parts[1]) + 1, int(parts[2]))
        except Exception as e:
            print e
        # end try
    # end if
    key = request.GET.get('key', False)
    piscinero = request.GET.get('piscinero', request.user.pk)
    if request.user.is_authenticated():
        piscinero = usuarios.Piscinero.objects.filter(pk = piscinero).first()
    else:
        piscinero = False
    # end if
    print piscinero
    if start and end:
        if novedad_select == '0' or novedad_select == '1':
            dates = dates + activities(request, start, end, now, piscinero)
        # end if
        if (novedad_select == '0' or novedad_select == '2') and not piscinero:
            dates = dates + seguimientos(request, start, end, now)
        # end if
        if (novedad_select == '0' or novedad_select == '3') and not piscinero:
            dates = dates + cumpleanios(request, start, end, now)
        # end if
    # end if
    return HttpResponse(json.dumps(dates, cls=DjangoJSONEncoder), content_type="application/json")
# end def



def activities(request, start, end, now, piscinero):
    acts = actividades.Actividad.objects.all()
    tipo_selected = request.GET.get('tipo_selected', '0')

    if tipo_selected != '0':
        acts = acts.filter(tipo_de_actividad=int(tipo_selected))
    # end if

    piscina = request.GET.get('piscina', '0')

    if piscina != '0':
        acts = acts.filter(piscina=int(piscina))
    # end if

    cliente = request.GET.get('cliente', '0')
    if cliente != '0':
        acts = acts.filter(piscina__casa__cliente=int(cliente))
    # end if
    if piscinero:
        acts = acts.filter(piscina__asignacionpiscinero__piscinero=piscinero)
    # end if
    acts = acts.extra({
        'piscinero':
            'select group_concat(piscinero_id) from usuarios_asignacionpiscinero where piscina_id=actividades_actividad.piscina_id ',
        'users':
            'select group_concat(username) from usuarios_asignacionpiscinero join auth_user on piscina_id=actividades_actividad.piscina_id and auth_user.id = usuarios_asignacionpiscinero.piscinero_id'

    })
    dates = []
    for act in acts:

        if act.repetir_cada == 'no':
            dates.append({
                'pk': act.id,
                'color': act.tipo_de_actividad.color,
                'title': "%s, %s" % (act.nombre, str(act.piscina)),
                'now': now.strftime("%Y-%m-%d %I:%M%p"),
                'start': act.fecha_de_ejecucion.strftime("%Y-%m-%d"),
                "_send_to_": ['Piscinero'],
                "users": act.users,
                'piscineros': act.piscinero,
                "urli": reverse('admin:%s_%s_change' % (act._meta.app_label,  act._meta.model_name),  args=[act.pk]),
                'type': 'Actividad'
            })
        else:
            str_cron = get_cron(act)
            cron = croniter.croniter(str_cron, datetime.combine(act.fecha_de_ejecucion, datetime.min.time()))
            nextdate = start
            while nextdate <= end:
                nextdate = cron.get_next(datetime)
                if nextdate >= now:
                    color = act.tipo_de_actividad.color
                else:
                    color = 'gray'
                # end if
                dates.append({
                    'pk': act.id,
                    'color': color,
                    'cron': str_cron,
                    'title': "%s, %s" % (act.nombre, unicode(act.piscina)),
                    'now': now.strftime("%Y-%m-%d %I:%M%p"),
                    'start': nextdate.strftime("%Y-%m-%d"),
                    "_send_to_": ['Piscinero'],
                    "users": act.users,
                    "urli": reverse('admin:%s_%s_change' % (act._meta.app_label,  act._meta.model_name),  args=[act.pk]),
                    'piscineros': act.piscinero,
                    'type': 'Actividad'
                })
            # end while
        # end if
    # end for
    return dates
# end def

def get_cron(instance):
    cron = ""
    if "dias[" in instance.repetir_cada:  # dias de la semana
        cron = "0 7 * * %s" % (instance.repetir_cada.replace(
            "dias[", "").replace("]", ""), )
    elif "mes[" in instance.repetir_cada:  # dias del mes
        cron = "0 7 %s * *" % (instance.repetir_cada.replace(
            "mes[", "").replace("]", ""), )
    else:
        if int(instance.repetir_cada) <= 0:
            instance.repetir_cada = '1'
            instance.save()
        # end if
        if instance.unidad_de_repeticion == 3:  # intervalo mensual
            cron = "0 7 %s */%s *" % ('%(dia)s', instance.repetir_cada, )
        elif instance.unidad_de_repeticion == 4:  # intervalo anual
            cron = "0 7 %s %s/%d *" % ('%(dia)s', '%(mes)s', int(instance.repetir_cada) * 12, )
        # end if
    return cron % {
        'dia': instance.fecha_de_ejecucion.day,
        'mes': instance.fecha_de_ejecucion.month,
        'dia_semana': instance.fecha_de_ejecucion.weekday()
    }
# end def
