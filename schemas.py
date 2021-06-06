import datetime
from pydantic import BaseModel
from decimal import Decimal

class ClientCreate(BaseModel):
    id: int
    fio: str
    city: str
    address: str
    telephone: str
    E_mail: str
    customer_discount: float


class DeliveryCreate(BaseModel):
    id: int
    delivery_method: str


class FlowersInAssortimentCreate(BaseModel):
    id: int
    type_code: float
    name: str
    price: Decimal
    vendor_code: float
    accounting: float


class OrderaCreate(BaseModel):
    id: int
    client_code: float
    client_address: str
    clirnt_city: str
    date_of_issue: datetime.datetime
    delivery_date: datetime.datetime
    delivery_code: float
    delivery_price: Decimal


class OrderedCreate(BaseModel):
    id: int
    product_code: float
    quantity: float


class OrderedServicesCreate(BaseModel):
    id: int
    service_code: float
    quantity: float


class PaymentMethodCreate(BaseModel):
    id: int
    payment: str


class ProviderCreate(BaseModel):
    id: int
    name: str
    address: str
    city: str
    telephone: str
    E_mail: str


class ServicessCreate(BaseModel):
    id: int
    name: str
    price: Decimal


class TypesCreate(BaseModel):
    id: int
    category: str
    description: str


class Client(ClientCreate):
    id: int

    class Config:
        orm_mode = True


class Delivery(DeliveryCreate):
    id: int

    class Config:
        orm_mode = True


class FlowersInAssortiment(FlowersInAssortimentCreate):
    id: int

    class Config:
        orm_mode = True


class Ordera(OrderaCreate):
    id: int

    class Config:
        orm_mode = True


class Ordered(OrderedCreate):
    id: int

    class Config:
        orm_mode = True


class OrderedServices(OrderedServicesCreate):
    id: int

    class Config:
        orm_mode = True


class PaymentMethod(PaymentMethodCreate):
    id: int

    class Config:
        orm_mode = True


class Provider(ProviderCreate):
    id: int

    class Config:
        orm_mode = True


class Servicess(ServicessCreate):
    id: int

    class Config:
        orm_mode = True


class Types(TypesCreate):
    id: int

    class Config:
        orm_mode = True
