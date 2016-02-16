from django.http import response
from typing import (Callable, Optional)
from marshmallow import Schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from contracts.exeptions import (RequestParameterException, ResourceNotFoundException)


def _base_request(request: Request, request_schema: Schema, response_schema: Schema,
                  method: Callable[[object, Optional[str]], object], is_paging: bool = False,
                  code=None, code_name: Optional[str] = None):
    """Request processing base method.

    :param request: Request object
    :param request_schema: RequestSchema Instance
    :param response_schema: ResponseSchema Instance
    :param method: method to be processed by the request
    :param is_paging: paging type request
    :param code: request identifier
    :param code_name: parameter name of request identifier
    :return:
    """
    if not request:
        return response.HttpResponseNotFound()
    request_param = {}
    if request.query_params:
        request_param.update(request.query_params)
    if request.data:
        request_param.update(request.data)
    if code and code_name:
        request_param[code_name] = code
    request_obj, errors = request_schema.load(request_param)
    if errors:
        return response.HttpResponseBadRequest(errors)
    try:
        if is_paging:
            path = _parse_path(request)
            response_obj = method(request_obj, path)
        else:
            response_obj = method(request_obj)
    except RequestParameterException:
        return response.HttpResponseBadRequest()
    except ResourceNotFoundException:
        return response.HttpResponseNotFound()
    except Exception as e:
        return response.HttpResponseServerError()
    data, _ = response_schema.load(response_obj)
    if request.method == 'POST':
        return Response(data, status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        return Response({}, status.HTTP_204_NO_CONTENT)
    else:
        return Response(data, status.HTTP_200_OK)


def _parse_path(request):
    return '{scheme}://{host}{path}'.format(
        scheme=request._get_scheme(),
        host=request.get_host(),
        path=request.path
    )