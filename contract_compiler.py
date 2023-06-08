import solcx

temp_file = solcx.compile_files(
    "AlertProcessor.sol",
    output_values=['abi', 'bin'],
    solc_version='0.8.18'
)

abi = temp_file['AlertProcessor.sol:AlertProcessor']['abi']
bytecode = temp_file['AlertProcessor.sol:AlertProcessor']['bin']

