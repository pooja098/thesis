# Constants for parsing GDB output

ASSEMBLY_START = "=>"
ASSEMBLER_DUMP = "End of assembler dump."
DUMP_OF_ASSEMBLY = "Dump of assembler code from"
IN_MAIN = "\"finish\" not meaningful in the outermost frame."
RETURN_TO_CONTINUE = "---Type <return> to continue, or q <return> to quit---"

ADDRESS_REGEX = "Symbol.*offset\s0\+([-|0-9]*)."
ARCH_REGEX = "file type mach-o-x86-([0-9]*)"
BOTTOM_REGEX = "[.|\s]*Stack level [0-9]+, frame at ([0-9a-zA-Z]*):"
BREAKPOINT_HIT_REGEX = "Breakpoint ([0-9]*),"
BREAKPOINT_NUM_REGEX = "Breakpoint\s([0-9]*)\sat"
BREAKPOINT_REGEX = "Breakpoint [0-9]*,"
EXIT_REGEX = "exited (.*)]"
FUNCTION_REGEX = "rip\s*=.*in\s+([0-9a-zA-Z\_\-]+)"
LINE_NUM_AND_ASSEMBLY_REGEX = "Line\s([0-9]*).*starts at address ([0-9a-zA-Z]*).*\s*and ends at ([0-9a-zA-Z]*)"
POP_ADDR_REGEX = "([0-9a-zA-Z]*)\s<.*>:\spop.*\s.*retq"
PRINT_REGISTER_REGEX = "[0-9]*\s=\s\(void \*\)\s(.*)"
PRINT_SAVED_REGISTER_REGEX = "\$[0-9]*\s=\s(\(void.*)"
REG_ADDR_REGEX = "\s([a-zA-Z]{3})\sat\s(0x[0-9a-zA-Z]*)"
RETURN_REGEX = "Value\sreturned\sis\s\$[0-9]*\s=\s([0-9a-zA-Z]*)"
STRUCT_REGEX = "(\(struct .* \*\))\s(0x[0-9a-zA-Z]*)"
SYMBOL_REGEX = "Symbol\s([0-9a-zA-Z_-]*).*offset\s0\+([-|0-9]*),\slength\s([0-9]*)"
VAL_REGEX = "\$[0-9]*\s=\s(.*)"
VAR_NAME_REGEX = "([a-zA-Z0-9_-]*)\s="