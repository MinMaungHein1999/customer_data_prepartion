from dynamo_db_manager import DynamoDbManager
class Pn2CustomerTableCreator:
    def __init__(self, table_name, region_name):
        self.table_name = table_name
        self.region_name = region_name
        self.set_global_secondary_indexes()
        self.set_local_secondary_indexes()
        self.set_table_attribute_definitions()
        self.set_key_schema()

    def create_table(self):
        DynamoDbManager.create_table_if_not_exists(
            self.table_name,
            self.key_schema,
            self.region_name,
            self.global_secondary_indexes,
            self.local_secondary_indexes,
            self.attribute_definitions)

    def set_global_secondary_indexes(self):
        self.global_secondary_indexes = [
            {
                'IndexName': 'NumberPlate3Index',
                'KeySchema': [
                    {
                        'AttributeName': 'Customer',
                        'KeyType': 'HASH'
                    },
                    {
                        'AttributeName': 'NumberPlate3',
                        'KeyType': 'RANGE'
                    }
                ],
                'Projection': {
                    'ProjectionType': 'ALL'
                },
                'ProvisionedThroughput': {
                    'ReadCapacityUnits': 1000,
                    'WriteCapacityUnits': 1000
                }
            },
            {
                'IndexName': 'NumberPlate4Index',
                'KeySchema': [
                    {
                        'AttributeName': 'Customer',
                        'KeyType': 'HASH'
                    },
                    {
                        'AttributeName': 'NumberPlate4',
                        'KeyType': 'RANGE'
                    }
                ],
                'Projection': {
                    'ProjectionType': 'ALL'
                },
                'ProvisionedThroughput': {
                    'ReadCapacityUnits': 1000,
                    'WriteCapacityUnits': 1000
                }
            },
            {
                'IndexName': 'NumberPlate5Index',
                'KeySchema': [
                    {
                        'AttributeName': 'Customer',
                        'KeyType': 'HASH'
                    },
                    {
                        'AttributeName': 'NumberPlate5',
                        'KeyType': 'RANGE'
                    }
                ],
                'Projection': {
                    'ProjectionType': 'ALL'
                },
                'ProvisionedThroughput': {
                    'ReadCapacityUnits': 1000,
                    'WriteCapacityUnits': 1000
                }
            },
            {
                'IndexName': 'NumberPlate6Index',
                'KeySchema': [
                    {
                        'AttributeName': 'Customer',
                        'KeyType': 'HASH'
                    },
                    {
                        'AttributeName': 'NumberPlate6',
                        'KeyType': 'RANGE'
                    }
                ],
                'Projection': {
                    'ProjectionType': 'ALL'
                },
                'ProvisionedThroughput': {
                    'ReadCapacityUnits': 1000,
                    'WriteCapacityUnits': 1000
                }
            },
            {
                'IndexName': 'NumberPlate2Index',
                'KeySchema': [
                    {
                        'AttributeName': 'NumberPlate2',
                        'KeyType': 'HASH'
                    }
                ],
                'Projection': {
                    'ProjectionType': 'ALL'
                },
                'ProvisionedThroughput': {
                    'ReadCapacityUnits': 1000,
                    'WriteCapacityUnits': 1000
                }
            }
        ]
    
    def set_local_secondary_indexes(self):
        self.local_secondary_indexes = [
            {
                'IndexName': 'NameKatakanaIndex',
                'KeySchema': [
                    {
                        'AttributeName': 'Customer',
                        'KeyType': 'HASH'
                    },
                    {
                        'AttributeName': 'NameKatakana',
                        'KeyType': 'RANGE'
                    }
                ],
                'Projection': {
                    'ProjectionType': 'ALL'
                }
            },
            {
                'IndexName': 'PhoneNumberIndex',
                'KeySchema': [
                    {
                        'AttributeName': 'Customer',
                        'KeyType': 'HASH'
                    },
                    {
                        'AttributeName': 'PhoneNumber',
                        'KeyType': 'RANGE'
                    }
                ],
                'Projection': {
                    'ProjectionType': 'ALL'
                }
            },
            {
                'IndexName': 'BranchNumberIndex',
                'KeySchema': [
                    {
                        'AttributeName': 'Customer',
                        'KeyType': 'HASH'
                    },
                    {
                        'AttributeName': 'BranchNumber',
                        'KeyType': 'RANGE'
                    }
                ],
                'Projection': {
                    'ProjectionType': 'ALL'
                }
            },
            {
                'IndexName': 'PolicyNumberIndex',
                'KeySchema': [
                    {
                        'AttributeName': 'Customer',
                        'KeyType': 'HASH'
                    },
                    {
                        'AttributeName': 'PolicyNumber',
                        'KeyType': 'RANGE'
                    }
                ],
                'Projection': {
                    'ProjectionType': 'ALL'
                }
            },
            {
                'IndexName': 'NumberPlate1Index',
                'KeySchema': [
                    {
                        'AttributeName': 'Customer',
                        'KeyType': 'HASH'
                    },
                    {
                        'AttributeName': 'NumberPlate1',
                        'KeyType': 'RANGE'
                    }
                ],
                'Projection': {
                    'ProjectionType': 'ALL'
                }
            }
        ]

    def set_key_schema(self):
        self.key_schema = [
            {
                'AttributeName': 'Customer',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'PolicyNumberAndBranchNumber',
                'KeyType': 'RANGE'
            }

        ]

    def set_table_attribute_definitions(self):
        self.attribute_definitions = [
            {
                'AttributeName': 'Customer',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'PolicyNumberAndBranchNumber',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'NameKatakana',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'PhoneNumber',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'BranchNumber',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'PolicyNumber',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'NumberPlate1',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'NumberPlate2',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'NumberPlate3',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'NumberPlate4',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'NumberPlate5',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'NumberPlate6',
                'AttributeType': 'S'
            }
            
        ]
