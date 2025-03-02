from server.dbClient import DataCursor

def random_testimonial(db:DataCursor):
    # this should really be an entity object but for now:
    rows = db.select('testimonials', ['name', 'date', 'statement'], None, ['RANDOM()'], None, 1)
    return None if rows is None else rows[0]
