"""this simple module will be used to serialise a requests session to be stored in flask session"""
import pickle as pk

def serialize_session(session):
    return pk.dumps(session)


def deserialize_session(data):
    return pk.loads(data)

