import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='')

origin = 'Centro, Florianópolis, SC, Brazil'
destination = 'Lagoa da Conceição, Florianópolis, SC, Brazil'

directions_result = gmaps.directions(
    origin=origin,
    destination=destination,
    mode="driving", 
    departure_time=datetime.now(), 
    traffic_model="best_guess"
)

if directions_result:
    print(f"Rotas entre {origin} e {destination}:")
    
    for step in directions_result[0]['legs'][0]['steps']:
        instruction = step['html_instructions']
        
        #verifica se há dados de 'duration_in_traffic', se não, usa 'duration'
        duration_info = step.get('duration_in_traffic', step['duration'])
        duration_text = duration_info['text']  # Extrai o texto legível do tempo

    
        print(f"Instrução: {instruction}")
        print(f"Tempo estimado: {duration_text}")
        print("-" * 40) 

else:
    print("Nenhuma rota encontrada.")
