def evaluate(test_annotation_file, user_annotation_file, phase_codename, **kwargs):
    output = {}
    output['result'] = [
                {
                    'train_split': {
                        'ML': 123,
                        'NLP': 123,
                        'CV': 123,
                        'Total': 123,
                    }
                },
                {
                    'test_split': {
                        'ML': 123,
                        'NLP': 123,
                        'CV': 123,
                        'Total': 123,
                    }
                }
            ]

    return output