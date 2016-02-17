from typing import Optional
from contracts.story import (GetStoryRequest, GetStoryResponse,
                             PostStoryRequest, PostStoryResponse,
                             PutStoryRequest, PutStoryResponse,
                             DeleteStoryRequest, DeleteStoryResponse)
from .repository import StoryRespository


class StoryServiceAgent(object):
    @classmethod
    def get_story(cls, request_obj: GetStoryRequest, path: str) -> GetStoryResponse:
        story_list, total_count = StoryRespository.get_story(limit=request_obj.limit, offset=request_obj.offset,
                                                             sort=request_obj.sort, category_id=request_obj.category_id)
        return GetStoryResponse(request=request_obj, response=story_list, path=path, total_count=total_count)

    @classmethod
    def post_story(cls, request_obj: PostStoryRequest) -> PostStoryResponse:
        story = StoryRespository.post_story(category_id=request_obj.category_id, name=request_obj.name,
                                            slug=request_obj.slug, description=request_obj.description,
                                            content=request_obj.content)
        return PostStoryResponse(**story.__dict__)

    @classmethod
    def put_story(cls, request_obj: PutStoryRequest) -> PutStoryResponse:
        story = StoryRespository.put_story(id=request_obj.id, category_id=request_obj.category_id,
                                           name=request_obj.name, slug=request_obj.slug,
                                           description=request_obj.description, content=request_obj.content)
        return PutStoryResponse(**story.__dict__)

    @classmethod
    def delete_story(cls, request_obj: DeleteStoryRequest) -> DeleteStoryResponse:
        story = StoryRespository.delete_story(id=request_obj.id)
        return DeleteStoryResponse(story)
