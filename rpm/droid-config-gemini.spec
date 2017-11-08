# These and other macros are documented in
# ../droid-configs-device/droid-configs.inc
%define device gemini
%define vendor xiaomi

%define vendor_pretty Xiaomi
%define device_pretty Mi 5

%define dcd_path ./

# Community HW adaptations need this
%define community_adaptation 1

# Adjust this for your device
%define pixel_ratio 2.0

# We assume most devices will
%define have_modem 1

Provides: ofono-configs

%include droid-configs-device/droid-configs.inc
