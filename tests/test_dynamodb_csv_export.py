from app.dynamodb import csv_export


def test_dynamodb_csv_export(table):
    """Unit test export DynamoDB table to csv

    Args:
        table (Table): boto3 DynamoDB table mock object
    """

    size = 1000
    output_file = "sample_exp.csv"

    result = csv_export(table, output_file)
    print(result)

    assert result == "{name} csv exported {count} items".format(
        name=table.name, count=size)
