import json
import yaml

my_config = {
    "username": "JohnJRambo",
    "password": "Rocky4Adrian",
    "weapons": ["M60", "Browning M2", "SVD Dragunov", "M72 LAW"],
    "personal_info": {
        "image": "/home/rambo/img/me_myself_i.jpg",
        "adrian": "https://www.youtube.com/watch?v=tad3NI68dKA"
    }
}

with open("rambo_data.yaml", mode="w", encoding="utf8") as fp:
    yaml.dump(my_config, fp, yaml.CDumper)

with open("demo_yaml.yml", encoding="utf8") as fp:
    data = yaml.load(fp, Loader=yaml.FullLoader)

print(json.dumps(data, indent=2))
