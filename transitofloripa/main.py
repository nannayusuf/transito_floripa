import googlemaps
from datetime import datetime
import pandas as pd
import time
from dotenv import load_dotenv
import os
import matplotlib.pyplot as plt

load_dotenv()

gmaps = googlemaps.Client(key=os.getenv('GOOGLE_MAPS_API_KEY'))

def collect_traffic_data():
    origin = 'Centro, Florianópolis, SC, Brazil'
    destination = 'Lagoa da Conceição, Florianópolis, SC, Brazil'
    
    directions = gmaps.directions(
        origin=origin,
        destination=destination,
        mode="driving",
        departure_time=datetime.now(),
        traffic_model="best_guess"
    )
    
    if directions:
        duration_info = directions[0]['legs'][0].get('duration_in_traffic', directions[0]['legs'][0]['duration'])
        duration_text = duration_info['text']
        
        df = pd.DataFrame({
            'origin': [origin],
            'destination': [destination],
            'estimated_time': [duration_text],
            'timestamp': [datetime.now()]
        })
        
        df.to_csv('traffic_data.csv', mode='a', header=False, index=False)
        print(f"Dados salvos: {origin} -> {destination}, Tempo estimado: {duration_text}")
    else:
        print("Nenhuma rota encontrada.")

def plot_traffic_data():
    try:
        df = pd.read_csv('traffic_data.csv', names=['origin', 'destination', 'estimated_time', 'timestamp'])
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        
        # Convert estimated_time to minutes
        df['time_in_minutes'] = df['estimated_time'].apply(lambda x: int(x.split()[0]))
        
        # Plot the graph
        plt.figure(figsize=(10, 6))
        plt.plot(df['timestamp'], df['time_in_minutes'], marker='o', linestyle='-')
        plt.title('Variação do Tempo de Viagem ao Longo do Tempo')
        plt.xlabel('Horário')
        plt.ylabel('Tempo Estimado (minutos)')
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    except FileNotFoundError:
        print("Arquivo de dados não encontrado.")

# Collect data and plot graph
while True:
    collect_traffic_data()
    plot_traffic_data()
    time.sleep(900)
