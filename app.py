from zebra import Zebra
from label import Label
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

z = Zebra('ZDesigner ZD411-203dpi ZPL')

hr_file = os.environ.get("HOMEROOM_FILE")
device_file = os.environ.get("DEVICE_FILE")

hr = pd.read_excel(hr_file, usecols='C')
devices = pd.read_csv(device_file, usecols=[2,7])

df = pd.merge(left = devices, right = hr, how='right', left_on='Student (email)', right_on='Email')

for index, row in df.iterrows():
    label = Label(f"{row['Serial Number']}")
    z.output(label.zebra_image)