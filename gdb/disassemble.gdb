# Get assembly code for given line number

set confirm off
set disassemble-next-line on
set logging overwrite on
set logging redirect on
set logging file ARG1
break ARG2
set logging on
run
set logging off
q