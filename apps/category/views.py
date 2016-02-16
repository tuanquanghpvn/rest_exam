from rest_framework.views import APIView
from contracts.category import CATEGORY_ID
from logics.category.logic import CategoryServiceAgent
from apps.base.views import _base_request
from apps.category.mappers import (GetCategoryRequestSchema, GetCategoryResponseSchema,
                                   PostCategoryRequestSchema, PostCategoryResponseSchema,
                                   PutCategoryRequestSchema, PutCategoryResponseSchema,
                                   DeleteCategoryRequestSchema, DeleteCategoryResponseSchema)


class CategoryView(APIView):
    def get(self, request):
        return _base_request(request=request,
                             request_schema=GetCategoryRequestSchema(),
                             response_schema=GetCategoryResponseSchema(),
                             method=CategoryServiceAgent.get_category,
                             is_paging=True)

    def post(self, request):
        return _base_request(request=request,
                             request_schema=PostCategoryRequestSchema(),
                             response_schema=PostCategoryResponseSchema(),
                             method=CategoryServiceAgent.post_category
                             )

    def put(self, request, code):
        return _base_request(request=request,
                             request_schema=PutCategoryRequestSchema(),
                             response_schema=PutCategoryResponseSchema(),
                             method=CategoryServiceAgent.put_category,
                             code_name=CATEGORY_ID,
                             code=code)

    def delete(self, request, code):
        return _base_request(request=request,
                             request_schema=DeleteCategoryRequestSchema(),
                             response_schema=DeleteCategoryResponseSchema(),
                             method=CategoryServiceAgent.delete_category,
                             code_name=CATEGORY_ID,
                             code=code)
