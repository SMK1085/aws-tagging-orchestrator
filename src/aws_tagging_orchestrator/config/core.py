from enum import Enum


class SettingsSourceType(str, Enum):
    yaml = "yaml"
    json = "json"
