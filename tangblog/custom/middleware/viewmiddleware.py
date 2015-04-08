
class ViewNameMiddleware(object):
    def process_view(self, request, view_func, view_args, view_kwargs):
        request.view_name = '.'.join((view_func.__module__, view_func.__name__))

def view_name_context_processor(request):
    return {
            'view_name': request.view_name,
    }
