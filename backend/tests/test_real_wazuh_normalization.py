import json

from app.services.event_normalizer import EventNormalizer


def test_normalize_real_wazuh_sample():
    with open(
        "../docs/samples/wazuh-alert.json",
        "r",
        encoding="utf-8",
    ) as f:
        alert = json.load(f)

    normalized = EventNormalizer.normalize_wazuh_alert(alert)

    assert normalized.source == "wazuh"
    assert normalized.event_type == "windows_eventchannel"
    assert normalized.host == "sigma"
    assert normalized.severity == 5
    assert normalized.timestamp is not None
    assert normalized.message == "License activation (slui.exe) failed."
    assert normalized.raw_data == alert
