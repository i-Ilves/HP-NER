from databases import Database

db = Database('sqlite:texts-db.db')

async def get(query, values={}):
  rows = await db.fetch_all(query=query, values=values)
  dicts = []
  for row in rows:
    dicts.append(dict(row))
  return dicts


async def run(query, values={}):
  return await db.execute(query=query, values=values)

async def get_texts():
  return await get('SELECT * FROM texts')


async def create_text(text):
  query = 'INSERT INTO texts(text) VALUES(:text)'
  return await run(query, {
    "text": text['text']
  })