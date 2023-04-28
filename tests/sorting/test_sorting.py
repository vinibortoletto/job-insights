from src.pre_built.sorting import sort_by
import pytest


@pytest.fixture
def job_list_ordered_by_min_salary():
    return [
        {
            "job_title": "Marketing",
            "company": "Relief",
            "state": "NY",
            "city": "New York",
            "min_salary": "100",
            "max_salary": "200",
            "job_desc": "Marketing operations of the company.",
            "industry": "Finance",
            "rating": "4.0",
            "date_posted": "2020-05-08",
            "valid_until": "2020-06-07",
            "job_type": "FULL_TIME",
            "id": "0",
        },
        {
            "job_title": "Registered Nurse",
            "company": "Queens Boulevard Endoscopy Center",
            "state": "NY",
            "city": "Rego Park",
            "min_salary": "200",
            "max_salary": "300",
            "job_desc": "Full-Time Registered Nurse!",
            "industry": "",
            "rating": "3.0",
            "date_posted": "",
            "valid_until": "2020-06-07",
            "job_type": "FULL_TIME",
            "id": "1",
        },
        {
            "job_title": "Dental Hygienist",
            "company": "Batista Dental",
            "state": "NJ",
            "city": "West New York",
            "min_salary": "",
            "max_salary": "",
            "job_desc": "Part-time or Full-timedental hygienist position.",
            "industry": "",
            "rating": "",
            "date_posted": "2020-05-02",
            "valid_until": "2020-06-07",
            "job_type": "PART_TIME",
            "id": "2",
        },
    ]


@pytest.fixture
def job_list_ordered_by_max_salary():
    return [
        {
            "job_title": "Registered Nurse",
            "company": "Queens Boulevard Endoscopy Center",
            "state": "NY",
            "city": "Rego Park",
            "min_salary": "200",
            "max_salary": "300",
            "job_desc": "Full-Time Registered Nurse!",
            "industry": "",
            "rating": "3.0",
            "date_posted": "",
            "valid_until": "2020-06-07",
            "job_type": "FULL_TIME",
            "id": "1",
        },
        {
            "job_title": "Marketing",
            "company": "Relief",
            "state": "NY",
            "city": "New York",
            "min_salary": "100",
            "max_salary": "200",
            "job_desc": "Marketing operations of the company.",
            "industry": "Finance",
            "rating": "4.0",
            "date_posted": "2020-05-08",
            "valid_until": "2020-06-07",
            "job_type": "FULL_TIME",
            "id": "0",
        },
        {
            "job_title": "Dental Hygienist",
            "company": "Batista Dental",
            "state": "NJ",
            "city": "West New York",
            "min_salary": "",
            "max_salary": "",
            "job_desc": "Part-time or Full-timedental hygienist position.",
            "industry": "",
            "rating": "",
            "date_posted": "2020-05-02",
            "valid_until": "2020-06-07",
            "job_type": "PART_TIME",
            "id": "2",
        },
    ]


@pytest.fixture
def job_list_ordered_by_date_posted():
    return [
        {
            "job_title": "Marketing",
            "company": "Relief",
            "state": "NY",
            "city": "New York",
            "min_salary": "100",
            "max_salary": "200",
            "job_desc": "Marketing operations of the company.",
            "industry": "Finance",
            "rating": "4.0",
            "date_posted": "2020-05-08",
            "valid_until": "2020-06-07",
            "job_type": "FULL_TIME",
            "id": "0",
        },
        {
            "job_title": "Dental Hygienist",
            "company": "Batista Dental",
            "state": "NJ",
            "city": "West New York",
            "min_salary": "",
            "max_salary": "",
            "job_desc": "Part-time or Full-timedental hygienist position.",
            "industry": "",
            "rating": "",
            "date_posted": "2020-05-02",
            "valid_until": "2020-06-07",
            "job_type": "PART_TIME",
            "id": "2",
        },
        {
            "job_title": "Registered Nurse",
            "company": "Queens Boulevard Endoscopy Center",
            "state": "NY",
            "city": "Rego Park",
            "min_salary": "200",
            "max_salary": "300",
            "job_desc": "Full-Time Registered Nurse!",
            "industry": "",
            "rating": "3.0",
            "date_posted": "",
            "valid_until": "2020-06-07",
            "job_type": "FULL_TIME",
            "id": "1",
        },
    ]


@pytest.fixture
def job_list_unordered():
    return [
        {
            "job_title": "Registered Nurse",
            "company": "Queens Boulevard Endoscopy Center",
            "state": "NY",
            "city": "Rego Park",
            "min_salary": "200",
            "max_salary": "300",
            "job_desc": "Full-Time Registered Nurse!",
            "industry": "",
            "rating": "3.0",
            "date_posted": "",
            "valid_until": "2020-06-07",
            "job_type": "FULL_TIME",
            "id": "1",
        },
        {
            "job_title": "Dental Hygienist",
            "company": "Batista Dental",
            "state": "NJ",
            "city": "West New York",
            "min_salary": "",
            "max_salary": "",
            "job_desc": "Part-time or Full-timedental hygienist position.",
            "industry": "",
            "rating": "",
            "date_posted": "2020-05-02",
            "valid_until": "2020-06-07",
            "job_type": "PART_TIME",
            "id": "2",
        },
        {
            "job_title": "Marketing",
            "company": "Relief",
            "state": "NY",
            "city": "New York",
            "min_salary": "100",
            "max_salary": "200",
            "job_desc": "Marketing operations of the company.",
            "industry": "Finance",
            "rating": "4.0",
            "date_posted": "2020-05-08",
            "valid_until": "2020-06-07",
            "job_type": "FULL_TIME",
            "id": "0",
        },
    ]


def test_sort_by_criteria(
    job_list_unordered,
    job_list_ordered_by_min_salary,
    job_list_ordered_by_max_salary,
    job_list_ordered_by_date_posted,
):
    last_index = len(job_list_unordered) - 1

    """Test if return is sorted by min_salary and ascending"""
    sort_by(job_list_unordered, "min_salary")
    assert job_list_unordered == job_list_ordered_by_min_salary
    assert job_list_unordered[last_index]["min_salary"] == ""

    """Test if return is sorted by max_salary and descending """
    sort_by(job_list_unordered, "max_salary")
    assert job_list_unordered == job_list_ordered_by_max_salary
    assert job_list_unordered[last_index]["max_salary"] == ""

    """Test if return is sorted by data_posted descending """
    sort_by(job_list_unordered, "date_posted")
    assert job_list_unordered == job_list_ordered_by_date_posted
    assert job_list_unordered[last_index]["date_posted"] == ""
