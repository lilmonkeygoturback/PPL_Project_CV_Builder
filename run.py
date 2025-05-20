import sys, os
import subprocess
from antlr4 import *
import json

# Define your variables
DIR = os.path.dirname(__file__)
ANTLR_JAR = 'D:/antlr/antlr4-4.9.2-complete.jar'  # Update this path if needed
CPL_Dest = 'CompiledFiles'
SRC = 'CV.g4'
DSL_FILE = 'dsl_cv.json'


def printUsage():
    print('python run.py gen')
    print('python run.py parse')


def generateAntlr2Python():
    print('Antlr4 is running...')
    subprocess.run([
        'java', '-jar', ANTLR_JAR,
        '-o', CPL_Dest,
        '-no-listener',
        '-visitor',
        '-Dlanguage=Python3',
        SRC
    ])
    print('Generate successfully')


def parseDSL():
    sys.path.insert(0, os.path.join(DIR, CPL_Dest))
    from CVLexer import CVLexer
    from CVParser import CVParser
    from CVVisitor import CVVisitor
    from CVToDictVisitor import CVToDictVisitor

    dsl_path = os.path.join(DIR, DSL_FILE)
    with open(dsl_path, 'r', encoding='utf-8') as file:
        input_stream = InputStream(file.read())

    lexer = CVLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CVParser(stream)
    tree = parser.cv()

    visitor = CVToDictVisitor()
    result = visitor.visit(tree)
    print(json.dumps(result, indent=2))


def main(argv):
    print('ANTLR jar file: ' + str(ANTLR_JAR))
    if len(argv) < 1:
        printUsage()
    elif argv[0] == 'gen':
        generateAntlr2Python()
    elif argv[0] == 'parse':
        parseDSL()
    else:
        printUsage()

if __name__ == '__main__':
    main(sys.argv[1:])
