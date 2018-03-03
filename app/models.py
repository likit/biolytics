from server import db
from sqlalchemy.sql import func

class UploadedData(db.Model):
    __tablename__ = 'uploaded_data'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    filename = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    uploaded_date = db.Column(db.DateTime(timezone=True), server_default=func.now())
    uploaded_by = db.Column(db.String(255))
