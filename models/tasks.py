class Task:
  def __init__(self, id, title, description, completed=False):
    self.__id = id
    self.title = title
    self.description = description
    self.completed = completed

  def get_id(self):
    return self.__id

  def to_dict(self):
    return {
      "id": self.get_id(),
      "title": self.title,
      "description": self.description,
      "completed": self.completed
    }