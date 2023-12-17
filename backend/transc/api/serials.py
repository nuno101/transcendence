def serialize_user(u):
    return {
        'id': u.id,
        'name': u.name,
        'fullname': u.fullname,
        'created_at': u.created_at,
        'updated_at': u.updated_at,
    }

def serialize_tournament(t):
    return {
        'id': t.id,
        'title': t.title,
        'description': t.description,
        'creator_id': t.creator_id,
        'status': t.status,
        'created_at': t.created_at,
        'updated_at': t.updated_at,
    }

