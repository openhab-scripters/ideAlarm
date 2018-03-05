# ideAlarm
Multi Zone Home Alarm Script for openHAB jsr223 jython

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## THIS REPOSITORY IS UNDER CONSTRUCTION. NOT FINISHED YET!

## About
ideAlarm is written in Jython and runs on openHAB 2.

The name ideAlarm comes from merging the two words ideal and alarm.

Your home is your castle. Keeping it safe and secure is a top priority of many homeowners. With ideAlarm, you can easily set up your own DIY Home Security System using the sensors that you already have in Domoticz.

#### Reliability
A dedicated home security system might provide higher reliability than what you achive by a DIY system. It depends how you set things up. With that said, in case don't already own a dedicated home security system but you still want to take advantage of the capabilities of your home automation system together with all its sensors you might want to use it to set up your own DIY home alarm system. Please make sure that you've read and understood the [disclaimer](https://github.com/OH-Jython-Scripters/ideAlarm#disclaimer)

#### Helps you to maintain safety also when unarmed
ideAlarm has an optional feature that you can use to alert you about doors, windows etc that you have forgotten to close. We call this feature [nagging](https://en.oxforddictionaries.com/definition/nag) 

#### Alarm Zones
Your ideAlarm system will have one or more [zones]. Zones might be areas located at different places. You might also want to use place certain kind of detectors in a separate zone (like water leak detectors) and always keep that zone armed. If an alert occurs the system informs you which zone is alerting and what sensor has been triggered.

#### Highly customizable 
ideAlarm has a number of predefined events that will trigger your custom event helpers. These will not be overwritten when upgrading. That way you can choose whatever shall happen on those events. 

#### Alarm Zone State
Each Alarm Zone has an Item that holds one of the following states: 'Normal', 'Arming', 'Alert', 'Error', 'Tripped' or 'Timed out'

#### Alarm Zone Arming Mode 
Each Alarm Zone has an Item that holds one of the following arming modes: 'Disarmed', 'Armed Home', or 'Armed Away'

#### Sections (sensors)
We prefer to use the name 'section' for a sensor. A section could for example be a group of windows, each with a physical contact connected in serial with a z-wave sensor. A section can also be a single physical sensor.

#### A section can be enabled or disabled
For your convenience you can easily enable or disable a section in the configuration file. If you wish you can also declare a function for a specific section in the configuration file that allows the senction to be automatically enabled for example only when it's dark or depending on the state of other openHAB Items. If you have implemented presence detection in your system, you could for example disable a specific section when you are at home.

## Installation

#### Prerequisits

The following should be installed, configured, tested and running before continuing with installing ideAlarm:

* [openHAB](https://docs.openhab.org/index.html) version **2.2** or later
* [Jython scripting for openHAB 2.x](https://github.com/steve-bate/openhab2-jython)
* openHAB [expire binding](https://docs.openhab.org/addons/bindings/expire1/readme.html)
* openHAB [persistence](https://docs.openhab.org/configuration/persistence.html) setup and working
* [mylib](https://github.com/OH-Jython-Scripters/mylib)


#### Download mapping files
Download the [mapping files](https://github.com/OH-Jython-Scripters/ideAlarm/tree/master/transform) in the language of your choise and save them on your system where you keep your mappings files (in the transform folder)

#### Define Item Groups (needed for persistence)
Below is an example how you can define some groups to help organize your ideAlarm Items. The important thing here is not the names of the groups but rather that you have defined your persistence so that the group **G_Persist** will be persisted on change and on system start up.
```
Group G_Persist // Persist on change and system start up
Group G_AlarmArmingMode (G_Persist)
Group G_AlarmStatus (G_Persist)
Group G_VirtualDevice (G_Persist)
Group G_Timer
```

#### Create Items for each alarm zone you intend to use
For each alarm zone that you wish to define, create the following items through text .items files located in the $OPENHAB_CONF/items folder. You are advised to keep the naming convention suggested at least until everything is set up and works well. Your first zone's items get item names starting with 'Z1'. Prepend your second zone items with 'Z2' etc.

```
Number Z1_Arming_Mode "Z1 Arming Mode: [MAP(en_armingmode.map):%s]" <alarm> (G_AlarmArmingMode)
Number Z1_Status "Z1 Status: [MAP(en_zonestatus.map):%s]" <alarm> (G_AlarmStatus)

Switch Toggle_Z1_Armed_Away "Toggle Z1 Armed Away" <switch> (G_VirtualDevice) {expire="1s,command=OFF"}
Switch Toggle_Z1_Armed_Home "Toggle Z1 Armed Home" <switch> (G_VirtualDevice) {expire="1s,command=OFF"}

Number Z1_Open_Sections "Z1 open sections [%.0f]" <door> (G_VirtualDevice)

Switch Z1_Entry_Timer "Z1 entry timer [%s]" <time> (G_Timer) {expire="15s,command=OFF"}
Switch Z1_Exit_Timer "Z1 exit timer [%s]" <time> (G_Timer) {expire="2m,command=OFF"}
Switch Z1_Nag_Timer "Z1 nag timer [%s]" <time> (G_Timer) {expire="4m,command=OFF"}
Switch Z1_Alert_Max_Timer "Z1 alert maximum time [%s]" <time> (G_Timer) {expire="20s,command=OFF"}
```

#### Create and edit the config file
* Copy the text from [The example config file](https://raw.githubusercontent.com/OH-Jython-Scripters/ideAlarm/master/automation/lib/2_zones_example_config.py) and paste it into a new file named $OPENHAB_CONF/automation/lib/python/idealarm/config.py
* Make your changes to the configuration file to suit your system.
* Copy and paste your configuration file into the form on [PythonBuddy](https://pythonbuddy.com/) to verify that it has the correct Python syntax. The two org.eclipse.smarthome imports will fail but you can ignore that.
* Save the file.

## Disclaimer
THIS SOFTWARE IS PROVIDED BY THE AUTHOR "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
