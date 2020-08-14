from time import sleep

def delay(seconds):
    print(f'Sleeping for {seconds} seconds(s)')
    sleep(seconds)

def main():
    for i in range(5):
        print(i)
        delay(seconds=2)

if __name__=='__main__':
    main()
