from db import db


class ProfileModel(db.Model):
    __tablename__ = "profile"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = db.relationship("UserModel", back_populates="profile",
                           uselist=False)
