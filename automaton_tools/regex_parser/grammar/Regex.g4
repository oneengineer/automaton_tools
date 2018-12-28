grammar Regex;

// this comes from http://www.cs.sfu.ca/~cameron/Teaching/384/99-3/regexp-plg.html


root: re EOF;

re
    : elementary op=('*'|'+')   #Closure
    | re '{' digits ',''}'      #RepeatMin
    | re '{' digits ',' digits '}'  #RepeatMinMax
    | elementary                #Basic
    | re '?'                    #Option
    | re re                     #Concatenate
    | re '|' re                 #OrRule
    ;

elementary
    : '(' re ')'        #Parenthesis
    | '.'               #Any
    | '$'               #Eos
    | '^'               #Start
    | char              #CharRule
    | range_expr        #Range
    ;

range_expr
    : '[^' range_item ']' #NegativeSet
    | '[' range_item ']'  #PositiveSet
    ;

range_item
    : range_item range_item #ConcatRangeItem
    | char '-' char     #CharRange
    | char              #SingleChar
    ;


char
    : anyChar             #Character
    | '\\' anyChar         #Escaped
    ;

digits: Digit+             #ManyDigits
    ;

Digit
    : '0' .. '9'
    ;

anyChar
    : Digit
    | Letter
    | ' '
    ;


Letter
    :
       '\u0041'..'\u005a' |
       '\u005f' |
       '\u0061'..'\u007a' |
       '\u00c0'..'\u00d6' |
       '\u00d8'..'\u00f6' |
       '\u00f8'..'\u00ff' |
       '\u0100'..'\u1fff' |
       '\u3040'..'\u318f' |
       '\u3300'..'\u337f' |
       '\u3400'..'\u3d2d' |
       '\u4e00'..'\u9fff' |
       '\uf900'..'\ufaff'
    ;