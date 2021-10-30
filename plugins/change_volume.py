import os

if os.name == 'nt':
    from ctypes import cast, POINTER
    from comtypes import CLSCTX_ALL
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
elif os.name == 'posix':
    from subprocess import call
else:
    from error_handling import error_handler
    error_handler.create_error_log('volume cannot run on your system')

def run(value):
    if os.name == 'nt':
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        scalarVolume = value / 100
        volume.SetMasterVolumeLevelScalar(scalarVolume, None)
    elif os.name == 'posix':
        call(["amixer", "-D", "pulse", "sset", "Master", str(value)+"%"])
