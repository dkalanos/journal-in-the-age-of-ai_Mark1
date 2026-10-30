# 5-published/ · J3 and J4, together or not at all

`<paper>/certificate/` and `<paper>/publication/` are written in one step by `mark1 issue`, or not written.
There is no partial certificate and no publication without one: a paper judged not new or not of interest
leaves nothing here.

**The certificate** (`certificate/certificate.yaml`, `.md`) states the record's hash; the standard, protocol,
check and generator versions; the journal run and its models; the data tier; the kind of newness, with the
evidence map beside it; the interest judgment with the criteria version; the AI-use declaration; and the names
of the three people who signed (appendix D.5).

**The publication** (`publication/`) is the version of record: the paper and appendix as certified, and
`manifest.yaml` with the DOI, the record's hash, the files, a pointer to the certificate, and a link to the
record at its access tier. The journal links the record; it does not host it. The DOI is a placeholder
(`10.5555/mark1.<paper>`, `minted: false`) until a journal mints one.

Empty: no paper has earned a certificate. The live record went through review in round 1 and stands at
"new" after round 2's intake, where its real history ends. The test suite takes a copy of the record along the whole
path to a certificate (`tests/test_journey.py`), and a real paper will do so here.
