"""Patch the generated Capacitor app/build.gradle: version + release signing (env-driven)."""
import re, sys
p, code, name = sys.argv[1:4]
s = open(p).read()
s = re.sub(r'versionCode \d+', 'versionCode ' + code, s)
s = re.sub(r'versionName "[^"]*"', 'versionName "' + name + '"', s)
signing = '''    signingConfigs {
        release {
            storeFile file(System.getenv("KS_FILE"))
            storeType System.getenv("KS_FILE").endsWith(".p12") ? "PKCS12" : "JKS"
            storePassword System.getenv("KS_PASSWORD")
            keyAlias System.getenv("KS_ALIAS")
            keyPassword System.getenv("KS_PASSWORD")
        }
    }
    buildTypes {'''
assert '    buildTypes {' in s
s = s.replace('    buildTypes {', signing, 1)
s = re.sub(r'(\n\s+release \{)(\s+minifyEnabled)', r'\1\n            signingConfig signingConfigs.release\2', s, count=1)
assert 'signingConfig signingConfigs.release' in s
open(p, 'w').write(s)
