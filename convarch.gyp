{
	'targets' : [{
			'target_name' :
				'convarch',
			'type' :
				'static_library',
			'sources' : [
				'src/lib/crypto/SymmetricAlgorithm.cpp',
				'src/lib/crypto/SymmetricKey.cpp',
				'src/lib/crypto/DESKey.cpp',
				'src/lib/crypto/DSAParameters.cpp',
				'src/lib/crypto/DSAPrivateKey.cpp',
				'src/lib/crypto/DSAPublicKey.cpp',
				'src/lib/crypto/RSAParameters.cpp',
				'src/lib/crypto/DHParameters.cpp',
				'src/lib/crypto/DHPrivateKey.cpp',
				'src/lib/crypto/DHPublicKey.cpp',
				'src/lib/crypto/ECParameters.cpp',
				'src/lib/crypto/ECPrivateKey.cpp',
				'src/lib/crypto/ECPublicKey.cpp',
				'src/lib/crypto/CryptoFactory.cpp',
				'src/lib/crypto/OSSLCryptoFactory.cpp',
				'src/lib/crypto/OSSLAES.cpp',
				'src/lib/crypto/HashAlgorithm.cpp',
				'src/lib/crypto/MacAlgorithm.cpp',
				'src/lib/crypto/OSSLGOST.cpp',
				'src/lib/crypto/OSSLGOSTKeyPair.cpp',
				'src/lib/crypto/OSSLGOSTPrivateKey.cpp',
				'src/lib/crypto/OSSLGOSTPublicKey.cpp',
				'src/lib/crypto/OSSLGOSTR3411.cpp',
				'src/lib/crypto/GOSTPrivateKey.cpp',
				'src/lib/crypto/GOSTPublicKey.cpp',
				'src/lib/crypto/AsymmetricAlgorithm.cpp',
				'src/lib/crypto/AsymmetricKeyPair.cpp',
				'src/lib/crypto/OSSLHMAC.cpp',
				'src/lib/crypto/OSSLECDH.cpp',
				'src/lib/crypto/OSSLECDSA.cpp',
				'src/lib/crypto/OSSLECKeyPair.cpp',
				'src/lib/crypto/OSSLECPrivateKey.cpp',
				'src/lib/crypto/OSSLECPublicKey.cpp',
				'src/lib/crypto/OSSLEVPHashAlgorithm.cpp',
				'src/lib/crypto/OSSLEVPMacAlgorithm.cpp',
				'src/lib/crypto/OSSLEVPSymmetricAlgorithm.cpp',
				'src/lib/crypto/OSSLMD5.cpp',
				'src/lib/crypto/OSSLRNG.cpp',
				'src/lib/crypto/OSSLRSA.cpp',
				'src/lib/crypto/OSSLRSAKeyPair.cpp',
				'src/lib/crypto/OSSLRSAPrivateKey.cpp',
				'src/lib/crypto/OSSLRSAPublicKey.cpp',
				'src/lib/crypto/RSAPrivateKey.cpp',
				'src/lib/crypto/RSAPublicKey.cpp',
				'src/lib/crypto/OSSLDES.cpp',
				'src/lib/crypto/OSSLSHA1.cpp',
				'src/lib/crypto/OSSLSHA224.cpp',
				'src/lib/crypto/OSSLSHA256.cpp',
				'src/lib/crypto/OSSLSHA384.cpp',
				'src/lib/crypto/OSSLSHA512.cpp',
				'src/lib/crypto/OSSLDH.cpp',
				'src/lib/crypto/OSSLDHKeyPair.cpp',
				'src/lib/crypto/OSSLDHPrivateKey.cpp',
				'src/lib/crypto/OSSLDHPublicKey.cpp',
				'src/lib/crypto/OSSLDSA.cpp',
				'src/lib/crypto/OSSLDSAKeyPair.cpp',
				'src/lib/crypto/OSSLDSAPrivateKey.cpp',
				'src/lib/crypto/OSSLDSAPublicKey.cpp',
				'src/lib/crypto/OSSLUtil.cpp',
				'src/lib/common/MutexFactory.cpp',
				'src/lib/common/osmutex.cpp',
				'src/lib/common/SimpleConfigLoader.cpp',
				'src/lib/common/log.cpp',
				'src/lib/common/fatal.cpp',
				'src/lib/common/Configuration.cpp',
				'src/lib/common/Configuration.h',
				'src/lib/data_mgr/ByteString.cpp',
				'src/lib/data_mgr/SecureDataManager.cpp',
				'src/lib/data_mgr/SecureMemoryRegistry.cpp',
				'src/lib/data_mgr/RFC4880.cpp',
				'src/lib/data_mgr/salloc.cpp',
				'src/lib/session_mgr/Session.cpp',
				'src/lib/session_mgr/SessionManager.cpp',
				'src/lib/object_store/Directory.cpp',
				'src/lib/object_store/File.cpp',
				'src/lib/object_store/FindOperation.cpp',
				'src/lib/object_store/Generation.cpp',
				'src/lib/object_store/ObjectFile.cpp',
				'src/lib/object_store/ObjectStore.cpp',
				'src/lib/object_store/ObjectStoreToken.cpp',
				'src/lib/object_store/OSAttribute.cpp',
				'src/lib/object_store/OSToken.cpp',
				'src/lib/object_store/SessionObject.cpp',
				'src/lib/object_store/SessionObjectStore.cpp',
				'src/lib/object_store/UUID.cpp',
				'src/lib/slot_mgr/Token.cpp',
				'src/lib/slot_mgr/Slot.cpp',
				'src/lib/slot_mgr/SlotManager.cpp',
				'src/lib/handle_mgr/Handle.cpp',
				'src/lib/handle_mgr/HandleManager.cpp'				
				
			],
			'include_dirs' : [
				'src/lib',
				'src/lib/cryptoki_compat',
				'src/lib/common',
				'src/lib/object_store',
				'src/lib/slot_mgr',
				'src/lib/session_mgr',
				'src/lib/handle_mgr',
				'src/lib/crypto',
				'src/lib/win32',
				'src/lib/data_mgr',
				'../../openssl/include'
			],
			'conditions' : [
				['OS=="win"',{
					'sources' : [
						'src/bin/win32/config.h',
						'src/lib/win32/syslog.cpp',
					],
					'include_dirs' : [
						'src/lib/win32',			
					]}
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
					'../../openssl/out32.dbg'
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
				'../../openssl/out32'
				]            
			}          
			}
		}
		}  
	}
}
