from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    path = "tests/mocks/brazilians_jobs.csv"
    result = read_brazilian_file(path)

    """ Test if keys in dict are in english """
    for job in result:
        assert "title" in job
        assert "salary" in job
        assert "type" in job
