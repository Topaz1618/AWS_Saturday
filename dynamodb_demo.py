"""
    Note: This demo is for create fake data, when you facing the following situation:
        When you need to test those compexility syntax of search
        - You couldn't find a data that match/can't match the syntax on our DynamoDB that can let you make sure the
        boundary of this work, and what's kind of situation this word won't work or can work
        - Spend many times on looking for a quified test data on our production DynamoDB
"""

import boto3
from boto3.dynamodb.conditions import Attr


def get_eid(vin, brand, dp_profile, region, env):
    "vwfawdpcn-prod-sim-state-manager-vehicle-state_vw_vw-faw_cn_prod"

    table_pattern = '-sim-status-metadata_vw_'
    dp_solution = dp_profile.split('-')[1]
    dp_session = boto3.session.Session(profile_name=dp_profile)
    ddb_resource = dp_session.resource('dynamodb')
    # Populate sim-status table name
    if region in ('eu', 'ca', 'na'):
        sim_status_table = dp_solution + '-' + env + table_pattern + brand + '_' + region + '_' + env
    elif region in ('fawcn', 'svwcn'):
        sim_status_table = dp_solution + '-' + env + table_pattern + brand + '-' + region[0:3] + '_cn_' + env
    else:
        print('invalid region')

    table = ddb_resource.Table(sim_status_table)
    responses = []
    scan_kwargs = {
        'ProjectionExpression': 'externalId',
        'FilterExpression': Attr('vin').eq(vin),
    }
    response = table.scan(**scan_kwargs)
    responses = responses + response['Items']

    while response.get('LastEvaluatedKey'):
        scan_kwargs['ExclusiveStartKey'] = response.get('LastEvaluatedKey')
        response = table.scan(**scan_kwargs)
        responses = responses + response['Items']

    eid_list = [x['externalId'] for x in responses]
    eid = eid_list[0]

    return eid


def get_all_table_list(ddb_resource):
    all_table_list = list(ddb_resource.tables.all())

    return all_table_list


def get_table_by_patterns(patterns, all_table_list):
    table_names = list()

    for t in all_table_list:
        if all(p in t.name for p in patterns):
            table_names.append(t.name)

    if len(table_names) > 1:
        print("More than 1 table match the pattern: ")
        for i in table_names:
            print(i)

    table_name = table_names[0]

    return table_name


if __name__ == "__main__":
    from time import time

    t1 = time()
    dp_session = boto3.session.Session(region_name="cn-north-1")
    db_resource = dp_session.resource('dynamodb')
    print(time() - t1, type(db_resource))

