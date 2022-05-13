from argparse import ArgumentParser
    
    
def main():
    rootParser	  = ArgumentParser(description='scrap')
    rootParser.add_argument('--name',default=None,type=str,required=True)
    rootParser.add_argument('--roll',default=None,type=int,required=False)
    rootParser.add_argument('--arg',default=None,type=str,required=False)
    args = rootParser.parse_args()
    print(args.__dict__)


if __name__ == "__main__":
    main()
