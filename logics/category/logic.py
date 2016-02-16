from contracts.category import (PostCategoryRequest, PostCategoryResponse,
                                PutCategoryRequest, PutCategoryResponse,
                                DeleteCategoryRequest, DeleteCategoryResponse)


class CategoryServiceAgent(object):
    @classmethod
    def post_category(cls, request_obj: PostCategoryRequest) -> PostCategoryResponse:
        pass

    @classmethod
    def put_category(cls, request_obj: PutCategoryRequest) -> PutCategoryResponse:
        pass

    @classmethod
    def delete_category(cls, request_obj: DeleteCategoryRequest) -> DeleteCategoryResponse:
        pass
