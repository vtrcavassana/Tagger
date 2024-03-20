from fastapi import FastAPI
from barcode import Code128
from barcode.writer import ImageWriter

from models import Item

app = FastAPI()

@app.get('/')
def home():
    return 'Oi'

@app.post('/create-tag')
async def create_tag(item: Item):
    code = item.code

    tag = Code128(code, writer=ImageWriter())
    arquivo_tag = tag.save('tag_nova')
    return {"Mensagem": arquivo_tag}