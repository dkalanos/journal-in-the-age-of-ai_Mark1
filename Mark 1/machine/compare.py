from .findings import Finding, FindingsReport


def mark_absent(journal: FindingsReport, author: FindingsReport) -> tuple[list[Finding], list[Finding]]:
    """Mark each journal finding the author's own run did not produce (appendix D.8); also list the reverse."""
    author_keys = {f.key for f in author.findings}
    journal_keys = {f.key for f in journal.findings}
    for f in journal.findings:
        f.absent_from_author = f.key not in author_keys
    absent = [f for f in journal.findings if f.absent_from_author]
    author_only = [f for f in author.findings if f.key not in journal_keys]
    return absent, author_only
