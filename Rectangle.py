class Rectangle:


  def __init__(self, x, y, h, w):
    '''
    assigns the self variable to be the higher of the parameter or 0
    args: self, x variable, y variable, height variable, width variable
    return: self.-the parameters
    '''
    self.x=max(0,x)
    self.y=max(0,y)
    self.height=max(0,h)
    self.width=max(0,w)

  def __str__(self):
    '''
    formats and prints the variables 
    args: self
    return: formatted display of variables
    '''
    s="(x: {}, y: {}) height: {}, width: {}"
    return s.format(self.x, self.y, self.height, self.width)

  
    
