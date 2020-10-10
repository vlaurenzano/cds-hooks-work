from cds_hooks_work.service import Service
from cds_hooks_work.response import Response
from cds_hooks_work.server import serve
from typing import List


class App(object):
    services: List[Service] = []

    def __init__(self, services: List[Service] = None):
        if services is None:
            self.services = []
        else:
            self.services = services

    def register_service(self, service: Service):
        self.services.append(service)

    def discovery(self):
        return {"services": [s.to_dict() for s in self.services]}

    def handle_hook(self, id: str, input: dict) -> Response:
        try:
            if "hook" in input:
                hook = input["hook"]
                for service in self.services:
                    if hook == service.hook and id == service.id:
                        return service.handle_input(input)
                # message = f"service with id: {id} and hook {hook} not found"
            return Response(statusCode=400)
        except Exception as e:
            return Response(statusCode=500)

    def patient_view(self, id: str, description: str, **kwargs):
        """ decorator that does the same thing as register service"""

        def decorator(handler):
            self.register_service(Service.patient_view(id, description, handler, **kwargs))
            return handler

        return decorator

    def serv(self, **kwargs):
        serve(self, **kwargs)
