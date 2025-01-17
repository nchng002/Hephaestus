import sys
import time
import binascii

def login(password):
  key = binascii.unhexlify("31333436").decode('utf-8')
  correct_counter = 0
  try:
    for index, digit in enumerate(password):
      start_time = time.time()
      if digit != key[index]:
        time.sleep(1)
      else:
        correct_counter += 1
      elapsed_time = time.time() - start_time
      print(elapsed_time)
  except Exception as e:
    print("\n")
    print(f"Access denied... {e}")
    print("\n")
    return
  if correct_counter == len(key):
    print("\n")
    print("Flag: 0x4067{TIMELAPSE_IS_ALL_ABOUT_SIDE_CHANNELS}")
    print("\n")
  else:
    print("\n")
    print("Access denied...")
    print("\n")


def main():
  print("""
  
███████  ██ ███    ███ ██████  ██      ██   ██ ██████  ███████ ██████  
     ██ ███ ████  ████      ██ ██      ██   ██ ██   ██ ██           ██ 
    ██   ██ ██ ████ ██  █████  ██      ███████ ██████  ███████  █████  
   ██    ██ ██  ██  ██      ██ ██           ██ ██           ██      ██ 
   ██    ██ ██      ██ ██████  ███████      ██ ██      ███████ ██████
  """)
  if len(sys.argv) < 2:
    print("Usage: ./timelapse <password>")
    print("Please enter the 4 digit numerical password...")
    print("\n")
  else:
    login(sys.argv[1])


if __name__ == "__main__":
  main()