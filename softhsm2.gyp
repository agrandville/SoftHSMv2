{
	'includes': [
		'configure.gypi'
	],
	'targets' : [{
			'target_name' :
				'softhsm2',
			'type' :
				'shared_library',
			'dependencies': [
				'convarch.gyp:convarch',
				'softhsm2-util.gyp:softhsm2-util',
				'softhsm2-test.gyp:cryptotest',
			],
			'sources' : [
				'src/lib/access.h',
				'src/lib/access.cpp',
				'src/lib/P11Attributes.cpp',
				'src/lib/P11Attributes.h',
				'src/lib/P11Objects.cpp',
				'src/lib/P11Objects.h',
				'src/lib/main.cpp',
				'src/lib/SoftHSM.cpp',
			],
			'include_dirs' : [
				'src/lib/cryptoki_compat',
				'src/lib/object_store',			
				'src/lib/data_mgr',
				'src/lib/common',
				'src/lib/slot_mgr',
				'src/lib/crypto',
				'src/lib/session_mgr',
				'src/lib/handle_mgr'
			],
			'conditions' : [
				['OS=="win"', {
					'sources' : [
						'src/bin/win32/getpassphase.cpp',
						'src/bin/win32/getopt.cpp',
						'src/bin/win32/getopt.h'
					],
					'defines' : [
						'WIN32'
					],
					'cflags': [
						'/WX','/Od'
					],
					'include_dirs' : [
						'src/bin/win32',
						'src/lib/win32'
					],
					'libraries' : [
						'convarch.lib',
						'Advapi32.lib',
						'User32.lib',
						'Crypt32.lib',
						'Gdi32.lib'
					]
				}],
				['OS=="linux"', {
						'sources' : [
							#'config.h'
						],	
						'include_dirs' : [
							'./'
						],						
						'ldflags' : [
							'-Wl,--no-whole-archive'
						],
						'cflags': [ 
							'-fPIC'
						],
						'libraries' : [
							'-lssl','-lcrypto'
						]
					}
				],
				[ 'enable_debug_to_stderr==1', {'defines': ['DEBUG_LOG_STDERR',],}],
				[ 'build_with_openssl==1', {
					'include_dirs' : [
						'../../openssl/include'
					],
					'libraries' : [
						'../../openssl/out32/ssleay32.lib',
						'../../openssl/out32/libeay32.lib',
					],
					'defines': [
						'WITH_OPENSSL',
					],
				}],
				[ 'build_with_botan==1', {
					'include_dirs' : [
						'../../botan/build/include'
					],
					'libraries' : [
						'../../botan/botan.lib'
					],
					'defines': [
						'WITH_BOTAN',
					],
				}]	
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
					'Release/lib'
				]            
			}          
			}
		}
		}  
	}
}
