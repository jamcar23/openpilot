Version 53
========================
  * New OP Params:
    * DISENGAGE_ON_GAS: Param(True, [bool], description='Whether you want openpilot to disengage on gas input or not.', live=True)
    * ENABLE_ROAD_SIGNS: Param(False, [bool], live=True, depends_on=SHOW_TOYOTA_OPTS, description='Use Toyota\'s road sign assist to control OP speed.')
  * Commits:
    * feat(car): add speed limit fields to car state
    * feat(toyota): populate speed limit from toyota's RSA
    * feat(controls): let speed based on car's speed limit
    * fix(toyota): make sure spdval1 is set before use in car state
    * docs(readme): add info about road sign assist
    * fix(controls): make sure speed limit is only applied if its above 0
    * feat(ui): show speed limit view on road when car has valid road sign
    * fix(ui): make sure draw road sign function gets called
    * fix(controls): make sure road signs are checked first
    * fix(controls): make sure the speed limit order of operations is correct
    * fix(ui): make sure speed limit sign shows up correct in onroad ui
    * fix(controls): apply last speed limit when there isn't a valid one
    * fix(controls): try to use button events to offset speed limit
    * fix(controls): make sure cruise setpoint can change when there isn't a road sign
    * fix(github): make sure workflows can push to git repo
    * fix(controls): offset speed limit from car's last speed
    * fix(controls): properly set last cruise speed when reenabling

