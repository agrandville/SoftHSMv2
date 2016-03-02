{
	'includes': [
		'configure.gypi'
	],
	'targets' : [{
			'target_name' :
				'softhsm2-util',
			'type' :
				'executable',
			'sources' : [
				'src/bin/util/softhsm2-util.cpp',
				'src/bin/common/getpw.cpp',
				'src/bin/common/library.cpp'
			],
			'include_dirs' : [
				'src/lib/cryptoki_compat',
				'src/bin/common',
				'src/lib/common'				
			],
			'defines' : [
				'PACKAGE_VERSION="<@(package_version)"',
				'MAX_PIN_LEN=<@(max_pin_len)',
				'MIN_PIN_LEN=<@(min_pin_len)',
			],
			'conditions' : [
				['OS=="win"',{
					'sources' : [
						'src/bin/win32/getopt.cpp',
						'src/lib/win32/syslog.cpp',
					],
					'include_dirs' : [
						'src/lib/win32',
						'src/bin/win32'
					],
					'libraries' : [
						'convarch.lib',
						'Advapi32.lib',
						'User32.lib',
						'Crypt32.lib',
						'Gdi32.lib'
					]}
				],
				['build_with_botan==1', {
					'sources' : [
						'src/bin/util/softhsm2-util-botan.cpp'
					],
					'include_dirs' : [
						'<@(botan_headers)',
					],
					'libraries' : [
						'<@(botan_libs)',
					]}
				],
				[ 'build_with_openssl==1', {
					'sources' : [
						'src/bin/util/softhsm2-util-ossl.cpp'
					],
					'include_dirs' : [
						'<@(openssl_headers)'
					],
					'libraries' : [
						'<@(openssl_libs)',
					]}
				],
				[ 'enable_debug_to_stderr==1', {'defines': ['DEBUG_LOG_STDERR',],}],
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
				'Optimization': 0,
			},
			'VCLinkerTool': {
				'ImageHasSafeExceptionHandlers': 'false',
				'LinkTimeCodeGeneration': 0,
				'OptimizeReferences': 2,
				'EnableCOMDATFolding': 2,
				'LinkIncremental': 1,
				'GenerateDebugInformation': 'true',
				'AdditionalLibraryDirectories': [
					#'../../openssl/out32.dbg',
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
				'ImageHasSafeExceptionHandlers': 'false',
				'LinkTimeCodeGeneration': 1,
				'OptimizeReferences': 2,
				'EnableCOMDATFolding': 2,
				'LinkIncremental': 1,
				'AdditionalLibraryDirectories': [
					#'../../openssl/out32',
					'Release/lib',
				]            
			}          
			}
		}
		}  
	}
}
