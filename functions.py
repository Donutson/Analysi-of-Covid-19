import numpy as np

def show_countries(countries, continents):
    """
        Show an numberd list of all countries in countries follow by it's continent
        
        Parameters:
       ------------
                    countries a ndarray containing the name of all the countries
                    continents a ndarray containing the name of all continents
    """
    count = 0
    n = len(countries)
    
    for i in range(n):
        count += 1
        print('   '+str(count)+'- '+countries[i]+'  ( '+continents[i]+' )')
        
    print()
    
    
def undo_cumulate(data):
    """
        Transform cumulative data to a non cumulative one.
        
        Parameters:
       ------------
                   data a ndarray containing the cumulative data
                   
       Return:
      -------
              A non cumulative version of our data
    """
    
    n = len(data)
    data1 = np.empty(n)
    data1[0] = data[0] 
    
    for i in range(n-1):
            data1[i+1]  = data[i+1] - data[i]
            
    return data1

