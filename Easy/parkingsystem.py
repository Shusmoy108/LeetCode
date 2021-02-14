class ParkingSystem(object):

    def __init__(self, big, medium, small):
        self.big=big
        self.medium=medium
        self.small=small
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        

    def addCar(self, carType):
        if carType==1 :
            if self.big==0:
                return False
            else:
                self.big=self.big-1
                return True
        elif carType==2 :
            if self.medium==0:
                return False
            else:
                self.medium=self.medium-1
                return True
        elif carType==3 :
            if self.small==0:
                return False
            else:
                self.small=self.small-1
                return True
        """
        :type carType: int
        :rtype: bool
        """
