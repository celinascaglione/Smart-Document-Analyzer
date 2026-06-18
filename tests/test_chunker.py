from chunker import split_text_into_chunks


def test_overlap_chunking_creates_multiple_chunks():

    text = "A" * 2500

    chunks = split_text_into_chunks(
        text=text,
        chunk_size=1000,
        overlap=100,
    )

    assert len(chunks) > 1


def test_overlap_chunking_preserves_overlap():

    text = "A" * 2500

    chunks = split_text_into_chunks(
        text=text,
        chunk_size=1000,
        overlap=100,
    )

    assert chunks[0][-100:] == chunks[1][:100]