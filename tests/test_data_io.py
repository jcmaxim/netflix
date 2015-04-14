def help_first_n_indices_of_generator_are_correct(data_point_generator, number_of_points, correct_index):
    from itertools import islice
    from utils.data_io import data_points
    from utils.data_paths import ALL_DATA_FILE_PATH, ALL_INDEX_FILE_PATH
    all_data = data_points(ALL_DATA_FILE_PATH)
    all_indices = data_points(ALL_INDEX_FILE_PATH)
    data_point = islice(data_point_generator, 0, number_of_points)
    for data_point in data_point:
        for some_point in all_data:
            index = int(next(all_indices)[0])
            if index == correct_index:
                assert data_point == some_point
                break


def test_base_points_returns_a_generator():
    from types import GeneratorType
    from utils.data_io import base_points

    assert isinstance(base_points(), GeneratorType)


def test_base_points_first_ten_are_correct():
    from utils.constants import BASE_INDEX
    from utils.data_io import base_points
    help_first_n_indices_of_generator_are_correct(base_points(), number_of_points=10, correct_index=BASE_INDEX)


def test_data_points_returns_a_generator():
    from types import GeneratorType
    from utils.data_io import data_points
    from utils.data_paths import ALL_DATA_FILE_PATH

    assert isinstance(data_points(ALL_DATA_FILE_PATH), GeneratorType)


def test_data_points_first_ten_are_correct():
    from utils.data_io import data_points
    from utils.data_paths import ALL_DATA_FILE_PATH

    data_points_generator = data_points(ALL_DATA_FILE_PATH)

    with open(ALL_DATA_FILE_PATH) as all_data_file:
        for _ in range(10):
            assert next(data_points_generator) == next(all_data_file).strip().split()


def test_hidden_points_first_ten_are_correct():
    from utils.constants import HIDDEN_INDEX
    from utils.data_io import hidden_points
    help_first_n_indices_of_generator_are_correct(hidden_points(), number_of_points=10, correct_index=HIDDEN_INDEX)


def test_hidden_points_returns_a_generator():
    from types import GeneratorType
    from utils.data_io import hidden_points

    assert isinstance(hidden_points(), GeneratorType)


def test_probe_points_first_ten_are_correct():
    from utils.constants import PROBE_INDEX
    from utils.data_io import probe_points
    help_first_n_indices_of_generator_are_correct(probe_points(), number_of_points=10, correct_index=PROBE_INDEX)


def test_probe_points_returns_a_generator():
    from types import GeneratorType
    from utils.data_io import probe_points

    assert isinstance(probe_points(), GeneratorType)


def test_qual_points_first_ten_are_correct():
    from utils.constants import QUAL_INDEX
    from utils.data_io import qual_points
    help_first_n_indices_of_generator_are_correct(qual_points(), number_of_points=10, correct_index=QUAL_INDEX)


def test_qual_points_returns_a_generator():
    from types import GeneratorType
    from utils.data_io import qual_points

    assert isinstance(qual_points(), GeneratorType)


def test_valid_points_first_ten_are_correct():
    from utils.constants import VALID_INDEX
    from utils.data_io import valid_points
    help_first_n_indices_of_generator_are_correct(valid_points(), number_of_points=10, correct_index=VALID_INDEX)


def test_valid_points_returns_a_generator():
    from types import GeneratorType
    from utils.data_io import valid_points

    assert isinstance(valid_points(), GeneratorType)


def test_indices_first_ten_correct():
    from utils.data_io import indices
    from utils.data_paths import ALL_INDEX_FILE_PATH

    indices_generator = indices(ALL_INDEX_FILE_PATH)

    with open(ALL_INDEX_FILE_PATH) as all_index_file:
        for _ in range(10):
            assert next(indices_generator) == int(next(all_index_file).strip())


def test_write_submission_creates_file():
    import os
    from utils.data_io import write_submission
    from utils.data_paths import SUBMISSIONS_DIR_PATH
    ratings = (1, 4, 3, 2, 5)
    submission_file_name = 'test.dta'
    submission_file_path = os.path.join(SUBMISSIONS_DIR_PATH, submission_file_name)
    assert not os.path.isfile(submission_file_path), "{} is for test_data_io's use only".format(submission_file_path)

    try:
        write_submission(ratings, submission_file_name)
        assert os.path.isfile(submission_file_path), 'write_submission did not create {}'.format(submission_file_path)
    finally:
        os.remove(submission_file_path)


def test_write_submission_writes_correct_ratings():
    import os
    from utils.data_io import write_submission
    from utils.data_paths import SUBMISSIONS_DIR_PATH
    ratings = (1, 4.0, 3.1, 2.01, 5.001)
    submission_file_name = 'test.dta'
    submission_file_path = os.path.join(SUBMISSIONS_DIR_PATH, submission_file_name)
    assert not os.path.isfile(submission_file_path), "{} is for test_data_io's use only".format(submission_file_path)

    try:
        write_submission(ratings, submission_file_name)
        with open(submission_file_path, 'r') as submission_file:
            for rating in ratings:
                assert float(next(submission_file).strip()) == float(rating)
    finally:
        os.remove(submission_file_path)
