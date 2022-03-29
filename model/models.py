# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Kuenstler(db.Model):
    __tablename__ = 'kuenstler'

    KuenstlerId = db.Column(db.Integer, primary_key=True, unique=True)
    Gehalt = db.Column(db.Integer)
    Herkunftsland = db.Column(db.String(40))
    Vorname = db.Column(db.String(40))
    Nachname = db.Column(db.String(40))
    ManagerId = db.Column(db.ForeignKey('manager.ManagerId'), index=True)

    manager = db.relationship('Manager', primaryjoin='Kuenstler.ManagerId == Manager.ManagerId', backref='kuenstlers')



class Lied(db.Model):
    __tablename__ = 'lied'

    LiedId = db.Column(db.Integer, primary_key=True, unique=True)
    Kuenstleranzahl = db.Column(db.Integer)
    Liedname = db.Column(db.String(40))
    Erscheinungsdatum = db.Column(db.Date)



class LiedKuenstler(db.Model):
    __tablename__ = 'lied_kuenstler'

    Id = db.Column(db.Integer, primary_key=True, unique=True)
    KuenstlerId = db.Column(db.ForeignKey('kuenstler.KuenstlerId'), index=True)
    LiedId = db.Column(db.ForeignKey('lied.LiedId'), index=True)

    kuenstler = db.relationship('Kuenstler', primaryjoin='LiedKuenstler.KuenstlerId == Kuenstler.KuenstlerId', backref='lied_kuenstlers')
    lied = db.relationship('Lied', primaryjoin='LiedKuenstler.LiedId == Lied.LiedId', backref='lied_kuenstlers')



class Manager(db.Model):
    __tablename__ = 'manager'

    ManagerId = db.Column(db.Integer, primary_key=True, unique=True)
    Vorname = db.Column(db.String(40))
    Nachname = db.Column(db.String(40))
    Firma = db.Column(db.String(40))
    Kuenstler_anzahl = db.Column(db.Integer)
