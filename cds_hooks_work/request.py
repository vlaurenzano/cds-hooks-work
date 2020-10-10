from dataclasses import asdict, dataclass
import json


class RequestValidationException(Exception):
    pass


@dataclass
class FHIRAuthorization:
    # https://cds-hooks.org/specification/current/#fhir-resource-access
    access_token: str  # REQUIRED:	string	This is the OAuth 2.0 access token that provides access to the FHIR server.
    token_type: str  # expires_in	REQUIRED	Fixed value: Bearer
    expires_in: str  # REQUIRED	integer	The lifetime in seconds of the access token.
    scope: str  # REQUIRED	string	The scopes the access token grants the CDS Service.
    subject: str  # REQUIRED	string	The OAuth 2.0 client identifier of the CDS Service, as registered with the CDS Client's authorization server.


class Request(object):
    hook: str  # REQUIRED: The hook that triggered this CDS Service call. See Hooks.
    hookInstance: str  # REQUIRED	string	A UUID for this particular hook call (see more information below).
    fhirServer: str = ""  # OPTIONAL: an fhir server to access
    fhirAuthorization: FHIRAuthorization = None  # OPTIONAL: an fhirAuthorization
    prefetch: object  # OPTIONAL	object	The FHIR data that was prefetched by the CDS Client (see more information below).

    def hydrate(self, req):
        self.set_hooks(req)
        self.set_auth(req)
        self.set_prefetch(req)

    def set_hooks(self, req: dict):
        self.hook = req["hook"]
        self.hookInstance = req["hookInstance"]
        return self

    def set_auth(self, req: dict):
        if "fhirServer" in req:
            self.fhirServer = req["fhirServer"]
        if "fhirAuthorization" in req:  # if it's defined it can fail
            self.fhirAuthorization = FHIRAuthorization(**req["fhirAuthorization"])
        return self

    def set_prefetch(self, req: dict):
        if "prefetch" in req:
            self.prefetch = req["prefetch"]
        return self

@dataclass
class PatientViwContext(object):
    userId: str  # REQUIRED: The id of the current user
    patientId: str  # REQUIRED: The FHIR Patient.id of the current patient in context
    encounterId: str = ""  # OPTIONAL: The FHIR Encounter.id of the current encounter in context


class PatientViewRequest(Request):
    context: PatientViwContext

    def __init__(self, request_dict: dict):
        try:
            self.context = PatientViwContext(**request_dict["context"])
            self.hydrate(request_dict)
        except Exception as e:
            raise RequestValidationException from e
