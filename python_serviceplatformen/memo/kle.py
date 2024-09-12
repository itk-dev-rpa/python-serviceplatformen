from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://kle-online.dk/"


@dataclass
class ActivityFacet:
    class Meta:
        name = "activityFacet"
        namespace = "http://kle-online.dk/"

    value: str = field(
        metadata={
            "required": True,
            "max_length": 256,
        },
    )


@dataclass
class Label:
    class Meta:
        name = "label"
        namespace = "http://kle-online.dk/"

    value: str = field(
        metadata={
            "required": True,
            "max_length": 256,
        },
    )


@dataclass
class SubjectKey:
    class Meta:
        name = "subjectKey"
        namespace = "http://kle-online.dk/"

    value: str = field(
        metadata={
            "required": True,
            "max_length": 256,
        },
    )


@dataclass
class Version:
    class Meta:
        name = "version"
        namespace = "http://kle-online.dk/"

    value: str = field(
        metadata={
            "required": True,
            "max_length": 256,
        },
    )


@dataclass
class Kledata:
    class Meta:
        name = "KLEdata"
        namespace = "http://kle-online.dk/"

    subject_key: SubjectKey = field(
        metadata={
            "name": "subjectKey",
            "type": "Element",
            "required": True,
        },
    )
    version: Version = field(
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    label: Label = field(
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    activity_facet: Optional[ActivityFacet] = field(
        default=None,
        metadata={
            "name": "activityFacet",
            "type": "Element",
        },
    )
