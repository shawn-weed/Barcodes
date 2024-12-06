from zebra import Zebra
from label import Label
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

z = Zebra('ZDesigner ZD411-203dpi ZPL')

device_file = os.environ.get("DEVICE_FILE")

devices = pd.read_csv(device_file)

for index, row in devices.iterrows():
    if f"{row['model']}" == 'HP Chromebook 11 G9 EE':
        print(f"{row['serialNumber']}")
        label = Label(f"{row['serialNumber']}")
        z.output(label.zebra_image)