from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.form-online.dk/"


@dataclass
class ActivityFacet:
    class Meta:
        name = "activityFacet"
        namespace = "http://www.form-online.dk/"

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
        namespace = "http://www.form-online.dk/"

    value: str = field(
        metadata={
            "required": True,
            "max_length": 256,
        },
    )


@dataclass
class TaskKey:
    class Meta:
        name = "taskKey"
        namespace = "http://www.form-online.dk/"

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
        namespace = "http://www.form-online.dk/"

    value: str = field(
        metadata={
            "required": True,
            "max_length": 256,
        },
    )


@dataclass
class Formdata:
    class Meta:
        name = "FORMdata"
        namespace = "http://www.form-online.dk/"

    task_key: TaskKey = field(
        metadata={
            "name": "taskKey",
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
    activity_facet: ActivityFacet = field(
        metadata={
            "name": "activityFacet",
            "type": "Element",
        },
    )
    label: Label = field(
        metadata={
            "type": "Element",
            "required": True,
        },
    )
