from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Float, Integer, DECIMAL, DateTime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine(
    "sqlite:///./flowers.db",
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

class ClientModel(Base):
    __tablename__ = 'client'
    id = Column(Integer, primary_key=True, index=True)
    fio = Column(String)
    city = Column(String)
    address = Column(String)
    telephone = Column(String)
    E_mail = Column(String)
    customer_discount = Column(Float)


class DeliveryModel(Base):
    __tablename__ = 'delivery'
    id = Column(Integer, primary_key=True, index=True)
    delivery_method = Column(String)


class FlowersInAssortimentModel(Base):
    __tablename__ = 'flowers_in_assortiment'
    id = Column(Integer, primary_key=True, index=True)
    type_code = Column(Float)
    name = Column(String)
    price = Column(DECIMAL)
    vendor_code = Column(Float)
    accounting = Column(Float)


class OrderaModel(Base):
    __tablename__ = 'ordera'
    id = Column(Integer, primary_key=True, index=True)
    client_code = Column(Float)
    client_address = Column(String)
    clirnt_city = Column(String)
    date_of_issue = Column(DateTime)
    delivery_date = Column(DateTime)
    delivery_code = Column(Float)
    delivery_price = Column(DECIMAL)


class OrderedModel(Base):
    __tablename__ = 'ordered'
    id = Column(Integer, primary_key=True, index=True)
    product_code = Column(Float)
    quantity = Column(Float)


class OrderedServicesModel(Base):
    __tablename__ = 'ordered_services'
    id = Column(Integer, primary_key=True, index=True)
    service_code = Column(Float)
    quantity = Column(Float)


class PaymentMethodModel(Base):
    __tablename__ = 'payment_method'
    id = Column(Integer, primary_key=True, index=True)
    payment = Column(String)


class ProviderModel(Base):
    __tablename__ = 'provider'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    address = Column(String)
    city = Column(String)
    telephone = Column(String)
    E_mail = Column(String)


class ServicessModel(Base):
    __tablename__ = 'servicess'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(DECIMAL)


class TypesModel(Base):
    __tablename__ = 'types'
    id = Column(Integer, primary_key=True, index=True)
    category = Column(String)
    description = Column(String)


Base.metadata.create_all(bind=engine)


def get_db():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    finally:
        session.close()

