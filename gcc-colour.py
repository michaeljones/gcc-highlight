# -*- coding: latin-1 -*-


from pygments.formatters import TerminalFormatter
from pygments.lexer import RegexLexer, bygroups
from pygments.token import Generic, Text, Name, Number
from pygments.style import Style

from pygments import highlight
import sys

class GccLexer(RegexLexer):
    name = 'gcc'
    aliases = ['gcc']
    filenames = ['*.gcc']

    tokens = {
        'root': [
            # Matches: <file>:<line>: error: <text>
            (r'(.*)(:)(.*)(:)( error)(:.*\n)', 
                bygroups( Name, Text, Number, Text, Generic.Error, Text ) ),

            # Matches: <file>:<line>: note: <text>
            (r'(.*)(:)(.*)(:)( note)(:.*\n)', 
                bygroups( Name, Text, Number, Text, Generic.Note, Text ) ),

            # Matches: <file>:<line>: warning: <text>
            (r'(.*)(:)(.*)(:)( warning)(:.*\n)', 
                bygroups( Name, Text, Number, Text, Generic.Warning, Text ) ),

            # Matches: In file included<file>: <text>
            (r'(In file included from [^:]*)(:)(.*)([:,]*\n)', 
                bygroups( Name, Text, Number, Text ) ),

            # Matches: <file>: <text>
            (r'([^:]*)(:.*:\n)', 
                bygroups( Name, Text ) ),

            (r'.*\n', Text),
        ]
    }


colours = {
        Generic.Error :     ( 'red', 'red' ),
        Generic.Note :      ( 'brown', 'brown' ),
        Generic.Warning :   ( 'yellow', 'yellow' ),
        Name :              ( 'teal', 'teal' ),
        Number :            ( 'white', 'white' ),
        Text :              ( 'lightgray', 'lightgray' ),
        }

while True:

    line = sys.stdin.readline()

    if not line:
        break

    output = highlight( line, GccLexer(), TerminalFormatter( colorscheme=colours ) )
    sys.stdout.write( output.encode( "latin-1" ) )


