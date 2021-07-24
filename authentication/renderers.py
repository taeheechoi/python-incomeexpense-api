import json
from rest_framework import renderers


class UserRenderer(renderers.JSONRenderer):
    charset = 'utf-8'  # must add this to custom renderer

    def render(self, data, accepted_media_type, renderer_context):
        response = ''

        # import pdb
        # pdb.set_trace()

        if 'ErrorDetail' in str(data):
            response = json.dumps({'errors': data})
        else:
            response = json.dumps({'data': data})
        return response
