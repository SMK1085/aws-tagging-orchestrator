from pydantic import Field
from pydantic_settings import BaseSettings

from .core import SettingsSourceType

class AppSettings(BaseSettings):
    source_type: SettingsSourceType = Field(
        ...,
        title="The source type",
        description="Defines where to pull the settings from",
    )
