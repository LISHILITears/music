#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2025.1.0),
    on 五月 12, 2025, at 01:17
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (
    NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, STOPPING, FINISHED, PRESSED, 
    RELEASED, FOREVER, priority
)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2025.1.0'
expName = '8'  # from the Builder filename that created this script
expVersion = ''
# a list of functions to run when the experiment ends (starts off blank)
runAtExit = []
# information about this experiment
expInfo = {
    'participant': '',
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'expVersion|hid': expVersion,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1536, 864]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']
    # replace default participant ID
    if prefs.piloting['replaceParticipantID']:
        expInfo['participant'] = 'pilot'

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version=expVersion,
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\lilis\\Desktop\\音乐情感实验\\musicalexperimentnina-master\\musicalexperimentnina-master\\8_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('exp')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    if PILOTING:
        # show a visual indicator if we're in piloting mode
        if prefs.piloting['showPilotingIndicator']:
            win.showPilotingIndicator()
        # always show the mouse in piloting mode
        if prefs.piloting['forceMouseVisible']:
            win.mouseVisible = True
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ptb'
        )
    if deviceManager.getDevice('keyWelcome') is None:
        # initialise keyWelcome
        keyWelcome = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='keyWelcome',
        )
    if deviceManager.getDevice('key_resp_welcome2') is None:
        # initialise key_resp_welcome2
        key_resp_welcome2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_welcome2',
        )
    if deviceManager.getDevice('key_respGender') is None:
        # initialise key_respGender
        key_respGender = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_respGender',
        )
    # create speaker 'soundfiles'
    deviceManager.addDevice(
        deviceName='soundfiles',
        deviceClass='psychopy.hardware.speaker.SpeakerDevice',
        index='-1',
        resample='True',
        latencyClass=1,
    )
    if deviceManager.getDevice('key_resp_endscreen') is None:
        # initialise key_resp_endscreen
        key_resp_endscreen = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_endscreen',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], currentRoutine=None):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    currentRoutine : psychopy.data.Routine
        Current Routine we are in at time of pausing, if any. This object tells PsychoPy what Components to pause/play/dispatch.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='PsychToolbox',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # dispatch messages on response components
        if currentRoutine is not None:
            for comp in currentRoutine.getDispatchComponents():
                comp.device.dispatchMessages()
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='PsychToolbox'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "Welcome_Screen" ---
    keyWelcome = keyboard.Keyboard(deviceName='keyWelcome')
    text_Welcome = visual.TextStim(win=win, name='text_Welcome',
        text='Welcome to my musical experiment!\n\nPress (SPACE) to start.',
        font='Arial',
        pos=(0, -0.05), draggable=False, height=0.05, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "Second_Welcome_Screen" ---
    Second_Welcome_Text = visual.TextStim(win=win, name='Second_Welcome_Text',
        text='Now you will hear some sound examples.\n\nPlease listen to the whole sound examples before deciding on your answer!\n\nPress (SPACE) to continue.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_welcome2 = keyboard.Keyboard(deviceName='key_resp_welcome2')
    
    # --- Initialize components for Routine "Age" ---
    text_Age = visual.TextStim(win=win, name='text_Age',
        text='How old are you? ',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    sliderAge = visual.Slider(win=win, name='sliderAge',
        startValue=None, size=(1.0, 0.1), pos=(0, -0.2), units=win.units,
        labels=('15-25', '25-35', '35-45', '45-'), ticks=(1, 2, 3,4), granularity=0,
        style=['rating'], styleTweaks=[], opacity=1,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='dkl',
        font='HelveticaBold', labelHeight=0.05,
        flip=False, ori=0, depth=-1, readOnly=False)
    
    # --- Initialize components for Routine "Gender" ---
    text_Gender = visual.TextStim(win=win, name='text_Gender',
        text="Please select your gender. Press 'f' for female and 'm' for male. ",
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    key_respGender = keyboard.Keyboard(deviceName='key_respGender')
    
    # --- Initialize components for Routine "Trial" ---
    soundfiles = sound.Sound(
        'A', 
        secs=-1, 
        stereo=True, 
        hamming=True, 
        speaker='soundfiles',    name='soundfiles'
    )
    soundfiles.setVolume(1)
    slider_sounds = visual.Slider(win=win, name='slider_sounds',
        startValue=None, size=(0.5, 0.1), pos=(0, -0.2), units=win.units,
        labels=('1', '2' , '3', '4', '5'), ticks=(1,2,3,4,5), granularity=1,
        style=['rating'], styleTweaks=[], opacity=1,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='dkl',
        font='HelveticaBold', labelHeight=0.05,
        flip=False, ori=0, depth=-1, readOnly=False)
    textsounds = visual.TextStim(win=win, name='textsounds',
        text='How aggressive do you percieve this piece of music? (1=not aggressive,5=very aggressive)',
        font='Arial',
        pos=(0, 0.17), draggable=False, height=0.05, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "musicalpreference_pop" ---
    text_PreferencePop = visual.TextStim(win=win, name='text_PreferencePop',
        text='On a scale from 1-5, how much do you like the genre Popular Music? (1=strongly disslike, 5=strongly like)',
        font='Arial',
        pos=[0,0.17], draggable=False, height=0.05, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    sliderPopPreference = visual.Slider(win=win, name='sliderPopPreference',
        startValue=None, size=(1.0, 0.1), pos=(0, -0.2), units=win.units,
        labels=('1', '2', '3', '4', '5'), ticks=(1, 2, 3, 4, 5), granularity=1,
        style=['rating'], styleTweaks=[], opacity=1,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='dkl',
        font='HelveticaBold', labelHeight=0.05,
        flip=False, ori=0, depth=-1, readOnly=False)
    
    # --- Initialize components for Routine "musicalpreference_classic" ---
    text_PreferenceClassic = visual.TextStim(win=win, name='text_PreferenceClassic',
        text='On a scale from 1-5, how much do you like the genre Classical Music? (1=strongly disslike, 5=strongly like)',
        font='Arial',
        pos=(0, 0.17), draggable=False, height=0.05, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    sliderClassicPreference = visual.Slider(win=win, name='sliderClassicPreference',
        startValue=None, size=(1.0, 0.1), pos=(0, -0.2), units=win.units,
        labels=('1', '2', '3', '4', '5'), ticks=[1, 2, 3, 4, 5], granularity=1,
        style=['rating'], styleTweaks=[], opacity=1,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='dkl',
        font='HelveticaBold', labelHeight=0.05,
        flip=False, ori=0, depth=-1, readOnly=False)
    
    # --- Initialize components for Routine "musicalpreference_heavymetal_" ---
    text_PreferenceHeavymetal = visual.TextStim(win=win, name='text_PreferenceHeavymetal',
        text='On a scale from 1-5, how much do you like the genre Heavy-Metal? (1=strongly disslike, 5=strongly like)',
        font='Arial',
        pos=(0, 0.17), draggable=False, height=0.05, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    slider_HeavymetalPreference = visual.Slider(win=win, name='slider_HeavymetalPreference',
        startValue=None, size=(1.0, 0.1), pos=(0, -0.2), units=win.units,
        labels=('1', '2', '3', '4', '5'), ticks=(1, 2, 3, 4, 5), granularity=1,
        style=['rating'], styleTweaks=[], opacity=1,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='dkl',
        font='HelveticaBold', labelHeight=0.05,
        flip=False, ori=0, depth=-1, readOnly=False)
    
    # --- Initialize components for Routine "EndScreen" ---
    textEnd = visual.TextStim(win=win, name='textEnd',
        text='Thanks for participating! \nPress space to leave the experiment!',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_endscreen = keyboard.Keyboard(deviceName='key_resp_endscreen')
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "Welcome_Screen" ---
    # create an object to store info about Routine Welcome_Screen
    Welcome_Screen = data.Routine(
        name='Welcome_Screen',
        components=[keyWelcome, text_Welcome],
    )
    Welcome_Screen.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for keyWelcome
    keyWelcome.keys = []
    keyWelcome.rt = []
    _keyWelcome_allKeys = []
    # store start times for Welcome_Screen
    Welcome_Screen.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Welcome_Screen.tStart = globalClock.getTime(format='float')
    Welcome_Screen.status = STARTED
    thisExp.addData('Welcome_Screen.started', Welcome_Screen.tStart)
    Welcome_Screen.maxDuration = None
    # keep track of which components have finished
    Welcome_ScreenComponents = Welcome_Screen.components
    for thisComponent in Welcome_Screen.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Welcome_Screen" ---
    Welcome_Screen.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *keyWelcome* updates
        waitOnFlip = False
        
        # if keyWelcome is starting this frame...
        if keyWelcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            keyWelcome.frameNStart = frameN  # exact frame index
            keyWelcome.tStart = t  # local t and not account for scr refresh
            keyWelcome.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyWelcome, 'tStartRefresh')  # time at next scr refresh
            # update status
            keyWelcome.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keyWelcome.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keyWelcome.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keyWelcome.status == STARTED and not waitOnFlip:
            theseKeys = keyWelcome.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _keyWelcome_allKeys.extend(theseKeys)
            if len(_keyWelcome_allKeys):
                keyWelcome.keys = _keyWelcome_allKeys[-1].name  # just the last key pressed
                keyWelcome.rt = _keyWelcome_allKeys[-1].rt
                keyWelcome.duration = _keyWelcome_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *text_Welcome* updates
        
        # if text_Welcome is starting this frame...
        if text_Welcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_Welcome.frameNStart = frameN  # exact frame index
            text_Welcome.tStart = t  # local t and not account for scr refresh
            text_Welcome.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_Welcome, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_Welcome.status = STARTED
            text_Welcome.setAutoDraw(True)
        
        # if text_Welcome is active this frame...
        if text_Welcome.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=Welcome_Screen,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Welcome_Screen.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Welcome_Screen.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Welcome_Screen" ---
    for thisComponent in Welcome_Screen.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Welcome_Screen
    Welcome_Screen.tStop = globalClock.getTime(format='float')
    Welcome_Screen.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Welcome_Screen.stopped', Welcome_Screen.tStop)
    thisExp.nextEntry()
    # the Routine "Welcome_Screen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Second_Welcome_Screen" ---
    # create an object to store info about Routine Second_Welcome_Screen
    Second_Welcome_Screen = data.Routine(
        name='Second_Welcome_Screen',
        components=[Second_Welcome_Text, key_resp_welcome2],
    )
    Second_Welcome_Screen.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_welcome2
    key_resp_welcome2.keys = []
    key_resp_welcome2.rt = []
    _key_resp_welcome2_allKeys = []
    # store start times for Second_Welcome_Screen
    Second_Welcome_Screen.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Second_Welcome_Screen.tStart = globalClock.getTime(format='float')
    Second_Welcome_Screen.status = STARTED
    thisExp.addData('Second_Welcome_Screen.started', Second_Welcome_Screen.tStart)
    Second_Welcome_Screen.maxDuration = None
    # keep track of which components have finished
    Second_Welcome_ScreenComponents = Second_Welcome_Screen.components
    for thisComponent in Second_Welcome_Screen.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Second_Welcome_Screen" ---
    Second_Welcome_Screen.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Second_Welcome_Text* updates
        
        # if Second_Welcome_Text is starting this frame...
        if Second_Welcome_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Second_Welcome_Text.frameNStart = frameN  # exact frame index
            Second_Welcome_Text.tStart = t  # local t and not account for scr refresh
            Second_Welcome_Text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Second_Welcome_Text, 'tStartRefresh')  # time at next scr refresh
            # update status
            Second_Welcome_Text.status = STARTED
            Second_Welcome_Text.setAutoDraw(True)
        
        # if Second_Welcome_Text is active this frame...
        if Second_Welcome_Text.status == STARTED:
            # update params
            pass
        
        # *key_resp_welcome2* updates
        waitOnFlip = False
        
        # if key_resp_welcome2 is starting this frame...
        if key_resp_welcome2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_welcome2.frameNStart = frameN  # exact frame index
            key_resp_welcome2.tStart = t  # local t and not account for scr refresh
            key_resp_welcome2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_welcome2, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_resp_welcome2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_welcome2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_welcome2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_welcome2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_welcome2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_welcome2_allKeys.extend(theseKeys)
            if len(_key_resp_welcome2_allKeys):
                key_resp_welcome2.keys = _key_resp_welcome2_allKeys[-1].name  # just the last key pressed
                key_resp_welcome2.rt = _key_resp_welcome2_allKeys[-1].rt
                key_resp_welcome2.duration = _key_resp_welcome2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=Second_Welcome_Screen,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Second_Welcome_Screen.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Second_Welcome_Screen.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Second_Welcome_Screen" ---
    for thisComponent in Second_Welcome_Screen.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Second_Welcome_Screen
    Second_Welcome_Screen.tStop = globalClock.getTime(format='float')
    Second_Welcome_Screen.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Second_Welcome_Screen.stopped', Second_Welcome_Screen.tStop)
    thisExp.nextEntry()
    # the Routine "Second_Welcome_Screen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Age" ---
    # create an object to store info about Routine Age
    Age = data.Routine(
        name='Age',
        components=[text_Age, sliderAge],
    )
    Age.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    sliderAge.reset()
    # store start times for Age
    Age.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Age.tStart = globalClock.getTime(format='float')
    Age.status = STARTED
    thisExp.addData('Age.started', Age.tStart)
    Age.maxDuration = None
    # keep track of which components have finished
    AgeComponents = Age.components
    for thisComponent in Age.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Age" ---
    Age.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_Age* updates
        
        # if text_Age is starting this frame...
        if text_Age.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_Age.frameNStart = frameN  # exact frame index
            text_Age.tStart = t  # local t and not account for scr refresh
            text_Age.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_Age, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_Age.started')
            # update status
            text_Age.status = STARTED
            text_Age.setAutoDraw(True)
        
        # if text_Age is active this frame...
        if text_Age.status == STARTED:
            # update params
            pass
        
        # *sliderAge* updates
        
        # if sliderAge is starting this frame...
        if sliderAge.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sliderAge.frameNStart = frameN  # exact frame index
            sliderAge.tStart = t  # local t and not account for scr refresh
            sliderAge.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sliderAge, 'tStartRefresh')  # time at next scr refresh
            # update status
            sliderAge.status = STARTED
            sliderAge.setAutoDraw(True)
        
        # if sliderAge is active this frame...
        if sliderAge.status == STARTED:
            # update params
            pass
        
        # Check sliderAge for response to end Routine
        if sliderAge.getRating() is not None and sliderAge.status == STARTED:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=Age,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Age.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Age.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Age" ---
    for thisComponent in Age.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Age
    Age.tStop = globalClock.getTime(format='float')
    Age.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Age.stopped', Age.tStop)
    thisExp.addData('sliderAge.response', sliderAge.getRating())
    thisExp.nextEntry()
    # the Routine "Age" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Gender" ---
    # create an object to store info about Routine Gender
    Gender = data.Routine(
        name='Gender',
        components=[text_Gender, key_respGender],
    )
    Gender.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_respGender
    key_respGender.keys = []
    key_respGender.rt = []
    _key_respGender_allKeys = []
    # store start times for Gender
    Gender.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Gender.tStart = globalClock.getTime(format='float')
    Gender.status = STARTED
    thisExp.addData('Gender.started', Gender.tStart)
    Gender.maxDuration = None
    # keep track of which components have finished
    GenderComponents = Gender.components
    for thisComponent in Gender.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Gender" ---
    Gender.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_Gender* updates
        
        # if text_Gender is starting this frame...
        if text_Gender.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_Gender.frameNStart = frameN  # exact frame index
            text_Gender.tStart = t  # local t and not account for scr refresh
            text_Gender.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_Gender, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_Gender.started')
            # update status
            text_Gender.status = STARTED
            text_Gender.setAutoDraw(True)
        
        # if text_Gender is active this frame...
        if text_Gender.status == STARTED:
            # update params
            pass
        
        # *key_respGender* updates
        waitOnFlip = False
        
        # if key_respGender is starting this frame...
        if key_respGender.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_respGender.frameNStart = frameN  # exact frame index
            key_respGender.tStart = t  # local t and not account for scr refresh
            key_respGender.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_respGender, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_respGender.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_respGender.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_respGender.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_respGender.status == STARTED and not waitOnFlip:
            theseKeys = key_respGender.getKeys(keyList=['f','m'], ignoreKeys=["escape"], waitRelease=False)
            _key_respGender_allKeys.extend(theseKeys)
            if len(_key_respGender_allKeys):
                key_respGender.keys = [key.name for key in _key_respGender_allKeys]  # storing all keys
                key_respGender.rt = [key.rt for key in _key_respGender_allKeys]
                key_respGender.duration = [key.duration for key in _key_respGender_allKeys]
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=Gender,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Gender.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Gender.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Gender" ---
    for thisComponent in Gender.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Gender
    Gender.tStop = globalClock.getTime(format='float')
    Gender.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Gender.stopped', Gender.tStop)
    # check responses
    if key_respGender.keys in ['', [], None]:  # No response was made
        key_respGender.keys = None
    thisExp.addData('key_respGender.keys',key_respGender.keys)
    if key_respGender.keys != None:  # we had a response
        thisExp.addData('key_respGender.rt', key_respGender.rt)
        thisExp.addData('key_respGender.duration', key_respGender.duration)
    thisExp.nextEntry()
    # the Routine "Gender" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_sounds = data.TrialHandler2(
        name='trials_sounds',
        nReps=1, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('inidpendent v.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(trials_sounds)  # add the loop to the experiment
    thisTrials_sound = trials_sounds.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_sound.rgb)
    if thisTrials_sound != None:
        for paramName in thisTrials_sound:
            globals()[paramName] = thisTrials_sound[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrials_sound in trials_sounds:
        trials_sounds.status = STARTED
        if hasattr(thisTrials_sound, 'status'):
            thisTrials_sound.status = STARTED
        currentLoop = trials_sounds
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_sound.rgb)
        if thisTrials_sound != None:
            for paramName in thisTrials_sound:
                globals()[paramName] = thisTrials_sound[paramName]
        
        # --- Prepare to start Routine "Trial" ---
        # create an object to store info about Routine Trial
        Trial = data.Routine(
            name='Trial',
            components=[soundfiles, slider_sounds, textsounds],
        )
        Trial.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        soundfiles.setSound(musik, hamming=True)
        soundfiles.setVolume(1, log=False)
        soundfiles.seek(0)
        slider_sounds.reset()
        # store start times for Trial
        Trial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Trial.tStart = globalClock.getTime(format='float')
        Trial.status = STARTED
        thisExp.addData('Trial.started', Trial.tStart)
        Trial.maxDuration = None
        # keep track of which components have finished
        TrialComponents = Trial.components
        for thisComponent in Trial.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Trial" ---
        Trial.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrials_sound, 'status') and thisTrials_sound.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *soundfiles* updates
            
            # if soundfiles is starting this frame...
            if soundfiles.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                soundfiles.frameNStart = frameN  # exact frame index
                soundfiles.tStart = t  # local t and not account for scr refresh
                soundfiles.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                soundfiles.status = STARTED
                soundfiles.play(when=win)  # sync with win flip
            
            # if soundfiles is stopping this frame...
            if soundfiles.status == STARTED:
                if bool(False) or soundfiles.isFinished:
                    # keep track of stop time/frame for later
                    soundfiles.tStop = t  # not accounting for scr refresh
                    soundfiles.tStopRefresh = tThisFlipGlobal  # on global time
                    soundfiles.frameNStop = frameN  # exact frame index
                    # update status
                    soundfiles.status = FINISHED
                    soundfiles.stop()
            
            # *slider_sounds* updates
            
            # if slider_sounds is starting this frame...
            if slider_sounds.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                slider_sounds.frameNStart = frameN  # exact frame index
                slider_sounds.tStart = t  # local t and not account for scr refresh
                slider_sounds.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slider_sounds, 'tStartRefresh')  # time at next scr refresh
                # update status
                slider_sounds.status = STARTED
                slider_sounds.setAutoDraw(True)
            
            # if slider_sounds is active this frame...
            if slider_sounds.status == STARTED:
                # update params
                pass
            
            # Check slider_sounds for response to end Routine
            if slider_sounds.getRating() is not None and slider_sounds.status == STARTED:
                continueRoutine = False
            
            # *textsounds* updates
            
            # if textsounds is starting this frame...
            if textsounds.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textsounds.frameNStart = frameN  # exact frame index
                textsounds.tStart = t  # local t and not account for scr refresh
                textsounds.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textsounds, 'tStartRefresh')  # time at next scr refresh
                # update status
                textsounds.status = STARTED
                textsounds.setAutoDraw(True)
            
            # if textsounds is active this frame...
            if textsounds.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=Trial,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Trial.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Trial.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Trial" ---
        for thisComponent in Trial.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Trial
        Trial.tStop = globalClock.getTime(format='float')
        Trial.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Trial.stopped', Trial.tStop)
        soundfiles.pause()  # ensure sound has stopped at end of Routine
        trials_sounds.addData('slider_sounds.response', slider_sounds.getRating())
        # the Routine "Trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisTrials_sound as finished
        if hasattr(thisTrials_sound, 'status'):
            thisTrials_sound.status = FINISHED
        # if awaiting a pause, pause now
        if trials_sounds.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            trials_sounds.status = STARTED
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials_sounds'
    trials_sounds.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    # get names of stimulus parameters
    if trials_sounds.trialList in ([], [None], None):
        params = []
    else:
        params = trials_sounds.trialList[0].keys()
    # save data for this loop
    trials_sounds.saveAsExcel(filename + '.xlsx', sheetName='trials_sounds',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    trials_sounds.saveAsText(filename + '_trials_sounds.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # --- Prepare to start Routine "musicalpreference_pop" ---
    # create an object to store info about Routine musicalpreference_pop
    musicalpreference_pop = data.Routine(
        name='musicalpreference_pop',
        components=[text_PreferencePop, sliderPopPreference],
    )
    musicalpreference_pop.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    sliderPopPreference.reset()
    # store start times for musicalpreference_pop
    musicalpreference_pop.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    musicalpreference_pop.tStart = globalClock.getTime(format='float')
    musicalpreference_pop.status = STARTED
    thisExp.addData('musicalpreference_pop.started', musicalpreference_pop.tStart)
    musicalpreference_pop.maxDuration = None
    # keep track of which components have finished
    musicalpreference_popComponents = musicalpreference_pop.components
    for thisComponent in musicalpreference_pop.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "musicalpreference_pop" ---
    musicalpreference_pop.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_PreferencePop* updates
        
        # if text_PreferencePop is starting this frame...
        if text_PreferencePop.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_PreferencePop.frameNStart = frameN  # exact frame index
            text_PreferencePop.tStart = t  # local t and not account for scr refresh
            text_PreferencePop.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_PreferencePop, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_PreferencePop.status = STARTED
            text_PreferencePop.setAutoDraw(True)
        
        # if text_PreferencePop is active this frame...
        if text_PreferencePop.status == STARTED:
            # update params
            pass
        
        # *sliderPopPreference* updates
        
        # if sliderPopPreference is starting this frame...
        if sliderPopPreference.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sliderPopPreference.frameNStart = frameN  # exact frame index
            sliderPopPreference.tStart = t  # local t and not account for scr refresh
            sliderPopPreference.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sliderPopPreference, 'tStartRefresh')  # time at next scr refresh
            # update status
            sliderPopPreference.status = STARTED
            sliderPopPreference.setAutoDraw(True)
        
        # if sliderPopPreference is active this frame...
        if sliderPopPreference.status == STARTED:
            # update params
            pass
        
        # Check sliderPopPreference for response to end Routine
        if sliderPopPreference.getRating() is not None and sliderPopPreference.status == STARTED:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=musicalpreference_pop,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            musicalpreference_pop.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in musicalpreference_pop.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "musicalpreference_pop" ---
    for thisComponent in musicalpreference_pop.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for musicalpreference_pop
    musicalpreference_pop.tStop = globalClock.getTime(format='float')
    musicalpreference_pop.tStopRefresh = tThisFlipGlobal
    thisExp.addData('musicalpreference_pop.stopped', musicalpreference_pop.tStop)
    thisExp.addData('sliderPopPreference.response', sliderPopPreference.getRating())
    thisExp.nextEntry()
    # the Routine "musicalpreference_pop" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "musicalpreference_classic" ---
    # create an object to store info about Routine musicalpreference_classic
    musicalpreference_classic = data.Routine(
        name='musicalpreference_classic',
        components=[text_PreferenceClassic, sliderClassicPreference],
    )
    musicalpreference_classic.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    sliderClassicPreference.reset()
    # store start times for musicalpreference_classic
    musicalpreference_classic.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    musicalpreference_classic.tStart = globalClock.getTime(format='float')
    musicalpreference_classic.status = STARTED
    thisExp.addData('musicalpreference_classic.started', musicalpreference_classic.tStart)
    musicalpreference_classic.maxDuration = None
    # keep track of which components have finished
    musicalpreference_classicComponents = musicalpreference_classic.components
    for thisComponent in musicalpreference_classic.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "musicalpreference_classic" ---
    musicalpreference_classic.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_PreferenceClassic* updates
        
        # if text_PreferenceClassic is starting this frame...
        if text_PreferenceClassic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_PreferenceClassic.frameNStart = frameN  # exact frame index
            text_PreferenceClassic.tStart = t  # local t and not account for scr refresh
            text_PreferenceClassic.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_PreferenceClassic, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_PreferenceClassic.status = STARTED
            text_PreferenceClassic.setAutoDraw(True)
        
        # if text_PreferenceClassic is active this frame...
        if text_PreferenceClassic.status == STARTED:
            # update params
            pass
        
        # *sliderClassicPreference* updates
        
        # if sliderClassicPreference is starting this frame...
        if sliderClassicPreference.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sliderClassicPreference.frameNStart = frameN  # exact frame index
            sliderClassicPreference.tStart = t  # local t and not account for scr refresh
            sliderClassicPreference.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sliderClassicPreference, 'tStartRefresh')  # time at next scr refresh
            # update status
            sliderClassicPreference.status = STARTED
            sliderClassicPreference.setAutoDraw(True)
        
        # if sliderClassicPreference is active this frame...
        if sliderClassicPreference.status == STARTED:
            # update params
            pass
        
        # Check sliderClassicPreference for response to end Routine
        if sliderClassicPreference.getRating() is not None and sliderClassicPreference.status == STARTED:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=musicalpreference_classic,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            musicalpreference_classic.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in musicalpreference_classic.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "musicalpreference_classic" ---
    for thisComponent in musicalpreference_classic.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for musicalpreference_classic
    musicalpreference_classic.tStop = globalClock.getTime(format='float')
    musicalpreference_classic.tStopRefresh = tThisFlipGlobal
    thisExp.addData('musicalpreference_classic.stopped', musicalpreference_classic.tStop)
    thisExp.addData('sliderClassicPreference.response', sliderClassicPreference.getRating())
    thisExp.addData('sliderClassicPreference.history', sliderClassicPreference.getHistory())
    thisExp.nextEntry()
    # the Routine "musicalpreference_classic" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "musicalpreference_heavymetal_" ---
    # create an object to store info about Routine musicalpreference_heavymetal_
    musicalpreference_heavymetal_ = data.Routine(
        name='musicalpreference_heavymetal_',
        components=[text_PreferenceHeavymetal, slider_HeavymetalPreference],
    )
    musicalpreference_heavymetal_.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    slider_HeavymetalPreference.reset()
    # store start times for musicalpreference_heavymetal_
    musicalpreference_heavymetal_.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    musicalpreference_heavymetal_.tStart = globalClock.getTime(format='float')
    musicalpreference_heavymetal_.status = STARTED
    thisExp.addData('musicalpreference_heavymetal_.started', musicalpreference_heavymetal_.tStart)
    musicalpreference_heavymetal_.maxDuration = None
    # keep track of which components have finished
    musicalpreference_heavymetal_Components = musicalpreference_heavymetal_.components
    for thisComponent in musicalpreference_heavymetal_.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "musicalpreference_heavymetal_" ---
    musicalpreference_heavymetal_.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_PreferenceHeavymetal* updates
        
        # if text_PreferenceHeavymetal is starting this frame...
        if text_PreferenceHeavymetal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_PreferenceHeavymetal.frameNStart = frameN  # exact frame index
            text_PreferenceHeavymetal.tStart = t  # local t and not account for scr refresh
            text_PreferenceHeavymetal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_PreferenceHeavymetal, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_PreferenceHeavymetal.status = STARTED
            text_PreferenceHeavymetal.setAutoDraw(True)
        
        # if text_PreferenceHeavymetal is active this frame...
        if text_PreferenceHeavymetal.status == STARTED:
            # update params
            pass
        
        # *slider_HeavymetalPreference* updates
        
        # if slider_HeavymetalPreference is starting this frame...
        if slider_HeavymetalPreference.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_HeavymetalPreference.frameNStart = frameN  # exact frame index
            slider_HeavymetalPreference.tStart = t  # local t and not account for scr refresh
            slider_HeavymetalPreference.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_HeavymetalPreference, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'slider_HeavymetalPreference.started')
            # update status
            slider_HeavymetalPreference.status = STARTED
            slider_HeavymetalPreference.setAutoDraw(True)
        
        # if slider_HeavymetalPreference is active this frame...
        if slider_HeavymetalPreference.status == STARTED:
            # update params
            pass
        
        # Check slider_HeavymetalPreference for response to end Routine
        if slider_HeavymetalPreference.getRating() is not None and slider_HeavymetalPreference.status == STARTED:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=musicalpreference_heavymetal_,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            musicalpreference_heavymetal_.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in musicalpreference_heavymetal_.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "musicalpreference_heavymetal_" ---
    for thisComponent in musicalpreference_heavymetal_.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for musicalpreference_heavymetal_
    musicalpreference_heavymetal_.tStop = globalClock.getTime(format='float')
    musicalpreference_heavymetal_.tStopRefresh = tThisFlipGlobal
    thisExp.addData('musicalpreference_heavymetal_.stopped', musicalpreference_heavymetal_.tStop)
    thisExp.addData('slider_HeavymetalPreference.response', slider_HeavymetalPreference.getRating())
    thisExp.nextEntry()
    # the Routine "musicalpreference_heavymetal_" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "EndScreen" ---
    # create an object to store info about Routine EndScreen
    EndScreen = data.Routine(
        name='EndScreen',
        components=[textEnd, key_resp_endscreen],
    )
    EndScreen.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_endscreen
    key_resp_endscreen.keys = []
    key_resp_endscreen.rt = []
    _key_resp_endscreen_allKeys = []
    # store start times for EndScreen
    EndScreen.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    EndScreen.tStart = globalClock.getTime(format='float')
    EndScreen.status = STARTED
    thisExp.addData('EndScreen.started', EndScreen.tStart)
    EndScreen.maxDuration = None
    # keep track of which components have finished
    EndScreenComponents = EndScreen.components
    for thisComponent in EndScreen.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "EndScreen" ---
    EndScreen.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textEnd* updates
        
        # if textEnd is starting this frame...
        if textEnd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textEnd.frameNStart = frameN  # exact frame index
            textEnd.tStart = t  # local t and not account for scr refresh
            textEnd.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textEnd, 'tStartRefresh')  # time at next scr refresh
            # update status
            textEnd.status = STARTED
            textEnd.setAutoDraw(True)
        
        # if textEnd is active this frame...
        if textEnd.status == STARTED:
            # update params
            pass
        
        # *key_resp_endscreen* updates
        waitOnFlip = False
        
        # if key_resp_endscreen is starting this frame...
        if key_resp_endscreen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_endscreen.frameNStart = frameN  # exact frame index
            key_resp_endscreen.tStart = t  # local t and not account for scr refresh
            key_resp_endscreen.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_endscreen, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_resp_endscreen.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_endscreen.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_endscreen.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_endscreen.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_endscreen.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_endscreen_allKeys.extend(theseKeys)
            if len(_key_resp_endscreen_allKeys):
                key_resp_endscreen.keys = _key_resp_endscreen_allKeys[-1].name  # just the last key pressed
                key_resp_endscreen.rt = _key_resp_endscreen_allKeys[-1].rt
                key_resp_endscreen.duration = _key_resp_endscreen_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=EndScreen,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            EndScreen.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EndScreen.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "EndScreen" ---
    for thisComponent in EndScreen.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for EndScreen
    EndScreen.tStop = globalClock.getTime(format='float')
    EndScreen.tStopRefresh = tThisFlipGlobal
    thisExp.addData('EndScreen.stopped', EndScreen.tStop)
    thisExp.nextEntry()
    # the Routine "EndScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # run any 'at exit' functions
    for fcn in runAtExit:
        fcn()
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
