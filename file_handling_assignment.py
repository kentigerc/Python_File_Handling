def main():
  try:
    #creating the file
    with open("my_file.txt", "w") as file:
      file.write("First Line\n")
      file.write("Second Line\n")
      file.write("Third Line\n")

     #file reading and display
    with open("my_file.txt", "r")as file:
         print("contents of my_file.txt:")
         for line in file:
            print(line.strip())
      #file appending
    with open("my_file.txt", "a") as file:
           file.write("Fourth Line\n")
           file.write("Fifth Line\n")
           file.write("Sixth Line\n")

  except FileNotFoundError:
      print("FIle not found.")

  except PermissionError:
      print("permission denied.")

  except Exception as e:
      print("An error occurred:", e)

  finally:
        print("Excecution complete.")

if __name__ == "__main__":
    main()                         