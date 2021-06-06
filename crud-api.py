from fastapi import FastAPI
from fastapi_crudrouter import SQLAlchemyCRUDRouter

from schemas import Client, Delivery, FlowersInAssortiment, Ordera, Ordered, OrderedServices, OrderedServicesCreate
from schemas import ClientCreate, DeliveryCreate, FlowersInAssortimentCreate, OrderaCreate, OrderedCreate
from schemas import PaymentMethod, PaymentMethodCreate, Provider, ProviderCreate, Servicess, ServicessCreate
from schemas import Types, TypesCreate
from model import ClientModel, DeliveryModel, FlowersInAssortimentModel, OrderaModel, OrderedModel, OrderedServicesModel
from model import PaymentMethodModel, ProviderModel, ServicessModel, TypesModel, get_db

app = FastAPI()

router_client = SQLAlchemyCRUDRouter(
    schema=Client,
    create_schema=ClientCreate,
    db_model=ClientModel,
    db=get_db,
    prefix='client'
)

router_delivery = SQLAlchemyCRUDRouter(
    schema=Delivery,
    create_schema=DeliveryCreate,
    db_model=DeliveryModel,
    db=get_db,
    prefix='delivery'
)

router_flowers_in_assortiment = SQLAlchemyCRUDRouter(
    schema=FlowersInAssortiment,
    create_schema=FlowersInAssortimentCreate,
    db_model=FlowersInAssortimentModel,
    db=get_db,
    prefix='flowers_in_assortiment'
)

router_ordera = SQLAlchemyCRUDRouter(
    schema=Ordera,
    create_schema=OrderaCreate,
    db_model=OrderaModel,
    db=get_db,
    prefix='ordera'
)

router_ordered = SQLAlchemyCRUDRouter(
    schema=Ordered,
    create_schema=OrderedCreate,
    db_model=OrderedModel,
    db=get_db,
    prefix='ordered'
)

router_ordered_services = SQLAlchemyCRUDRouter(
    schema=OrderedServices,
    create_schema=OrderedServicesCreate,
    db_model=OrderedServicesModel,
    db=get_db,
    prefix='ordered_services'
)

router_payment_method = SQLAlchemyCRUDRouter(
    schema=PaymentMethod,
    create_schema=PaymentMethodCreate,
    db_model=PaymentMethodModel,
    db=get_db,
    prefix='payment_method'
)

router_provider = SQLAlchemyCRUDRouter(
    schema=Provider,
    create_schema=ProviderCreate,
    db_model=ProviderModel,
    db=get_db,
    prefix='provider'
)

router_servicess = SQLAlchemyCRUDRouter(
    schema=Servicess,
    create_schema=ServicessCreate,
    db_model=ServicessModel,
    db=get_db,
    prefix='servicess'
)

router_types = SQLAlchemyCRUDRouter(
    schema=Types,
    create_schema=TypesCreate,
    db_model=TypesModel,
    db=get_db,
    prefix='types'
)

app.include_router(router_client)
app.include_router(router_delivery)
app.include_router(router_flowers_in_assortiment)
app.include_router(router_ordera)
app.include_router(router_ordered)
app.include_router(router_ordered_services)
app.include_router(router_payment_method)
app.include_router(router_provider)
app.include_router(router_servicess)
app.include_router(router_types)