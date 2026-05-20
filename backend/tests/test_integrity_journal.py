from datetime import datetime, timezone

from app.core.integrity_journal import IntegrityJournalEntry


def test_integrity_journal_hash_is_deterministic():
    timestamp = datetime(2026, 5, 20, 12, 0, tzinfo=timezone.utc)
    previous_hash = "0" * 64

    first_hash = IntegrityJournalEntry.calculate_hash(
        timestamp=timestamp,
        organization_id="org-1",
        actor_id="actor-1",
        subject_type="evidence",
        subject_id="evidence-1",
        event_type="evidence_registered",
        reference_id="ref-1",
        previous_hash=previous_hash,
        metadata_json={"sha256": "abc"},
    )
    second_hash = IntegrityJournalEntry.calculate_hash(
        timestamp=timestamp,
        organization_id="org-1",
        actor_id="actor-1",
        subject_type="evidence",
        subject_id="evidence-1",
        event_type="evidence_registered",
        reference_id="ref-1",
        previous_hash=previous_hash,
        metadata_json={"sha256": "abc"},
    )

    assert first_hash == second_hash
    assert len(first_hash) == 64


def test_integrity_journal_hash_changes_with_metadata():
    timestamp = datetime(2026, 5, 20, 12, 0, tzinfo=timezone.utc)
    previous_hash = "0" * 64

    first_hash = IntegrityJournalEntry.calculate_hash(
        timestamp=timestamp,
        subject_type="evidence",
        event_type="evidence_registered",
        previous_hash=previous_hash,
        metadata_json={"sha256": "abc"},
    )
    second_hash = IntegrityJournalEntry.calculate_hash(
        timestamp=timestamp,
        subject_type="evidence",
        event_type="evidence_registered",
        previous_hash=previous_hash,
        metadata_json={"sha256": "def"},
    )

    assert first_hash != second_hash
