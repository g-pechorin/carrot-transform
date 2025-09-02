"""
integration tests for cases where we "reuse person IDs" - a feature we've not looked at before

- no check to verify that the new IDs don't collide with
"""



@pytest.mark.integration
def test_reuse_dull(tmp_path: Path):
    raise 'run the test with no re-used ids and no file'

@pytest.mark.integration
def test_reuse_blank(tmp_path: Path):
    raise 'run the test with an empty file'

@pytest.mark.integration
def test_reuse_dull(tmp_path: Path):
    raise 'run the test with no re-used ids, but, some IDs in the file'

@pytest.mark.integration
def test_reuse_some(tmp_path: Path):
    raise 'run the test with some, but, not all ids resued'

@pytest.mark.integration
def test_reuse_full(tmp_path: Path):
    raise 'run the test with all re-used'


@pytest.mark.integration
def test_reuse_extra(tmp_path: Path):
    raise '??? do something to try and force a collision with new IDs and old IDs that are unused'


