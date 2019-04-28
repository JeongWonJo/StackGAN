import os
import argparse
import sys
import skipthoughts
import pickle

dir_path = (os.path.abspath(os.path.join(os.path.realpath(__file__), './.')))
sys.path.append(dir_path)

model = skipthoughts.load_model()

def parse_args():
    parser = argparse.ArgumentParser(description='Yield Skip-Thought-Embedding')
    parser.add_argument('--caption_path', dest='caption_path',
                        help='directory to caption_path',
                        type=str)
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    print(args.caption_path)
    if args.caption_path is None:
        print("Specify your caption path")
    else:
        caption_path = os.getcwd().split("code")[0] + args.caption_path
        X = open(caption_path, 'r')
        lines  = X.readlines()
        lines = [line.strip() for line in lines]
        X.close()
        print("Converting to skip-thoughts embedding...")
        vectors = skipthoughts.encode(model, lines)
        f = open(caption_path.replace("txt", "pkl"), 'wb')
        pickle.dump(vectors, f)
        f.close()

