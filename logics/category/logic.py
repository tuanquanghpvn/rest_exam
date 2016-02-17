from contracts.category import (GetCategoryRequest, GetCategoryResponse,
                                PostCategoryRequest, PostCategoryResponse,
                                PutCategoryRequest, PutCategoryResponse,
                                DeleteCategoryRequest, DeleteCategoryResponse)
from contracts.exeptions import ResourceNotFoundException
from .repository import CategoryRepository


class CategoryServiceAgent(object):
    @classmethod
    def get_category(cls, request_obj: GetCategoryRequest, path: str) -> GetCategoryResponse:
        category_list, total_count = CategoryRepository.get_category(limit=request_obj.limit,
                                                                     offset=request_obj.offset,
                                                                     sort=request_obj.sort)
        return GetCategoryResponse(request=request_obj, response=category_list, path=path, total_count=total_count)

    @classmethod
    def post_category(cls, request_obj: PostCategoryRequest) -> PostCategoryResponse:
        category = CategoryRepository.post_category(name=request_obj.name, slug=request_obj.slug)
        return PostCategoryResponse(**category.__dict__)

    @classmethod
    def put_category(cls, request_obj: PutCategoryRequest) -> PutCategoryResponse:
        update_count = CategoryRepository.put_category(id=request_obj.id, name=request_obj.name, slug=request_obj.slug)
        if update_count:
            category = CategoryRepository.find_category(id=request_obj.id)
            return PutCategoryResponse(**category.__dict__)
        else:
            raise ResourceNotFoundException

    @classmethod
    def delete_category(cls, request_obj: DeleteCategoryRequest) -> DeleteCategoryResponse:
        category = CategoryRepository.delete_category(id=request_obj.id)
        return DeleteCategoryResponse(category)
