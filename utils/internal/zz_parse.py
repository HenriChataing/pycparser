from __future__ import print_function

import sys
from pycparser import c_parser, c_generator, c_ast, parse_file


if __name__ == "__main__":
    parser = c_parser.CParser()
    code = r'''
    const int ci;
    const int* pci;
    _Atomic(int) ai;
    _Atomic(int*) pai;
    _Atomic(_Atomic(int)*) ppai;
    '''

    print(code)
    ast = parser.parse(code)
    ast.show(attrnames=True, nodenames=True)
    #print(ast.ext[0].__slots__)
    #print(dir(ast.ext[0]))

    #print("==== From C generator:")
    #generator = c_generator.CGenerator()
    #print(generator.visit(ast))
