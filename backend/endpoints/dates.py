from fastapi import APIRouter, Request
from database.database import find_one_collection, add_to_collection, update_to_collection, delete_from_collection
from misc.misc import read_json, format_error_msg, format_success_msg, generate_unique_6_digit
import hashlib
import random
import string
import asyncio

router = APIRouter()

@router.post("/createDate")
async def createDateRequest(request: Request):
    a_pubkey,
    b_pubkey,
    a_id,
    b_id,
    stake,
    restaurant_pubkey,
    deadline,
    secA,
    secB,
    condA,
    condB,
    seqA,
    seqB, 
    error = await read_json(request, [
        "a_pubkey",
        "b_pubkey",
        "a_id",
        "b_id",
        "stake",
        "restaurant_pubkey",
        "deadline",
        "secA",
        "secB",
        "condA",
        "condB",
        "seqA",
        "seqB"])

    date_id = str(generate_unique_6_digit())
    if error:
        return format_error_msg(error)
    return createDate(date_id,
        a_pubkey,
        b_pubkey,
        a_id,
        b_id,
        stake,
        restaurant_pubkey,
        deadline,
        secA,
        secB,
        condA,
        condB,
        seqA,
        seqB)

def createDate(
    date_id,
    a_pubkey,
    b_pubkey,
    a_id,
    b_id,
    stake,
    restaurant_pubkey,
    deadline,
    secA,
    secB,
    condA,
    condB,
    seqA,
    seqB):
    date_jsn =  {
        "date_id": date_id,
        "a_pubkey": a_pubkey,
        "b_pubkey": b_pubkey,
        "a_id": a_id,
        "b_id": b_id,
        "stake": stake,
        "restaurant_pubkey": restaurant_pubkey,
        "deadline": deadline,
        "secA": secA,
        "secB": secB,
        "condA": condA,
        "condB": condB,
        "seqA": seqA,
        "seqB": seqB, 
        "isCompleted": False 
    }
    date = add_to_collection(date_jsn, "dates")
    return format_success_msg({"access": True})

@router.post("/getDate")
async def getDateRequest(request: Request):
    dateID, error = await read_json(request, ["dateID"])
    if error:
        return format_error_msg(error)
    return getDate(dateID)

def getDate(dateID):
    res = find_one_collection({"date_id": dateID}, "dates")
    if res != None:
        return format_success_msg({"date": res})
    else:
        return format_error_msg("No date found with this ID")

# Testing

temp = generate_unique_6_digit()
print(createDate(temp,
    "a_pubkey",
    "b_pubkey",
    "a_id",
    "b_id",
    100,
    "restaurant_pubkey",
    "deadline",
    "secA",
    "secB",
    "condA",
    "condB",
    "seqA",
    "seqB"))
print(getDate(temp))