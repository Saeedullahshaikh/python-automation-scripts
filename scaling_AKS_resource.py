import requests
import subprocess

def get_weather_data(city):
    api_key = 'our weather api'
    base_url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}'
    response = requests.get(base_url)
    data = response.json()

    if 'error' not in data:
        weather =  data['current']['condition']['text']
        temp_c = data['current']['temp_c']
        print(f"weather in {city}: {weather}, temprature: {temp_c}Here you go — just copy and paste:Here you go — just copy and paste:°C")

        if 'Heavy rain' in weather:
            print("Scaling up AKS due to heavy rain. Scaling the no of pods in AKS")
            scale_aks_pods_using_kubectl(namespace='ourapp', deployment_name='ourapp', replicas=3)
        else:
            print(f"weather condition is not heavy rain. No scaling action is required")
    else:
        print(f"Error fetching data for {city}: {data['error']['message']}")
        
def scale_aks_pods_using_kubectl(namespace, deployment_name, replicas):
    try:
        subprocess.run([
            'kubectl', 'scale', f'deployment/{deployment_name}', f'--replicas={replicas}', '-n', namespace 
        ], check=True)
        print(f"scaled the deployment {deployment_name} to {replicas} pods.")
    except subprocess.CalledProcessError as e:
        print(f"Failed scale to pods: {e}")

get_weather_data('city')


