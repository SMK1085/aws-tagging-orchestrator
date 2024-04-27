import os
from unittest import mock

from aws_tagging_orchestrator.config import AppSettings, SettingsSourceType

@mock.patch.dict(os.environ, { "SOURCE_TYPE": "yaml" })
def test_source_type_yaml():
    settings = AppSettings()
    assert settings.source_type == SettingsSourceType.yaml

@mock.patch.dict(os.environ, { "SOURCE_TYPE": "json" })
def test_source_type_json():
    settings = AppSettings()
    assert settings.source_type == SettingsSourceType.json
