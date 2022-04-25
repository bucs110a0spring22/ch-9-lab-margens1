from Rectangle import Rectangle

class Surface:

  def __init__(self, filename, x, y, h, w):
    '''
    assigns self with filename and rectangle class
    args: self, filename, x, y, h, w
    return: self.image and self.rect
    '''
    self.image=filename
    self.rect=Rectangle(x,y,h,w)
  
  def getRect(self):
    '''
    returns self rectangle
    args: self
    return: self rectangle
    '''
    return self.rect