{
	'targets' : [{
			'target_name' :
				'softhsm2-util',
			'type' :
				'executable',
			'sources' : [
				'src/bin/util/softhsm2-util.cpp',
				'src/bin/util/softhsm2-util-ossl.cpp',
				'src/bin/common/getpw.cpp',
				'src/bin/common/library.cpp'
			],
			'include_dirs' : [
				'src/lib/cryptoki_compat',
				'src/bin/common',
				'../../openssl/include'
			],
			'conditions' : [
				['OS=="win"',{
					'sources' : [
						'src/bin/win32/getopt.cpp',
						'src/bin/win32/config.h',
						'src/lib/win32/syslog.cpp',
					],
					'include_dirs' : [
						'src/lib/win32',
						'src/bin/win32'
					],
					'libraries' : [
						'ssleay32.lib',
						'libeay32.lib',
						'convarch.lib',
						'Advapi32.lib',
						'User32.lib',
						'Crypt32.lib',
						'Gdi32.lib'
					]
					}
				]
			]
		}
	],
    'target_defaults': {
		'default_configuration': 'Release',
		'configurations': {
		'Debug': {
			'defines': [ 'DEBUG', '_DEBUG' ],
			'msvs_settings': {
			'VCCLCompilerTool': {
				'RuntimeLibrary': 1, 
			},
			'VCLinkerTool': {
				'LinkTimeCodeGeneration': 0,
				'OptimizeReferences': 2,
				'EnableCOMDATFolding': 2,
				'LinkIncremental': 1,
				'GenerateDebugInformation': 'true',
				'AdditionalLibraryDirectories': [
					'../../openssl/out32.dbg',
					'Debug/lib',
				]
			}          
			}
		},
		'Release': {
			'defines': [ 'NDEBUG' ],
			'msvs_settings': {
			'VCCLCompilerTool': {
				'RuntimeLibrary': 0,
				'Optimization': 3,
				'FavorSizeOrSpeed': 1,
				'InlineFunctionExpansion': 2,
				'WholeProgramOptimization': 'true',
				'OmitFramePointers': 'true',
				'EnableFunctionLevelLinking': 'true',
				'EnableIntrinsicFunctions': 'true'            
			},
			'VCLinkerTool': {
				'LinkTimeCodeGeneration': 1,
				'OptimizeReferences': 2,
				'EnableCOMDATFolding': 2,
				'LinkIncremental': 1,
				'AdditionalLibraryDirectories': [
					'../../openssl/out32',
					'Release/lib',
				]            
			}          
			}
		}
		}  
	}
}
