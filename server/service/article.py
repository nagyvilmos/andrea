import server.repository.article as article_repository

def article_list(db, released):
    return article_repository.article_list(db, released)
    
def article(db, id, released):
    return article_repository.article(db,id, released)
    