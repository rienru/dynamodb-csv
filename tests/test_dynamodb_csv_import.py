from app.dynamodb import csv_import


def test_dynamodb_csv_import(table):
    """Unit test csv import into DynamoDB table

    Args:
        table (Table): boto3 DynamoDB table mock object
    """

    csv_file = "sample.csv"

    result = csv_import(table, csv_file)
    print(result)

    assert result == "{name} csv imported {count} items".format(
        name=table.name, count=300)
