import os

def main():
    try:
        from chatthew.chatthew import Chatthew
        c = Chatthew()
        c.run(os.getenv('TOKEN'))
    except Exception as e:
        print(e)
        
if __name__ == '__main__':
    main()
                            
