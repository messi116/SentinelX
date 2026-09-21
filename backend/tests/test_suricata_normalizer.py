import json

from app.services.event_normalizer import EventNormalizer


def test_normalize_real_suricata_event():
    with open(r".\sentinelx-suricata-event.json", "r", encoding="utf-8") as f:
        event = json.load(f)

    normalized = EventNormalizer.normalize_suricata_event(event)

    assert normalized.source == "suricata"
    assert normalized.event_type == "mdns"
    assert normalized.host == "eth0"
    assert normalized.source_ip == "192.168.18.204"
    assert normalized.source_port == 5353
    assert normalized.destination_ip == "224.0.0.251"
    assert normalized.destination_port == 5353
    assert normalized.message == "Suricata mdns event over UDP"
    assert normalized.raw_data == event
    assert normalized.raw_data["proto"] == "UDP"
    assert normalized.raw_data["flow_id"] == 783501271730494
