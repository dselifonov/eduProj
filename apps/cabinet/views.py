from urllib.parse import quote

from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from django.template import loader

from .models import UserFile


def index(request):
    user_list = User.objects.all()
    template = loader.get_template('cabinet/index.html')
    context = {
        'user_list': user_list
    }
    return HttpResponse(template.render(context, request))


def detail(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Http404()
    else:
        user_file_list = user.userfile_set.all()
        template = loader.get_template('cabinet/detail.html')
        context = {
            'user': user,
            'user_file_list': user_file_list
        }
        return HttpResponse(template.render(context, request))


def download_file(request, file_id):
    try:
        document = UserFile.objects.get(pk=file_id)
    except UserFile.DoesNotExist:
        return Http404
    else:
        file = document.upload
        filename_header = '' if u'MSIE' in request.META['HTTP_USER_AGENT'] else 'filename*=UTF-8\'\'%s' % quote(file.instance.title)
        response = HttpResponse(file, content_type='text/plain')
        response['Content-Disposition'] = 'inline; %s' % filename_header
        return response
