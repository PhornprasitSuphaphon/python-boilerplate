import schema
def validate(data) : 

  format = schema.Schema({
    'text': str
  })

  try:
    format.validate(data)
    return True
  except schema.SchemaError:
    return False
