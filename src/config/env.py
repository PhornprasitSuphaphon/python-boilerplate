
import os
import argparse
from dotenv import load_dotenv
from src.helper.logging import Logger

def parseArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['dev', 'prod'], default='dev', help='Set the environment mode Ex. python3 main.py dev')
    return parser.parse_args()

def loadEnvironment(mode):
    dotenvPath = f'.env.{mode}'
    load_dotenv(dotenvPath)
    return os.getenv('ENVIRONMENT')

def initiateEnv():
    args = parseArguments()
    mode = loadEnvironment(args.mode)
    Logger.info(f'Environment: {mode}\n')