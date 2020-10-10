from typing import List
from cds_hooks_work.request import Request, PatientViewRequest
from cds_hooks_work.response import Response
from collections.abc import Callable

HookHandler = callable([Request, Response])
PatientViewHandler = callable([PatientViewRequest, Response])


class Service(object):
    # https://cds-hooks.org/specification/current/#discovery
    hook: str  # REQUIRED	string	The hook this service should be invoked on. See Hooks.
    id: str  # REQUIRED	string	The {id} portion of the URL to this service which is available at {baseUrl}/cds-services/{id}
    description: str  # REQUIRED	string	The description of this service.
    title: str = ""  # RECOMMENDED	string	The human-friendly name of this service.
    prefetch: object = ""  # optional
    handler: HookHandler

    def __init__(self, hook, id, description, title="", prefetch="", handler: HookHandler = None):
        self.hook = hook
        self.id = id
        self.description = description
        self.title = title
        self.prefetch = prefetch
        self.handler = handler

    def to_dict(self):
        return {
            "hook": self.hook,
            "id": self.id,
            "description": self.description,
            "title": self.title,
            "prefetch": self.prefetch
        }

    def set_handler(self, handler: Callable):
        self.handler = handler

    @staticmethod
    def patient_view(id: str, description: str, handler: HookHandler, title: str = "", prefetch: str = ""):
        return Service("patient-view", id, description, title=title, prefetch=prefetch, handler=handler)

    def handle_input(self, request_dict: dict):
        if self.hook == 'patient-view':
            request = PatientViewRequest(request_dict)
            return self.handler(request)
        else:
            raise NotImplemented
