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

#FIXME: can return additional tournament, user attributes if required 
def serialize_game(g):
    return {
        'id': g.id,
        'tournament_id': g.tournament_id.id,
        'player_id': g.player_id.id,
        'player2_id': g.player2_id.id,
        'status': g.status,
        'score': g.score,
        'created_at': g.created_at,
        'updated_at': g.updated_at,
    }

