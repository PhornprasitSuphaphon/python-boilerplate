import os
import argparse
from dotenv import load_dotenv
# from libs.test import some_function

parser = argparse.ArgumentParser()
parser.add_argument('mode', choices=['dev', 'prod'], default='dev', help='Set the environment mode')
args = parser.parse_args()
dotenv_path = f'.env.{args.mode}'
load_dotenv(dotenv_path=dotenv_path)

if __name__ == '__main__':
  current_mode = os.getenv('ENVIRONMENT')
  print(f'Environment Mode: {current_mode}')
  
