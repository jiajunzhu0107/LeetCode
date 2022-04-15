from portApi import db
from model import Port

def init_db():
    # db.drop_all()    
    db.create_all()
    db.session.commit()