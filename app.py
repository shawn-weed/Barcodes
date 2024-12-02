from zebra import Zebra
from label import Label

z = Zebra()

label = Label("Test")

z.send_command(label.create_label())