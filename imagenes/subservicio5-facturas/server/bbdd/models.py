from datetime import date


from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, Date
from sqlalchemy.orm import relationship

from .database import Base




class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    vehiculos = relationship("Vehiculo",back_populates="owner")
class Vehiculo(Base):
    __tablename__ = "vehiculos"

    id = Column(Integer, primary_key=True, index=True)
    cliente = Column(Integer, ForeignKey("clientes.id"))
    owner =     relationship("Cliente",back_populates="vehiculos")





class Factura(Base):
    __tablename__ = "facturas"
    id = Column(Integer,primary_key=True,index =True)
    cliente_id = Column(Integer)
    fecha_emision = Column(String)
    importe_total = Column(Float)
    conceptos = relationship("FacturasConceptos",back_populates="factura_cliente")
    
class FacturasConceptos(Base):
    __tablename__ = "facturasconceptos"
    id = Column(Integer,primary_key=True,index = True)
    factura_id = Column(Integer,ForeignKey("facturas.id"))
    concepto_id = Column(Integer)
    importe = Column(Integer)
    factura_cliente = relationship("Factura",back_populates="conceptos")

