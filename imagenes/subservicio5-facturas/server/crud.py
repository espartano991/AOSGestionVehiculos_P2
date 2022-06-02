from http.client import HTTPException
from sqlalchemy.orm import Session
import bbdd.models as models
import schemas
from fastapi.encoders import jsonable_encoder


def get_Cliente(db: Session, Cliente_id: int):
    return db.query(models.Cliente).filter(models.Cliente.id == Cliente_id).first()


def get_Cliente_by_id(db: Session, id: str):
    return db.query(models.Cliente).filter(models.Cliente.id == id).first()


def get_Clientes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Cliente).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.ClienteCreate):
    db_user = models.Cliente()
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_Vehiculos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Vehiculo).offset(skip).limit(limit).all()


def create_Cliente_Vehiculo(db: Session, Vehiculo: schemas.VehiculoCreate, Cliente_id: int):
    db_Vehiculo = models.Vehiculo(**Vehiculo.dict(), owner_id=Cliente_id)
    db.add(db_Vehiculo)
    db.commit()
    db.refresh(db_Vehiculo)
    return db_Vehiculo

def get_clients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Cliente).offset(skip).limit(limit).all()


def get_facturas(db: Session,skip: int=0,limit: int=100):
    return db.query(models.Factura).offset(skip).limit(limit).all()

def create_factura(db: Session, Factura: schemas.FacturaCreate,id: int):
    
    conceptos = Factura.conceptos
    delattr(Factura,'conceptos')
    db_factura = models.Factura(**Factura.dict())    
    db.add(db_factura)
    for c in conceptos:
        db_concepto = models.FacturasConceptos(**c.dict())
        db.add(db_concepto)
    db.commit()
    db.refresh(db_factura)
    return db_factura

def get_factura_by_id(db: Session,factura_id: int):
    return db.query(models.Factura).filter(models.Factura.id == factura_id)

def get_facturas_by_cliente_id(db: Session, cliente_id: int):
    return db.query(models.Factura).filter(models.Factura.cliente_id==cliente_id)

def delete_factura(db: Session, id_factura: int):
    db.query(models.Factura).filter(models.Factura.id == id_factura).delete()
    db.commit()
    return 0

def update_factura(db: Session, Factura: schemas.Factura):
    factura = db.query(models.Factura).filter(models.Factura.id == Factura.id).first()
    if factura is not None:
        update_factura = Factura.dict(exclude_unset=True)
      
        if 'conceptos' in update_factura.keys():
            conceptos = update_factura['conceptos']
            update_factura.pop('conceptos',None)
        for key,value in update_factura.items():
            setattr(factura,key,value)
        for c in conceptos:
            db_concepto = models.FacturasConceptos(**c)
            db.add(db_concepto)
            db.commit()
        db.commit()
        db.refresh()
        return jsonable_encoder(factura)
    else:
        return HTTPException()
    