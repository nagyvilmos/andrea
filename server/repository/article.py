from server.dbClient import DataCursor

def article_list(db:DataCursor, released:bool|None):
    # this should really be an entity object but for now:
    where = None if released is None else 'released = :released'
    return db.select('articles', ['link', 'title'], where, ['link'], {'released':released})

def article(db:DataCursor, id:str, released:bool|None):
    # this should really be an entity object but for now:
    where = 'link = :link' if released is None else 'link = :link and released = :released'
    return db.select_single('articles', ['link', 'title', 'content', 'released'], where, None, {'link': id, 'released':released})
