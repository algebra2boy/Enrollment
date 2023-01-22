pipeline = [
    {
        '$lookup': {
            'from': 'enrollment', 
            'localField': 'user_id', 
            'foreignField': 'user_id', 
            'as': 'result1'
        }
    }, {
        '$unwind': {
            'path': '$result1', 
            'includeArrayIndex': 'result1_id', 
            'preserveNullAndEmptyArrays': False
        }
    }, {
        '$lookup': {
            'from': 'course', 
            'localField': 'result1.courseID', 
            'foreignField': 'courseID', 
            'as': 'result2'
        }
    }, {
        '$unwind': {
            'path': '$result2', 
            'preserveNullAndEmptyArrays': False
        }
    }, {
        '$match': {
            'user_id': 1
        }
    }, {
        '$sort': {
            'courseID': 1
        }
    }
]