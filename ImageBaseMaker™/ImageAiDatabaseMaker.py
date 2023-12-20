try:
    from bing_image_downloader import downloader
except ImportError:
    import subprocess
    subprocess.run(["pip", "Install", "bing_image_downloader"])
try:
    from colorama import Fore, Back, Style
except ImportError:
    import subprocess
    subprocess.run(["pip", "Install", "colorama"])
import threading
print(f""" {Fore.BLUE} 
█████ █   █ █████ ████  █████  ███  █     ████  █████ █████ ████  
  █   █   █ █     █   █ █     █   █ █     █   █ █     █     █   █ 
  █   █████ ████  ████  ████  █████ █     ████  ████  ████  █   █ 
  █   █   █ █     █   █ █     █   █ █     █   █ █     █     █   █ 
  █   █   █ █████ █   █ █████ █   █ █████ █   █ █████ █████ ████  Coded by Reed, Have fun building your AI (I bet you will make something better than DALL-E even)""")
image = input(f" {Fore.GREEN}[?] What image to you want: ")
Num = int(input("[?] How many do you want: "))
threadsss = int(input("[?] How many threads 0=normal (Faster But gives A little more images (Thats a bug needed to be fixed)): "))
def MainJ():
  downloader.download(image, limit=Num, output_dir="ImageBase", adult_filter_off=False)
if __name__ == "__main__":
    threads = []  # Create a list to hold all threads
    for _ in range(threadsss):  # Replace 10 with the actual number of threads you want
        thread = threading.Thread(target=MainJ, args=())  # Create a new thread
        threads.append(thread)  # Add the new thread to the list
        thread.start()  # Start the new thread

    for thread in threads:
        thread.join()  # Wait for all threads to complete
