from typing import List

from fastapi import APIRouter, Depends, HTTPException, status, Path, Query
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.schemas.contacts import ContactCreate, ContactResponce
from src.repository import contacts as repository_contacts

router = APIRouter(prefix='/contacts', tags=['contacts'])

@router.get('/all', response_model=List[ContactResponce])
async def get_contacts(db: Session = Depends(get_db)):
    contacts = await repository_contacts.get_contacts(db)
    return contacts

@router.get("/birthday", response_model=List[ContactResponce])
async def contacts_birthday(db: Session = Depends(get_db)):
    contacts = await repository_contacts.get_birthday_per_week(db)
    if contacts is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contacts not found")
    return contacts

@router.get('/{contact_id}', response_model=ContactResponce)
async def get_contact(contact_id: int = Path(ge=1), db: Session = Depends(get_db)):
    contact = await repository_contacts.get_contact_by_id(contact_id, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not found!')
    return contact

@router.get("/search/{query}", response_model=List[ContactResponce])
async def search_contact(query: str, db: Session = Depends(get_db)):
    contact = await repository_contacts.search_contact(query, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found!")
    return contact
    
@router.post('/', response_model=ContactResponce, status_code=status.HTTP_201_CREATED)
async def create_contact(body: ContactCreate, db: Session = Depends(get_db)):
    contact = await repository_contacts.get_contact_by_email(body.email, db)
    if contact:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Email is exists!')
    contact = await repository_contacts.create_contact(body, db)
    return contact

@router.put('/{contact_id}', response_model=ContactResponce)
async def update_contacts(body: ContactCreate, contact_id: int = Path(ge=1), db: Session = Depends(get_db)):
    contact = await repository_contacts.update_contact(contact_id, body, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not found!')
    return contact

@router.delete('/{contact_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_contacts(contact_id: int = Path(ge=1), db: Session = Depends(get_db)):
    contact = await repository_contacts.delete_contact(contact_id, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not found!')