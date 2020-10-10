from dataclasses import asdict, dataclass
from typing import List


@dataclass
class Card(object):
    # https://cds-hooks.org/specification/current/#card-attributes
    indicator: str  # REQUIRED	string	Urgency/importance of what this card conveys. Allowed values, in order of increasing urgency, are: info, warning, critical. The CDS Client MAY use this field to help make UI display decisions such as sort order or coloring.
    summary: str  # REQUIRED	string	One-sentence, <140-character summary message for display to the user inside of this card.
    source: str  # REQUIRED	object	Grouping structure for the Source of the information displayed on this card. The source should be the primary source of guidance for the decision support the card represents.
    uuid: str = None  # OPTIONAL	string	Unique identifier of the card. MAY be used for auditing and logging cards and SHALL be included in any subsequent calls to the CDS service's feedback endpoint.
    detail: str = None  # OPTIONAL	string	Optional detailed information to display; if provided MUST be represented in (GitHub Flavored) Markdown. (For non-urgent cards, the CDS Client MAY hide these details until the user clicks a link like "view more details...").
    suggestions: list = None  # OPTIONAL	array of Suggestions	Allows a service to suggest a set of changes in the context of the current activity (e.g. changing the dose of the medication currently being prescribed, for the medication-prescribe activity). If suggestions are present, selectionBehavior MUST also be provided.
    selectionBehavior: str = None  # OPTIONAL	string	Describes the intended selection behavior of the suggestions in the card. Allowed values are: at-most-one, indicating that the user may choose none or at most one of the suggestions;any, indicating that the end user may choose any number of suggestions including none of them and all of them. CDS Clients that do not understand the value MUST treat the card as an error.
    overrideReasons: str = None  # OPTIONAL	array of Coding	Override reasons can be selected by the end user when overriding a card without taking the suggested recommendations. The CDS service MAY return a list of override reasons to the CDS client. The CDS client SHOULD present these reasons to the clinician when they dismiss a card. A CDS client MAY augment the override reasons presented to the user with its own reasons.
    links: list = None  # OPTIONAL array of Links	Allows a service to suggest a link to an app that the user might want to run for additional information or to help guide a decision.

    @staticmethod
    def info(summary, source, **kwargs):
        return Card("info", summary, source, **kwargs)

    @staticmethod
    def warning(summary, source, **kwargs):
        return Card("warning", summary, source, **kwargs)

    @staticmethod
    def critical(summary, source, **kwargs):
        return Card("critical", summary, source, **kwargs)

    def to_dict(self):
        return asdict(self)


class Response(object):

    def __init__(self, cards=None, statusCode=None):
        if cards is None:
            self.cards = []
        if statusCode is None:
            self.httpStatusCode = 0

    cards: List[Card]
    systemActions: str
    httpStatusCode: int  # any http code but mainly 200 or 412: The CDS Service is unable to retrieve the necessary FHIR data to execute its decision support, either through a prefetch request or directly calling the FHIR server.

    def to_dict(self) -> (dict, int):
        return {"cards": [c.to_dict() for c in self.cards]}
