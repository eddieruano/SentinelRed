# -*- coding: utf-8 -*-
# @Author: Eddie Ruano
# @Date:   2017-06-16 03:49:48
# @Last Modified by:   Eddie Ruano
# @Last Modified time: 2017-06-16 13:31:02

import subprocess

class DESIVoice(object):
    # These are the locations of the audio files
    RespondStart   = "audio/wav_lets_start.wav"
    RespondSpeed00 = "audio/wav_tspeed0.wav"
    RespondSpeed01 = "audio/wav_tspeed1.wav"
    RespondSpeed02 = "audio/wav_tspeed2.wav"
    RespondSpeed03 = "audio/wav_tspeed3.wav"
    RespondSpeed04 = "audio/wav_tspeed4.wav"
    RespondPause = "audio/wav_pause2.wav"
    RespondPaused = "audio/wav_paused.wav"
    RespondOkay = "audio/wav_okay_megan.wav"
    RespondRails = "audio/wav_rem_rails.wav"
    RespondProx = "audio/wav_rem_rails.wav"
    RespondRestart = "audio/wav_restart.wav"

    def __init__(self):
        