from app.detection.rules import DETECTION_RULES


def test_detection_rules_have_required_fields():
    required_fields = {
        "id",
        "name",
        "severity",
        "conditions",
        "mitre_technique",
        "response",
    }

    for rule in DETECTION_RULES:
        assert required_fields.issubset(rule.keys())


def test_detection_rule_conditions_have_event_types():
    for rule in DETECTION_RULES:
        conditions = rule["conditions"]

        assert isinstance(conditions, dict)
        assert "event_types" in conditions
        assert isinstance(conditions["event_types"], list)
        assert len(conditions["event_types"]) > 0


def test_detection_rule_severity_is_valid():
    for rule in DETECTION_RULES:
        assert isinstance(rule["severity"], int)
        assert 1 <= rule["severity"] <= 10


def test_detection_rule_ids_are_unique():
    rule_ids = [rule["id"] for rule in DETECTION_RULES]

    assert len(rule_ids) == len(set(rule_ids))
