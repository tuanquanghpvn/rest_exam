from contracts.category import (GetCategoryRequest, GetCategoryResponse,
                                PostCategoryRequest, PostCategoryResponse,
                                PutCategoryRequest, PutCategoryResponse,
                                DeleteCategoryRequest, DeleteCategoryResponse)
from .repository import CategoryRepository


class CategoryServiceAgent(object):
    @classmethod
    def get_category(cls, request_obj: GetCategoryRequest, path: str) -> GetCategoryResponse:
        category_list = CategoryRepository.get_category(limit=request_obj.limit,
                                                        offset=request_obj.offset,
                                                        sort=request_obj.sort)
        category_dics = []
        for category in category_list:
            category_dics.append(category)
        return GetCategoryResponse(request=request_obj, response=category_dics, path=path)

    @classmethod
    def post_category(cls, request_obj: PostCategoryRequest) -> PostCategoryResponse:
        pass

    @classmethod
    def put_category(cls, request_obj: PutCategoryRequest) -> PutCategoryResponse:
        pass

    @classmethod
    def delete_category(cls, request_obj: DeleteCategoryRequest) -> DeleteCategoryResponse:
        pass
