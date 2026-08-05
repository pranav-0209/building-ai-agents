from schemas import ResearchFinding, Source


def collect_unique_sources(
    findings: list[ResearchFinding]
) -> list[Source]:

    unique_sources = {}

    for finding in findings:

        for source in finding.sources:

            if source.url not in unique_sources:
                unique_sources[source.url] = source

    return list(unique_sources.values())