from evidently.test_suite import TestSuite
from evidently.tests import *


def check_data_integrity(df):

    data_integrity_dataset_tests = TestSuite(tests=[
    TestNumberOfColumns(),
    TestNumberOfRows(),
    TestNumberOfMissingValues(),
    TestShareOfMissingValues(),
    TestNumberOfColumnsWithMissingValues(),
    TestNumberOfRowsWithMissingValues(),
    TestShareOfColumnsWithMissingValues(),
    TestShareOfRowsWithMissingValues(),
    TestNumberOfDifferentMissingValues(),
    TestNumberOfConstantColumns(),
    TestNumberOfEmptyRows(),
    TestNumberOfEmptyColumns(),
    TestNumberOfDuplicatedRows(),
    TestNumberOfDuplicatedColumns(),
    TestColumnsType(),
    
    ])

    data_integrity_column_tests.run(reference_data=df, current_data=None)
    results = data_integrity_dataset_tests.as_dict()
    return results['all_passed']