Version 52
========================
  * Commits:
    * no heading cost (#20594)
    * MPC retune for laneless fix (#20616)
    * fix(planner): properly set custom steer rate cost
    * fix(planner): temp remove wide camera from lat planner
    * fix(planner): get bool param correctly

Version 51
========================
  * New OP Params:
    * HIGH_BEAM_BRIGHTNESS: Param(20, VT.number, depends_on=ENABLE_SCREEN_BRIGHTNESS_HEAD_LIGHTS)
    * DISENGAGE_ON_GAS: Param(True, [bool], description='Whether you want openpilot to disengage on gas input or not.', live=True)
  * Commits:
    * feat(params): enable optional disengage on gas
    * fix(param); made disengage on gas a live param
    * Merge branch 'src' into disengage-on-gas
    * docs(readme): add ToC section for notable op params

Version 50
========================
  * New OP Params:
    * SHOW_BUILD_OPTS: Param(False, [bool], live=False, description='Show options for compile time features.')
    * ENABLE_SCREEN_BRIGHTNESS_HEAD_LIGHTS: Param(False, [bool], depends_on=SHOW_BUILD_OPTS, description='When enabled, the screen brightness will adjust depending on the car headlights.')
    * DAY_BRIGHTNESS: Param(245, VT.number, depends_on=ENABLE_SCREEN_BRIGHTNESS_HEAD_LIGHTS)
    * NIGHT_BRIGHTNESS: Param(50, VT.number, depends_on=ENABLE_SCREEN_BRIGHTNESS_HEAD_LIGHTS)
    * HIGH_BEAM_BRIGHTNESS: Param(20, VT.number, depends_on=ENABLE_SCREEN_BRIGHTNESS_HEAD_LIGHTS)
  * Commits:
    * fix(param): made show build options a live param
    * fix(params): clarify what enable_screen_brightness_head_lights does
    * feat(params): add params for brightness when high beams are on
    * docs(readme): add spot about screen brightness via head lights

Version 49
========================
  * Commits:
    * fix(ui): change home screen to say flexpilot instead of op

Version 48
========================
  * New OP Params:
    * STEER_RATE_COST: Param(1., VT.number, live=True, depends_on=ENABLE_STEER_RATE_COST)
    * SHOW_BUILD_OPTS: Param(False, [bool])
    * ENABLE_SCREEN_BRIGHTNESS_HEAD_LIGHTS: Param(True, [bool], depends_on=SHOW_BUILD_OPTS, description='When enabled the screen brightness will be brightness_m when head lights are off.')
    * DAY_BRIGHTNESS: Param(0.8, VT.number, depends_on=ENABLE_SCREEN_BRIGHTNESS_HEAD_LIGHTS)
    * NIGHT_BRIGHTNESS: Param(0.15, VT.number, depends_on=ENABLE_SCREEN_BRIGHTNESS_HEAD_LIGHTS)
  * Commits:
    * feat(param): add build params for enable head light screen brightness
    * feat(toyota): add head light info for toyota's into car state
    * feat(ui): update screen brightness based on head lights
    * debug(ui): log what screen brightness is getting set to
    * fix(ui): fix ui debug log
    * debug(ui): add more debug statements for ui
    * fix(ui): check if enable screen brightness is defined
    * fix(ui): properly call head light types
    * fix(ui): fix typo in accessing captin proto enums
    * tests(processes): update process replay refs for head-light-screen-brightness

Version 47
========================
  * Commits:
    * bump version to 0.8.3
    * CI: fix webcam cache
    * scons cache in CI (#20197)
    * qt fixups (#20171)
    * qt confirmation dialogs (#20202)
    * Additional 2021 Corolla Camera FW (#20203)
    * Add missing ESP f/w for CAR.CAMRY_TSS2 (#20199)
    * (msm_sensor_power_setting*) type conversions are not required (#20191)
    * Qt ui: fix minimum pass length
    * tici fix ambient temperature zone
    * camera_qcom.h: regroup variables by usage (#20196)
    * default this on
    * fix log values with non-utf8 characters and remove index_log (#20173)
    * Tici art4 (#20210)
    * oneplus cleanup (#20200)
    * Add Lexus RX Ecu.engine fw version (#20198)
    * 2020 RDX Ecu.combinationMeter firmware (#20215)
    * juggle.py: add exception
    * Tici MIPI config (#20205)
    * fix rotation on input dialog
    * tici driverview support (#20223)
    * fix SSL errors in Qt UI on NEOS (#20225)
    * fix typo
    * UI: rename frontview to driver_view (#20228)
    * Fxing some typos in vehicle_model.py comments (#20220)
    * num_cids should be 1 (#20190)
    * move intrinsic_matrix into modeldata.h, removed duplicate definitions. (#20051)
    * cameras_qcom: use std::mutex (#20181)
    * Set hyundai start accel
    * ui.py: draw lines on radarState leads
    * modeld.cc construct matrix directly from data
    * move function calib_frame_to_full_frame to ui.cc (#20230)
    * Update values.py to add more 2021 Sonata FWs (#20219)
    * merge the china golf 7.5 missing values in the existing fingerprint (#20218)
    * modeld.cc fix matrix storage order
    * remove build arg from manager prepare_managed_process (#20229)
    * UI: Move the variables need to be updated by socket to UIScene (#19783)
    * Replace hardcoded values for Pi (#20235)
    * force same gamma
    * clean up tici camera registers (#20209)
    * camerad: fix thumbnail cnt (#20236)
    * set brightness, catch exceptions
    * needs to be int
    * ui: check sensor list size
    * better transition
    * oneplus cleanup (continue) (#20212)
    * fix tici sound card check
    * VW MQB: Get steering rate-change sign from the correct signal (#20238)
    * 2021 Ridgeline (#20240)
    * 2020 Avalon (#20241)
    * VW: update process replay route (#20239)
    * Update README.md
    * VW MQB: Add support for blind spot monitoring radar (#20242)
    * bump opendbc
    * UI touchups (#20243)
    * VW MQB: Add support for stock FCW and AEB (#20244)
    * ui: remove unused roadCameraState from SubMaster (#20245)
    * camera_qcom: move opencl stuff into class LapConv  (#20180)
    * Manager cleanup (#20231)
    * 2020 HRV FW (#20246)
    * agnos 0.7 (#20249)
    * agnos 0.8 (#20267)
    * offroad alert for agnos update (#20270)
    * bump panda
    * fix uninstall after manager refactor
    * raw_logger: remove unneeded recursive_mutex (#20274)
    * fix manager crash on PC after going offroad
    * don't run dmonitoringmodeld in sim
    * also skip ubloxd in sim
    * fix managed_processes for tests
    * Fix simulator docker: CPU only for now (#20227)
    * modeldata.h: new function get_model_yuv_transform (#20257)
    * ui/update_line_data: use max_idx as paramater instead of max_distance (#20256)
    * camera_qcom: remove eeprom related stuff (#20254)
    * cameras_qcom: use macros for actuator moving dir (#20259)
    * camera_qcom: change unsigned int to uint32_t (#20262)
    * camera_qcom: better error message for apply exp error (#20265)
    * use cached buffer for FlatArrayMessageReader (#20233)
    * Process config cleanup (#20276)
    * manager: check if process is running before sending signal
    * start_openpilot_docker.sh: pull image
    * bridge.py: don't clear params
    * revert to divide first
    * android logcatd test reliability (#20284)
    * only show EON charge alert on EONs
    * Add watchdog check to manager (#20277)
    * small carla docker fixes
    * Add firmware values for 2021 Acura RDX (#20282)
    * merge tools/misc and tools/scripts
    * Move simulator CI to tools workflow (#20285)
    * qt_sound: lower volume
    * these are no longer in the pipfile
    * Run models in function run_model (#20272)
    * Boardd: Track ublox message frequency and re-init (#20278)
    * board: respect 10 second ublox init time
    * fix default plotjuggler path
    * manager watchdog, log exit code
    * VW MQB: Support for other transmission types (#20253)
    * boardd: remove check on CLASS_MON
    * bump opendbc
    * boardd: increase CLASS_RXM timeout
    * boardd: 0.9s timeout, only log no reset
    * Use exposure for screen brightness (#20290)
    * Revert fix default plotjuggler path
    * Spinner: wait for UI to start (#20279)
    * update to python 3.8.5 (#20217)
    * update_requirements: install pipenv
    * VW MQB: Use raw steering angle signal (#20247)
    * 2021 Acura RDX firmware clean up + update readme (#20288)
    * power monitoring script
    * fix mac CI (#20292)
    * use xx pipfile when available
    * fix static analysis CI
    * better way to set pipfile
    * fix cached mac CI run (#20294)
    * minor bug fixes in sim (#20286)
    * turn pigeon off when going offroad (#20296)
    * smoother spinner transition on startup
    * uncomment
    * optimizing simulator performance (#20295)
    * turn off gpsMalfunction alert until uBlox config is fixed
    * boardd: stricter ublox logging
    * bump opendbc
    * Kia Ceed 2019 (#20283)
    * paint.cc: fix indentation & code style (#20302)
    * tuning simulator parameters (#20304)
    * UI HW Abstraction layer (#20301)
    * fix setting brightness on tici
    * LapConv::Update: use CL_TRUE instead of true (#20311)
    * FrameBuffer: move the status,success variables closer to usage (#20308)
    * softmax(): use std::max_element (#20306)
    * ui.cc: lane lines have different x values
    * Add several missing Palisade firmwares (#20312)
    * ui/update_model: cleanup (#20313)
    * driving.h: fix indentation (#20315)
    * transform_queue: const mat3& projection (#20316)
    * VW MQB: Updated message and signal data, round 1 (#20297)
    * only destroy if inited (#20317)
    * bump laika
    * improving tools readme (#20305)
    * Kia Seltos 2021 (#20321)
    * bump opendbc and cereal
    * add kia seltos to release notes
    * Better high speed alert message (#20322)
    * use loop index (#20307)
    * refactor function alloc (#20192)
    * Minimize sim docker image size (#20324)
    * bump cereal
    * bump pycapnp version (#20326)
    * LateralPlanner should only compute curvature (#20289)
    * add latcontrol angle to release files
    * thneed: remove redundant function nanos_since_boot (#20329)
    * reduce log spam (#20330)
    * bump opendbc
    * Add missing engine f/w for HIGHLANDERH_TSS2 (#20332)
    * Add GM steering rate and EPS torque to CarState (#20319)
    * set_exposure_target test (#20318)
    * cleanup camera_qcom const structs (#20251)
    * fix Fix problematic realloc (#19812)
    * camera_qcom2: add std::mutex exp_lock (#20183)
    * camera_frame_stream.h: remove unused variables (#20340)
    * NEOS 16 (#20214)
    * Honda CRV 2021 fw versions (#20341)
    * 2018 Lexus NX300: Add missing EPS & engine f/w (#20337)
    * Specify comma containers come from ghcr.io in docker pull commands. (#20342)
    * only restart crashed UI on tici
    * Fix vehicleModelInvalid alert (#20352)
    * juggle.py: make CAN optional to speed up parsing
    * boardd.cc: lower log level of ublox timing issues
    * make vehicleModelInvalid a NoEntry
    * ublox logs level logging.debug -> logging.info
    * Some OCD FW_VERSIONS section cleanup/sorting (#20348)
    * Add missing RAV4_TSS2 EPS f/w (#20347)
    * pass cloudlog to EKF_sym
    * ui.cc: fix update_lead segfault (#20351)
    * bump cereal
    * Improve screen brightness by also using camera gain (#20357)
    * Qt UI: simplify terms (#20349)
    * VW MQB: Updated message and signal data, round 2 (#20298)
    * agnos 0.9 (#20363)
    * fix reboot button in offroad alerts
    * cameras:move cameras_supported to the top (#20370)
    * CameraBuf::acquire: remove reference frame_data, use cur_frame_data to keep consistency (#20361)
    * use class AlignedBuffer from cereal (#20343)
    * BMX055 dont use FIFO registers (#20374)
    * Revert use class AlignedBuffer from cereal (#20343)
    * Sane curvature rate limit in plannerd (#20366)
    * 2021 Camry camera fw (#20378)
    * Fix warning popup for file not found, batman. (#20364)
    * CameraBuf: remove class variable yuv_metas (#20376)
    * mount openpilot in simulator docker image (#20379)
    * update simulator README
    * bump cereal
    * only do hardware supported check if PandaState is not None (#20385)
    * verify safetyParam read back from PandaState (#20384)
    * bump panda
    * bump cereal
    * use class AlignedBuffer (#20388)
    * update line length (#20391)
    * fixup profiler
    * profiler: use more recent drive
    * Add missing engine & EPS f/w for LEXUS_IS (#20398)
    * include PACIFICA_2020 in late-model behavior (#20399)
    * QT: click outside of confirmation dialog to dismiss (#20394)
    * remove legacy launch.sh script
    * record front lock (#20400)
    * update .dockerignore
    * qt: faster training guide (#20407)
    * OffroadAlert: read alert keys in constructor (#20408)
    * radar fw for Acura RDX 2021 (#20411)
    * Update locationd (#20410)
    * bump opendbc
    * Qt UI: offroad home touchups (#20416)
    * terms fixups (#20392)
    * fix margin after setting DPI
    * remove unused line (#20426)
    * README.md for SSH (#20365)
    * SettingsWindow: use list instead of map to preserve insertion order for sidebar items. (#20424)
    * 2021 RAV4 Hybrid Engine fingerprint (#20427)
    * cleanup ui_draw_vision_event (#20386)
    * Qt: update developer page when it's visible (#20396)
    * remove redundant update available title
    * log when nvme isn't mounted (#20428)
    * Qt: use the AbstractControl for multiple types of controls (#20417)
    * fix margin on c2
    * Qt UI: SSH keys (#20430)
    * small style improvement in settings
    * int(round()) on apply_steer for correct comparison after rate limiting (#20425)
    * it's qt time (#20433)
    * tici touch ups (#20434)
    * fix offroad home on tici (#20435)
    * agnos 0.10 (#20437)
    * Qt UI: scale volume with speed (#20441)
    * Remove lane change toggle and default LDW to off (#20442)
    * offroad alert improvements (#20443)
    * start_openpilot_docker.sh: fix docker container name (#20444)
    * sim/build_container.sh: fix container name
    * CH-R Hybrid Firmware (#20449)
    * auotmatic jenkins setup (#20448)
    * Camry Firmware (#20450)
    * increasing time for PlotJuggler CI
    * add descriptions in settings (#20453)
    * add description for SSH keys
    * ui: unify terms scrolling
    * New KL model + laneless toggle (#20454)
    * use scons to build panda fw (#20457)
    * bump panda
    * Upload android tombstones (#20459)
    * split
    * Qt UI: power saving (#20456)
    * APK purge (#20446)
    * agnos 0.11 (#20461)
    * QML terms (#20439)
    * Qt touchups (#20465)
    * Start ui before manager preimport (#20468)
    * Kill processes in parallel when going offroad (#20469)
    * add spinner to release files
    * log to file and send through athena (#20250)
    * Qt input: pass QString by reference (#20467)
    * remove cython dependency in swaglog
    * VW MQB: UDS fingerprinting support (#20271)
    * updated: log git diff on overlay init (#20476)
    * fix (#20477)
    * review training guide button (#20466)
    * fix athena calls that do not use params
    * add prebuilt text window to release files
    * new description for laneless (#20474)
    * test build script in CI (#20482)
    *  show persistent dashcam mode alert (#20483)
    * VW MQB: Volkswagen Tiguan Mk2 (#20484)
    * add tiguan to release notes
    * fix qt spinner height
    * Release note (#20486)
    * update scons nodes
    * VW MQB: VW Jetta Mk7, Škoda Kodiaq Mk1 (#20487)
    * always qt
    * add rest of vw to release notes
    * NEOS 16.2 (#20485)
    * bump panda
    * Qt: cache home screen state (#20395)
    * RELEASES.md: Skoda -> Škoda (#20496)
    * drive_stats.cc: fix distance rounding
    * Cache prime/points widget (#20497)
    * qt ui add gitignore to release
    * VW MQB: SEAT Ateca Mk1 (#20492)
    * Add 2020 Skoda Scala (#20494)
    * VW MQB: Volkswagen Passat Mk8 (#20493)
    * add debug script to run paramsd on route
    * temporarily increase ui cpu allowance
    * run paramsd: sort messages
    * bump panda
    * Revert temporarily increase ui cpu allowance
    * camerad jenkins box test (#20413)
    * update release notes
    * VW MQB: Škoda Superb Mk3 (#20500)
    * new training guide (#20495)
    * temporarily tolerate higher UI cpu usage in test
    * logging cleanup (#20502)
    * UI: limit version string length for master-ci
    * ui: don't log slow frame message in driverview (#20509)
    * filter out touches while in android activity (#20515)
    * 2021 RAV4 values (#20503)
    * 2021 Kia Seltos FW (#20513)
    * sound cleanup (#20491)
    * VW MQB: Update to Volkswagen Golf Mk7 (#20498)
    * log cpr voltages (#20519)
    * show serial number in settings
    * Qt: show username for current SSH keys (#20508)
    * disable buttons when onroad (#20475)
    * fix offroadTransition signal name
    * release2 build: fix panda build and remove DLC model file
    * CPR3 logging only on C2
    * add qml files to release
    * release files: cant add non existing files
    * Add qml-module-qtquick2 to package list
    * Kia Niro EV 2021 FW versions (#20518)
    * scrolling improvements (#20524)
    * Remove oneplus fan support (#20520)
    * settings scrolling improvement (#20525)
    * training guide: make coordinates relative to img
    * C-HR Hybrid camera fw (#20529)
    * cleanup tici networking + remove pagination (#20528)
    * also use e2e model output for DM policy (#20526)
    * OffroadAlert: update alerts inplace (#20463)
    * remove Rav4 ICE firmware from Rav4H (#20527)
    * add qcamera support to Route (#20521)
    * faster driverview start (#20507)
    * Added new util class FirstOrderFilter (#20303)
    * dump.py: lower poll timeout for faster exit
    * Params: python-like interface (#20506)
    * refactor draw_circle_image (#20473)
    * Add device_type to class Hardware (#20535)
    * Revert Add device_type to class Hardware (#20535)
    * prevent corrupted log messages (#20530)
    * cloudlog on RTC read/write (#20536)
    * supported year cleanup (#20539)
    * Merge branch 'master' into update-0.8.3
    * feat(mngr): add disabled processes backed to manager
    * fix(ui): fix merge conflicts from 0.8.3 in ui
    * fix(lat): fix merge issues in lat planner & indi controller
    * fix(lat): update live lat controller to support angle controller
    * fix(lat): add missing import to lat live
    * fix(ui): fix missing merge conflict in ui
    * fix(ui): fix dev ui for 0.8.3
    * fix(params): fix desired steer bp source, replace with curvature
    * fix(tests): update op params test for 0.8.3 changes
    * tests(params): update multi bp tests to always pass
    * fix(github): remove scons cache from build release job
    * fix(mngr): fix typo in op params in manager
    * fix(ui): add external gps sub to ui process
    * tests(processes): update process replay refs for update-0.8.3

Version 46
========================
  * Commits:
    * feat(ui): port colored lane lines from shane
    * fix(ui): add model reader to ui scene
    * docs(readme): update GH action status badges

Version 45
========================
  * Commits:
    * hotfix(docker): make sure docker images build correctly
    * hotfix(github): properly copy files from docker container when using fat image
    * hotfix(github): properly make ci release without extra files
    * hotfeat(github): make ci release manually invokable
    * feat(ui): draw measurements from dev ui in 0.8.1
    * fix(ui): update CPU temp and perc in dev UI
    * fix(ui): update gps accuracy and altitude in dev ui
    * fix(ui): update aEgo and steeringTorqueEps in dev ui
    * fix(ui): update radar state / lead data in dev ui
    * fix(ui): update angleSteers in dev ui
    * fix(ui): update angleSteersDes in dev ui
    * fix(ui): update engine rpm in dev ui
    * fix(ui): add bdr_is for dev ui
    * fix(ui): properly call viz_rect in dev ui
    * fix(ui): fix static declaration issue; all compiler errors fixed
    * fix(ui): shrink existing UI to make room for dev ui
    * fix(ui): move DM face view icon down a bit more
    * fix(ui): correct measurement method names
    * refactor(ui): split dev ui stats into individual methods
    * fix(ui): fix dev ui frames to be the correct size
    * refactor(ui): use marcos for color in dev ui
    * fix(ui): reposition measurement frames for dev ui
    * feat(ui): made dev ui frames more like max speed frame
    * fix(ui): use correct rect to draw dev ui frames
    * feat(ui): shrink border of frames to match old dev ui
    * fix(ui): move dev ui frames to be behind measurements
    * fix(ui): properly show aEgo in dev ui
    * refactor(ui): change grouping of dev ui measurements

Version 44
========================
  * New OP Params:
    * STEER_ACTUATOR_DELAY_BP_MULTI: Param([[0], [0, 4, 9, 17]], [list, float, int], live=True, depends_on=ENABLE_ACTUATOR_DELAY_BPS_MULTI)
    * STEER_ACTUATOR_DELAY_V_MULTI: Param([[0.45, 0.4, 0.3, 0.16]], [list, float, int], live=True, depends_on=ENABLE_ACTUATOR_DELAY_BPS_MULTI)
    * INDI_INNER_GAIN_BP_MULTI: Param([[0, 6, 15], [20, 24, 30]], [list, float, int], live=True, depends_on=ENABLE_MULTI_INDI_BREAKPOINTS)
    * INDI_INNER_GAIN_V_MULTI: Param([[5.25, 5.5, 6.5], [6.25, 6.75, 8.5], [7.5, 8.5, 10]], [list, float, int], live=True, depends_on=ENABLE_MULTI_INDI_BREAKPOINTS)
    * INDI_OUTER_GAIN_BP_MULTI: Param([[0, 3, 7], [20, 24, 30]], [list, float, int], live=True, depends_on=ENABLE_MULTI_INDI_BREAKPOINTS)
    * INDI_OUTER_GAIN_V_MULTI: Param([[4, 4.5, 6], [4.5, 5.25, 6.25], [6, 6.5, 7.5]], [list, float, int], live=True, depends_on=ENABLE_MULTI_INDI_BREAKPOINTS)
    * INDI_TIME_CONSTANT_BP_MULTI: Param([[0, 5, 10], [20, 24, 30]], [list, float, int], live=True, depends_on=ENABLE_MULTI_INDI_BREAKPOINTS)
    * INDI_TIME_CONSTANT_V_MULTI: Param([[0.3, 0.5, 1], [1.25, 1.5], [2.25]], [list, float, int], live=True, depends_on=ENABLE_MULTI_INDI_BREAKPOINTS)
    * INDI_ACTUATOR_EFFECTIVENESS_BP_MULTI: Param([[0, 5], [20, 24]], [list, float, int], live=True, depends_on=ENABLE_MULTI_INDI_BREAKPOINTS)
    * INDI_ACTUATOR_EFFECTIVENESS_V_MULTI: Param([[1.5, 1.75], [2, 3]], [list, float, int], live=True, depends_on=ENABLE_MULTI_INDI_BREAKPOINTS)
  * Commits:
    * bump version to 0.8.2
    * more external cleanup
    * apk gets built in CI now
    * bump cereal
    * fix startup spinner for non-C2 (#19536)
    * tici: implement sound check
    * fix up waste script
    * offroad home styling and cleanup
    * build Qt UI with clazy (#19537)
    * uninstall from qt offroad (#19538)
    * Toyota Highlander Engine FW (#19544)
    * ublox_msg.cc: simplify map operations in gen_nav_data (#2004)
    * small ubloxd cleanup
    * cleanup DM tests (#19540)
    * Add 2021 Lexus RX350 engine FW (#19542)
    * increase athena test timeout
    * Toyota RAV4H FW (#19546)
    * 2020 Camry FW (#19547)
    * Honda Insight FW (#19559)
    * make onboarding a bit nicer
    * cameras: use common transform (#19552)
    * build nui with scons (#19561)
    * Qt settings: highlight selected nav button
    * ui: delete the variable do_exit that is no longer used (#19551)
    * Update script usage (#19571)
    * Sound: destructor should be virtual too (#19570)
    * don't go onroad if internet needed (#19572)
    * bump cereal
    * remove old event
    * UI: add function ui_read_params (#19565)
    * add start_time parameter to unlogger (#19573)
    * 2021 Highlander ESP fw (#19577)
    * don't check dMonitorState's frame if frontview is false (#19584)
    * improved handle_display_state (#19574)
    * spinner: pre-compute rotations
    * simpilify ui_read_params (#19585)
    * qt settings style (#19588)
    * make wifi settings a bit nicer
    * jenkins: disable cache clear
    * offroad home style (#19593)
    * camerad: revert tbuffer dispatch change (#19589)
    * Fix typo in README.md (#19598)
    * 2021 Corolla Hybrid TS 1.8 (EU) engine fingerprint (#19599)
    * Added fingerprint for Ecu.programmedFuelInjection in Honda Civic Bosch (#19603)
    * unlogger.py: make sure img is always set
    * Update config.py code (#19609)
    * bump tombstone size limit for tici
    * 2019 Civic Hatch fw (#19611)
    * lgtm fixes (#19610)
    * add 2021 palisade fw
    * Added LEXUS_RX_TSS2 ESP & Engine f/w (#19618)
    * ui_draw_chevron: simplify calc size (#19616)
    * add 2021 honda insight fw (#19620)
    * IONIQ_EV_LTD f/w (#19601)
    * manager tests + make all processes exit cleanly (#19595)
    * tici: fix backlight timer interval
    * sensord is only a persistent process for C2
    * square looks better
    * update CI route sync script for new version of azcopy
    * another update_ci_routes fix
    * move to github container registry + CI speedup (#19621)
    * disable cpu usage test until CAN replay hw is fixed
    * fix LGTM C++ extraction (#19630)
    * UI:shorten variable name (#19633)
    * Make macos ci homebrew dep-caching fast (#19632)
    * cleanup mac build CI job
    * Car Port: Lexus ESH 2018 (#19624)
    * add lexus esh port to release notes
    * should not break if poll timeout (#19578)
    * fix thread safety issue in camera focusing (#19576)
    * Nicer blue/red colors offroad alert button
    * offroad alerts: put back reboot button
    * round close button
    * max_idx should be initialized as -1 (#19625)
    * refactor qlog_counter (#19626)
    * UI: reducing CPU usage from 13% to 4% when offroad (#19575)
    * bump opendbc: add pacifica cruise state signal
    * UI: simplify ui_draw_vision_speed (#19594)
    * adaptive cruise can no longer be bypassed on toyota (#2708)
    * simplify ui_draw_vision_maxspeed (#19642)
    * simplify logcatd (#19640)
    * Replace usleep with util::sleep_for (#19643)
    * Update values.py (#19644)
    * update CI routes, add back destination key
    * ui.py: white text on graphs (#19636)
    * Fix macOS CI (#19646)
    * external cleanup (#19647)
    * Car Port: 2021 Camry Hybrid TSS 2.5 (#19649)
    * add camry h port to release notes
    * Toyota interface.py refactor. Move default long tune before candidate check. (#19652)
    * shorten variable name (#19659)
    * refactor ui_draw_image (#19656)
    * bump opendbc
    * Revert bump opendbc
    * cleanup draw alert (#19655)
    * bump opendbc
    * setup clang tidy (#19533)
    * make android logcat exit cleanly (#19666)
    * 2018 Lexus RX350 fw (#19667)
    * tici loggerd fixes (#19622)
    * common exit handler (#19661)
    * hyundai: update palisade tuning (#19606)
    * hyundai: increase number of resume messages sent at a time (#19634)
    * fix race condition with encoder thread
    * fix problem with drawing path (#19670)
    * Move all CarControllerParams into values.py (#19663)
    * dont show speed below zero
    * UI: refactor model related functions (#19657)
    * paint.cc car_space_to_full_frame less paramaters (#19676)
    * Chrysler non-ACC Fix - Only allow openpilot in ACC mode (#19581)
    * only run logcatd while onroad
    * logcatd_android: use sleep_for instead of usleep
    * Lexus RX 2020 fw (#19678)
    * loggerd tests (#19671)
    *  remove double semicolons (#19681)
    *  remove double semicolons (#19682)
    * remove double semicolon in paint.cc (#19684)
    * sidebar.cc remove prefix for static functions (#19683)
    * Rebuild acado and add scons command to regenerate mpc (#19685)
    * Add FW versions for 2018 Lexus NX Hybrid (#19645)
    * Add indi breakpoints (#19664)
    * bump cereal and update ref
    * update Corolla TSS2 wheelbase
    * smp_pipenv (#19687)
    * bump laika
    * add other libraries
    * Civic Hatch 2017 fw (#19688)
    * qt reset and setup improvements
    * loggerd cleanup (#19668)
    * VisionIPC 2.0 (#19641)
    * bump cereal
    * Fix battery voltage reading (#19699)
    * pyopencl pipenv
    * refactor ui_draw_driver_view (#19597)
    * Refactor alert blinking (#19583)
    * cleanup (#19564)
    * create_thumbnail in camera_common (#19553)
    * dmonitoringd: add helper function get_yuv_buf (#19590)
    * loggerd: fix use after free and memory leaks (#19695)
    * reenable cpu usage test
    * Test segs 08 (#19701)
    * Prius Prime 2021 (#19651)
    * merge utilpp.h into util.h (#19710)
    * Fix build error after merge utilpp.h to util.h (#19714)
    * ui.cc: cleanup includes (#19704)
    * disable again for now, replay hw is down
    * ublox_msg.h: remove #define min (#19718)
    * replace std::this_thread::sleep_for with util::sleep_fo (#19717)
    * Add scanner for Cython dependencies (#19722)
    * ui.cc: fix driverview (#19723)
    * Refactor image texture stuff into class (#19719)
    * bump cereal
    * cleanup unused android libs in phonelibs (#19702)
    * EPS fw RAV4H_TSS2 (#19694)
    * 2021 RAV4 ESP and Engine FW (#19707)
    * RDX FW (#19709)
    * bump cereal and opendbc
    * loggerd: fix double encoder open (#19703)
    * Video Encoder abstraction (#19729)
    * FIX: It is not safe to call cameras_close before all threads are done. (#19555)
    * CameraBuf::stop() is not used
    * Hyundai Sonata 2021 transmission firmware (#19727)
    * convert glutil.c to gltuil.cc & add class GLShader (#19720)
    * hyundai: support for controlling cruise speed via HDA (#19635)
    * use scons cache for QCOM replay build in CI
    * build master-ci with the relase2 build device
    * Loggerd for PC (#19730)
    * loggerd: another rotation test (#19742)
    * fix tici debayer GPU page faults
    * fix tici dm
    * remove read_param from ui_init (#19745)
    * new laika
    * new ref commit
    * add clpeak to profiling tools
    * patch clpeak to run continuously
    * add prebuilt clpeak3
    * Extra test segs (#19749)
    * added Hyundai Santafe limited 2020 FP in hyundai values and updated description for SANTA_FE (#19746)
    * Update values.py (#19740)
    * bump cereal
    * CameraBuf: removed unused variables (#19735)
    * hyundai: increase steering angle limit for custom eps fw (#19744)
    * Add 2020 Santa Fe to readme
    * whoops, wrong car. fixed!
    * fix rounding error
    * GPS malfunction alert (#19756)
    * fix camera malfunction alert (#19757)
    * 2020 Corolla Hybrid fw (#19759)
    * better can replay script
    * fix import error
    * Mpc rework2 (#19660)
    * fix init
    * compensate for tilt
    * matches real data better
    * update prebuilt docker container (#19767)
    * fix tests
    * changing lag changes this
    * camerad use std::thread (#19771)
    * fill_frame_image: reduce function parameters (#19736)
    * ui.cc: rename update related functions (#19761)
    * Use  Rect as the parameter of draw_rect (#19696)
    * UI: refactor transform (#19658)
    * qt/home.cc: set fb_w&fb_h in function framebuffer_init,same as android (#19765)
    * camera_qcom2:  simplify camera_process_frame (#19763)
    * CameraBuf::acquire : using a scoped lock (#19764)
    * RecordFront remove ifdef (#19773)
    * Pacifica Fingerprint Addition (#19750)
    * text.c->text.cc (#19734)
    * reenable cpu usage test
    * replay improvements for testing closet
    * 2017 Civic Hatch fw (#19777)
    * Remove spaces (#19779)
    * OmxEncoder: use macro to check error (#19785)
    * back to open loop (#19781)
    * use std::map for images (#19768)
    * Toyota Avalon 2021 (#19790)
    * few fixes from LGTM
    * athena fixups (#19791)
    * On-device onroad CI test (#19792)
    * loggerd: do not LOGW twice when logger.part == 0 (#19795)
    * don't need the client anymore
    * OmxEncoder: use std::vector to keep buffer (#19807)
    * loggerd: make sure to print one statistics every 1000 times (#19803)
    * gpio.h: remove extern C (#19799)
    * Qt offroad: pairing (#19675)
    * Linux tombstones: add stacktrace and upload (#19737)
    * swaglog: use std::mutex & remove extern C (#19817)
    * add option for external sconscript (#19821)
    * fix mac build
    * clutil.h: remove extern C (#19809)
    * Fix macOS CI (#19822)
    * new macOS cache
    * no vehicle was more confusing
    * Update Subaru and GM test routes (#19828)
    * Carla fixes (#19824)
    * fix mac CI (#19829)
    * Cleanup pathplanner (#19827)
    * fix tombstoned path length
    * start timer only after ui init
    * agnos v0.2
    * OS version needs to be unset on script start
    * also unset here
    * update pairing text
    * tombstoned: fault address is also not unique due to ASLR
    * bump cereal
    * visionipc connect, make sure opengl context is current
    * qt ui: sync fps with camera
    * loggerd: split bootlog to a separate program (#19831)
    * Add fingerprint for Kia Forte GT 2021. (#19830)
    * update VW and nissan test routes
    * fix loggerd after bootlog split (#19840)
    * OmxEncoder: set s->of to nullptr after close (#19814)
    * CameraBuf: private variables (#19811)
    * camerad: remove duplicate set_realtime_priority
    * hyundai: add fpv2 for palisade with power steering fw mod (#19789)
    * params helpers (#19788)
    * camera frame stream cleanup (#19741)
    * 2021 Pacifica Hybrid confirmed working
    * face icon reflects DM policy  (#19842)
    * fix order of Lexus ES Hybrids
    * update refs for new dMonitoringState field
    * remove sidebar gps text, we have alerts for this
    * Remove incorrect esp fw in engine (Rav4_TSS2) (#19841)
    * remove old model packet (#19769)
    * Thneed load/save (#19700)
    * remove docker prebuilt CI job
    * build openpilot prebuilt on schedule (#19847)
    * Change qcom2 fserial and readout timing (#19820)
    * fix /dev/shm permisisons, fixes offroad
    * 2021 Corolla Hybrid camera fw (#19859)
    * 2021 Pacifica Hybrid fingerprint (#19846)
    * 2021 Lexus RX Hybrid fw (#19861)
    * modeld: remove template from fill_meta (#19862)
    * fix LGTM issues (#19868)
    * Hotspot password (#19854)
    * INDI: Time constant is used based on breakpoints (#19858)
    * OMX encoder stability (#19758)
    * move Qr code lib to phonelibs (#19871)
    * hotfix(params): update default multi-bp for corolla tune
    * Don't clean scons build on dirty branches
    * Qt parents3 (#19870)
    * qt ui: slow frame warning
    * qt ui: fix segfault if networkmanager is not running
    * qt ui: don't refresh wifi widget if it is not visible (#19876)
    * qt ui: remove line between poweroff/reboot
    * ui: remove satelliteCount (#19878)
    * UI: cleanup draw_alerts condition (#19875)
    * fill sof
    * fix qt onboarding text color
    * 2019 Toyota CHR Engine fw (#19881)
    * boardd: declare MessageBuilder close to usage (#19883)
    * boardd: use std::atomic for ignition to ensure thread-safety (#19882)
    * agnos 0.3
    * add device type to clouglog ctx (#19890)
    * util.h: use const reference for std::string parameter (#19885)
    * loggerd: remove vipc arg from encode frame
    * tici jenkins build (#19505)
    * Audi A3 8v support (#19873)
    * add audi a3 to release notes
    * Fix loggcatd: removed duplicate call to android_logger_list_free  (#19903)
    * more tici tests in jenkins (#19908)
    * make loggerd rotation test more reliable
    * OS Updater improvements (#19914)
    * qt: default token validity 1 hour
    * camera_webcam: add thumbnail to Pubmaster (#19919)
    * pigeon: use const reference for std::string parameter (#19886)
    * make onroad test more reliable
    * manager.py broadcast process states (#19880)
    * Panda: replace pthread_mutex with std::mutex (#19909)
    * Fix panda:  dangling pointer problem in can_receive (#19892)
    * dmonitoring_init: use &s->output[0] instead of &s->output (#19918)
    * agnos 0.4 (#19924)
    * model_init: remove memset (#19921)
    * camera_common: rename create_thumbnail to publish_thumbnail (#19920)
    * 2018 Hyundai Sonata (#19915)
    * Panda: add can_send buffer caching (#19910)
    * can_list_to_can_capnp_cpp: write message directly to the output string (#19912)
    * cameras_qcom: fix dangling pointer in fill_frame_image (#19891)
    * boardd: use setUbloxRaw to avoid memory alloc&copy in pigeon_publish_raw (#19884)
    * TTYPigeon::send : delete unnecessary temporary variables (#19898)
    * fix boardd loopback test after #19880
    * wait for pandad to start boardd
    * important for indi (#19926)
    * fix indentation (#19925)
    * actually wait for boardd to start
    * new ref for rateSteers fix
    * Split planner and pathplanner publishing into separate 'publish' methods (#19860)
    * Civic Hatch Diesel fw (#19929)
    * 2021 Toyota Highlander engine fw (#19930)
    * fill_frame_data: remove unused paramater cnt (#19936)
    * Add Github SSH keys (#19879)
    * CameraBuf::acquire : release on failure (#19935)
    * Thneed::clinit() : use cl_get_device_id helper(#19934)
    * util.h: re-indent function string_format and use const std::string & for read_file (#19931)
    * minor wifi improvements (#19938)
    * wifi connecting is not hidden any more
    * vision-only radar toggle (#19849)
    * remove legacy reset line support (#19770)
    * remove temporary fixes
    * tombstoned: fix address offset in string
    * hyundai: ability to create ACC messages (#19850)
    * hyundai: car state with longitudinal control support (#19851)
    * hyundai: add follow distance button (#19852)
    * Put bootlog in own folder (#19939)
    * OMXEncoder: add calls to OMX_Init()&OMX_Deinit() (#19905)
    * Fix BSM signal for Hyundai Santa Fe (#19855)
    * UI: handle alert in function update_alert (#19762)
    * fix up encoder test for tici rotation (#19941)
    * dmonitoring_publish: use kj::ArrayPtr<const float> raw_pred as paramater instead of float (#19916)
    * fix updated bug that allows for mismatch openpilot/agnos (#19943)
    * don't reflash agnos update if already flashed (#19944)
    * Revert OMXEncoder: add calls to OMX_Init()&OMX_Deinit() (#19905)
    * not relevant at high speed (#19946)
    * fix qt UI after #19762
    * bootlog: fix dangling pointer problem in logger_build_boot (#19942)
    * C++ swaglog (#19825)
    * fix valgrind complaints about swaglog
    * convert framebuffer to class  (#19800)
    * remove cqueue, use class SafeQueue (#19774)
    * fix safequeue import
    * draw lead indicator in 3D (#19793)
    * panda: refactor get_serial, return std::optional<std::string> (#19895)
    * Panda: refactor get_firmware_version, return std::optional<std::vector> (#19896)
    * Panda: use 'std::atomic<bool> connected' to ensure thread-safety (#19954)
    * keyboard.cc: get value by reference in ranged based loop (#19950)
    * OmxEncoder:  new function set_state, set and wait state changed  (#19906)
    * Revert OmxEncoder:  new function set_state, set and wait state changed  (#19906)
    * Set use_bsm on KIA_NIRO_EV, I've tested it seems to be generating (#19955)
    * match driverView with new model
    * pyTorch DM (#19760)
    * camerad frame lag/drop jenkins tests (#19945)
    * Panda: add check for connected in usb_read (#19957)
    * bump cereal
    * boardd: refactor usb_connect, delete panda on failure (#19956)
    * Wifi correct ip (#19961)
    * Qt training guide (#19953)
    * cleanup training guide
    * blue bg in training guide
    * tici dcam AE (#19970)
    * fix panda: remove uninitialized err and check after (#19974)
    * boardd: remove global variables spoofing_started&fake_send (#19966)
    * fix static analysis checks after mypy update
    * pin pre-commit hook versions
    * faster webcam CI (#19975)
    * UI: function update_status (#19679)
    * bump opendbc
    * move agnos manifest to selfdrive/hardware (#19889)
    * loggerd: small cleanup (#19864)
    * dmonitoring: use the same way as driving to build model output more clearly (#19933)
    * OMXEncoder: remove pthread_mutex_t lock  from member variables (#19948)
    * pigeon_publish_raw: use capnp::Data::Reader instead of Builder  (#19952)
    * pigeon_thread: ensure the pigeon->init() will not be called twice (#19963)
    * Add ESP FW for 2021 Hyundai Sonata SEL (#19980)
    * get_frame_image: moved the global variables into function static (#19982)
    * build release3 (#19984)
    * copy continue.sh into release3
    * copy into installer/
    * need to build from here since we link against the absolute paths
    * Longitudinal tune for Corolla TSS2 (#2746)
    * bump panda
    * Add back replay_many script for unlogging over jungles
    * bump panda
    * Pigeon::receive:  reserve 4kb+64b for std::string (#19951)
    * Multithreaded ssh activation (#19988)
    * shouldn't need that anymore
    * cloudlog once on commIssue (#19949)
    * tici fcam vignette compensation (#19971)
    * logcatd bugfix + tests (#19689)
    * UI: mv sidebar_collapsed&viz_rect to struct UIState (#19782)
    * model_publish: use kj::ArrayPtr<const float> raw_pred (#19917)
    * fix thneed build
    * split the build and test running
    * Logger: new class BZFile (#19959)
    * skip dashcam3 build for now
    * OmxEncoder: use c++ mutex&condition_variable (#19786)
    * mv logger_build_boot to bootlog.cc (#19996)
    * Logger: added function logger_get_route_name (#19995)
    * BMX055 magnetometer calibration (#19992)
    * Don't call function in assert (#19997)
    * move global connected_once into function static (#19999)
    * small tombstoned cleanup
    * Fix jwt.encode return type (#19776) (#19958)
    * nui is built with scons now
    * Deal with long lag compensation (#20004)
    * don't show on tici
    * implement ublox MON_HW2 message (#19962)
    * update libs (#20009)
    * Remove curv factor (#20011)
    * Cereal cleanup (#20003)
    * logcatd:  fix bug: subsequent reads after the first always return empty (#19994)
    * fix logcatd after bugfix
    * thneed: lookup dlsym offset at compile time (#20019)
    * look in /usr/local/lib first
    * fix ui.py
    * ui.py fix current steering angle
    * camera offsets (#20022)
    * skip manager check in sim
    * swap factory reset order
    * make thneed compile more robust
    * support for Nissan Leaf with ADAS ECU in alt location (instrument cluster) (#19619)
    * move global SET_SPEED_NA to function that uses it (#20026)
    * Different lag comp (#20024)
    * show sat count in sidebar (#20028)
    * fix font weights in qt ui
    * Agnos v0.5 (#20023)
    * UI: make onroad/offroad transition more robust (#20030)
    * Timezoned (#19960)
    * android logcatd fixes + better test (#20036)
    * Qt UI refactoring + improvements (#20033)
    * Chrysler Pacifica: additional 2020 Fingerprint values (#20032)
    * loggerd: remove the segment variable from encoders (#20034)
    * removed margin paramater from car_space_to_full_frame (#20017)
    * Toyota interface.py: Create separate section for custom long tune (#20021)
    * Remove dockerhub references from CI (#20038)
    * boardd: check do_exit in usb_retry_connect (#20007)
    * UI: remove struct track_vertices_data (#20018)
    * Fixup ui.py (#20040)
    * fix timestamps (#20029)
    * ui.py: topdown fixes
    * ui.cc: replace s->scene with scene (#20045)
    * dont print slow frame on pc
    * ui.cc: fix divide by zero
    * bump cereal
    * add visionipc cython to release files
    * bump cereal
    * Unlogger send video over VisionIPC (#20046)
    * combinationMeter f/w for Acura ILX (#20050)
    * fix failing CI jobs
    * fix low speed lateral (#20053)
    * 2021 Corolla Hatch confirmed working
    * fixup ui (#20049)
    * disable release3 build for now
    * update cereal
    * Update RELEASES.md
    * use gpsOK flag from locationd
    * Honda Odyssey tune (#20058)
    * remove gpsd (#20027)
    * improve cpu usage test robustness (#20067)
    * reset panda on startup (#20065)
    * fanSpeedRpmDesired -> fanSpeedPercentDesired
    * bump cereal
    * update frequencies for tici
    * adjust qcamera quality (#20066)
    * plotjuggler (#20063)
    * camerad fixes for updated agnos kernel (#20062)
    * Qt add Terms & Conditions (#19998)
    * Toyota Corolla Sport 2021 fw (#20059)
    * don't need this, driver view works on pc
    * COROLLA_TSS2 firmwares (#20070)
    * changing release name for plotjuggler
    * ignore everything from vscode
    * UI fixes (#20069)
    * Add fingerprint for 2018 Nissan Leaf G (Japan) (#20081)
    * timezoned: only one api request per hour
    * qt; fix setup build
    * should work (#20083)
    * Toyota: always learn offset to accurate steer angle sensor (#20087)
    * Locationd process noise typo (#20085)
    * Fix division by zero in lateral_planner.py (#20071)
    * update ref after divide by zero fix
    * added Toyota Corolla Touring Sport 2021 engine fwVersion (#20088)
    * Add RAV4_TSS2 and RAV4H_TSS2 to Improved long tune (#20079)
    * Qt ui: set timeout on all dbus interfaces in wifiManager (#20090)
    * Added missing ESP f/w for Kona EV (#20089)
    * ui: log visionipc receive timeout
    * onroad test: increase timeout waiting for logs
    * Honda Fit Tune (#20094)
    * camera_qcom: cleanup main() (#19805)
    * cereal cleanup part 2 (#20092)
    * speed up log writing
    * Fix ubloxd test compilation (#20101)
    * add catch2 header
    * juggle a whole route (#20099)
    * argparser for plotjuggler (#20103)
    * tools: cleanup + setup CI (#20104)
    * plotjuggler falling back to qlog (#20105)
    * juggle: add qlog argument
    * fix ui and unlogger after cereal cleanup
    * loggerd: clean exit on SIGPWR (#20100)
    * 2021 Camry fw (#20110)
    * 2019 Civic Hatch fw (#20111)
    * Do not allow engagement outside of training distribution (#20112)
    * agnos 0.6 (#20077)
    * Update RELEASES.md
    * add some error handling to juggle log loading
    * replace sleep with util::sleep_for (#20108)
    * add tss2 long tune to release notes
    * add visionIPC rewrite to release notes
    * script for CI env
    * fix apk after cereal cleanup (#20098)
    * camerad: rename variables&functions to follow new convention (#20096)
    * update agnos
    * Toyota: simplify angle offsetting (#20102)
    * timezoned: fix updating on /data/etc (#20119)
    * bump submodules
    * Toyota: fix DSU detection on no DSU cars (#20120)
    * Nissan altima (#2742)
    * update release notes
    * update scons nodes
    * eliminate python-logstash-async
    * fix prebuilt docker build (#20123)
    * add car bug report template
    * tici camerart III: prehistoric visuals (#20012)
    * bump cereal
    * Qt ui: close settings on onroad transition (#20114)
    * Add support for 2020 Toyota CH-R (#20126)
    * RELEASES.md: add qcam resolution and fix typo
    * also shutdown on tici (#20130)
    * offline usage for filter_log_message.py (#20131)
    * up tici hevc bitrate (#20093)
    * juggle.py: don't remove CAN data
    * 2018 Audi A3 (#20136)
    * add 2018 a3 to release notes
    * Adding new srs value to Honda CRV 2020 fingerprint (#20134)
    * Always linearize, better way of compensating for lag (#20133)
    * plotjuggler: also ignore symlink to bin directory
    * Qt-UI Close settings when screen turns off  (#20117)
    * add script to show rlog/qlog breakdown
    * bump cereal
    * set DBC_NAME env when juggling (#20139)
    * test loggerd: limit samples to number of services
    * Fix tici powerdown and add support for forcing (#20132)
    * remove some pip packages
    * fix inject_model import
    * Update A3 package
    * fix pylint errors
    * tici camerart 3.1 (#20143)
    * it's a 2017
    * 2021 Highlander engine fw (#20144)
    * only allow INDI wind down on user override (#20080)
    * Turn up brightness a little when UI crashes (#20142)
    * Qt-UI fix escaping all wifi access points (#20147)
    * Chrysler: Default fingerprint argument to empty fingerprint (#20146)
    * fix some refactor commits that weren't tested (#20140)
    * Revert fix some refactor commits that weren't tested (#20140)
    * 2021 Rav4 Hybrid EPS fw (#20150)
    * working with snap (#20155)
    * Qt on NEOS (#20153)
    * Qt-UI add driver monitoring view in offroad (#20148)
    * BMX055 magnetometer fixes and advanced self-test (#20118)
    * Qt-UI fix ssh username (#20159)
    * juggle: gitignore leftover rlog files
    * better gain values
    * gamma last and only one ccm
    * add file to disable lte while onroad (#20163)
    * neos networking (#20165)
    * 2021 pacifica hybrid - additional fingerprint values (#20164)
    * add a couple FW signatures for 2021 hyundai sonata SEL (#20162)
    * Qt-UI Cleanup SSH and Tethering password (#20169)
    * Qt standalone wifi chooser (#20141)
    * camerad: remove param pix_ptr from set_exposure_target (#20157)
    * write params in initData as Data
    * bump laika
    * PlotJuggler CI with build from source (#20166)
    * PlotJuggler demo (#20172)
    * Fix uiview.py (#20175)
    * Move duplicate function declarations to camera_common.h (#20176)
    * add new sentry client package (#20178)
    * plotjuggler readme screenshot
    * Merge branch 'master' into update-0.8.2
    * chore(git): update submodule to 0.8.2
    * chore(github): update github folder with upstream changes for 0.8.2
    * feat(actions): create initial script to setup ci env vars
    * fix(github): fix typo in old test yaml workflow
    * fix(github): make sure ci_env_vars.sh is executable
    * fix(github): make sure workflow clones repo
    * fix(github): properly eval conditions and export results in bash script
    * feat(github): export all env vars from bash script to setup_workflow job
    * fix(github): fix bash issues in ci_env_vars.sh
    * fix(github): fix syntax error in bash ci env var script
    * refactor(github): refactor selfdrive tests workflow to use env vars from script
    * fix(github): fix selfdrive tests workflow syntax
    * fix(github): fix selfdrive tests workflow whitespace syntax
    * fix(github): pull lfs files for process replay
    * refactor(github): move docker building workflow into its own file
    * fix(github): fix syntax for setting error message in job
    * fix(github): properly stop docker job earily early
    * feat(github): move ci release job into its own workflow
    * fix(github): fix ci release to properly check tests and make new ci branch
    * fix(github): properly select head branch name
    * fix(github): properly select branch name and allow for more time to build
    * refactor(github): move webcam & MacOS CI steps into their own workflows
    * feat(github): replace openpilot tests workflow with seperate files / workflows
    * fix(github): make sure we wait for selfdrive tests to finish
    * fix(github): check to wait for selfdrive must start right away
    * Merge branch 'ci-fixes-0.8.2' into update-0.8.2
    * fix(ui): remove dev-ui from fork / reset on road UI back to stock OP
    * fix(github): make it so wait for selfdrive only runs on pushes
    * fix(controls): update long plan source for new object name
    * fix(github): fix yaml syntax in selfdrive tests
    * fix(controls): fix long plan source in long planner
    * fix(github): make sure selfdrive unit tests run correctly
    * fix(planner): update path_plan message to lateralPlan
    * fix(planner): properly set desired steer before using
    * fix(tests): update op params tests with lateral plan changes
    * fix(controls): update indi controller to support breakpoints from CarParams
    * tests(processes): update process replay refs for update-0.8.2
    * fix(planner): remove unused import in plannerd
    * fix(tombstoned): add missing and remove unused imports
    * fix(planner): fix import issues in planner files
    * feat(planner): lateral & lane planners now getting opParams from plannerd
    * fix(github): remove unneed copy logs for selfdrive workflow
    * chore(github): disable webcam workflow
    * fix(sentryd): get git commit the new way
    * perf(github): sped up update-refs command by pulling prebuilt docker images
    * tests(processes): update process replay refs for update-0.8.2
    * fix(github): increase check interval to 60 secs
    * perf(github): improve wait for selfdrive be waiting in order of speed
    * fix(github): run wait for selfdrive on PRs too
    * fix(toyota): fix default tss2 corolla indi values
    * fix(github): wait for the correct selfdrive result
    * fix(github): docker build no longer throws an error when it skips building

Version 43
========================
  * New OP Params:
    * ENABLE_ACTUATOR_DELAY_BPS_MULTI: Param(False, bool, live=True, depends_on=SHOW_ACTUATOR_DELAY_PARAMS)
    * STEER_ACTUATOR_DELAY_BP_MULTI: Param([[0], [0, 4, 7]], [list, float, int], live=True, depends_on=ENABLE_ACTUATOR_DELAY_BPS_MULTI)
    * STEER_ACTUATOR_DELAY_V_MULTI: Param([[0.5, 0.35, 0.3]], [list, float, int], live=True, depends_on=ENABLE_ACTUATOR_DELAY_BPS_MULTI)
    * STEER_DELAY_MULTI_BP_SOURCE: Param(['vego', 'desired_steer_abs'], [list, str], live=True, depends_on=ENABLE_ACTUATOR_DELAY_BPS_MULTI)
    * ENABLE_ACCEL_HYST_GAP: Param(False, bool, live=True, depends_on=SHOW_TOYOTA_OPTS)
    * ACCEL_HYST_GAP: Param(0.02, VT.number, live=True, depends_on=ENABLE_ACCEL_HYST_GAP)
    * ENABLE_ACCEL_HYST_GAP_BPS: Param(False, bool, live=True, depends_on=ENABLE_ACCEL_HYST_GAP)
    * ACCEL_HYST_GAP_BP: Param([0.], [list, float, int], live=True, depends_on=ENABLE_ACCEL_HYST_GAP_BPS)
    * ACCEL_HYST_GAP_V: Param([0.02], [list, float], live=True, depends_on=ENABLE_ACCEL_HYST_GAP_BPS)
    * ENABLE_INDI_BREAKPOINTS: Param(False, bool, live=True, depends_on=SHOW_INDI_PARAMS)
    * INDI_INNER_GAIN_BP: Param([20, 24, 30], [list, float, int], live=True, depends_on=ENABLE_INDI_BREAKPOINTS)
    * INDI_INNER_GAIN_V: Param([7.25, 7.5, 9], [list, float, int], live=True, depends_on=ENABLE_INDI_BREAKPOINTS)
    * INDI_OUTER_GAIN_BP: Param([20, 24, 30], [list, float, int], live=True, depends_on=ENABLE_INDI_BREAKPOINTS)
    * INDI_OUTER_GAIN_V: Param([6, 7.25, 6], [list, float, int], live=True, depends_on=ENABLE_INDI_BREAKPOINTS)
    * INDI_TIME_CONSTANT_BP: Param([20, 24], [list, float, int], live=True, depends_on=ENABLE_INDI_BREAKPOINTS)
    * INDI_TIME_CONSTANT_V: Param([1.6, 1.83], [list, float, int], live=True, depends_on=ENABLE_INDI_BREAKPOINTS)
    * INDI_ACTUATOR_EFFECTIVENESS_BP: Param([0, 24], [list, float, int], live=True, depends_on=ENABLE_INDI_BREAKPOINTS)
    * INDI_ACTUATOR_EFFECTIVENESS_V: Param([2, 3], [list, float, int], live=True, depends_on=ENABLE_INDI_BREAKPOINTS)
    * ENABLE_MULTI_INDI_BREAKPOINTS: Param(False, bool, live=True, depends_on=SHOW_INDI_PARAMS)
    * INDI_INNER_GAIN_BP_MULTI: Param([[0, 10], [20, 24, 30]], [list, float, int], live=True, depends_on=ENABLE_MULTI_INDI_BREAKPOINTS)
    * INDI_INNER_GAIN_V_MULTI: Param([[5.5, 6, 7.5], [7.25, 7.5, 9]], [list, float, int], live=True, depends_on=ENABLE_MULTI_INDI_BREAKPOINTS)
    * INDI_OUTER_GAIN_BP_MULTI: Param([[0, 10], [20, 24, 30]], [list, float, int], live=True, depends_on=ENABLE_MULTI_INDI_BREAKPOINTS)
    * INDI_OUTER_GAIN_V_MULTI: Param([[5, 5.75], [6, 7.25, 7.5]], [list, float, int], live=True, depends_on=ENABLE_MULTI_INDI_BREAKPOINTS)
    * INDI_TIME_CONSTANT_BP_MULTI: Param([[0, 10], [20, 24, 30]], [list, float, int], live=True, depends_on=ENABLE_MULTI_INDI_BREAKPOINTS)
    * INDI_TIME_CONSTANT_V_MULTI: Param([[1, 1.25], [2.2, 2.5]], [list, float, int], live=True, depends_on=ENABLE_MULTI_INDI_BREAKPOINTS)
    * INDI_ACTUATOR_EFFECTIVENESS_BP_MULTI: Param([[0, 10], [20, 24, 30]], [list, float, int], live=True, depends_on=ENABLE_MULTI_INDI_BREAKPOINTS)
    * INDI_ACTUATOR_EFFECTIVENESS_V_MULTI: Param([[1.25, 1.5], [2, 3]], [list, float, int], live=True, depends_on=ENABLE_MULTI_INDI_BREAKPOINTS)
    * INDI_MULTI_BREAKPOINT_SOURCE: Param(['desired_steer_abs', 'vego'], [list, str], live=True, depends_on=ENABLE_MULTI_INDI_BREAKPOINTS)
    * ENABLE_UNSAFE_STEERING_RATE_SELFDRIVE: Param(False, bool, depends_on=ENABLE_UNSAFE_STEERING_RATE, description='Toyota only.\nThis is HIGHLY unsafe, '
    * 'a_cruise_max_v_following': Param([1.6, 1.6, 0.65, .4], [list, float], live=True, depends_on=ENABLE_PLNR_ACCEL_LIMITS)
    * ENABLE_STEER_RATE_COST: Param(False, [bool], live=True, depends_on=ENABLE_PLANNER_PARAMS, description='Technically live but treat it like it\'s not.')
    * STEER_RATE_COST: Param(1., VT.number, live=True, depends_on=ENABLE_STEER_RATE_COST)
  * Commits:
    * fix(toyota): unsafe steer delta is now correct in selfdrive
    * feat(params): add steer rate cost to live params
    * fix(py): log when lat mpc resets
    * refactor(toyota): refactor steer delta params to be methods
    * refactor(chrysler): update steer limit params to match toyota's
    * fix(planner): fix steer rate cost condition logic
    * fix(planner): use member variable for steer rate cost
    * fix(py): add self to method in path planner
    * fix(py): add CP to update params in path planner
    * fix(params): made steer rate selfdrive depend on unsafe steer rate
    * feat(params): add accel hyst gap breakpoints
    * fix(toyota): apply correct limit to acc type
    * refactor(params): refactor indi params for multi breakpoints
    * fix(py): use multi key for actuactor effectiveness
    * feat(params): add first attempt at multi indi breakpoints
    * feat(params): definie initial inner gain multi break point
    * fix(py): fix type in array syntax
    * test(params): add basic test for multi breakpoint correctness
    * debug(params): print multi-bp array in tests
    * fix(py): fix invalid syntax in print statement
    * test(params): properly test multi-bp correctness
    * fix(params): fix multi-bp to pass initial correctness test
    * test(params): update multi-bp correctness test by testing single items
    * refactor(params): rename eval_breakpoint_type to eval_breakpoint_source
    * refactor(params): use contant keys for break point sources and param modifiers
    * test(params): add correct test for multi-bp when evaluating bp source
    * test(params): add multi-bp tests with short and no steer bp
    * test(params): properly check when first breakpoint source is missing
    * test(params): partially passing missing second breakpoint source test
    * test(params): completely passing missing second bp source test
    * test(params): passing correctness test for multi-bp short v
    * refactor(params): move interp_multi_bp to opParams from debug multi-bp file
    * test(params): partially passing multi-bp fuzzing
    * test(params): fuzz multi-bp for proper steer set, extra vego
    * test(params): fuzz multi-bp for proper steer set, normal vego (no set)
    * test(params): proper fuzz multi-bp for missing second source and flat array
    * test(params): fuzz multi-bp for extra args in break point sets
    * test(params): fuzz multi-bp for extra value set
    * test(params): fuzz multi-bp missing one steer
    * test(params): fuzz multi-bp for normal first source breakpoints (no set)
    * refactor(tests): replace other multi-bp tests with fuzzing test
    * feat(params): support multi dimensional lists in op edit
    * feat(indi): implement multi-bp in indi controller
    * feat(indi): update default multi-bp values
    * fix(toyota): use CS.out for vEgo in car controller
    * test(params): fuzz multi-bp for errors, fix index out of range
    * fix(params): fix op edit to save lists of lists properly
    * docs(readme): update readme with fork features and multi bp examples
    * docs(readme): add multi-bp eval example
    * feat(params): add multi-bp to steer actuator delay
    * docs(readme): update readme with multi-bp sources and modifiers
    * docs(readme): update readme with UI changes
    * docs(readme): add final multi bp thoughts and fix typos
    * docs(readme): use complete installation command
    * docs(readme): add my favorite multi bp tune to readme

Version 42
========================
  * Commits:
    * feat(actions): only push out release if build release works

Version 41
========================
  * New OP Params:
    * TOYOTA_PERMIT_BRAKING: Param(1, [1, 0, 'lead'], live=True, depends_on=ENABLE_TOYOTA_ACCEL_PARAMS)
    * ENABLE_PLANNER_PARAMS: Param(False, [bool], live=True)
    * ENABLE_PLNR_ACCEL_LIMITS: Param(False, [bool], live=True, depends_on=ENABLE_PLANNER_PARAMS)
    * 'a_cruise_min_bp': Param([0., 5.,  10., 20.,  40.], [list, float], live=True, depends_on=ENABLE_PLNR_ACCEL_LIMITS)
    * 'a_cruise_min_v': Param([-1.0, -.8, -.67, -.5, -.30], [list, float], live=True, depends_on=ENABLE_PLNR_ACCEL_LIMITS)
    * 'a_cruise_min_v_following': Param([-1.0, -.8, -.67, -.5, -.30], [list, float], live=True, depends_on=ENABLE_PLNR_ACCEL_LIMITS)
    * 'a_cruise_max_bp': Param([0.,  6.4, 22.5, 40.], [list, float], live=True, depends_on=ENABLE_PLNR_ACCEL_LIMITS)
    * 'a_cruise_max_v': Param([1.2, 1.2, 0.65, .4], [list, float], live=True, depends_on=ENABLE_PLNR_ACCEL_LIMITS)
    * 'a_cruise_max_v_following': Param([1.6, 1.6, 0.65, .4], [list, float], live=True, depends_on=ENABLE_PLNR_ACCEL_LIMITS)
  * Commits:
    * feat(params): add param to toggle planner params

Version 40
========================
  * Commits:
    * feat(version): update dirty tag to be based on my fork
    * feat(events): don't show startup event when on r2++
    * refactor(sentry): move sentry from crash and tombstone into sentryd
    * fix(sentry): pass args and kwargs to client
    * fix(sentry): track discord username before dongle id

Version 39
========================
  * Commits:
    * hotfix(actions): add missing 's' when checking for main branch
    * hotifx(docker): add new line to op fat docker file
    * chore(actions): remove unused sim tests workflow
    * feat(github): update issue templates for new labels
    * feat(actions): add workflow to clean up old ci branches
    * feat(actions): check for error when deleting branch
    * fix(actions): properly get branch name sub string
    * feat(actions): log which branches are found
    * fix(actions): get correct length, set correct ref, and check correct status code
    * feat(actions): limit branch clean up to src branch

Version 38
========================
  * Commits:
    * feat(actions): publish my own docker image to github
    * feat(actions): remove old build workflow and don't rebuild for markdown changes
    * refactor(actions): replace broken step with basic log step in setup_workflow
    * feat(actions): check for main branch using setup_workflow
    * feat(actions): update docker jobs to use setup outputs
    * feat(actions): update docker_push_prebuilt with setup_workflow vars
    * feat(actions): pull ci docker #file when not on main branch
    * feat(docker): update ci image to use my base image
    * refactor(actions): refactor setup_workflow to be more DRY
    * feat(actions): update all jobs to use docker_build command
    * feat(docker): create fat docker image containing the dev env & repo
    * feat(actions): update jobs with dynamic docker run command
    * refactor(actions): extract shared items into base docker run command
    * fix(tools): fix tools unit test for new docker env
    * fix(docker): make sure op_edit is included in fat image
    * fix(params): ignore bare except in op_edit

Version 37
========================
  * New OP Params:
    * DISABLED_PROCESSES: Param(None, [str, list, type(None)], description='You\'re on your own here', depends_on=ENABLE_MANAGER_PARAMS)
    * ENABLE_TOYOTA_CAN_PARAMS: Param(False, [bool], live=True, depends_on=SHOW_TOYOTA_OPTS)
    * ENABLE_TOYOTA_ACCEL_PARAMS: Param(False, [bool], live=True, depends_on=ENABLE_TOYOTA_CAN_PARAMS)
    * TOYOTA_ACC_TYPE: Param(1, [int], live=True, depends_on=ENABLE_TOYOTA_ACCEL_PARAMS)
    * TOYOTA_PERMIT_BRAKING: Param(1, [1, 0, 'lead'], live=True, depends_on=ENABLE_TOYOTA_ACCEL_PARAMS)
  * Commits:
    * feat(params): update op params with toyota specific can params
    * feat(toyota): update car controller to allow can message modification
    * fix(params): fix op edit to cast default values to str
    * tests(processes): update process replay refs for can-tuning

Version 36
========================
  * Commits:
    * Make the DSP work everywhere (#2621)
    * Added 2020 Honda HRV (#2643)
    * Error checking macros for opencl (#2615)
    * simplify building capnp messages with arrays (#2617)
    * Add missing engine f/w for CAR.RAV4H_TSS2 (#2653)
    * bump version to 0.8.1
    * remove ui sidebar hint (#2662)
    * more margin
    * add user agent to installer
    * move that to two init
    * add wifi to setup (#2604)
    * qt setup keyboard (#2663)
    * fix setup installer download
    * Offroad alerts (#2664)
    * small UI improvements (#2669)
    * setup rest of installers
    * Updated README to include 2020-2021 Honda Civic Hatchback (#2659)
    * Add CAR.RAV4H_TSS2 engine fw (#2670)
    * Move thermald hardware calls into HW abstraction layer (#2630)
    * tici timing improvements (#2613)
    * raw pred api (#2611)
    * set camera and gpu irq affinities (#2678)
    * Qt offroad home screen (#2672)
    * bump panda
    * bump cereal
    * Add event for commIssueWarning
    * fix typo in event name
    * Set correct HW type in initData (#2685)
    * Don't re-init pigeon while offroad (#2687)
    * bump cereal: add minSpeedCan
    * 2021 RX fw (#2683)
    * Add 2021 Lexus RX
    * use name
    * simplify common_camera_process_front (#2470)
    * bump opendbc
    * Parametrize MIN_CAN_SPEED in car interfaces (#2684)
    * Add y offset to video (#2694)
    * set y offset to zero for now
    * move offroad alerts to home screen (#2681)
    * fix fille lead (#2703)
    * Tethering (#2676)
    * Add fingerprint for EU 2019 Civic Hatch (#2698)
    * Rav4 Hybrid engine FW
    * 2021 Australia Rav4 hybrid FW (#2712)
    * Lexus IS firmware
    * save calibration as JSON again
    * UI style improvements with improved keyboard (#2710)
    * small cleanup (#2715)
    * dont init wifi widget if there is no adapter
    * too wide
    * 2021 Rav4 LE Engine FW
    * make fingerprint script nice
    * remove raw logger (#2719)
    * 2017 Civic Bosch engine fw
    * Fix random encoder lockups (#2707)
    * log DSP execution time (#2723)
    * reliability? (#2722)
    * Revert simplify
    * Added model_replay and fixed some bugs in camera_replay (#2679)
    * fix camerad exiting on pc
    * add modelV2 to model replay (#2725)
    * Update Hyundai firmware in values.py for 2021 Sonata (#2714)
    * Update Sonata year in readme
    * Add fingerprint for 2019 Acura ILX (#2724)
    * add two dev packages for training
    * road camera malfunction alert (#2697)
    * make qcom2 robust to moving v4l-subdevs
    * Revert add two dev packages for training
    * Test model refactor (#2720)
    * Add label if no network manager is found (#2718)
    * Dynamically colored alert widget.  (#2717)
    * WiFI UI show IP (#2735)
    * More Rav4 fw
    * rhd dm AE sign flip
    * destroy rgb_to_yuv_state (#2702)
    * camerad: fix memory leak in create_thumbnail (#2743)
    * Add thumbnails to camera_frame_stream
    * clutil refactor (#2733)
    * bump panda: nissan altima support
    * bump cereal: add stoppingBrakeRate
    * Parametrize stoppingBrakeRate (#2745)
    * increase startup timeout for camera malfunction
    * add LOGW
    * transform.h: remove extern C  (#2755)
    * better debug msg for fw fingerprinting test
    * more robust fingerprint test
    * Revert More Rav4 fw
    * oneplus deprecation (#2748)
    * fix camerad not exiting cleanly (#2768)
    * covert rgb_to_yuv.c to rgb_to_yuv.cc (#2757)
    * convert loadyuv.c to loadyuv.cc (#2754)
    * adb over smays
    * model timing benchmark script
    * mask off cores 2-3 from RPS (#2692)
    * output clang compile database with test build
    * fix aarch64 build
    * paint.cc: fix y offset
    * add optional margin to car_space_to_full_frame check
    * Updated FW values for honda civic  (#2752)
    * hardware.py: get network info over dbus (#2727)
    * Handle python-dbus not installed
    * set CarState.steeringRateLimited for Hyundai (#19495)
    * log remote and branch in sentry (#16766)
    * remove fsck logging in updated
    * add oneplus deprection to release notes
    * Set camerad CL priority to 4 (#2747)
    * refactor imgproc/utils (#2766)
    * Thneed refactors for future functions (#2673)
    * qcom2 init hevc tier correctly (#19496)
    * camera_qcom: read SensorEvents in op thread  (#2764)
    * Qt system reset (#19502)
    * fix camerad qcom2 build
    * paint.cc: lower y offset
    * cleanup camera malfunction alert (#2751)
    * fix camera malfunction ui timeout
    * factory reset -> system reset
    * qcom: make camera_process_frame more readable (#2765)
    * Rav4 2021 fw (#19514)
    * Set GPU priorities + improved modeld priorities (#2691)
    * 2021 Toyota Highlander / Highlander Hybrid fw (#2729)
    * Revert Handle python-dbus not installed
    * Early model 081 (#19510)
    * athenad: add getNetworkType (#19517)
    * Add Forester 2020 fingerprint (#2763)
    * bump cereal: add startingBrakeRate
    * Fix to allow brakes to release on resume press (#2709)
    * Rav4 and Rav4 Hybrid FW (#19501)
    * remove per-branch build caching for CI builds
    * 2020 RDX fw (#19523)
    * Parametrize startingBrakeRate (#19511)
    * fixed fingerprint for cpu usage test
    * don't wait for 4 seconds before it starts steering again after steering fault (#19520)
    * Fix TSS2 creep issue, no need to send standstill request (#2716)
    * new ref
    * 0b6e45f8-21c1-408a-b61d-3dce02a69d23/500 (#19528)
    * already prepped
    * HW abstraction layer (#19530)
    * Move MCLK freq on tici (#19494)
    * Revert MCLK change
    * Separate Hyundai Ioniq Hybrid and EV 2020 Premium SE (#19500)
    * cleanup qcom2 (#19506)
    * manager cleanup (#2634)
    * bump cereal
    * disable updater for oneplus EONs
    * fix supported years on Ioniq Electric
    * bump cereal
    * remove commIssueWarning from events
    * Car Port: 2021 Toyota Camry (TSS 2.5) (#2721)
    * update release notes
    * increase controls alert timeout
    * fix unkillable reboot logging on tici
    * remove simg2img from external
    * Add toyota creep to release notes
    * agnos updater (#2600)
    * Only register when needed (#19526)
    * Qt Offroad stats (#19498)
    * Add exception handlers to dbus network stats
    * Add timeout to dbus calls
    * chore(git): update submodules to 0.8.1
    * Merge branch 'src' into update-0.8.1
    * Merge branch 'src' into update-0.8.1
    * chore(git): bump cereal submodule
    * fix(py): fix indentation in longcontrol
    * fix(py): fix hardware import statement
    * fix(py): fix hardware import; fix stopping rate
    * fix(py): fix pandad imports after 0.8.1
    * tests(processes): update process replay refs for update-0.8.1
    * Merge branch 'src' into update-0.8.1

Version 35
========================
  * Commits:
    * fix(toyota): update default corolla tss2 indi tune

Version 34
========================
  * New OP Params:
    * COROLLA_BODY_TYPE: Param('hatchback', ['sedan', 'hatchback'], depends_on=SHOW_TOYOTA_OPTS)
    * ENABLE_MANAGER_PARAMS: Param(False, [bool], depends_on=SHOW_UNSAFE_OPTS)
    * DISABLED_PROCESSES: Param(None, [str, list, type(None)], description='You\'re on your own here', depends_on=ENABLE_MANAGER_PARAMS)
  * Commits:
    * feat(params): add param to disable processes
    * feat(mngr): update manager to start allowed processes
    * fix(params): only check list default if not none
    * fix(params): only check if not default
    * fix(params): allow op_edit to handle none as list default

Version 33
========================
  * Commits:
    * tests(numpy): add more tests for interp when array lens varry
    * fix(numpy): make interp work when fp is shorter
    * fix(numpy): possible fix for when xp is shorter
    * tests(numpy): add more test cases for when bp is shorter
    * fix(numpy): properly return last value when xp has reached the end
    * tests(numpy): add more test cases for when v is shorter
    * tests(numpy): add test case for xp containing values not in x
    * refactor(numpy): move calc_interp function back into get_interp

Version 32
========================
  * Commits:
    * 0b6e45f8-21c1-408a-b61d-3dce02a69d23/500 (#19528)

Version 31
========================
  * Commits:
    * Early model 081 (#19510)

Version 30
========================
  * Commits:
    * Revert fix(ui): remove engine rpm from ui

Version 29
========================
  * New OP Params:
    * 'corolla_use_indi': Param(False, bool, depends_on=SHOW_TOYOTA_OPTS)
    * 'accel_hyst_gap': Param(0.02, VT.number, live=True, depends_on=SHOW_TOYOTA_OPTS)
    * ENABLE_START_STOP_PARAMS: Param(False, bool, live=True, depends_on=ENABLE_LONG_PARAMS)
    * STOP_BRAKE_RATE_BP: Param([0], [list, float, int], live=True, depends_on=ENABLE_START_STOP_PARAMS)
    * STOP_BRAKE_RATE_V: Param([0.2], [list, float, int], live=True, depends_on=ENABLE_START_STOP_PARAMS)
    * START_BRAKE_RATE_BP: Param([0], [list, float, int], live=True, depends_on=ENABLE_START_STOP_PARAMS)
    * START_BRAKE_RATE_V: Param([0.8], [list, float, int], live=True, depends_on=ENABLE_START_STOP_PARAMS)
    * SHOW_TOYOTA_OPTS: Param(False, [bool], live=True, description='Shows options toyota cars.')
    * COROLLA_BODY_TYPE: Param('hatchback', ['sedan', 'hatchback'], depends_on=SHOW_TOYOTA_OPTS)
  * Commits:
    * fix(toyota): set the correct wheelbase for corolla
    * feat(params): add starting / stopping rate to op params
    * fix(toyota): fix tss2 brake creep, thanks to @briskspirit
    * fix(toyota): made briskspirit braking optional
    * refactor(params): made starting and stopping brake rates into breakpoints
    * fix(toyota): set old corolla wheelbase by default
    * fix(toyota): fix tss2 double braking
    * fix(toyota): apply briskspirit braking by default
    * fix(py): remove unused imports

Version 28
========================
  * Commits:
    * feat(ui): add dev ui to 0.8
    * fix(ui): remove liveMpc info from ui
    * fix(ui): remove engine rpm from ui
    * fix(release): make sure to include dashcam.h in release files
    * feat(toyota): record engine rpm into car state
    * tests(processes): update process replay refs for dev-ui

Version 27
========================
  * Commits:
    * bump version to 0.7.10
    * UI: refactor light sensor (#2129)
    * Fix MacOS CI (#2145)
    * radard profiling (#2265)
    * radard cleanup (#2266)
    * CI: Add valgrind (#2245)
    * LSM6DS3 (#2268)
    * Reduced wheel touch time (#2259)
    * transient considerations (#2276)
    * eliminate round-trip reading entire file (#2275)
    * bump cereal
    * Fix calibration invalid alert on startup (#2270)
    * paramsd profiling
    * don't want to profile that
    * write car params before profiling
    * fix not going onroad on clean dashcam install (#2280)
    * Update radard cpu usage
    * bump cereal
    * bump cereal
    * loggerd does not need to babysit this
    * report git branch to testing closet
    * add offroad to cpu usage script
    * cleanup duplicate function
    * remove green temp processes (#2286)
    * fix style inconsistencies in release notes (#2284)
    * add check for partial response code (#2282)
    * Present alert if fan isn't spinning (#2258)
    * Fix gyro field name
    * don't run jenkins on testing closet branches
    * fix loggerd rotate (#2291)
    * Use math instead of numpy for calculating TTC, on average 80% faster (#2293)
    * update sonata fingerprint
    * Add sonata engine FW
    * Upgrade to SNPE 1.41.0 (#2285)
    * UI cleanup + startup time improvement (#2295)
    * boardd always send can packet (#2307)
    * Fix dcamera inaccurate fps on OP3T and LP3 (#2305)
    * add acura rdx test route
    * remove unused img
    * add timeout to modeld replay
    * tici camera art II (#2223)
    * Test camerad in CI (#2297)
    * improve profiler
    * 2018 Lexus RX 350 engine fw (#2306)
    * Add Sienna engine fw
    * more accurate profiling (#2287)
    * RAV4TSS2: Additional fw (#2317)
    * bump opendbc
    * fix webcam build error (#2320)
    * Process replay for C++ daemons (#2288)
    * fix building modeld on pc (#2313)
    * Update README.md (#2299)
    * Try only extracting python folder (#2321)
    * white/grey/black pandas still have power ctrl function (#2308)
    * build sim container with available cores
    * Build sim container once an hour
    * Update 2020 Hyundai Palisade FW versions (#2322)
    * Startup speedup: scons decider (#2309)
    * remove hotspot exceptions in uploader (#2319)
    * Add Nissan Leaf 2020 (#2311)
    * Speedup android permissions (#2331)
    * add caching to CI tests (#2269)
    * remove on status
    * Remove czmq part 1 (#2332)
    * Params refactor, simplified (#2300)
    * Fix typo in README
    * change macos cache policy and fix typo
    * Fix lane change when blinker is turned off early (#2324)
    * don't show giraffe alert with relay (#2335)
    * Add more Rav4 fw
    * was supposed to be on branch
    * fix params permissions after refactor
    * Nissan Rogue 2018 (#2336)
    * fix params on PC and when reading path from env (#2340)
    * set default path for put_nonblocking helper
    * clear irrelevant alerts on state transition (#2318)
    * 2021 Rav4 confirmed working
    * Alert cleanup (#2274)
    * HKG fixups (#2342)
    * Params path only in one place (#2344)
    * fix encoder build
    * script to add ssh keys
    * Fix macOS CI (#2345)
    * Add logs for why start was blocked (#2312) (#2346)
    * Jenkins: 1 hour pipeline timeout
    * tici: set brightness in std::async (#2347)
    * tici: reboot
    * fix order of cpuset adjustments on launch
    * revert apk launch thread
    * More macOS CI fixes (#2352)
    * 2019 Sonata not standard with SCC
    * Add Ridgeline 2020 camera fw
    * Build openpilot with webcam support in CI (#2070)
    * 2020 Ridgeline fw
    * Clean up and test camerad refactor (#2310)
    * fix build warnings (#2355)
    * --std=c++17 (#2330)
    * fix params permissions for offroad (#2356)
    * Fingerprint for 2021 RAV4H XLE (#2357)
    * need that one too
    * The correct (factory) way of displaying barriers on toyotas (#2281)
    * quick toyota EPS scale factor script
    * fix pylint import error
    * NEOS 15 (#2084)
    * Add 2020 Acura RDX (#1557)
    * tap to wake with accelerometer (#2267)
    * update release notes
    * use iterator to loop over first 1000 entries (#2359)
    * fix typo in params path on PC
    * Reset liveParameters if starting with invalid values (#2360)
    * no CI on testing closet branches
    * explicitly turn display on in updater (#2362)
    * add cars with LQR and INDI lat control to process replay (#2363)
    * 0.7.10 release notes
    * fix build warning (#2365)
    * numpy tolerance for INDI
    * matrix subclass not recommended way to represent matrices (#2348)
    * UI: get video aspect ratio from camera intrinsics (#2351)
    * store params in ~/.comma on PC (#2369)
    * prevent snapshot while onroad (#2366)
    * don't fail CI if artifacts don't upload
    * std::async has nodiscard in 20.04, i believe that function won't return until the async completes
    * support for halve in Window
    * camerad AE hotfix (#2371)
    * infinite sound (#2372)
    * Log last 1000 lines of tmux output in bootlog (#2149)
    * NEOS: expose kernel workqueues over sysfs (#2375)
    * update total scons nodes
    * add error handling to pandad get signature
    * update release notes
    * Add SNPE update to release notes
    * only log startup blocked on conditions changed (#2382)
    * improve  Qt ui smoothess (#2380)
    * pyenv version file
    * improve update_requirements.sh
    * make scons work immediately after install
    * simplify settings a bit (#2384)
    * Rav4 Hybrid 2020 fw
    * Car Port: Prius 2021 TSS2 (#2163)
    * camera malfunction alert (#2391)
    * remove unused params function
    * Add 2018 Lexus IS 350 fw
    * update update_requirements.sh
    * bump version to 0.7.11
    * bump c++ version for index_log
    * fix camera malfunction alert in sim
    * Add 2019 Highlander Hybrid (#2412)
    * restore behavior (#2418)
    * fix cpu test thresholds after downclock
    * Additional CAR.CAMRY f/w (#2422)
    * fix camera malfunction alert on startup
    * enable event processing in UI
    * grey panda deprecation (#2406)
    * sbigmodel, a bigmodel with the size of a smallmodel
    * update release notes
    * update date
    * stop sounds after going offroad
    * Update README.md
    * neos 15-1 (#2430)
    * external cleanup (#2434)
    * bump opendbc
    * get rid of rest of czmq
    * Abstract set_unsafe_mode function to Panda (#2431)
    * Add 2018 China Honda Inspire Fingerprint (#2437)
    * Fix mac CI (#2439)
    * Hyundai Veloster fingerprint (#2407)
    * Hyundai Genesis tuning (#2405)
    * move Inspire to be alphabetical
    * update GMC Acadia requirements
    * Car Port: 2020 Kia Niro EV (#2416)
    * add kia nero to release notes
    * fix niro spelling
    * just use the same (#2419)
    * bump opendbc
    * Allow Hyundai Santa Fe to use 384 STEER_MAX (#2411)
    * Kona EV 2020 fingerprint (#2444)
    * fix fingerprint script
    * ubuntu 16.04 -> 20.04 (#2378)
    * webcam cleanup: remove unused variables (#2450)
    * Rav4 Hybrid 2021 confirmed working
    * fix manager crash when sending signal to a dead proc
    * Veloster torque increase (#2457)
    * Qt offroad (#2451)
    * Car bug fix: 2020 Kia Niro EV orange lanes icon and LKAS error on cluster display (#2454)
    * big button
    * add blosc to pipfile (#2464)
    * Qt onboarding (#2465)
    * qt settings touchups
    * lower volume
    * RAV4 Hybrid 2019 Fingerprint (#2472)
    * add sonata 2020 Korean version fingerprint (#2449)
    * new laika
    * bump laika
    * Focus Actuator Comments (#2478)
    * add lexus ES hybrid fw
    * bump laika
    * Car Port: Lexus NX300  (#2481)
    * Add HRV fw
    * update process replay test routes (#2482)
    * switch build flags to use opengl framework rather than gl library for OSX (#2467)
    * grey panda is unsupported (#2458)
    * check for safety mode mismatch (#2443)
    * qt cleanup (#2476)
    * qt sound cleanup
    * set y too (#2448)
    * generalize camera assumptions (#2423)
    * add kia optima fingerprint
    * trim trailing whitespace
    * hyundai cleanup (#2486)
    * pin blosc version
    * Revert pin blosc version
    * pin blosc (#2492)
    * remove wrong fw version from genesis g70
    * Genesis G70 fingerprint and tuning (#2491)
    * Qt text window (#2489)
    * works on 2020 Lexus ES
    * Works on Camry Hybrid 2020
    * Qt spinner (#2494)
    * pytorch cuda 11.0 (#2496)
    * Revert pytorch cuda 11.0 (#2496) (didn't work!)
    * No uncertain ll (#2495)
    * params_pyx_setup.py: -std=c++17 (#2503)
    * don't show unspported alert with no health packet
    * give loggerd min rt priority
    * remove old loggerd priority
    * some laneplanner updates (#2505)
    * convert mat.h to a c++ header file (#2499)
    * fsync_dir: remove goto (#2498)
    * Revert convert mat.h to a c++ header file (#2499)
    * ui.py: fix transform
    * Corolla 2021
    * bump panda
    * cleanup planner (#2519)
    * Fix lane width (#2520)
    * paint.cc: fix drawing lane lines on sidebar
    * Scons builder for cython extensions (#2485)
    * use different SubMasters for driverState/sensorEvents (#2522)
    * continued: Update DM awareness times (#2527)
    * Torch model (#2452)
    * a new dawn
    * update panda in sim (#2528)
    * cut-in detection
    * update comments
    * remove std::clamp (#2530)
    * Qt setup + installer (#2511)
    * Simple improvements for quality gate (#2517)
    * Add fingerprint for european/nordic Hyundai Kona EV 2019 (#2515)
    * new laika
    * only qcom
    * Tici Focal (#2459)
    * use enabled flag from controlsState instead of carState (#2518)
    * larch64 spinner
    * larch64 text window
    * improve onboarding (#2537)
    * 2020 RDX comes standard with AcuraWatch
    * 2019 Camry fw
    * stop pc from spamming logs (#2544)
    * Add 2017 Lexus IS 350 (#2553)
    * cpu usage test debug print
    * remove old lib
    * fix setup for new weston build
    * add onnx and bump versions in Pipfile.lock
    * ./compile_torch.py 5034ac8b-5703-4a49-948b-11c064d10880/780 b5e5c420-7042-4d0c-92e5-770eb09936a5/800 with skip connection in temporal summarizer
    * nicer spinner
    * update model refs
    * fix spinner and text diff
    * Update Simulator-Related READMEs with links to /wiki/CARLA (#2557)
    * bump laika
    * Reduce Kp/Ki by 30% to eliminate steer oscillation (#1985)
    * tici has a real /tmp
    * sometimes never goes into the loop
    * was wasting a ton of GPU on this debayer (#2566)
    * Minor fixes 08 (#2565)
    * Add sonata firmware version
    * clear both possible places for the scons cache
    * CAR.RAV4_TSS2 added engine & EPS f/w (#2570)
    * update simulator to ubuntu 20.04 (#2463)
    * send frame in packet on demand (#2567)
    * remove duplicate enc_idx logging (#2562)
    * upgrade pip
    * update waste for variable cores
    * underflew
    * replay assume segment number
    * QT UI: Wifi chooser (#2062)
    * Tombstoned check crashlog permissions (#2576)
    * Qt ui: only stop repeat sounds (#2577)
    * Upgrade pip in ubuntu setup (#2573)
    * preinit locationd filter (#2569)
    * bump cereal
    * tici front/wide encodeIdx msgs (#2564)
    * model replay improvements (#2580)
    * fix frame drop percentage (#2578)
    * Stricter check on date for RTC time sync (#2582)
    * use HARDWARE.reboot() when unkillable process doesnt stop
    * Qt ui: turn off screen after inactivity (#2583)
    * Qt keyboard (#2381)
    * reproduce dmon lag
    * repros better with cache clears
    * simpler repro, no vector required
    * other includes to build repro on pc
    * simpler repro for dmon lag issue
    * fix some lack of cache awareness in yuvframe2tensor
    * Improve on-screen keyboard (#2587)
    * log DM model execution time (#2589)
    * waste can become memory bound
    * fix lexus is fw fingerprinting
    * should be seconds
    * waste prints memory bandwidth
    * do the average correctly in waste
    * New settings for governors, +30% memory bandwidth (#2590)
    * fix small terms (#2593)
    * Qt wifi cleanup (#2594)
    * no spinner if not main
    * update frame drop filter (#2592)
    * Fix Wifi UI not working on PC (#2597)
    * don't need this anymore
    * Revert don't need this anymore, need to fix cereal first
    * new wifi strength icon (#2601)
    * Add Genesis G80 to special panda safety mode (#2602)
    * genesis g80 test route
    * Qt setup improvements (#2591)
    * fix loggerd unittest
    * show os version in qt settings
    * remove g80 from non tested cars list
    * put hash in version (#2607)
    * Add missing EPS f/w for CAR.COROLLA_TSS2 (#2609)
    * model lag warning (#2608)
    * Make next and prev buttons (#2598)
    * move mdss irq to core 1
    * Prerotate dmonitoringmodeld input (#2606)
    * More governance work, fix thneed (#2610)
    * Added missing engine f/w for 2021 RAV4 XLE (ICE) (#2612)
    * set GPU perf governor
    * give the model GPU context highest priority
    * mask out the priority
    * qt ui: dont resize window on start
    * Qt ui: fix onboarding
    * Qt ui: make sure ui_state is initialzed to 0
    * remove model lag warning, leave red alert at 20
    * fix release version tag
    * add release date
    * fix double awk
    * Update RELEASES.md
    * two spaces
    * ugh, this was using half the CI device's storage
    * 2019 Hyundai Santa Fe fixes (#2490)
    * Qt cleanup (#2622)
    * Typing experiments (#1633)
    * don't need that
    * new and improved text window
    * stacked widget
    * small onboarding cleanup
    * add back run on status
    * On status still triggers recursive builds
    * didn't build on device
    * Wifi improvements (#2618)
    * update contributing doc
    * bump cereal
    * bump cereal again
    * pad vlayout (#2626)
    * add legacy reset line support (#2625)
    * wider keyboard (#2629)
    * bump opendbc + scons cleanup
    * fix release build
    * close spinner when manager fails to start
    * remove check on frame drop in modeld (#2638)
    * Qt ui: improve toggle buttons (#2639)
    * quick toggles cleanup
    * no gl inside nvg frame
    * small calibration refactor + tests (#2641)
    * Fix toyota_eps_factor.py script (#2647)
    * Merge branch 'src' into update-0.8.0
    * chore(git): update submodules to v0.8 master
    * chore(git): merge submodules src into 0.8
    * chore(actions): update actions to run on ubuntu 20.04
    * fix(uploader): deal with merge conflict in uploader
    * chore(git): update gitignore to not ignore snpe dsp files
    * chore(git): update panda submodule for 0.8.0 hotfixes
    * Merge branch 'src' into update-0.8.0
    * chore(git): update git ignores to not ignore placeholder files
    * fix(panda): create panda obj dir if not exists
    * tests(processes): update process replay refs for update-0.8.0
    * fix(params): op_edit shouldn't check type name when there aren't default types
    * fix(params): don't trim param list if it's longer than param

Version 26
========================
  * New OP Params:
    * self.fork_params = {CAM_OFFSET: Param(0.06, VT.number, 'Your camera offset to use in lane_planner.py', live=True)
    * 'indi_inner_gain': Param(9.0, VT.number, live=True, depends_on=SHOW_INDI_PARAMS)
    * 'indi_outer_gain': Param(8.9, VT.number, live=True, depends_on=SHOW_INDI_PARAMS)
    * 'indi_time_constant': Param(5.5, VT.number, live=True, depends_on=SHOW_INDI_PARAMS)
    * 'indi_actuator_effectiveness': Param(9.0, VT.number, live=True, depends_on=SHOW_INDI_PARAMS)
    * SHOW_ACTUATOR_DELAY_PARAMS: Param(False, bool, live=True, depends_on=ENABLE_LAT_PARAMS)
    * STEER_ACTUATOR_DELAY: Param(0.60, VT.number, live=True, depends_on=SHOW_ACTUATOR_DELAY_PARAMS)
    * ENABLE_ACTUATOR_DELAY_BPS: Param(False, bool, live=True, depends_on=SHOW_ACTUATOR_DELAY_PARAMS)
    * STEER_ACTUATOR_DELAY_BP: Param([0.], [list, float, int], live=True, depends_on=ENABLE_ACTUATOR_DELAY_BPS)
    * STEER_ACTUATOR_DELAY_V: Param([0.6], [list, float, int], live=True, depends_on=ENABLE_ACTUATOR_DELAY_BPS)
    * ENABLE_COASTING: Param(False, bool, 'When true the car will try to coast down hills instead of braking.', live=True, depends_on=SHOW_EXPERIMENTAL_OPTS)
    * ENABLE_LONG_PID_PARAMS: Param(False, bool, live=True, depends_on=ENABLE_LONG_PARAMS)
    * LONG_PID_KP_BP: Param([0., 5., 35.], [list, float, int], live=True, depends_on=ENABLE_LONG_PID_PARAMS)
    * LONG_PID_KP_V: Param([3.6, 2.4, 1.5], [list, float, int], live=True, depends_on=ENABLE_LONG_PID_PARAMS)
    * LONG_PID_KI_BP: Param([0., 35.], [list, float, int], live=True, depends_on=ENABLE_LONG_PID_PARAMS)
    * LONG_PID_KI_V: Param([0.54, 0.36], [list, float, int], live=True, depends_on=ENABLE_LONG_PID_PARAMS)
    * LONG_PID_KF: Param(1., VT.number, live=True, depends_on=ENABLE_LONG_PID_PARAMS)
    * LONG_PID_SAT_LIMIT: Param(0.8, VT.number, live=True, depends_on=ENABLE_LONG_PID_PARAMS)
    * ENABLE_LONG_DEADZONE_PARAMS: Param(False, bool, live=True, depends_on=ENABLE_LONG_PARAMS)
    * LONG_DEADZONE_BP: Param([0., 9.], [list, float, int], live=True, depends_on=ENABLE_LONG_DEADZONE_PARAMS)
    * LONG_DEADZONE_V: Param([0., .15], [list, float, int], live=True, depends_on=ENABLE_LONG_DEADZONE_PARAMS)
    * INDI_SHOW_BREAKPOINTS: Param(False, bool, live=True, depends_on=SHOW_INDI_PARAMS)
    * 'a_cruise_min_bp': Param([0., 5.,  10., 20.,  40.], [list, float], live=True, depends_on=SHOW_A_CRUISE)
    * 'a_cruise_min_v': Param([-1.0, -.8, -.67, -.5, -.30], [list, float], live=True, depends_on=SHOW_A_CRUISE)
    * 'a_cruise_min_v_following': Param([-1.0, -.8, -.67, -.5, -.30], [list, float], live=True, depends_on=SHOW_A_CRUISE)
    * 'a_cruise_max_bp': Param([0.,  6.4, 22.5, 40.], [list, float], live=True, depends_on=SHOW_A_CRUISE)
    * 'a_cruise_max_v': Param([1.2, 1.2, 0.65, .4], [list, float], live=True, depends_on=SHOW_A_CRUISE)
    * 'a_cruise_max_v_following': Param([1.6, 1.6, 0.65, .4], [list, float], live=True, depends_on=SHOW_A_CRUISE)
    * ENABLE_UNSAFE_STEERING_RATE: Param(False, bool, depends_on=SHOW_UNSAFE_OPTS, description='Toyota only.\nThis is HIGHLY unsafe, '
    * ENABLE_LAT_PARAMS: Param(False, bool, live=True, description="When true, the lat params set in op_edit.")
    * WHICH_LAT_CTRL: Param('indi', ['pid', 'indi', 'lqr'], live=True, depends_on= ENABLE_LAT_PARAMS, description='Which lat controller to use, '
    * SHOW_LQR_PARAMS: Param(False, [bool], live=True, depends_on=ENABLE_LAT_PARAMS)
    * LQR_SCALE: Param(1500.0, VT.number, live=True, depends_on=SHOW_LQR_PARAMS)
    * LQR_KI: Param(0.05, VT.number, live=True, depends_on=SHOW_LQR_PARAMS)
    * LQR_A: Param([0., 1., -0.22619643, 1.21822268], [list, float, int], live=True, depends_on=SHOW_LQR_PARAMS)
    * LQR_B: Param([-1.92006585e-04, 3.95603032e-05], [list, float, int], live=True, depends_on=SHOW_LQR_PARAMS)
    * LQR_C: Param([1., 0.], [list, float, int], live=True, depends_on=SHOW_LQR_PARAMS)
    * LQR_K: Param([-110.73572306, 451.22718255], [list, float, int], live=True, depends_on=SHOW_LQR_PARAMS)
    * LQR_L: Param([0.3233671, 0.3185757], [list, float, int], live=True, depends_on=SHOW_LQR_PARAMS)
    * LQR_DC_GAIN: Param(0.002237852961363602, VT.number, live=True, depends_on=SHOW_LQR_PARAMS)
    * STEER_LIMIT_TIMER: Param(0.4, VT.number, live=True, depends_on=ENABLE_LAT_PARAMS)
    * SHOW_LAT_PID_PARAMS: Param(False, [bool], live=True, depends_on=ENABLE_LAT_PARAMS)
    * LAT_PID_KP_BP: Param([0., 5., 35.], [list, float, int], live=True, depends_on=SHOW_LAT_PID_PARAMS)
    * LAT_PID_KP_V: Param([3.6, 2.4, 1.5], [list, float, int], live=True, depends_on=SHOW_LAT_PID_PARAMS)
    * LAT_PID_KI_BP: Param([0., 35.], [list, float, int], live=True, depends_on=SHOW_LAT_PID_PARAMS)
    * LAT_PID_KI_V: Param([0.54, 0.36], [list, float, int], live=True, depends_on=SHOW_LAT_PID_PARAMS)
    * LAT_PID_KF: Param(1., VT.number, live=True, depends_on=SHOW_LAT_PID_PARAMS)
    * SHOW_INDI_PARAMS: Param(False, [bool], live=True, depends_on=ENABLE_LAT_PARAMS)
    * SHOW_UNSAFE_OPTS: Param(False, [bool], live=True, description='Shows options for unsafe / dangerous features. '
    * SHOW_EXPERIMENTAL_OPTS: Param(False, [bool], live=True, description='Shows options for experimental, unfinished, features. '
  * Commits:
    * feat(lat): add new live lat controller
    * feat(lat): controlsd now uses live lat controller
    * fix(params): op params allowed types can work with values
    * fix(lat): fix typos in live lat controller
    * feat(lat): update lqr to op params
    * fix(lat): only init lqr when CP is using it
    * fix(lat): properly check for lqr default
    * feat(pid): make PIController use op params
    * feat(params): update long and pid controllers  for live tuning
    * feat(params): expose long deadzone in op params
    * feat(params): add live params to lat pid controller
    * fix(params): make lqr params the correct default type in op params
    * fix(params): make sure lqr param values have correct type
    * fix(pid): check if use_ops is a lambda in pid controller
    * fix(pid): check for string type in pid controller
    * test(params): run process relay with long params enabled
    * test(params): run process replay with lat params enabled
    * refactor(params): adjust nested op params
    * fix(lat): fix lqr lat controller and update op params with prius lqr tuning
    * test(params): run process replay with pid lat tune
    * test(params): run process replay with lqr lat tune
    * chore(params): reset op params back to defaults
    * fix(params): default steer actuator from car params
    * refactor(params): change nested params in op edit
    * docs(readme): add info about my fork to readme
    * docs(readme): update github actions link with my repo's url
    * tests(processes): update process replay refs for tuning
    * refactor(release): change release files order so that custom files are at the top
    * feat(lat): add optional steer actuator breakpoints
    * feat(params): made it possible to use ints as bools in op_edit
    * fix(lat): properly reset vars back to car params in indi and lqr
    * fix(pid): properly pass p, i, and f to pid controller using car and op params
    * fix(planner): shift lane planner p_poly when using custom camera offset
    * refactor(params): change a_cruise op params to match stock values
    * tests(processes): update process replay refs for tuning

Version 25
========================
  * Commits:
    * refactor(sentry): log all exceptions to sentry
    * fix(sentry): remove unused import in crash.py

Version 24
========================
  * Commits:
    * feat(actions): update refs now removes old refs
    * chore(sentry): replace comma's sentry url with my own
    * feat(sentry): improve crash logging
    * fix(sentry): upload error tags to sentry

Version 23
========================
  * Commits:
    * fix(params): fix entering values into a list
    * fix(coasting): only update planner for updated model if coasting is enable

Version 22
========================
  * Commits:
    * Revert Latest torch model

Version 21
========================
  * New OP Params:
    * ENABLE_COASTING: Param(False, bool, 'When true the car will try to coast down hills instead of braking.', live=True)
    * COAST_SPEED: Param(10.0, VT.number, 'The amount of speed to coast by before applying the brakes. Unit: MPH',
    * SETPOINT_OFFSET: Param(0, int, 'The difference between the car\'s set cruise speed and OP\'s. Unit: MPH', live=True)
    * DOWNHILL_INCLINE: Param(-1, VT.number, 'If the angle between the current road and the future predicted road is less than this value, '
    * ALWAYS_EVAL_COAST: Param(False, bool, live=True, depends_on=ENABLE_COASTING)
    * EVAL_COAST_LONG: Param(False, bool, live=True, depends_on=ENABLE_COASTING)
    * ENABLE_LONG_PARAMS: Param(False, bool, live=True, description='When true the long controller will used the params in opParam '
    * ENABLE_GAS_PARAMS: Param(True, bool, live=True, depends_on=ENABLE_LONG_PARAMS)
    * GAS_MAX_BP: Param([0., 20, 33], [list, float, int], live=True, depends_on=ENABLE_GAS_PARAMS)
    * GAS_MAX_V: Param([0.3, 0.2, 0.075], [list, float], live=True, depends_on=ENABLE_GAS_PARAMS)
    * ENABLE_BRAKE_PARAMS: Param(False, bool, live=True, depends_on=ENABLE_LONG_PARAMS)
    * BRAKE_MAX_BP: Param([0., 20, 33], [list, float, int], live=True, depends_on=ENABLE_BRAKE_PARAMS)
    * BRAKE_MAX_V: Param([0.5, 0.5, 0.5], [list, float], live=True, depends_on=ENABLE_BRAKE_PARAMS)
    * INDI_SHOW_BREAKPOINTS: Param(False, bool, live=True)
    * 'indi_use_vego_breakpoints': Param(False, bool, live=True, depends_on=INDI_SHOW_BREAKPOINTS)
    * 'indi_use_steer_angle_breakpoints': Param(False, bool, live=True, depends_on=INDI_SHOW_BREAKPOINTS)
    * 'indi_inner_gain_bp': Param([0, 255, 255], [list, float, int], live=True, depends_on=INDI_SHOW_BREAKPOINTS)
    * 'indi_inner_gain_v': Param([6.0, 6.0, 6.0], [list, float, int], live=True, depends_on=INDI_SHOW_BREAKPOINTS)
    * 'indi_outer_gain_bp': Param([0, 255, 255], [list, float, int], live=True, depends_on=INDI_SHOW_BREAKPOINTS)
    * 'indi_outer_gain_v': Param([15, 15, 15], [list, float, int], live=True, depends_on=INDI_SHOW_BREAKPOINTS)
    * 'indi_time_constant_bp': Param([0, 255, 255], [list, float, int], live=True, depends_on=INDI_SHOW_BREAKPOINTS)
    * 'indi_time_constant_v': Param([5.5, 5.5, 5.5], [list, float, int], live=True, depends_on=INDI_SHOW_BREAKPOINTS)
    * 'indi_actuator_effectiveness_bp': Param([0, 255, 255], [list, float, int], live=True, depends_on=INDI_SHOW_BREAKPOINTS)
    * 'indi_actuator_effectiveness_v': Param([6, 6, 6], [list, float, int], live=True, depends_on=INDI_SHOW_BREAKPOINTS)
    * SHOW_A_CRUISE: Param(False, bool, live=True)
    * 'a_cruise_min_bp': Param([0.0, 5.0, 10.0, 20.0, 55.0], [list, float], live=True, depends_on=SHOW_A_CRUISE)
    * 'a_cruise_min_v': Param([-1.0, -0.7, -0.6, -0.5, -0.3], [list, float], live=True, depends_on=SHOW_A_CRUISE)
    * 'a_cruise_min_v_following': Param([-3.0, -2.5, -2.0, -1.5, -1.0], [list, float], live=True, depends_on=SHOW_A_CRUISE)
    * 'a_cruise_max_bp': Param([0., 5., 10., 20., 55.], [list, float], live=True, depends_on=SHOW_A_CRUISE)
    * 'a_cruise_max_v': Param([0.8, 0.9, 1.0, 0.4, 0.2], [list, float], live=True, depends_on=SHOW_A_CRUISE)
    * 'a_cruise_max_v_following': Param([1.6, 1.4, 1.4, .7, .3], [list, float], live=True, depends_on=SHOW_A_CRUISE)
  * Commits:
    * refactor(params): refactor coasting op params to use string constants
    * fix(controls): only replace setpoint offset with coast speed if coasting is enabled
    * feat(logs): add script to log segment to txt file
    * feat(coasting): calc incline of road using new model
    * feat(coasting): add downhill incline to op params and planner
    * fix(planner): remove unused import and correctly op params
    * feat(coasting): treat cruiseGas like stock cruise
    * fix(tools): remove unused imports in log_segment
    * fix(long): fix typo in long controller
    * fix(planner): properly subscribe to modelV2
    * feat(coasting): run planner when model updates and optionally eval coast in long controller
    * fix(coasting): long controller shouldn't brake with gas
    * Merge branch 'src' into coasting
    * fix(coasting): eval coast plan when going downhill or above setpoint
    * fix(planner): log new coasting values before setting old ones
    * feat(params): add depends on feature to op params
    * feat(params): op edit shows 3 dots instead of every disabled param
    * refactor(params): add show options to op params
    * refactor(long): made gas max an optional live opParam
    * feat(params): opEdit supports t or f for true or false
    * feat(params): op edit now supports nested dependencies
    * feat(params): max brake is now an op param
    * feat(params): indent nested params in op edit
    * fix(params): properly hide children when parent's parent's are disabled
    * tests(process): reset params to pass stock process replay
    * tests(processes): update process replay refs for coasting
    * fix(params): fix op edit to properly select all params
    * feat(params): add ability to append values to lists in op edit
    * feat(params): remove index from list in op edit
    * feat(params): add ability to replace lists in op edit
    * fix(params): check types when replacing list in op params

Version 20
========================
  * Commits:
    * feat(models): update model to 5034ac8b-5703-4a49-948b-11c064d10880/780 b5e5c420-7042-4d0c-92e5-770eb09936a5/800

Version 19
========================
  * Commits:
    * db090195-8810-42de-ab38-bb835d775d87/601

Version 18
========================
  * Commits:
    * 2895ace6-a296-47ac-86e6-17ea800a74e5/550

Version 17
========================
  * Commits:
    * chore(git): update panda submodule

Version 16
========================
  * New OP Params:
    * 'coast_speed': Param(10.0, VT.number, 'The amount of speed to coast by before applying the brakes. Unit: MPH')
    * 'a_cruise_max_v_following': Param([1.6, 1.4, 1.4, .7, .3], [list, float], live=True)
    * ENABLE_UNSAFE_STEERING_RATE: Param(False, bool)
  * Commits:
    * feat(toyota): add optional unsafe steering torqure rate

Version 15
========================
  * Commits:
    * Added pytorch supercombo
    * fix rebase
    * no more keras
    * Hacky solution to the NCHW/NHWC incompatibility between SNPE and our frame data
    * Revert no camera for VW
    * dont break dmonitoringd, final model 229e3ce1-7259-412b-85e6-cc646d70f1d8/430
    * fix hack
    * Revert fix hack
    * Removed axis permutation hack
    * Folded padding layers into conv layers
    * Removed the last pad layer from the dlc
    * Revert Removed the last pad layer from the dlc
    * Revert Folded padding layers into conv layers
    * vision model: 5034ac8b-5703-4a49-948b-11c064d10880/780  temporal model: 229e3ce1-7259-412b-85e6-cc646d70f1d8/430  with permute + pool opt
    * fix ui drawing with clips
    * ./compile_torch.py 5034ac8b-5703-4a49-948b-11c064d10880/780 dfcd2375-81d8-49df-95bf-1d2d6ad86010/450 with variable history length

Version 14
========================
  * New OP Params:
    * 'indi_inner_gain': Param(9.0, VT.number, live=True)
    * 'indi_outer_gain': Param(8.9, VT.number, live=True)
    * 'indi_actuator_effectiveness': Param(9.0, VT.number, live=True)
    * 'steer_actuator_delay': Param(0.60, VT.number, live=True)
    * 'indi_actuator_effectiveness_v': Param([6, 6, 6], [list, float, int], live=True)
    * 'a_cruise_min_bp': Param([0.0, 5.0, 10.0, 20.0, 55.0], [list, float], live=True)
    * 'a_cruise_min_v': Param([-1.0, -0.7, -0.6, -0.5, -0.3], [list, float], live=True)
    * 'a_cruise_min_v_following': Param([-3.0, -2.5, -2.0, -1.5, -1.0], [list, float], live=True)
    * 'a_cruise_max_bp': Param([0., 5., 10., 20., 55.], [list, float], live=True)
    * 'a_cruise_max_v': Param([0.8, 0.9, 1.0, 0.4, 0.2], [list, float], live=True)
    * 'a_cruise_max_v_following': Param([1.6, 1.4, 1.4, .7, .3], [list, float], live=True)
  * Commits:
    * feat(planner): made min/max cruise accel an op param
    * fix(params): update op params with new default indi values
    * fix(ui): draw road edges with a higher alpha value
    * fix(tests): fix following distance unit tests
    * Merge branch 'src' into eco-mode
    * feat(actions): add slash command to update refs
    * fix(actions): remove git config user info
    * fix(actions): fix indentation typo in run command
    * fix(actions): docker map volume when updating refs
    * fix(actions): fix typo in docker run command
    * fix(actions): commit ref_commit file in update-refs workflow
    * fix(actions): use PAT for update_refs workflow
    * fix(actions): properly commit updated ref files
    * fix(actions): checkout repo with PAT
    * tests(processes): update process replay refs for eco-mode

Version 13
========================
  * Commits:
    * hotfix(actions): remove lfs support when checking out project
    * fix(params): stop op params from reading file during ci
    * fix(tests): update refs now uses windows compatible file names
    * chore(git): update git lfs attributes
    * tests(processes): add local refs for process replay
    * tests(process): integration tests now work with local files
    * tests(processes): update local refs for integration test
    * fix(actions): update actions to run local process replay tests
    * fix(actions): increase size of docker container
    * fix(actions): increase size of docker container to 2 GB
    * fix(actions): don't build op base image
    * fix(actions): fix typo in PERSIST command
    * fix(actions): remove cache from in docker build commands
    * fix(actions): build docker images, don't pull
    * fix(actions): process replay checkout with lfs
    * fix(actions): add process replay debug
    * fix(tests): replace | with ! in process replay refs
    * tests(processes): remove old process replay files
    * tests(processes): update process replay refs
    * fix(tests): fix process replay to look for files with a !
    * feat(actions): move build workflow into test workflow
    * fix(actions): use proper string syntax
    * fix(actions): properly exit prebuilt job
    * fix(actions): use proper pr ci branch name and don't use ::set-env

Version 12
========================
  * Commits:
    * refactor draw model
    * rebase master
    * correct valid_len
    * rename function
    * rename variables
    * white space
    * rebase to master
    * e16c13ac-927d-455e-ae0a-81b482a2c787
    * start rewriting
    * save proress
    * compiles!
    * oops
    * many fixes
    * seems to work
    * fix desires
    * finally cleaned
    * wrong std for ll
    * dont pulse none
    * compiles!
    * ready to test
    * WIP does not compile
    * compiles
    * various fixes
    * does something!
    * full 3d
    * not needed
    * draw up to 100m
    * fix segfault
    * wrong sign
    * fix flicker
    * add road edges
    * finish v2 packet
    * no camera for VW
    * Merge branch 'src' into refactor-model
    * fix(models): add missing 3D model lfs hash

Version 11
========================
  * New OP Params:
    * 'indi_outer_gain_v': Param([15, 15, 15], [list, float, int], live=True)
  * Commits:
    * bump to 0.7.8
    * fix tested branch detection
    * Update values.py (#1824)
    * Revert Update values.py (#1824)
    * Nissan: Tweaking steeringPressed/LKAS_MAX_TORQUE (#1865)
    * Add 2020 Insight FW (#1879)
    * bump opendbc
    * Honda CRV BSM alert from B-CAN (#1867)
    * update pipfile.lock (#1896)
    * add tolerance to process replay compare (#1904)
    * fix modeld replay test
    * fix cppcheck on ubuntu 19.10
    * make sure boardd loopback test can run standalone
    * boardd: release claimed interface before closing usb (#1855)
    * fix buffer overflow (#1871)
    * boardd: Add new functions usb_read, usb_write (#1856)
    * Add fwdCamera f/w for 2020 Corolla Hybrid ZR (AUS) (#1911)
    * fix spinner
    * skip 1st segment in debug replay
    * Subaru Global generated dbc and new signals (#1908)
    * add HYUNDAI_GENESIS test route
    * Only draw lead car indicators when controlling longitudinal (#1914)
    * add test route for HYUNDAI.KIA_SORENTO
    * Use hyundai legacy safety for Kia Sorento (#1912)
    * update refs
    * add timeout on procLog socket for CPU usage test
    * Update pip to 20.1.1 so python-opencv installation succeeds
    * remove old params learner (#1918)
    * Improve on-device CI reliability (#1922)
    * Test Car Models 2.0 (#1903)
    * Car cleanup (#1924)
    * kia stinger: use hyundaiLegacy safety mode and add test route
    * boardd: use enum instead of magic number (#1927)
    * sidebar: remove unnecessary checks on uilayout_sidebarcollapsed (#1928)
    * qcom2 build fixes
    * bump cereal
    * Local variable ARCH isn't used anymore (#1930)
    * remove dead lines from boardd cython setup
    * Add Lexus RX300 2019 FW (#1838)
    * Update TOTAL_SCONS_NODES (#1938)
    * EfficientNet driver monitoring (#1907)
    * start 0.7.8 release notes
    * UI cleanup (#1941)
    * Add a minimal debugging tool to show the UI while device not in car (#1937)
    * needed in pipeline
    * can't directly access sockets anymore
    * Revert can't directly access sockets anymore, was supposed to be on branch
    * new palisade fingerprint (#1945)
    * fail new car model unit tests if missing a test route
    * Remove get_one_can from messaging (#1946)
    * not useful
    * bump panda
    * add locationd, paramsd, dmonitoringd to CPU usage script
    * Misc locationd improvements (#1714)
    * fix locationd profiling
    * dont init sound
    * Panda abstraction layer in boardd (#1919)
    * modeld: read frame_id if sm.update(0)>0 (#1947)
    * Driver view refactor (#1869)
    * Test can valid in car unit tests (#1961)
    * bump opendbc
    * Run CI tests in parallel (#1962)
    * remove duplicate call to getDMonitoringState (#1964)
    * Add frequency check to hyundai camera can parser (#1965)
    * bump opendbc
    * Update Hyundai DBC (#1968)
    * we have routes for these now
    * Add Hyundai Veloster 2019 (#1955)
    * add hyundai veloster to release notes
    * veloster steers down to zero
    * Add missing chrysler can parser checks (#1967)
    * Update bug_report.md
    * Cleanup locationd msg building (#1972)
    * add fall filter and less FP on posenet (#1971)
    * remove selfdrive/common/visionstream.c (#1931)
    * Add Kia Stinger transmission FW version (#1975)
    * improve updated responsiveness (#1973)
    * makes more sense
    * Make sure memory is released by using unique_ptr (#1958)
    * persist falling test
    * Revert persist falling test
    * Cleanup updated (#1981)
    * camerad: cache rgb_roi_buf&conv_result (#1979)
    * wrong units
    * Setup PC testing in Jenkins (#1984)
    * add CI dependency for new tests
    * Improve update reliability and responsiveness (#1986)
    * fix counter mismatch in sim
    * Scripts for containerized CARLA (#1987)
    * remove dead lines from calibrationd
    * second segment is ok for car unit tests
    * persist falling until message sent (#1982)
    * Track calib spread (#1988)
    * release opencl objects (#1978)
    * Add Camry 2020 camera fw
    * Updater tests (#1974)
    * Subaru pre-global: add support for Subaru Legacy 2015-18 (#1805)
    * only check offroad in dmonitoringd on init
    * Add 2020 Accord
    * bump panda
    * tf 2.2.
    * Remove non-SCC Hyundai Kona port (#1997)
    * fix missing negative limit in pid controller (#2001)
    * update_ci_routes.py: upload route by arg
    * fix bug that visionstream_destroy may be called twice (#1999)
    * camerad: close ops_sock in camera_close (#1998)
    * Improve CPU usage test reliability (#2002)
    * Car Port: Hyundai Genesis G70 2018 (#2000)
    * add genesis g70 to release notes
    * fix for PC: detach panda kernel driver if active (#1950)
    * default pull request template
    * can't do nested html comments
    * Build openpilot on mac in CI (#1792)
    * bump panda
    * update dm new model description
    * Add preglobal Subaru Forester and Outback (#1993)
    * Fix Readme
    * Fix Genesis G70 in readme
    * Test standalone binary builds in CI (#2008)
    * Added additional IS 300 engine f/w (#2015)
    * camerad: protect concurrent access to shared variables and avoid race conditions (#1966)
    * Nissan harnesses for sale
    * Car Port: 2020 Hyundai Kona (#2010)
    * increase controlsd CPU test threshold
    * add kona to release notes
    * Alert when updated consistently fails (#2013)
    * update total scons nodes
    * update optima fingerprint and Fw Fp (#2017)
    * fix linter
    * fix boardd build
    * Don't check dirty on prebuilt release (#2014)
    * Force battery temperature to 0 on comma two
    * NEOS background updater (#1892)
    * add background download to release notes
    * add missing agent for jenkins job
    * fix get_git_remote not returning a value
    * add date to release notes
    * add launch_env.sh to release files
    * Pigeon abstraction layer (#1977)
    * bump panda
    * increase CPU test timeout to allow for installing new APKs
    * Setup script improvements to MacOS / Ubuntu (#2012)
    * EU Corolla Hybrid TSS2 EPS f/w (#2027)
    * Add fwdCamera f/w for CAR.COROLLA_TSS2 (#2028)
    * exit camerad cleanly on PC (#2035)
    * init and destroy transform_lock (#2003)
    * remove old test runner
    * Kilometers per hour now displayed as km/h (#2032)
    * add function cl_get_device_id (#1948)
    * Car power integrator + power management refactor (#1994)
    * fix two little bugs (#2033)
    * paint.cc: remove redundant calls  (#2025)
    * more panda fault types (#2036)
    * bump version to 0.7.9
    * remove dead code in updated
    * remove old tests (#2040)
    * fd should be initialized as -1 (#2041)
    * ui: refactor model related functions (#2026)
    * log when thermald shuts down device
    * add a sleep after cloudlog
    * clip carBatteryCapacity to 0
    * more init time in cpu test
    * Qt ui for PC (#2023)
    * Revert more init time in cpu test
    * Don't build by default
    * Fix qt env in SConstruct
    * boardd: return early from usb functions if not connected
    * Add Lexus RX esp FW (#2050)
    * ui: force GLES context
    * ui: larger font size
    * Added fingerprint for my 2020 Corolla Hybrid Sx sedan (#2052)
    * small dmonitoringd cleanup
    * Prius 2018 Engine FW (#2054)
    * Add 2020 RAV4 LE Hybrid engine f/w (#2058)
    * 2020 Corolla Hybrid Sx sedan FW (#2059)
    * update code stats script
    * type hints for messaging (#2061)
    * split dockerfile into base image and CI image (#2066)
    * move matmul3 into live_thread (#2069)
    * remove device_id&context from ModelFrame (#2064)
    * visionstream: fix doube fd close (#2057)
    * fingerprint for China 2019 CRV Hybrid (#2056)
    * paint.cc: deleted two meaningless lines (#2043)
    * Thermald cleanup (#2049)
    * bump cereal
    * fix prebuilt container
    * Pandad: turn on panda power (#2073)
    * Remove unnecessary string copy (#2067)
    * More Insight FW versions
    * mac ui kind of works (#2079)
    * Universal clocksd (#2075)
    * bump cereal
    * Loggerd rotation test (#2077)
    * wait longer for tici camerad startup
    * Tici sensord (#2072)
    * sensord: more precise 100 Hz, compensate for time spend measuring
    * Hardware abstraction class (#2080)
    * Systemd logcatd (#2085)
    * larch64 modeld fixes (#2086)
    * apport support for tombstoned (#2087)
    * larch64 dmonitoringmodeld fixes
    * hardware.py: PC is wifi so uploader works
    * bump panda
    * add frame count check to loggerd rotation test
    * missing two f's, loggerd should really work on pc
    * Fix OMX error on loggerd rotation when using multiple cameras (#1953)
    * Tici camerad (#2048)
    * open by path instead of number
    * make sure snpe can find libopencl
    * UI cleanup (#2091)
    * increase timeout on mac CI build
    * small uploader cleanup
    * Sound stability test (#2089)
    * not show soft recover alerts
    * remove read_param_timeout (#2095)
    * bump cereal
    * fix CI cache auto-deletion
    * need no divided by 2
    * lidar is a scam (#2094)
    * fix hyundai editing can parser values
    * driver monitoring cleanup (#2101)
    * Show lane lines and path while using uiview.py (#2104)
    * Added Toyota Camry 2019 (AUS) SX(2.5L FWD, 6speed) firmware versions (#2096)
    * build script that uses docker container (#1944)
    * Revert Added Toyota Camry 2019 (AUS) SX(2.5L FWD, 6speed) firmware versions (#2096)
    * Remove opencv from phonelibs (#2107)
    * Fix camera view on PC
    * ui: simplify shader versions and fix hardcoded texture size (#2112)
    * Wait 5 minutes after offroad before changing thresholds (#2113)
    * use buffered meta
    * remove recurrent LOGD and prints
    * bump panda
    * Reduce plannerd and dmonitoringd CPU usage (#2108)
    * paramsd process replay test (#2118)
    * Add Insight fw
    * 1024 MB should be enough for anyone
    * pc ui: print opengl version on startup
    * tici: fix set_realtime_priority (#2124)
    * sensord cleanup (#2111)
    * Add 2020 Highlander engine fw
    * release copy_q in visionbuf_free (#2121)
    * add more opengl info on startup to pc ui
    * UI vision refactor (#2115)
    * clean up old params
    * TextWindow Enhancements (#2114)
    * pytorch pip packages
    * fix pylint errors
    * remove vp everywhere (#2122)
    * make calibrationInvalid a permanent alert
    * update refs after new alert
    * sidebar cleanup (#2130)
    * CAR.CAMRY f/w (#2134)
    * Fix loggerd not rotating encoder if dcamera upload disabled (#2133)
    * UI: support multiple frame sizes (#2099)
    * Always keep display on with ignition (#2138)
    * link ui against right opengl(ES) lib
    * Update CONTRIBUTING.md
    * ui: glTexImage2D only redundant on QCOM
    * hide camera view when in reverse (#2144)
    * bump rednose
    * bump submodules
    * QT UI: sounds (#2078)
    * temporarily disable mac build
    * wait 5s before showing waiting for controls
    * Add 2020 Highlander Hybrid fw
    * simple unit test for startup alert
    * fix timing issues with new test
    * set params for new test
    * Split car identities to CX5, CX9, and Mazda3 (#2097)
    * turn display on in spinner (#2148)
    * dockerize carla + openpilot (#2011)
    * only build sim container on schedule
    * cleanup controlsd env variable reading
    * add repo check to sim ci build
    * bump cereal
    * Tici light sensor (#2150)
    * Reduce paramsd and calibrationd CPU usage (#2119)
    * remove unused import in cycle_alerts
    * run deleter on tici
    * Update README.md
    * Update README.md
    * swap ur/dl (#2153)
    * don't ship QT UI in release
    * Revert don't ship QT UI in release, needed by release CI test for now
    * handle exception in android service call
    * fix simulator CI (#2159)
    * prevent reversing alert from showing while changing gears
    * tici driver monitoring (#2158)
    * tici launch script (#2155)
    * UI: simplify layout calculation (#2131)
    * bump cereal
    * message builder (#2161)
    * set canValid for mock car
    * more messagebuilder (#2162)
    * send initial calibration packet immediately
    * use MessageBuilder::toBytes (#2167)
    * Auto reset bad calibration (#2151)
    * Update README.md (#2156)
    * Cut down unnecessary DM uncertain alerts (#2157)
    * cleanup README PC section
    * need to free tici DSP asap
    * improve tici camerad robustness (#2135)
    * fix stretched UI on pc
    * fix tbuffer img tearing
    * bump max vision clients for tici
    * only do reset if already calibrated (#2176)
    * Fix typo
    * update pipenv install
    * more pipenv version updates
    * remove schedule-triggered CI workflow (#2178)
    * Update 17 Corolla safetyParam (#2175)
    * bump opendbc
    * disable CI simulator container build until fixed
    * tici: fix ui rotation (#2184)
    * hub is handled by systemd gpio service (#2172)
    * remove unused submaster (#2187)
    * Add firmwares for CAR.COROLLA_TSS2 (#2185)
    * Add CAR.LEXUS_RX various missing firmware (#2189)
    * Update readme for 2018 Lexus RX
    * Improve realtime performance on NEOS (#2166)
    * add android procs to cpu usage sript
    * Add 2020 Highlander and Ridgeline fw
    * fix tici ui lag
    * rt debug scripts (#2165)
    * FileReader: cache files locally (#2170)
    * Tici hardware abstraction layer (#2183)
    * tici: offroad ui powersave (#2191)
    * these should be debug logs
    * Realtime shield (#2194)
    * promote hyundai palisade to offically supported (#2195)
    * type hints for alerts and fix community feature alert (#2196)
    * Get power usage from current sensor (#2192)
    * Only run rtshield when onroad
    * tici: take into account frame timestamp (#2199)
    * tici camera art (#2188)
    * revert tici ui rotate
    * tici: set volume at 90%
    * 2019 C-HR fw
    * alertmanager type hints (#2201)
    * quick lgtm fixes
    * add type hints to selfdrive/version.py
    * Revert tici: take into account frame timestamp (#2199)
    * remove parallel url downloader
    * cleanup long planner, mpc: unused globals and arguments (#2211)
    * touch.c:deleting useless function (#2208)
    * bump cereal
    * add function write_file() (#2181)
    * Fix makefiles after read_file() helper
    * tici: BMX055 magnetometer& temperature sensor (#2212)
    * read bool param with read_db_bool (#2205)
    * Add CAR.RAV4H_TSS2 ESP f/w (#2213)
    * Pilot 2019 is same platform as 2016-18
    * Fix Highlander order in readme
    * bump cereal
    * Uploader speedup (#2214)
    * Improved updater robustness (#2046)
    * Make readme consistent
    * remove unused alert
    * All Insight trims have Honda Sensing
    * fix unused dt entry on android (#2160)
    * fix dmonitoringmodeld random high CPU usage (#2216)
    * bump laika
    * Lexus CT Hybrid needs LSS
    * Add 2020 Honda Odyssey fw
    * tici: fix ui rotation (#2222)
    * remove unused globals, use self.reset() (#2220)
    * Params: use a multiple-reader / single-writer flock to improve concurrency (#2207)
    * SConstruct better tici detection
    * camerad: close file descriptors (#2065)
    * qcom2 needs cc conversion (#2125)
    * Add 2017 Lexus RX engine fw
    * bump cereal
    * fix modeld launch script larch64 detection
    * Update README.md
    * Combine Toyota Avalon rows
    * ProPILOT
    * Typo: thershold -> threshold (#2230)
    * Add engine f/w for CAR.LEXUS_RX (#2235)
    * Add symphony-cpu lib once (#2232)
    * close lock_fd if flock failed (#2231)
    * Fix grade force in test_long plant (#2225)
    * Add 2021 Corolla Hybrid to Supported Cars in README.md (#2229)
    * Enable Ctrl-C for Carla Server (#2240)
    * no more question issue type, we have discussions
    * this sounds better
    * Name openpilot docker container (#2239)
    * tici light sensor (#2238)
    * add 1 second delay to acc pedal alert (#2221)
    * pre-reqs for honda bosch longitudinal control (#1458)
    * fix compilation with Clang 10 on ubuntu 20.04
    * Revert fix compilation with Clang 10 on ubuntu 20.04
    * add ECU disable script from #1459
    * updated: log git corruption (#2242)
    * bump submodules
    * fix resource leak when rotating encoder (#2141)
    * Add Flags to Control Simulator (#2246)
    * fix paths for waste3 debug script
    * updated: remove old overlay init file
    * jenkins: clean workspace (#2248)
    * fix compilation with Clang 10 on ubuntu 20.04 (#2243)
    * update testing closet client
    * simplify testing closet client
    * Update release notes
    * 0.7.9 release notes tweak
    * Increase HKG torque limit (#2249)
    * bump submodules
    * run loggerd tests in CI (#2241)
    * Tici updated (#2126)
    * Run all driving processes on cores 2-3 (#2257)
    * Refactor loggerd rotations (#2247)
    * Merge branch 'master' into update-0.7.9
    * chore(git): update submodules to proper commits
    * fix(ui): fix build issues with model and path data
    * fix(ui): fix issues with poly data type
    * fix(ui): update poly to capnp list reader
    * fix(ui): replace paint with 0.7.9 paint
    * Fix calibration invalid alert on startup (#2270)
    * fix not going onroad on clean dashcam install (#2280)
    * hotfix(params): correct name for indi outer gain
    * fix(actions): update build action to 0.7.9
    * chore(git): update forked submodules to 0.7.9
    * Merge branch 'update-0.7.9' into src
    * feat(tools): add initial script to transfer drives between devices
    * feat(tools): add script from upstream to calc toyota eps factor
    * fix(tools): replace URLFile with request
    * fix(tools): require only date for route
    * fix(tools): add newline seperator after finish upload
    * feat(tools): add ability to transfer all drives
    * fix(tools): fix various typos and timeouts
    * fix(tools): properly check if route has already been uploaded
    * fix(tools): retry if fetching files fails
    * fix(tools): properly retry all network connections
    * fix(tools): python3 fixes for transfer script
    * fix(tools): switch to better retry function
    * fix(tools): fix kwargs in transfer script
    * fix(tools): improve logging in transfer script when requests fail
    * fix(tools): improve logging in transfer script
    * fix(tools): remove unused imports in transfer script

Version 10
========================
  * New OP Params:
    * 'indi_inner_gain': Param(6.0, VT.number, live=True)
    * 'indi_outer_gain': Param(15.0, VT.number, live=True)
    * 'indi_time_constant': Param(5.5, VT.number, live=True)
    * 'indi_actuator_effectiveness': Param(6.0, VT.number, live=True)
    * 'steer_actuator_delay': Param(0.57, VT.number, live=True)
    * 'coast_speed': Param(10.0, VT.number, 'The amount of speed to coast by before applying the brakes. Unit: MPH')
    * 'accel_hyst_gap': Param(0.02, VT.number, live=True)
    * 'gas_max_bp': Param([0., 20, 33], [list, float, int])
    * 'gas_max_v': Param([0.3, 0.2, 0.075], [list, float])
    * 'indi_use_vego_breakpoints': Param(False, bool, live=True)
    * 'indi_use_steer_angle_breakpoints': Param(False, bool, live=True)
    * 'indi_inner_gain_bp': Param([0, 255, 255], [list, float, int], live=True)
    * 'indi_inner_gain_v': Param([6.0, 6.0, 6.0], [list, float, int], live=True)
    * 'indi_outer_gain_bp': Param([0, 255, 255], [list, float, int], live=True)
    * 'indi_outer_grain_v': Param([15, 15, 15], [list, float, int], live=True)
    * 'indi_time_constant_bp': Param([0, 255, 255], [list, float, int], live=True)
    * 'indi_time_constant_v': Param([5.5, 5.5, 5.5], [list, float, int], live=True)
    * 'indi_actuator_effectiveness_bp': Param([0, 255, 255], [list, float, int], live=True)
    * 'indi_actuator_effectiveness_v': Param([6, 6, 6], [list, float, int], live=True)
  * Commits:
    * hotfix(toyota): update corolla safetyParam to 50
    * feat(params): add new values to op params for indi breakpoints
    * feat(indi): update indi controller to have live breakpoints
    * fix(toyota): reset gas clip to 1.0
    * fix(params): properly op param default values match expected type

Version 9
========================
  * Commits:
    * feat(toyota): update corolla TSS2 safety param
    * chore(git): update opendbc submodule for corolla TSS2 safety param
    * chore(git): fix opendbc submodule to use v0.7.7

Version 8
========================
  * New OP Params:
    * 'corolla_use_indi': Param(False, bool)
    * 'accel_hyst_gap': Param(0.02, float, live=True)
    * 'always_eval_coast_plan': Param(False, bool)
    * 'gas_max_bp': Param([0., 20, 33], [list, float])
    * 'gas_max_v': Param([0.3, 0.2, 0.075], [list, float])
    * return Param(None, type(None))
  * Commits:
    * hotfix(params): hotfix default param in opParams
    * fix(ci): add gitignore after commit
    * chore(git): update git ignore to not ignore certain release files
    * fix(ci): include placeholder in panda gitignore
    * fix(ci): prevent coping phonelibs twice
    * fix(ci): remove gitignore from panda folder
    * chore(git): override ignore for all release phonelibs
    * feat(coasting): lower accel to 0 when coasting
    * fix(actions): fix build command to build pr branch
    * fix(coasting): lower gas when last output was positive
    * Revert Better poly (#1437)
    * Merge branch 'src' into coasting
    * fix(coasting): out min of last output or curent output
    * fix(coasting): change curise plan wehn gasbrake is in between accel hyst gap
    * fix(coasting): fix typo in toyota car controller
    * fix(coasting): fix F841 in toyota car controller
    * fix(coasting): apply accel_gap to correct function
    * perf(params): optimize opParams reading to read only if the file was modified
    * fix(coasting): optionally always eval coasting state
    * fix(params): fix issues using list types in op params
    * feat(toyota): made max gas an op param

Version 7
========================
  * New OP Params:
    * 'enable_coasting': Param(False, bool, 'When true the car will try to coast down hills instead of braking.')
    * 'coast_speed': Param(10.0, float, 'The amount of speed to coast by before applying the brakes. Unit: MPH')
    * 'setpoint_offset': Param(0, int, 'The difference between the car\'s set cruise speed and OP\'s. Useful for toyotas when coasting. Unit: MPH')
  * Commits:
    * refactor(planner): use LONG_PLAN_SOURCE instead of hard coded strings
    * feat(coasting): impl initial coasting ideas from qadmus
    * fix(coasting): reset long plan source back to cruise if it's not a valid option
    * Merge branch 'src' into coasting
    * feat(coasting): add new long plan sources for coasting state
    * feat(coasting): update planner, longcontrol, and controlsd with qadmus coasting logic
    * fix(coasting): add missing carControl sub to plannerd
    * feat(coasting): move coast speed to op params
    * feat(coasting): enable cruise offset for coasting w/ toyota
    * fix(coasting): import correct long plan source in planner
    * fix(coasting): fix process replay tests for planner
    * Fix grade force in test_long plant (#2225)
    * Merge branch 'src' into coasting

Version 6
========================
  * Commits:
    * Better poly (#1437)

Version 5
========================
  * New OP Params:
    * 'alca_min_speed': Param(20.0, VT.number, 'The minimum speed allowed for an automatic lane change (in MPH)')
    * 'corolla_use_indi': Param(False, bool)
  * Commits:
    * feat(toyota): made corolla indi optional

Version 4
========================
  * Commits:
    * chore(git): update cereal submodule to point to my fork
    * chore(git): replace all submodule relative urls with github urls

Version 3
========================
  * Commits:
    * fix(actions): fix build action to include phonelibs
    * fix(actions): copy op_edit to release build
    * fix(actions): copy over op_params and create panda obj file
    * fix(ci): add op_params and related files to common files
    * refactor(actions): move build release job into its own script
    * fix(actions): checkout with lfs
    * feat(actions): change release version to be date & time
    * feat(actions): add new action for build slash command
    * feat(actions): add build as a possible slash command

Version 2
========================
  * New OP Params:
    * 'steer_actuator_delay': Param(0.57, float, live=True)
    * 'alca_nudge_required': Param(False, bool, 'Whether to wait for applied torque to the wheel (nudge)
    * 'alca_min_speed': Param(20.0, VT.number, 'The minimum speed allowed for an automatic lane change (in MPH)')
  * Commits:
    * hotfix(actions): switch release branch to r2++
    * feat(path): add auto lane change option
    * fix(path): update default lane change values
    * fix(path): fix E502 in path planner
