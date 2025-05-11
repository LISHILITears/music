/********** 
 * 8 *
 **********/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2025.1.0.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = '8';  // from the Builder filename that created this script
let expInfo = {
    'participant': '',
    'session': '001',
};
let PILOTING = util.getUrlParameters().has('__pilotToken');

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); },flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(Welcome_ScreenRoutineBegin());
flowScheduler.add(Welcome_ScreenRoutineEachFrame());
flowScheduler.add(Welcome_ScreenRoutineEnd());
flowScheduler.add(Second_Welcome_ScreenRoutineBegin());
flowScheduler.add(Second_Welcome_ScreenRoutineEachFrame());
flowScheduler.add(Second_Welcome_ScreenRoutineEnd());
flowScheduler.add(AgeRoutineBegin());
flowScheduler.add(AgeRoutineEachFrame());
flowScheduler.add(AgeRoutineEnd());
flowScheduler.add(GenderRoutineBegin());
flowScheduler.add(GenderRoutineEachFrame());
flowScheduler.add(GenderRoutineEnd());
const trials_soundsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_soundsLoopBegin(trials_soundsLoopScheduler));
flowScheduler.add(trials_soundsLoopScheduler);
flowScheduler.add(trials_soundsLoopEnd);


flowScheduler.add(musicalpreference_popRoutineBegin());
flowScheduler.add(musicalpreference_popRoutineEachFrame());
flowScheduler.add(musicalpreference_popRoutineEnd());
flowScheduler.add(musicalpreference_classicRoutineBegin());
flowScheduler.add(musicalpreference_classicRoutineEachFrame());
flowScheduler.add(musicalpreference_classicRoutineEnd());
flowScheduler.add(musicalpreference_heavymetalRoutineBegin());
flowScheduler.add(musicalpreference_heavymetalRoutineEachFrame());
flowScheduler.add(musicalpreference_heavymetalRoutineEnd());
flowScheduler.add(EndScreenRoutineBegin());
flowScheduler.add(EndScreenRoutineEachFrame());
flowScheduler.add(EndScreenRoutineEnd());
flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  });
  
psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2025.1.0';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var Welcome_ScreenClock;
var keyWelcome;
var text_Welcome;
var Second_Welcome_ScreenClock;
var Second_Welcome_Text;
var key_resp_welcome2;
var AgeClock;
var text_Age;
var sliderAge;
var GenderClock;
var text_Gender;
var key_respGender;
var TrialClock;
var soundfiles;
var slider_sounds;
var textsounds;
var musicalpreference_popClock;
var text_PreferencePop;
var sliderPopPreference;
var musicalpreference_classicClock;
var text_PreferenceClassic;
var sliderClassicPreference;
var musicalpreference_heavymetal_Clock;
var text_PreferenceHeavymetal;
var slider_HeavymetalPreference;
var EndScreenClock;
var textEnd;
var key_resp_endscreen;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "Welcome_Screen"
  Welcome_ScreenClock = new util.Clock();
  keyWelcome = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_Welcome = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_Welcome',
    text: 'Welcome to my musical experiment!\n\nPress (SPACE) to start.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.05)], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "Second_Welcome_Screen"
  Second_Welcome_ScreenClock = new util.Clock();
  Second_Welcome_Text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Second_Welcome_Text',
    text: 'Now you will hear some sound examples.\n\nPlease listen to the whole sound examples before deciding on your answer!\n\nPress (SPACE) to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_welcome2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Age"
  AgeClock = new util.Clock();
  text_Age = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_Age',
    text: 'How old are you? ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  sliderAge = new visual.Slider({
    win: psychoJS.window, name: 'sliderAge',
    startValue: undefined,
    size: [1.0, 0.1], pos: [0, (- 0.2)], ori: 0, units: psychoJS.window.units,
    labels: ["15-25", "25-35", "35-45", "45-"], fontSize: 0.05, ticks: [1, 2, 3, 4],
    granularity: 0, style: ["RATING"],
    color: new util.Color('LightGray'), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    opacity: 1, fontFamily: 'HelveticaBold', bold: true, italic: false, depth: -1, 
    flip: false,
  });
  
  // Initialize components for Routine "Gender"
  GenderClock = new util.Clock();
  text_Gender = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_Gender',
    text: "Please select your gender. Press 'f' for female and 'm' for male. ",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_respGender = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Trial"
  TrialClock = new util.Clock();
  soundfiles = new sound.Sound({
      win: psychoJS.window,
      value: 'A',
      secs: (- 1),
      });
  soundfiles.setVolume(1);
  soundfiles.isPlaying = false;
  soundfiles.isFinished = false;
  slider_sounds = new visual.Slider({
    win: psychoJS.window, name: 'slider_sounds',
    startValue: undefined,
    size: [0.5, 0.1], pos: [0, (- 0.2)], ori: 0, units: psychoJS.window.units,
    labels: ["1", "2", "3", "4", "5"], fontSize: 0.05, ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: ["RATING"],
    color: new util.Color('LightGray'), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    opacity: 1, fontFamily: 'HelveticaBold', bold: true, italic: false, depth: -1, 
    flip: false,
  });
  
  textsounds = new visual.TextStim({
    win: psychoJS.window,
    name: 'textsounds',
    text: 'How aggressive do you percieve this piece of music? (1=not aggressive,5=very aggressive)',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.17], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "musicalpreference_pop"
  musicalpreference_popClock = new util.Clock();
  text_PreferencePop = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_PreferencePop',
    text: 'On a scale from 1-5, how much do you like the genre Popular Music? (1=strongly disslike, 5=strongly like)',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.17], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  sliderPopPreference = new visual.Slider({
    win: psychoJS.window, name: 'sliderPopPreference',
    startValue: undefined,
    size: [1.0, 0.1], pos: [0, (- 0.2)], ori: 0, units: psychoJS.window.units,
    labels: ["1", "2", "3", "4", "5"], fontSize: 0.05, ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: ["RATING"],
    color: new util.Color('LightGray'), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    opacity: 1, fontFamily: 'HelveticaBold', bold: true, italic: false, depth: -1, 
    flip: false,
  });
  
  // Initialize components for Routine "musicalpreference_classic"
  musicalpreference_classicClock = new util.Clock();
  text_PreferenceClassic = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_PreferenceClassic',
    text: 'On a scale from 1-5, how much do you like the genre Classical Music? (1=strongly disslike, 5=strongly like)',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.17], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  sliderClassicPreference = new visual.Slider({
    win: psychoJS.window, name: 'sliderClassicPreference',
    startValue: undefined,
    size: [1.0, 0.1], pos: [0, (- 0.2)], ori: 0, units: psychoJS.window.units,
    labels: ["1", "2", "3", "4", "5"], fontSize: 0.05, ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: ["RATING"],
    color: new util.Color('LightGray'), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    opacity: 1, fontFamily: 'HelveticaBold', bold: true, italic: false, depth: -1, 
    flip: false,
  });
  
  // Initialize components for Routine "musicalpreference_heavymetal_"
  musicalpreference_heavymetal_Clock = new util.Clock();
  text_PreferenceHeavymetal = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_PreferenceHeavymetal',
    text: 'On a scale from 1-5, how much do you like the genre Heavy-Metal? (1=strongly disslike, 5=strongly like)',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.17], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  slider_HeavymetalPreference = new visual.Slider({
    win: psychoJS.window, name: 'slider_HeavymetalPreference',
    startValue: undefined,
    size: [1.0, 0.1], pos: [0, (- 0.2)], ori: 0, units: psychoJS.window.units,
    labels: ["1", "2", "3", "4", "5"], fontSize: 0.05, ticks: [1, 2, 3, 4, 5],
    granularity: 1, style: ["RATING"],
    color: new util.Color('LightGray'), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    opacity: 1, fontFamily: 'HelveticaBold', bold: true, italic: false, depth: -1, 
    flip: false,
  });
  
  // Initialize components for Routine "EndScreen"
  EndScreenClock = new util.Clock();
  textEnd = new visual.TextStim({
    win: psychoJS.window,
    name: 'textEnd',
    text: 'Thanks for participating! \nPress space to leave the experiment!',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_endscreen = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var routineForceEnded;
var Welcome_ScreenMaxDurationReached;
var _keyWelcome_allKeys;
var Welcome_ScreenMaxDuration;
var Welcome_ScreenComponents;
function Welcome_ScreenRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Welcome_Screen' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    Welcome_ScreenClock.reset();
    routineTimer.reset();
    Welcome_ScreenMaxDurationReached = false;
    // update component parameters for each repeat
    keyWelcome.keys = undefined;
    keyWelcome.rt = undefined;
    _keyWelcome_allKeys = [];
    psychoJS.experiment.addData('Welcome_Screen.started', globalClock.getTime());
    Welcome_ScreenMaxDuration = null
    // keep track of which components have finished
    Welcome_ScreenComponents = [];
    Welcome_ScreenComponents.push(keyWelcome);
    Welcome_ScreenComponents.push(text_Welcome);
    
    for (const thisComponent of Welcome_ScreenComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Welcome_ScreenRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Welcome_Screen' ---
    // get current time
    t = Welcome_ScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *keyWelcome* updates
    if (t >= 0.0 && keyWelcome.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      keyWelcome.tStart = t;  // (not accounting for frame time here)
      keyWelcome.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { keyWelcome.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { keyWelcome.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { keyWelcome.clearEvents(); });
    }
    
    // if keyWelcome is active this frame...
    if (keyWelcome.status === PsychoJS.Status.STARTED) {
      let theseKeys = keyWelcome.getKeys({keyList: 'space', waitRelease: false});
      _keyWelcome_allKeys = _keyWelcome_allKeys.concat(theseKeys);
      if (_keyWelcome_allKeys.length > 0) {
        keyWelcome.keys = _keyWelcome_allKeys[_keyWelcome_allKeys.length - 1].name;  // just the last key pressed
        keyWelcome.rt = _keyWelcome_allKeys[_keyWelcome_allKeys.length - 1].rt;
        keyWelcome.duration = _keyWelcome_allKeys[_keyWelcome_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_Welcome* updates
    if (t >= 0.0 && text_Welcome.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_Welcome.tStart = t;  // (not accounting for frame time here)
      text_Welcome.frameNStart = frameN;  // exact frame index
      
      text_Welcome.setAutoDraw(true);
    }
    
    
    // if text_Welcome is active this frame...
    if (text_Welcome.status === PsychoJS.Status.STARTED) {
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Welcome_ScreenComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Welcome_ScreenRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Welcome_Screen' ---
    for (const thisComponent of Welcome_ScreenComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Welcome_Screen.stopped', globalClock.getTime());
    keyWelcome.stop();
    // the Routine "Welcome_Screen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Second_Welcome_ScreenMaxDurationReached;
var _key_resp_welcome2_allKeys;
var Second_Welcome_ScreenMaxDuration;
var Second_Welcome_ScreenComponents;
function Second_Welcome_ScreenRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Second_Welcome_Screen' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    Second_Welcome_ScreenClock.reset();
    routineTimer.reset();
    Second_Welcome_ScreenMaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_welcome2.keys = undefined;
    key_resp_welcome2.rt = undefined;
    _key_resp_welcome2_allKeys = [];
    psychoJS.experiment.addData('Second_Welcome_Screen.started', globalClock.getTime());
    Second_Welcome_ScreenMaxDuration = null
    // keep track of which components have finished
    Second_Welcome_ScreenComponents = [];
    Second_Welcome_ScreenComponents.push(Second_Welcome_Text);
    Second_Welcome_ScreenComponents.push(key_resp_welcome2);
    
    for (const thisComponent of Second_Welcome_ScreenComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Second_Welcome_ScreenRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Second_Welcome_Screen' ---
    // get current time
    t = Second_Welcome_ScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Second_Welcome_Text* updates
    if (t >= 0.0 && Second_Welcome_Text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Second_Welcome_Text.tStart = t;  // (not accounting for frame time here)
      Second_Welcome_Text.frameNStart = frameN;  // exact frame index
      
      Second_Welcome_Text.setAutoDraw(true);
    }
    
    
    // if Second_Welcome_Text is active this frame...
    if (Second_Welcome_Text.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *key_resp_welcome2* updates
    if (t >= 0.0 && key_resp_welcome2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_welcome2.tStart = t;  // (not accounting for frame time here)
      key_resp_welcome2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_welcome2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_welcome2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_welcome2.clearEvents(); });
    }
    
    // if key_resp_welcome2 is active this frame...
    if (key_resp_welcome2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_welcome2.getKeys({keyList: 'space', waitRelease: false});
      _key_resp_welcome2_allKeys = _key_resp_welcome2_allKeys.concat(theseKeys);
      if (_key_resp_welcome2_allKeys.length > 0) {
        key_resp_welcome2.keys = _key_resp_welcome2_allKeys[_key_resp_welcome2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_welcome2.rt = _key_resp_welcome2_allKeys[_key_resp_welcome2_allKeys.length - 1].rt;
        key_resp_welcome2.duration = _key_resp_welcome2_allKeys[_key_resp_welcome2_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Second_Welcome_ScreenComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Second_Welcome_ScreenRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Second_Welcome_Screen' ---
    for (const thisComponent of Second_Welcome_ScreenComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Second_Welcome_Screen.stopped', globalClock.getTime());
    key_resp_welcome2.stop();
    // the Routine "Second_Welcome_Screen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var AgeMaxDurationReached;
var AgeMaxDuration;
var AgeComponents;
function AgeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Age' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    AgeClock.reset();
    routineTimer.reset();
    AgeMaxDurationReached = false;
    // update component parameters for each repeat
    sliderAge.reset()
    psychoJS.experiment.addData('Age.started', globalClock.getTime());
    AgeMaxDuration = null
    // keep track of which components have finished
    AgeComponents = [];
    AgeComponents.push(text_Age);
    AgeComponents.push(sliderAge);
    
    for (const thisComponent of AgeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function AgeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Age' ---
    // get current time
    t = AgeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_Age* updates
    if (t >= 0.0 && text_Age.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_Age.tStart = t;  // (not accounting for frame time here)
      text_Age.frameNStart = frameN;  // exact frame index
      
      text_Age.setAutoDraw(true);
    }
    
    
    // if text_Age is active this frame...
    if (text_Age.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *sliderAge* updates
    if (t >= 0.0 && sliderAge.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sliderAge.tStart = t;  // (not accounting for frame time here)
      sliderAge.frameNStart = frameN;  // exact frame index
      
      sliderAge.setAutoDraw(true);
    }
    
    
    // if sliderAge is active this frame...
    if (sliderAge.status === PsychoJS.Status.STARTED) {
    }
    
    
    // Check sliderAge for response to end Routine
    if (sliderAge.getRating() !== undefined && sliderAge.status === PsychoJS.Status.STARTED) {
      continueRoutine = false; }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of AgeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function AgeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Age' ---
    for (const thisComponent of AgeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Age.stopped', globalClock.getTime());
    psychoJS.experiment.addData('sliderAge.response', sliderAge.getRating());
    // the Routine "Age" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var GenderMaxDurationReached;
var _key_respGender_allKeys;
var GenderMaxDuration;
var GenderComponents;
function GenderRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Gender' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    GenderClock.reset();
    routineTimer.reset();
    GenderMaxDurationReached = false;
    // update component parameters for each repeat
    key_respGender.keys = undefined;
    key_respGender.rt = undefined;
    _key_respGender_allKeys = [];
    psychoJS.experiment.addData('Gender.started', globalClock.getTime());
    GenderMaxDuration = null
    // keep track of which components have finished
    GenderComponents = [];
    GenderComponents.push(text_Gender);
    GenderComponents.push(key_respGender);
    
    for (const thisComponent of GenderComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function GenderRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Gender' ---
    // get current time
    t = GenderClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_Gender* updates
    if (t >= 0.0 && text_Gender.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_Gender.tStart = t;  // (not accounting for frame time here)
      text_Gender.frameNStart = frameN;  // exact frame index
      
      text_Gender.setAutoDraw(true);
    }
    
    
    // if text_Gender is active this frame...
    if (text_Gender.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *key_respGender* updates
    if (t >= 0.0 && key_respGender.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_respGender.tStart = t;  // (not accounting for frame time here)
      key_respGender.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_respGender.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_respGender.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_respGender.clearEvents(); });
    }
    
    // if key_respGender is active this frame...
    if (key_respGender.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_respGender.getKeys({keyList: ['f','m'], waitRelease: false});
      _key_respGender_allKeys = _key_respGender_allKeys.concat(theseKeys);
      if (_key_respGender_allKeys.length > 0) {
        key_respGender.keys = _key_respGender_allKeys.map((key) => key.name);  // storing all keys
        key_respGender.rt = _key_respGender_allKeys.map((key) => key.rt);
        key_respGender.duration = _key_respGender_allKeys.map((key) => key.duration);
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of GenderComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function GenderRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Gender' ---
    for (const thisComponent of GenderComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Gender.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_respGender.corr, level);
    }
    psychoJS.experiment.addData('key_respGender.keys', key_respGender.keys);
    if (typeof key_respGender.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_respGender.rt', key_respGender.rt);
        psychoJS.experiment.addData('key_respGender.duration', key_respGender.duration);
        routineTimer.reset();
        }
    
    key_respGender.stop();
    // the Routine "Gender" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var trials_sounds;
function trials_soundsLoopBegin(trials_soundsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_sounds = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'inidpendent v.xlsx',
      seed: undefined, name: 'trials_sounds'
    });
    psychoJS.experiment.addLoop(trials_sounds); // add the loop to the experiment
    currentLoop = trials_sounds;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrials_sound of trials_sounds) {
      snapshot = trials_sounds.getSnapshot();
      trials_soundsLoopScheduler.add(importConditions(snapshot));
      trials_soundsLoopScheduler.add(TrialRoutineBegin(snapshot));
      trials_soundsLoopScheduler.add(TrialRoutineEachFrame());
      trials_soundsLoopScheduler.add(TrialRoutineEnd(snapshot));
      trials_soundsLoopScheduler.add(trials_soundsLoopEndIteration(trials_soundsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_soundsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_sounds);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_soundsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var TrialMaxDurationReached;
var TrialMaxDuration;
var TrialComponents;
function TrialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Trial' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    TrialClock.reset();
    routineTimer.reset();
    TrialMaxDurationReached = false;
    // update component parameters for each repeat
    soundfiles.isFinished = false;
    soundfiles.setValue(musik);
    soundfiles.setVolume(1);
    slider_sounds.reset()
    psychoJS.experiment.addData('Trial.started', globalClock.getTime());
    TrialMaxDuration = null
    // keep track of which components have finished
    TrialComponents = [];
    TrialComponents.push(soundfiles);
    TrialComponents.push(slider_sounds);
    TrialComponents.push(textsounds);
    
    for (const thisComponent of TrialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function TrialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Trial' ---
    // get current time
    t = TrialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    if (soundfiles.status === STARTED) {
        soundfiles.isPlaying = true;
        if (t >= (soundfiles.getDuration() + soundfiles.tStart)) {
            soundfiles.isFinished = true;
        }
    }
    // start/stop soundfiles
    if (t >= 0.0 && soundfiles.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      soundfiles.tStart = t;  // (not accounting for frame time here)
      soundfiles.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ soundfiles.play(); });  // screen flip
      soundfiles.status = PsychoJS.Status.STARTED;
    }
    if (soundfiles.status === PsychoJS.Status.STARTED && Boolean(false) || soundfiles.isFinished) {
      // keep track of stop time/frame for later
      soundfiles.tStop = t;  // not accounting for scr refresh
      soundfiles.frameNStop = frameN;  // exact frame index
      // update status
      soundfiles.status = PsychoJS.Status.FINISHED;
      // stop playback
      soundfiles.stop();
    }
    
    // *slider_sounds* updates
    if (t >= 0.0 && slider_sounds.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider_sounds.tStart = t;  // (not accounting for frame time here)
      slider_sounds.frameNStart = frameN;  // exact frame index
      
      slider_sounds.setAutoDraw(true);
    }
    
    
    // if slider_sounds is active this frame...
    if (slider_sounds.status === PsychoJS.Status.STARTED) {
    }
    
    
    // Check slider_sounds for response to end Routine
    if (slider_sounds.getRating() !== undefined && slider_sounds.status === PsychoJS.Status.STARTED) {
      continueRoutine = false; }
    
    // *textsounds* updates
    if (t >= 0.0 && textsounds.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textsounds.tStart = t;  // (not accounting for frame time here)
      textsounds.frameNStart = frameN;  // exact frame index
      
      textsounds.setAutoDraw(true);
    }
    
    
    // if textsounds is active this frame...
    if (textsounds.status === PsychoJS.Status.STARTED) {
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of TrialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function TrialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Trial' ---
    for (const thisComponent of TrialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Trial.stopped', globalClock.getTime());
    soundfiles.stop();  // ensure sound has stopped at end of Routine
    psychoJS.experiment.addData('slider_sounds.response', slider_sounds.getRating());
    // the Routine "Trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var musicalpreference_popMaxDurationReached;
var musicalpreference_popMaxDuration;
var musicalpreference_popComponents;
function musicalpreference_popRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'musicalpreference_pop' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    musicalpreference_popClock.reset();
    routineTimer.reset();
    musicalpreference_popMaxDurationReached = false;
    // update component parameters for each repeat
    sliderPopPreference.reset()
    psychoJS.experiment.addData('musicalpreference_pop.started', globalClock.getTime());
    musicalpreference_popMaxDuration = null
    // keep track of which components have finished
    musicalpreference_popComponents = [];
    musicalpreference_popComponents.push(text_PreferencePop);
    musicalpreference_popComponents.push(sliderPopPreference);
    
    for (const thisComponent of musicalpreference_popComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function musicalpreference_popRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'musicalpreference_pop' ---
    // get current time
    t = musicalpreference_popClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_PreferencePop* updates
    if (t >= 0.0 && text_PreferencePop.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_PreferencePop.tStart = t;  // (not accounting for frame time here)
      text_PreferencePop.frameNStart = frameN;  // exact frame index
      
      text_PreferencePop.setAutoDraw(true);
    }
    
    
    // if text_PreferencePop is active this frame...
    if (text_PreferencePop.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *sliderPopPreference* updates
    if (t >= 0.0 && sliderPopPreference.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sliderPopPreference.tStart = t;  // (not accounting for frame time here)
      sliderPopPreference.frameNStart = frameN;  // exact frame index
      
      sliderPopPreference.setAutoDraw(true);
    }
    
    
    // if sliderPopPreference is active this frame...
    if (sliderPopPreference.status === PsychoJS.Status.STARTED) {
    }
    
    
    // Check sliderPopPreference for response to end Routine
    if (sliderPopPreference.getRating() !== undefined && sliderPopPreference.status === PsychoJS.Status.STARTED) {
      continueRoutine = false; }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of musicalpreference_popComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function musicalpreference_popRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'musicalpreference_pop' ---
    for (const thisComponent of musicalpreference_popComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('musicalpreference_pop.stopped', globalClock.getTime());
    psychoJS.experiment.addData('sliderPopPreference.response', sliderPopPreference.getRating());
    // the Routine "musicalpreference_pop" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var musicalpreference_classicMaxDurationReached;
var musicalpreference_classicMaxDuration;
var musicalpreference_classicComponents;
function musicalpreference_classicRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'musicalpreference_classic' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    musicalpreference_classicClock.reset();
    routineTimer.reset();
    musicalpreference_classicMaxDurationReached = false;
    // update component parameters for each repeat
    sliderClassicPreference.reset()
    psychoJS.experiment.addData('musicalpreference_classic.started', globalClock.getTime());
    musicalpreference_classicMaxDuration = null
    // keep track of which components have finished
    musicalpreference_classicComponents = [];
    musicalpreference_classicComponents.push(text_PreferenceClassic);
    musicalpreference_classicComponents.push(sliderClassicPreference);
    
    for (const thisComponent of musicalpreference_classicComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function musicalpreference_classicRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'musicalpreference_classic' ---
    // get current time
    t = musicalpreference_classicClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_PreferenceClassic* updates
    if (t >= 0.0 && text_PreferenceClassic.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_PreferenceClassic.tStart = t;  // (not accounting for frame time here)
      text_PreferenceClassic.frameNStart = frameN;  // exact frame index
      
      text_PreferenceClassic.setAutoDraw(true);
    }
    
    
    // if text_PreferenceClassic is active this frame...
    if (text_PreferenceClassic.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *sliderClassicPreference* updates
    if (t >= 0.0 && sliderClassicPreference.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sliderClassicPreference.tStart = t;  // (not accounting for frame time here)
      sliderClassicPreference.frameNStart = frameN;  // exact frame index
      
      sliderClassicPreference.setAutoDraw(true);
    }
    
    
    // if sliderClassicPreference is active this frame...
    if (sliderClassicPreference.status === PsychoJS.Status.STARTED) {
    }
    
    
    // Check sliderClassicPreference for response to end Routine
    if (sliderClassicPreference.getRating() !== undefined && sliderClassicPreference.status === PsychoJS.Status.STARTED) {
      continueRoutine = false; }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of musicalpreference_classicComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function musicalpreference_classicRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'musicalpreference_classic' ---
    for (const thisComponent of musicalpreference_classicComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('musicalpreference_classic.stopped', globalClock.getTime());
    psychoJS.experiment.addData('sliderClassicPreference.response', sliderClassicPreference.getRating());
    psychoJS.experiment.addData('sliderClassicPreference.history', sliderClassicPreference.getHistory());
    // the Routine "musicalpreference_classic" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var musicalpreference_heavymetalMaxDurationReached;
var musicalpreference_heavymetalMaxDuration;
var musicalpreference_heavymetalComponents;
function musicalpreference_heavymetalRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'musicalpreference_heavymetal' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    musicalpreference_heavymetalClock.reset();
    routineTimer.reset();
    musicalpreference_heavymetalMaxDurationReached = false;
    // update component parameters for each repeat
    slider_HeavymetalPreference.reset()
    psychoJS.experiment.addData('musicalpreference_heavymetal.started', globalClock.getTime());
    musicalpreference_heavymetalMaxDuration = null
    // keep track of which components have finished
    musicalpreference_heavymetalComponents = [];
    musicalpreference_heavymetal_Components.push(text_PreferenceHeavymetal);
    musicalpreference_heavymetal_Components.push(slider_HeavymetalPreference);
    
    for (const thisComponent of musicalpreference_heavymetalComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function musicalpreference_heavymetalRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'musicalpreference_heavymetal' ---
    // get current time
    t = musicalpreference_heavymetalClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_PreferenceHeavymetal* updates
    if (t >= 0.0 && text_PreferenceHeavymetal.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_PreferenceHeavymetal.tStart = t;  // (not accounting for frame time here)
      text_PreferenceHeavymetal.frameNStart = frameN;  // exact frame index
      
      text_PreferenceHeavymetal.setAutoDraw(true);
    }
    
    
    // if text_PreferenceHeavymetal is active this frame...
    if (text_PreferenceHeavymetal.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *slider_HeavymetalPreference* updates
    if (t >= 0.0 && slider_HeavymetalPreference.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider_HeavymetalPreference.tStart = t;  // (not accounting for frame time here)
      slider_HeavymetalPreference.frameNStart = frameN;  // exact frame index
      
      slider_HeavymetalPreference.setAutoDraw(true);
    }
    
    
    // if slider_HeavymetalPreference is active this frame...
    if (slider_HeavymetalPreference.status === PsychoJS.Status.STARTED) {
    }
    
    
    // Check slider_HeavymetalPreference for response to end Routine
    if (slider_HeavymetalPreference.getRating() !== undefined && slider_HeavymetalPreference.status === PsychoJS.Status.STARTED) {
      continueRoutine = false; }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of musicalpreference_heavymetalComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function musicalpreference_heavymetalRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'musicalpreference_heavymetal' ---
    for (const thisComponent of musicalpreference_heavymetalComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('musicalpreference_heavymetal.stopped', globalClock.getTime());
    psychoJS.experiment.addData('slider_HeavymetalPreference.response', slider_HeavymetalPreference.getRating());
    // the Routine "musicalpreference_heavymetal_" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var EndScreenMaxDurationReached;
var _key_resp_endscreen_allKeys;
var EndScreenMaxDuration;
var EndScreenComponents;
function EndScreenRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'EndScreen' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    EndScreenClock.reset();
    routineTimer.reset();
    EndScreenMaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_endscreen.keys = undefined;
    key_resp_endscreen.rt = undefined;
    _key_resp_endscreen_allKeys = [];
    psychoJS.experiment.addData('EndScreen.started', globalClock.getTime());
    EndScreenMaxDuration = null
    // keep track of which components have finished
    EndScreenComponents = [];
    EndScreenComponents.push(textEnd);
    EndScreenComponents.push(key_resp_endscreen);
    
    for (const thisComponent of EndScreenComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function EndScreenRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'EndScreen' ---
    // get current time
    t = EndScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textEnd* updates
    if (t >= 0.0 && textEnd.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textEnd.tStart = t;  // (not accounting for frame time here)
      textEnd.frameNStart = frameN;  // exact frame index
      
      textEnd.setAutoDraw(true);
    }
    
    
    // if textEnd is active this frame...
    if (textEnd.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *key_resp_endscreen* updates
    if (t >= 0.0 && key_resp_endscreen.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_endscreen.tStart = t;  // (not accounting for frame time here)
      key_resp_endscreen.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_endscreen.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_endscreen.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_endscreen.clearEvents(); });
    }
    
    // if key_resp_endscreen is active this frame...
    if (key_resp_endscreen.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_endscreen.getKeys({keyList: 'space', waitRelease: false});
      _key_resp_endscreen_allKeys = _key_resp_endscreen_allKeys.concat(theseKeys);
      if (_key_resp_endscreen_allKeys.length > 0) {
        key_resp_endscreen.keys = _key_resp_endscreen_allKeys[_key_resp_endscreen_allKeys.length - 1].name;  // just the last key pressed
        key_resp_endscreen.rt = _key_resp_endscreen_allKeys[_key_resp_endscreen_allKeys.length - 1].rt;
        key_resp_endscreen.duration = _key_resp_endscreen_allKeys[_key_resp_endscreen_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of EndScreenComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function EndScreenRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'EndScreen' ---
    for (const thisComponent of EndScreenComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('EndScreen.stopped', globalClock.getTime());
    key_resp_endscreen.stop();
    // the Routine "EndScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
