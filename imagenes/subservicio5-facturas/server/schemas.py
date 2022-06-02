from datetime import date
import string
from tokenize import String
from typing import List, Optional

from pydantic import BaseModel


class VehiculoBase(BaseModel):
    title: str
    description: Optional[str] = None


class VehiculoCreate(VehiculoBase):
    pass


class Vehiculo(VehiculoBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class ClienteBase(BaseModel):
    pass
class ClienteCreate(ClienteBase):
    pass


class Cliente(ClienteBase):
    id: int
    vehiculos: List[Vehiculo] = []

    class Config:
        orm_mode = True


class FacturaBase(BaseModel):
    id : int
    cliente_id : int
    fecha_emision : str
    importe_total : float
    class Config:
        orm_mode = True
class ConceptoBase(BaseModel):
    id : int
    concepto_id: int
    importe: float
    factura_id: int

    class Config:
        orm_mode = True

class Concepto(ConceptoBase):
    pass


class Factura(FacturaBase):
    conceptos : List[Concepto] = []

class FacturaCreate(FacturaBase):

    pass


    