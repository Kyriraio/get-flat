from lib.service.kufar import get_new_flats as get_kufar_flats

def getNewFlats():
    flats = []
    kufar_flats = get_kufar_flats()
    if( len(kufar_flats) > 0):
        flats = flats + kufar_flats
    
    return flats; 