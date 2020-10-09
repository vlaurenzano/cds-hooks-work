from typing import List
from dataclasses import asdict, dataclass


@dataclass
class Service(object):
    # https://cds-hooks.org/specification/current/#discovery
    hook: str  # REQUIRED	string	The hook this service should be invoked on. See Hooks.
    id: str  # REQUIRED	string	The {id} portion of the URL to this service which is available at {baseUrl}/cds-services/{id}
    description: str  # REQUIRED	string	The description of this service.
    title: str = ""  # RECOMMENDED	string	The human-friendly name of this service.
    prefetch: object = ""  # optional

    def to_dict(self):
        return asdict(self)

    @staticmethod
    def patient_view(id: str, description: str, title="", prefetch=""):
        return Service("patient-view", id, description, title, prefetch)



class Services(object):
    services: List[Service] = []

    def register_service(self, service: Service):
        self.services.append(service)

    def to_dict(self):
        return {"services": s.to_dict() for s in self.services}
