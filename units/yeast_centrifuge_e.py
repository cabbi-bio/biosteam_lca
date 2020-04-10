# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 22:56:08 2019

@author: cyshi
"""
from biosteam import YeastCentrifuge
from built_in_EF import *
from units.fix import fix_results

if __name__ == '__main__':
    import YeastCentrifuge_e
    raise Exception('Succesfully Imported :-)')

def simulate(self):
    super().simulate()

def baseLCA(self, location=None):
    pass

#class YeastCentrifuge(Unit):
#    """Create a yeast centrifuge that separates out solids according to user defined split. Assume a continuous scroll solid bowl. 
#    
#    **Parameters**
#    
#        **split:** *[array_like]* Component splits to 0th output stream
#        
#        **solids:** *tuple[str]* IDs of solids 
#    
#    **ins**
#    
#        [:] Input streams
#    
#    **outs**
#    
#        [0] Liquid stream
#        
#        [1] Solids stream
#    
#    """
#    
#    _kwargs = {'split': None,
#               'solids': None}
#    
#    _run = Splitter._run
#    
#    def _cost(self):
#        Cost = self._results['Cost']
#        solids = self._kwargs['solids']
#        index = self.outs[0].indices(*solids)
#        mass_solids = 0
#        for s in self.ins:
#            mass_solids += s.mass[index]
#        ts = np.asarray(mass_solids).sum() # Total solids
#        ts *= 0.0011023 # To short tons (2000 lbs/hr)
#        if 2 < ts < 40:
#            Cost['Centrifuge'] = self.CEPCI*68040/567*ts**0.50
#        else:
#            raise DesignError(f'Solids loading ({ts}) is not within 2 and 40 tonns')
#        return Cost
