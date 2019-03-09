import connexion

import crypto_helpers as c
from swagger_server import db_path
from swagger_server.models.admin import Admin  # noqa: E501


def dump_db():  # noqa: E501
    """dump the database as a json object

    dump the database as a json object # noqa: E501


    :rtype: Admin
    """
    aes = c.AEScipher(db_path)
    data = aes.dump()
    aes.close()
    return {'status': 200, 'data': data}


def load_db(IdentityItems=None):  # noqa: E501
    """load set of IDs records from json object

    load set of IDs records from json object # noqa: E501

    :param IdentityItems: Collection of Identity items to add
    :type IdentityItems: list | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        aes = c.AEScipher(db_path)
        data = connexion.request.get_json()
        try:
            aes.load(data)
            # IdentityItems = [Id.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
            # for i in IdentityItems:
            #     aes.save(i.id, i.username, i.password)
            aes.close()
            
            return {'status': 200, 'message': 'Load successful'}
        
        except Exception:
            aes.close()
            return {'status': 400, 'message': 'Load failed'}
