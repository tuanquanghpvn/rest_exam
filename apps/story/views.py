from apps.base.views import BaseView
from contracts.story import STORY_ID
from apps.base.views import _base_request
from logics.story.logic import StoryServiceAgent
from apps.story.mappers import (GetStoryRequestSchema, GetStoryResponseSchema,
                                PostStoryRequestSchema, PostStoryResponseSchema,
                                PutStoryRequestSchema, PutStoryResponseSchema,
                                DeleteStoryRequestSchema, DeleteStoryResponseSchema)


class StorysView(BaseView):
    def get(self, request):
        return _base_request(request=request,
                             request_schema=GetStoryRequestSchema(),
                             response_schema=GetStoryResponseSchema(),
                             method=StoryServiceAgent.get_story,
                             is_paging=True)

    def post(self, request):
        return _base_request(request=request,
                             request_schema=PostStoryRequestSchema(),
                             response_schema=PostStoryResponseSchema(),
                             method=StoryServiceAgent.post_story)


class StoryView(BaseView):
    def get(self, request, code):
        pass

    def put(self, request, code):
        return _base_request(request=request,
                             request_schema=PutStoryRequestSchema(),
                             response_schema=PutStoryResponseSchema(),
                             method=StoryServiceAgent.put_story,
                             code=code,
                             code_name=STORY_ID)

    def delete(self, request, code):
        return _base_request(request=request,
                             request_schema=DeleteStoryRequestSchema(),
                             response_schema=DeleteStoryResponseSchema(),
                             method=StoryServiceAgent.delete_story,
                             code=code,
                             code_name=STORY_ID)
