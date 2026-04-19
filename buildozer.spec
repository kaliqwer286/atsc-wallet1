[app]

title = ATSC钱包
package.name = atscwallet
package.domain = org.atsc.wallet
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0
requirements = python3,kivy==2.2.1,requests,websocket-client,Pillow
orientation = portrait
fullscreen = 1
android.permissions = INTERNET,ACCESS_NETWORK_STATE
android.api = 30
android.minapi = 21
android.ndk = 23b
android.sdk = 30
android.archs = arm64-v8a, armeabi-v7a
android.allow_background = 1
android.logcat_filters = *:S python:D
android.clean_build = 1
android.debug = 1

[buildozer]

log_level = 2
warn_on_root = 1
