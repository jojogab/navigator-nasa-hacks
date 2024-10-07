def calculate_habitability(temperature, density, mass):

    temperature_habitable = 273.15 <= temperature <= 323.15  
    density_habitable = 1000 <= density <= 5000  
    mass_habitable = 1 <= mass <= 5 

    score = 0
    if temperature_habitable:
        score += 40 
    if density_habitable:
        score += 30  
    if mass_habitable:
        score += 30  

    return score

def calculate_obserbility(distanceEarth, planetRadius, planetMass):

<<<<<<< HEAD
=======
      
    
>>>>>>> 30e5e37d310589f88c0741bfa711fc8f8167db2f
    s_radius = (planetRadius - (0.75)/(3.5- 0.75)) * 0.4
    s_distance = (1 - (distanceEarth/613)) * 0.2 
    s_mass = ((planetMass - 1)/(5- 1)) * 0.4     
    score = (s_radius + s_distance + s_mass) * 100
    
    if(s_radius > 3.5):
        return 0
    
    return score


