Inputs for the Android build (.github/workflows/android.yml):
  icon.png / icon-round.png  launcher icons
  cpower.p12                 fallback signing key (public, password "cpower-public") so that
                             APKs from different builds share one signature and update in place.
                             Override with repo secrets ANDROID_KEYSTORE_B64 / _PASSWORD / _ALIAS.
