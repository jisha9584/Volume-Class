###########################################################
#   Computer Project #11
#
#   class Volume:
#       define functions
#           1. __init__: it is the construction function, it initializes objects.
#           2. __str__: for a valid object, display the magnitude (rounded to three dp) and the units, with one space between them.
#           3. __repr__: for a valid object, display the magnitude (rounded to six dp) and the units, with one space between them.
#           4. is_valid: checks if V is valid.
#           5. get_units: returns "ml" or "oz" if V is valid, None otherwise.
#           6. get_magnitude: returns magnitude stored during construction.
#           7. metric: returns a Volume object equivalent to V (in metric).
#           8. customary: returns a Volume object equivalent to V (in customary).
#           9. __eq__: the methods will compare the magnitudes of the two “Volume” objects. 
#           10. add: the class will support addition of two “Volume” objects.
#           11. sub: the class will support subtraction of two “Volume” objects.
###########################################################

UNITS = ["ml","oz"]
MLperOZ = 29.5735295625  # ml per oz
DELTA = 0.000001

class Volume(object):
    def __init__(self, magnitude = 0, units = 'ml'):   
        '''
        It is the construction function, it initializes objects.
        Parameters: magnitude and units
        Returns: None
        '''
        #checking if input is valid else returning none if invalid
        if units not in UNITS: 
            self.units = None 
            self.magnitude = None
        #checking if the magnitude is valid i.e.- a float or more than 0
        elif (type(magnitude) == float or type(magnitude) == int) and \
            (magnitude > 0):
            self.units = units
            self.magnitude = magnitude
        #in all other instances the units are None and the magnitude is 0
        else: 
            self.units = None
            self.magnitude = 0      

        
    def __str__(self):    
        '''
        For a valid object, the function will display the magnitude (rounded \
                        to 6 dp) and the units, with one space between them.
        Parameters: self
        Returns: (magnitude and units) or Not a Volume
        '''
        #if the units are valid pass for formating else return not a volume
        if self.units != None: 
            return "{:.3f} {}".format(self.magnitude, self.units)
        else: 
            return "Not a Volume"

        
    def __repr__(self):    # this line is incomplete: parameters needed
        '''
        For a valid object, the function will display the magnitude (rounded \
                        to 3 dp) and the units, with one space between them.
        Parameters: self
        Returns: (magnitude and units) or 'Not a Volume'
        '''
        #if the units are valid pass for formating else return not a volume
        if self.units != None: 
            return "{:.6f} {}".format(self.magnitude, self.units)
        else: 
            return "Not a Volume"

        
    def is_valid(self):     
        '''
        Checks if V is valid.
        Parameters: self
        Returns: bool
        '''
        #checking for the units being valid, returning true if the unit exists 
        return self.units != None

              
    def get_units(self):    
        '''
        Gets units stored during construction.
        Parameters: self
        Returns: 'ml', 'oz' or 'None'
        '''
        #returns the units
        return self.units

    
    def get_magnitude(self):  
        '''
        Gets magnitude stored during construction.
        Parameters: self
        Returns: numeric value if magnitude of V is valid or 0, None otherwise
        '''
        #if the magnitude is not in valid (None) return the magnitude
        if self.magnitude != None:
            return self.magnitude

    
    def metric(self):      
        '''
        Gets a Volume object equivalent to V (in metric).
        Parameters: self
        Returns: volume or None
        '''
        #checks if the units is in ml
        if self.units == 'ml':
            #if true returns the unit and magnitude 
            magnitude = self.get_magnitude()
            volume = Volume(self.magnitude, self.units)
        #checks if the units is in oz
        elif self.units == 'oz':
            #if true converts it from oz to ml
            magnitude = (self.get_magnitude())*MLperOZ
            units = 'ml'
            #returns the volume with updated magnitude and units
            volume = Volume(magnitude, units)   
        else:
            #if the units are None returns None for both
            return Volume(None, None)
        return volume

        
    def customary(self):    
        '''
        Gets a Volume object equivalent to V (in customary).
        Parameters: self
        Returns: volume or None
        '''
        #checks if the units is in oz
        if self.units == 'oz':
            #if true returns the unit and magnitude 
            magnitude = self.get_magnitude()
            volume = Volume(self.magnitude, self.units)
        #checks if the units is in ml
        elif self.units == 'ml':
            #if true converts it from ml to oz
            magnitude = (self.get_magnitude())/MLperOZ
            units = 'oz'
            #returns the volume with updated magnitude and units
            volume = Volume(magnitude, units)   
        else:
            #if the units are None returns None for both
            return Volume(None, None)
        return volume

                
    def __eq__(self, other): 
        '''
        The methods will compare the magnitudes of the two “Volume” objects. 
        Parameters: self, other
        Returns: bool
        '''
        #use isinstance
        if not isinstance(other, Volume):
            return False
        #checking for same units similarity
        elif self.units == other.units:
            return abs(self.magnitude - other.magnitude) < DELTA
        #checking for metric conversion similarity
        elif self.units  == 'ml' and other.units == 'oz':
            magnitude = other.metric()
            return abs(self.magnitude - other.magnitude) < DELTA
        #checking for customary conversion (initial val convert) similarity
        elif self.units  == 'oz' and other.units == 'ml':
            magnitude = self.metric()
            return abs(magnitude - other.magnitude) < DELTA    

                    
    def add(self, magnitude_inital):
        '''
        The function will support addition of two “Volume” objects.
        Parameters: self, magnitude_inital
        Returns: (the sum of volume and unit) or none
        '''
        magnitude = self.magnitude
        #use isinstance
        if isinstance(magnitude_inital, Volume):
            #checking for true units (i.e. not none)
            if magnitude_inital.units and self.units:
                #if the units are the same add (no conversion required)
                if self.units == magnitude_inital.units:
                    magnitude = self.magnitude
                    return Volume(self.magnitude + magnitude_inital.magnitude,\
                                  self.units)
                else:
                    #if V1 is in ml convert v2 to ml and then add
                    if self.units == 'ml': #rember switch 
                        m1 = magnitude_inital.metric()
                        return Volume(self.magnitude + m1.magnitude, \
                                      self.units)
                    #if V1 is in oz convert v2 to oz and then add
                    elif self.units == 'oz':
                        m1 = magnitude_inital.customary()
                        return Volume(self.magnitude + m1.magnitude, \
                                      self.units)
        #use isinstance, for adding constants if flt or int            
        elif isinstance(magnitude_inital, (float, int)):
            if self.units:
                return Volume(self.magnitude + magnitude_inital, self.units)
        return Volume(None, None)
        
            
    def sub(self, magnitude_inital): 
        '''
        The function will support subtraction of two “Volume” objects.
        Parameters: self, magnitude_inital
        Returns: (the difference of volume and unit) or none
        '''
        #SAME AS THE ADD FUNCTION JUST CHANGE SIGNS (+) BECOMES (-)
        magnitude = self.magnitude
        if isinstance(magnitude_inital, Volume):
            if magnitude_inital.units and self.units:  
                if self.units == magnitude_inital.units:
                    magnitude = self.magnitude
                    return Volume(self.magnitude - magnitude_inital.magnitude,\
                                  self.units)
                else:
                    
                    if self.units == 'ml': #rember switch 
                        m1 = magnitude_inital.metric()
                        return Volume(self.magnitude - m1.magnitude, \
                                      self.units)
                    elif self.units == 'oz':
                        m1 = magnitude_inital.customary()
                        return Volume(self.magnitude - m1.magnitude, \
                                      self.units)          
        elif isinstance(magnitude_inital, (float, int)):
            if self.units:
                return Volume(self.magnitude - magnitude_inital, self.units)
        return Volume(None, None)