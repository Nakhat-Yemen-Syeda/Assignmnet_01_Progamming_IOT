from sense_hat import SenseHat
sense = SenseHat()

# Define the colours red and green
red = (255, 0, 0)
green = (0, 255, 0)

while True:

  # Take readings 
  t = sense.get_temperature()
  
  # Round the values to one decimal place
  t = round(t, 1)
  
  
  # Create the message
  # str() converts the value to a string so it can be concatenated
  message = "Temperature: " + str(t)
  
  if t <=10 :
    bg = blue
  elif t >= 10 and t<=25:
      bg=green
  else:
    bg = red
  
  # Display the scrolling message
  sense.show_message(message, scroll_speed=0.05, back_colour=bg)