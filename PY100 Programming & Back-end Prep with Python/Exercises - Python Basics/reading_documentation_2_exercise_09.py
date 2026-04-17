# exception SyntaxError(message, details)
# Raised when the parser encounters a syntax error. This may occur in an import statement, in a call to the built-in functions compile(), exec(), or eval(), or when reading the initial script or standard input (also interactively).

# The str() of the exception instance returns only the error message. Details is a tuple whose members are also available as separate attributes.

# filename
# The name of the file the syntax error occurred in.
# lineno
# Which line number in the file the error occurred in. This is 1-indexed: the first line in the file has a lineno of 1.
# offset
# The column in the line where the error occurred. This is 1-indexed: the first character in the line has an offset of 1.
# text
# The source code text involved in the error.
# end_lineno
# Which line number in the file the error occurred ends in. This is 1-indexed: the first line in the file has a lineno of 1.
# end_offset
# The column in the end line where the error occurred finishes. This is 1-indexed: the first character in the line has an offset of 1.
# For errors in f-string fields, the message is prefixed by “f-string: ” and the offsets are offsets in a text constructed from the replacement expression. For example, compiling f’Bad {a b} field’ results in this args attribute: (‘f-string: …’, (‘’, 1, 2, ‘(a b)n’, 1, 5)).