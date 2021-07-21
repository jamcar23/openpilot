Version 7.2.0 (openpilot v0.8.5)
========================
  Source commit: d1164ea1
  * New OP Params:
    * ENABLE_CURVE_RATE_LIMITS: Param(False, [bool], live=True, depends_on=ENABLE_LAT_PARAMS, description='Override the default max curvature rates when true.')
    * MAX_CURVE_RATE_BP: Param([0, 35], VT.list_of_numbers, live=True, depends_on=ENABLE_CURVE_RATE_LIMITS)
    * MAX_CURVE_RATE_V: Param([0.03762194918267951, 0.003441203371932992], VT.list_of_numbers, live=True, depends_on=ENABLE_CURVE_RATE_LIMITS,
  * Commits:
    * feat(params): add new op params for overriding max curvature rate
    * feat(controls): override max curvature rate limits
    * fix(params): make sure MAX_CURVE_RATE_V is below line limit
    * fix(params): include lists in allowed types for max curve rate bp & v

Version 7.1.0 (openpilot v0.8.5)
========================
  Source commit: 751753eb
  * Commits:
    * Refactor lateral lag compensation (#21334)
    * Refactor long (#21433)
    * New desire model (#21458)
    * fix(controls): make sure lat plan has been set
    * fix(controls): make sure curvature is float
    * fix(controls): check if lat_plan is reader
    * fix(controls): desired curvature now comes from controls state
    * fix(ui): convert curvature to degrees in dev ui
    * fix(controls): send desired curvature degrees
    * fix(controls): calc desired steer from curve using vehicle model
    * tests(processes): update process replay refs for port-model-0.8.6
    * tests(opParams): update opParams unit test with desired steer changes
    * tests(long): add longitudinal tests for new long mpc
    * fix(py): remove unused imports
    * fix(tools): update tools & sim for long refactor
    * fix(params): make sure multi bp has consistent behavior from past releases

Version 7.0.0 (openpilot v0.8.5)
========================
  Source commit: a3412b60
  * Openpilot Changes:
    *  NEOS update: improved reliability and stability with better voltage regulator configuration
    *  Smart model-based Forward Collision Warning
    *  CAN-based fingerprinting moved behind community features toggle
    *  Improved longitudinal control on Toyotas with a comma pedal
    *  Improved auto-brightness using road-facing camera
    *  Added "Software" settings page with updater controls
    *  Audi Q2 2018 support thanks to jyoung8607!
    *  Hyundai Elantra 2021 support thanks to CruiseBrantley!
    *  Lexus UX Hybrid 2019-2020 support thanks to brianhaugen2!
    *  Toyota Avalon Hybrid 2019 support thanks to jbates9011!
    *  SEAT Leon 2017 & 2020 support thanks to jyoung8607!
    *  Škoda Octavia 2015 & 2019 support thanks to jyoung8607!

Version 6.7.0 (openpilot v0.8.3)
========================
  Source commit: 99dba134
  * Commits:
    * feat(tools): abstract part of ubuntu_setup to new script
    * fix(tools): make sure some bash scripts execute that way
    * feat(tools): add method to get git logs from python
    * feat(tools): get diffs between merges, looks like gh pr
    * feat(github): add test workflow to generate changelog
    * feat(github): add workflow dispatch run option to gen_changelog
    * fix(github): fix typo in gen_changelog workflow
    * fix(github): try to generate changelog outside of docker
    * feat(tools): gen changelog now correctly gets diffs
    * feat(tools): parse new op params for each pr
    * fix(tools): only strip last char if found
    * feat(tools): generate initial changelog for last pr
    * refactor(tools): create method to create text indents for changelog
    * feat(tools): changelog now includes commit messages
    * feat(tools): don't include commits from OP version changes in changelog
    * refactor(tools): refactor changelog to create sections first
    * feat(tools): changelog now includes src commit
    * fix(tools): check for update merge messages from git cli
    * feat(tools): gen changelog for version 1 of flexpilot
    * feat(tools): changelog now shows op version too
    * perf(tools): used cached op version when creating changelog
    * feat(tools): changelog now updates existing file instead of starting over
    * feat(tools): switch changelog to semver
    * fix(tools): make sure latest version is at the top of changelog
    * feat(tools): changelog now gets commits between both parents
    * fix(tools): changelog no longer shows comma's commits when changing op versions
    * feat(tools): changelog now shows OP changes too on major version increase
    * fix(tools): don't include changed params as new params in changelog
    * fix(tools): properly account for already included params
    * feat(ui): show changelog when inside update ui
    * feat(github): add changelog generation and semver to ci pipeline
    * fix(tools): correctly get next semver number
    * fix(github): remove unused docker code in gen_changelog workflow
    * fix(tools): try to fix subprocess communication on linux
    * fix(tools): make sure changelog doesn't update if there are no changes
    * fix(github): fix build_release_ci script to properly flag errors
    * fix(tools): export semver without pythonenv setup
    * fix(ci): run build_release_ci without precommit check (it never worked anyway)
    * fix(tools): try to find commit locally if web request fails
    * fix(tools): use last written hash if available

Version 6.6.0 (openpilot v0.8.3)
========================
  Source commit: 33e98404
  * New OP Params:
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

Version 6.5.0 (openpilot v0.8.3)
========================
  Source commit: 92d4c8f6
  * Commits:
    * no heading cost (#20594)
    * MPC retune for laneless fix (#20616)
    * fix(planner): properly set custom steer rate cost
    * fix(planner): temp remove wide camera from lat planner
    * fix(planner): get bool param correctly

Version 6.4.0 (openpilot v0.8.3)
========================
  Source commit: 124b95b3
  * New OP Params:
    * DISENGAGE_ON_GAS: Param(True, [bool], description='Whether you want openpilot to disengage on gas input or not.', live=True)
  * Commits:
    * feat(params): enable optional disengage on gas
    * fix(param); made disengage on gas a live param
    * Merge branch 'src' into disengage-on-gas

Version 6.3.0 (openpilot v0.8.3)
========================
  Source commit: a378051f
  * New OP Params:
    * HIGH_BEAM_BRIGHTNESS: Param(20, VT.number, depends_on=ENABLE_SCREEN_BRIGHTNESS_HEAD_LIGHTS)
  * Commits:
    * fix(param): made show build options a live param
    * fix(params): clarify what enable_screen_brightness_head_lights does
    * feat(params): add params for brightness when high beams are on
    * docs(readme): add spot about screen brightness via head lights

Version 6.2.0 (openpilot v0.8.3)
========================
  Source commit: dcd91d2f
  * Commits:
    * fix(ui): change home screen to say flexpilot instead of op

Version 6.1.0 (openpilot v0.8.3)
========================
  Source commit: 550c0109
  * New OP Params:
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

Version 6.0.0 (openpilot v0.8.3)
========================
  Source commit: 48763617
  * Openpilot Changes:
    *  New model
    *  Trained on new diverse dataset from 2000+ users from 30+ countries
    *  Trained with improved segnet from the comma-pencil community project
    *  🥬 Dramatically improved end-to-end lateral performance 🥬
    *  Toggle added to disable the use of lanelines
    *  NEOS update: update packages and support for new UI
    *  New offroad UI based on Qt
    *  Default SSH key only used for setup
    *  Kia Ceed 2019 support thanks to ZanZaD13!
    *  Kia Seltos 2021 support thanks to speedking456!
    *  Added support for many Volkswagen and Škoda models thanks to jyoung8607!

Version 5.2.0 (openpilot v0.8.2)
========================
  Source commit: 2caaf37f
  * Commits:
    * feat(ui): port colored lane lines from shane
    * fix(ui): add model reader to ui scene

Version 5.1.0 (openpilot v0.8.2)
========================
  Source commit: 3b2b4e0b
  * Commits:
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

Version 5.0.0 (openpilot v0.8.2)
========================
  Source commit: 4d975819
  * Openpilot Changes:
    *  Use model points directly in MPC (no more polyfits), making lateral planning more accurate
    *  Use model heading prediction for smoother lateral control
    *  Smarter actuator delay compensation
    *  Improve qcamera resolution for improved video in explorer and connect
    *  Adjust maximum engagement speed to better fit the model's training distribution
    *  New driver monitoring model trained with 3x more diverse data
    *  Improved face detection with masks
    *  More predictable DM alerts when visibility is bad
    *  Rewritten video streaming between openpilot processes
    *  Improved longitudinal tuning on TSS2 Corolla and Rav4 thanks to briskspirit!
    *  Audi A3 2015 and 2017 support thanks to keeleysam!
    *  Nissan Altima 2020 support thanks to avolmensky!
    *  Lexus ES Hybrid 2018 support thanks to TheInventorMan!
    *  Toyota Camry Hybrid 2021 support thanks to alancyau!

Version 4.7.0 (openpilot v0.8.1)
========================
  Source commit: d3aeeba1
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

Version 4.6.0 (openpilot v0.8.1)
========================
  Source commit: 0e6dcd1b
  * Commits:
    * feat(actions): only push out release if build release works

Version 4.5.0 (openpilot v0.8.1)
========================
  Source commit: 55e9f61e
  * New OP Params:
    * ENABLE_PLANNER_PARAMS: Param(False, [bool], live=True)
    * ENABLE_PLNR_ACCEL_LIMITS: Param(False, [bool], live=True, depends_on=ENABLE_PLANNER_PARAMS)
  * Commits:
    * feat(params): add param to toggle planner params

Version 4.4.0 (openpilot v0.8.1)
========================
  Source commit: 0f74b346
  * Commits:
    * feat(version): update dirty tag to be based on my fork
    * feat(events): don't show startup event when on r2++
    * refactor(sentry): move sentry from crash and tombstone into sentryd
    * fix(sentry): pass args and kwargs to client
    * fix(sentry): track discord username before dongle id

Version 4.3.0 (openpilot v0.8.1)
========================
  Source commit: 5c6def4d
  * Commits:
    * chore(actions): remove unused sim tests workflow
    * feat(actions): add workflow to clean up old ci branches
    * feat(actions): check for error when deleting branch
    * fix(actions): properly get branch name sub string
    * feat(actions): log which branches are found
    * fix(actions): get correct length, set correct ref, and check correct status code
    * feat(actions): limit branch clean up to src branch

Version 4.2.0 (openpilot v0.8.1)
========================
  Source commit: 446ba0b8
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

Version 4.1.0 (openpilot v0.8.1)
========================
  Source commit: 17619301
  * New OP Params:
    * ENABLE_TOYOTA_CAN_PARAMS: Param(False, [bool], live=True, depends_on=SHOW_TOYOTA_OPTS)
    * ENABLE_TOYOTA_ACCEL_PARAMS: Param(False, [bool], live=True, depends_on=ENABLE_TOYOTA_CAN_PARAMS)
    * TOYOTA_ACC_TYPE: Param(1, [int], live=True, depends_on=ENABLE_TOYOTA_ACCEL_PARAMS)
    * TOYOTA_PERMIT_BRAKING: Param(1, [1, 0, 'lead'], live=True, depends_on=ENABLE_TOYOTA_ACCEL_PARAMS)
  * Commits:
    * feat(params): update op params with toyota specific can params
    * feat(toyota): update car controller to allow can message modification
    * fix(params): fix op edit to cast default values to str
    * tests(processes): update process replay refs for can-tuning

Version 4.0.0 (openpilot v0.8.1)
========================
  Source commit: 7f4bc738
  * Openpilot Changes:
    *  Original EON is deprecated, upgrade to comma two
    *  Better model performance in heavy rain
    *  Better lane positioning in turns
    *  Fixed bug where model would cut turns on empty roads at night
    *  Fixed issue where some Toyotas would not completely stop thanks to briskspirit!
    *  Toyota Camry 2021 with TSS2.5 support
    *  Hyundai Ioniq Electric 2020 support thanks to baldwalker!

Version 3.8.0 (openpilot v0.8.0)
========================
  Source commit: 6440d9fc
  * Commits:
    * fix(toyota): update default corolla tss2 indi tune

Version 3.7.0 (openpilot v0.8.0)
========================
  Source commit: 97d6a4e3
  * New OP Params:
    * ENABLE_MANAGER_PARAMS: Param(False, [bool], depends_on=SHOW_UNSAFE_OPTS)
    * DISABLED_PROCESSES: Param(None, [str, list, type(None)], description='You\'re on your own here', depends_on=ENABLE_MANAGER_PARAMS)
  * Commits:
    * feat(params): add param to disable processes
    * feat(mngr): update manager to start allowed processes
    * fix(params): only check list default if not none
    * fix(params): only check if not default
    * fix(params): allow op_edit to handle none as list default

Version 3.6.0 (openpilot v0.8.0)
========================
  Source commit: 063e93e6
  * Commits:
    * tests(numpy): add more tests for interp when array lens varry
    * fix(numpy): make interp work when fp is shorter
    * fix(numpy): possible fix for when xp is shorter
    * tests(numpy): add more test cases for when bp is shorter
    * fix(numpy): properly return last value when xp has reached the end
    * tests(numpy): add more test cases for when v is shorter
    * tests(numpy): add test case for xp containing values not in x
    * refactor(numpy): move calc_interp function back into get_interp

Version 3.5.0 (openpilot v0.8.0)
========================
  Source commit: b8436a2e
  * Commits:
    * 0b6e45f8-21c1-408a-b61d-3dce02a69d23/500 (#19528)

Version 3.4.0 (openpilot v0.8.0)
========================
  Source commit: a7a81f91
  * Commits:
    * Early model 081 (#19510)

Version 3.3.0 (openpilot v0.8.0)
========================
  Source commit: bb4a2226
  * Commits:
    * Revert fix(ui): remove engine rpm from ui

Version 3.2.0 (openpilot v0.8.0)
========================
  Source commit: d50d2dd4
  * New OP Params:
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

Version 3.1.0 (openpilot v0.8.0)
========================
  Source commit: 7baf74bb
  * Commits:
    * feat(ui): add dev ui to 0.8
    * fix(ui): remove liveMpc info from ui
    * fix(ui): remove engine rpm from ui
    * fix(release): make sure to include dashcam.h in release files
    * feat(toyota): record engine rpm into car state
    * tests(processes): update process replay refs for dev-ui

Version 3.0.0 (openpilot v0.8.0)
========================
  Source commit: ae1083d7
  * Openpilot Changes:
    *  New driving model: fully 3D and improved cut-in detection
    *  UI draws 2 road edges, 4 lanelines and paths in 3D
    *  Major fixes to cut-in detection for openpilot longitudinal
    *  Grey panda is no longer supported, upgrade to comma two or black panda
    *  Lexus NX 2018 support thanks to matt12eagles!
    *  Kia Niro EV 2020 support thanks to nickn17!
    *  Toyota Prius 2021 support thanks to rav4kumar!
    *  Improved lane positioning with uncertain lanelines, wide lanes and exits
    *  Improved lateral control for Prius and Subaru

Version 2.15.0 (openpilot v0.7.9)
========================
  Source commit: 36e9cd24
  * New OP Params:
    * self.fork_params = {CAM_OFFSET: Param(0.06, VT.number, 'Your camera offset to use in lane_planner.py', live=True)
    * SHOW_ACTUATOR_DELAY_PARAMS: Param(False, bool, live=True, depends_on=ENABLE_LAT_PARAMS)
    * STEER_ACTUATOR_DELAY: Param(0.60, VT.number, live=True, depends_on=SHOW_ACTUATOR_DELAY_PARAMS)
    * ENABLE_ACTUATOR_DELAY_BPS: Param(False, bool, live=True, depends_on=SHOW_ACTUATOR_DELAY_PARAMS)
    * STEER_ACTUATOR_DELAY_BP: Param([0.], [list, float, int], live=True, depends_on=ENABLE_ACTUATOR_DELAY_BPS)
    * STEER_ACTUATOR_DELAY_V: Param([0.6], [list, float, int], live=True, depends_on=ENABLE_ACTUATOR_DELAY_BPS)
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

Version 2.14.0 (openpilot v0.7.9)
========================
  Source commit: b95f8e32
  * Commits:
    * refactor(sentry): log all exceptions to sentry
    * fix(sentry): remove unused import in crash.py

Version 2.13.0 (openpilot v0.7.9)
========================
  Source commit: b70f8916
  * Commits:
    * chore(sentry): replace comma's sentry url with my own
    * feat(sentry): improve crash logging
    * fix(sentry): upload error tags to sentry

Version 2.12.0 (openpilot v0.7.9)
========================
  Source commit: b3d323d4
  * Commits:
    * fix(params): fix entering values into a list
    * fix(coasting): only update planner for updated model if coasting is enable

Version 2.11.0 (openpilot v0.7.9)
========================
  Source commit: 1ac1945e
  * Commits:
    * Revert Latest torch model

Version 2.10.0 (openpilot v0.7.9)
========================
  Source commit: 14162240
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
    * SHOW_A_CRUISE: Param(False, bool, live=True)
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

Version 2.9.0 (openpilot v0.7.9)
========================
  Source commit: ab8f6d5a
  * Commits:
    * feat(models): update model to 5034ac8b-5703-4a49-948b-11c064d10880/780 b5e5c420-7042-4d0c-92e5-770eb09936a5/800

Version 2.8.0 (openpilot v0.7.9)
========================
  Source commit: bada60f2
  * Commits:
    * db090195-8810-42de-ab38-bb835d775d87/601

Version 2.7.0 (openpilot v0.7.9)
========================
  Source commit: 1419a444
  * Commits:
    * 2895ace6-a296-47ac-86e6-17ea800a74e5/550

Version 2.6.0 (openpilot v0.7.9)
========================
  Source commit: a4e29af3
  * Commits:
    * chore(git): update panda submodule

Version 2.5.0 (openpilot v0.7.9)
========================
  Source commit: d7b005c5
  * New OP Params:
    * ENABLE_UNSAFE_STEERING_RATE: Param(False, bool)
  * Commits:
    * feat(toyota): add optional unsafe steering torqure rate

Version 2.4.0 (openpilot v0.7.9)
========================
  Source commit: 1f05c49d
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

Version 2.3.0 (openpilot v0.7.9)
========================
  Source commit: 784e5e90
  * New OP Params:
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
    * tests(processes): update process replay refs for eco-mode

Version 2.2.0 (openpilot v0.7.9)
========================
  Source commit: 2f1e9cf6
  * Commits:
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

Version 2.1.0 (openpilot v0.7.9)
========================
  Source commit: 0161ddc7
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

Version 2.0.0 (openpilot v0.7.9)
========================
  Source commit: 239ebfad
  * New OP Params:
    * 'indi_outer_gain_v': Param([15, 15, 15], [list, float, int], live=True)
  * Openpilot Changes:
    *  Improved car battery power management
    *  Improved updater robustness
    *  Improved realtime performance
    *  Reduced UI and modeld lags
    *  Increased torque on 2020 Hyundai Sonata and Palisade

Version 1.9.0 (openpilot v0.7.7)
========================
  Source commit: 4bac8e22
  * New OP Params:
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
    * feat(params): add new values to op params for indi breakpoints
    * feat(indi): update indi controller to have live breakpoints
    * fix(toyota): reset gas clip to 1.0
    * fix(params): properly op param default values match expected type

Version 1.8.0 (openpilot v0.7.7)
========================
  Source commit: 2ea8066f
  * Commits:
    * feat(toyota): update corolla TSS2 safety param
    * chore(git): update opendbc submodule for corolla TSS2 safety param
    * chore(git): fix opendbc submodule to use v0.7.7

Version 1.7.0 (openpilot v0.7.7)
========================
  Source commit: 88e7ed25
  * New OP Params:
    * 'accel_hyst_gap': Param(0.02, float, live=True)
    * 'always_eval_coast_plan': Param(False, bool)
    * 'gas_max_bp': Param([0., 20, 33], [list, float])
    * 'gas_max_v': Param([0.3, 0.2, 0.075], [list, float])
  * Commits:
    * feat(coasting): lower accel to 0 when coasting
    * fix(coasting): lower gas when last output was positive
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

Version 1.6.0 (openpilot v0.7.7)
========================
  Source commit: 3f6f12f3
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

Version 1.5.0 (openpilot v0.7.7)
========================
  Source commit: 8a62d538
  * Commits:
    * Better poly (#1437)

Version 1.4.0 (openpilot v0.7.7)
========================
  Source commit: edfa06a8
  * New OP Params:
    * 'corolla_use_indi': Param(False, bool)
  * Commits:
    * feat(toyota): made corolla indi optional

Version 1.3.0 (openpilot v0.7.7)
========================
  Source commit: fbfcac23
  * Commits:
    * chore(git): update cereal submodule to point to my fork
    * chore(git): replace all submodule relative urls with github urls

Version 1.2.0 (openpilot v0.7.7)
========================
  Source commit: 1821c6b1
  * Commits:
    * feat(actions): add new action for build slash command

Version 1.1.0 (openpilot v0.7.7)
========================
  Source commit: 3305587d
  * New OP Params:
    * 'alca_nudge_required': Param(False, bool, 'Whether to wait for applied torque to the wheel (nudge)
    * 'alca_min_speed': Param(20.0, VT.number, 'The minimum speed allowed for an automatic lane change (in MPH)')
  * Commits:
    * feat(path): add auto lane change option
    * fix(path): update default lane change values
    * fix(path): fix E502 in path planner

Version 1.0.0 (openpilot v0.7.7)
========================
  Source commit: a811bf18
  * New OP Params:
    * self.fork_params = {'camera_offset': Param(default=0.06, allowed_types=VT.number)
    * 'indi_inner_gain': Param(6.0, float, live=True)
    * 'indi_outer_gain': Param(15.0, float, live=True)
    * 'indi_time_constant': Param(5.5, float, live=True)
    * 'indi_actuator_effectiveness': Param(6.0, float, live=True)
    * 'steer_actuator_delay': Param(0.57, float, live=True)
    * self.fork_params['username'] = Param(None, [type(None), str, bool], 'Your identifier provided with any crash logs sent to Sentry.\nHelps the developer reach out to you if anything goes wrong')
  * Commits:
    * feat(params): add op_params and op_edit from shane's fork
    * feat(params): add support for live indi tunning and actuator breakpoints
    * refactor(params): remove unused op_params from shane's code
    * fix(params): add missing colors file for op params / edit
    * fix(indi): remove actuator effectiveness breakpoints
    * fix(params): fix flake incompatible types in assignment of colors
    * fix(indi): fix F401, unused import
    * fix(indi): reimport clip; fixes F821
    * fix(params): fix E1101; using Colors instead of COLORS
    * fix(params): fix W0102 in op_params
    * fix(params): fix W0102; remove default assignment
    * fix(params): fix missing assignment in constructor
    * fix(params): print instead of erroring out when reading file
    * fix(params): only read and write op params on mobile
    * fix(params): catch exception when can't write file
    * fix(params): turn err into string
    * fix(params): only change param file permissions if write passed

