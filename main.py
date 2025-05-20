import sys
import json
from antlr4 import *
from CVLexer import CVLexer
from CVParser import CVParser
from CVToDictVisitor import CVToDictVisitor


def main():
    # Read the DSL CV JSON file
    with open("dsl_cv.json", "r", encoding="utf-8") as file:
        input_stream = InputStream(file.read())

    # Create lexer and parser
    lexer = CVLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CVParser(stream)

    # Parse the file
    tree = parser.cv()

    # Convert parse tree to Python dict
    visitor = CVToDictVisitor()
    result = visitor.visit(tree)

    # Print as JSON
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
