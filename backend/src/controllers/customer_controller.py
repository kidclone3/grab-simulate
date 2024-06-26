from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from src.models import get_session
from src.models.customers import *
from src.services import customer_service
from src.utils.exceptions import ExceptionMessage

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_customers(
        db: Session = Depends(get_session),
) -> ListCustomerSchema | ExceptionMessage:
    try:
        list_customers = await customer_service.get_all_customers(db)
        return list_customers
    except HTTPException as exception:
        message_exception = exception.detail
        return {"message": message_exception}


@router.post("/", status_code=status.HTTP_200_OK)
async def create_customer(
        customer: CustomerSchema,
        db: Session = Depends(get_session),
) -> ExceptionMessage:
    try:
        message = await customer_service.create_customer(customer, db)
        return message
    except HTTPException as exception:
        message_exception = exception.detail
        return {"message": message_exception}


@router.post("/update_destination", status_code=status.HTTP_200_OK)
async def update_destination(
        customer_id: str,
        destination: str,
        db: Session = Depends(get_session),
) -> ExceptionMessage:
    try:
        message = await customer_service.update_destination(customer_id, destination, db)
        return message
    except HTTPException as exception:
        message_exception = exception.detail
        return {"message": message_exception}


@router.get("/id", status_code=status.HTTP_200_OK)
async def get_customer(
        customer_id: str,
        db: Session = Depends(get_session),
) -> CustomerSchema | ExceptionMessage | None:
    try:
        customer = await customer_service.get_customer(customer_id, db)
        return customer
    except HTTPException as exception:
        message_exception = exception.detail
        return {"message": message_exception}


@router.delete("/id", status_code=status.HTTP_200_OK)
async def delete_customer(
        customer_id: str,
        db: Session = Depends(get_session),
) -> ExceptionMessage:
    try:
        message = await customer_service.delete_customer(customer_id, db)
        return message
    except HTTPException as exception:
        message_exception = exception.detail
        return {"message": message_exception}


@router.patch("/id", status_code=status.HTTP_200_OK)
async def update_customer_status(
        customer_id: str,
        active: bool,
        db: Session = Depends(get_session),
) -> ExceptionMessage:
    try:
        message = await customer_service.update_customer_status(customer_id, active, db)
        return message
    except HTTPException as exception:
        message_exception = exception.detail
        return {"message": message_exception}
