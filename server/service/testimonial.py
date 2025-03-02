import server.repository.testimonial as testimonial_repository

def random_testimonial(db):
    return testimonial_repository.random_testimonial(db)
    