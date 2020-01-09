"""why do we need unittest? for testing? why do I need unittest? for
future refernce"""
import unittest
import pickle
import json

def request(id):
    # load the pickled model and scaled data
    X = pickle.load(open('./data/X_scaled.pkl', 'rb'))
    loaded_model = pickle.load(open('./models/kn_model.pkl', 'rb'))

    # run the request through the model
    results = loaded_model.kneighbors([X[id]])[1]

    # change results from ndarray to list for json dumping
    test_r = results.tolist()
    tj = json.dumps({'results': test_r})
    return tj

class TestStringMethods(unittest.TestCase):

    def test_requests(self):
        self.assertEqual(request(1),
'{"results": [[1, 177063, 69405, 197511, 83304, 108122, 6383, 107378, 101051, 136745]]}')

#adding a unittest for this is ridiculously long as the value returned is base64
# def test_visual(self):
#     self.asserEqual(visual(1), """ """)
if __name__=='__main__':
    unittest.main()
