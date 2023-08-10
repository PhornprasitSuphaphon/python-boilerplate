class Login:
  def __init__(self):
    self.text = 'hello word'

  @classmethod
  def get(self):
      return self.text

  @classmethod
  def set(self, text):
    self.text = text


if __name__ == '__main__':
  pass