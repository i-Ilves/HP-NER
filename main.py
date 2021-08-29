from sanic import Sanic, response as res

app = Sanic(__name__)

@app.get('/api/texts')
async def get_texts(req):
  from database import get_texts
  return res.json(await get_texts())


@app.post('/api/texts')
async def post_text(req):
  from database import create_text

  text = req.json
  text['id'] = await create_text(text)

  from nlp import getEntities
  entities = getEntities(text)
  return res.json(entities)

if __name__ == "__main__":
  app.run(port=8000)