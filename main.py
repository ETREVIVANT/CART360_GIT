import machine
import time

led = machine.Pin("LED", machine.Pin.OUT) # The onboard green LED
# Setup Potentiometer on GP26
pot = machine.ADC(26)
pot2 = machine.ADC(27)

while True:
  led.toggle() # Flash the LED every time data is sent  
  # Read the value (0-65535)
  val = pot.read_u16()
  val2 = pot2.read_u16()
  
  # Send the value followed by a newline
  # We use a custom prefix "pot1:" so TouchDesigner can identify it easily
  print(f"pot1:{val}")
  print(f"pot2:{val2}")
  
  # Send data at 60fps (match TouchDesigner's default frame rate)
  time.sleep(1/30)