class Service(object):
    # https://cds-hooks.org/specification/current/#discovery
    hook: str  # REQUIRED	string	The hook this service should be invoked on. See Hooks.
    title: str  # RECOMMENDED	string	The human-friendly name of this service.
    description: str  # REQUIRED	string	The description of this service.
    id: str  # REQUIRED	string	The {id} portion of the URL to this service which is available at {baseUrl}/cds-services/{id}
    prefetch: object  # optional
