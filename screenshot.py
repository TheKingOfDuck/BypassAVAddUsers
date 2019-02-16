try:
  from PIL import ImageGrab
  im = ImageGrab.grab()
  im.save('screenshot.png')
  print("success")
except:
  print("error")
