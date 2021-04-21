Version 53
========================
  Source commit: 33e98404
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
  Source commit: 92d4c8f6
  * Commits:
    * no heading cost (#20594)
    * MPC retune for laneless fix (#20616)
    * fix(planner): properly set custom steer rate cost
    * fix(planner): temp remove wide camera from lat planner
    * fix(planner): get bool param correctly

Version 51
========================
  Source commit: 124b95b3
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
  Source commit: a378051f
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
  Source commit: dcd91d2f
  * Commits:
    * fix(ui): change home screen to say flexpilot instead of op

Version 48
========================
  Source commit: 550c0109
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
  Source commit: 48763617

Version 46
========================
  Source commit: 2caaf37f
  * Commits:
    * feat(ui): port colored lane lines from shane
    * fix(ui): add model reader to ui scene
    * docs(readme): update GH action status badges

Version 45
========================
  Source commit: 3b2b4e0b
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
  Source commit: 4d975819
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

Version 43
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
  Source commit: 0e6dcd1b
  * Commits:
    * feat(actions): only push out release if build release works

Version 41
========================
  Source commit: 55e9f61e
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
  Source commit: 0f74b346
  * Commits:
    * feat(version): update dirty tag to be based on my fork
    * feat(events): don't show startup event when on r2++
    * refactor(sentry): move sentry from crash and tombstone into sentryd
    * fix(sentry): pass args and kwargs to client
    * fix(sentry): track discord username before dongle id

Version 39
========================
  Source commit: 5c6def4d
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

Version 37
========================
  Source commit: 17619301
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
  Source commit: 7f4bc738

Version 35
========================
  Source commit: 6440d9fc
  * Commits:
    * fix(toyota): update default corolla tss2 indi tune

Version 34
========================
  Source commit: 97d6a4e3
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

Version 32
========================
  Source commit: b8436a2e
  * Commits:
    * 0b6e45f8-21c1-408a-b61d-3dce02a69d23/500 (#19528)

Version 31
========================
  Source commit: a7a81f91
  * Commits:
    * Early model 081 (#19510)

Version 30
========================
  Source commit: bb4a2226
  * Commits:
    * Revert fix(ui): remove engine rpm from ui

Version 29
========================
  Source commit: d50d2dd4
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
  Source commit: 7baf74bb
  * Commits:
    * feat(ui): add dev ui to 0.8
    * fix(ui): remove liveMpc info from ui
    * fix(ui): remove engine rpm from ui
    * fix(release): make sure to include dashcam.h in release files
    * feat(toyota): record engine rpm into car state
    * tests(processes): update process replay refs for dev-ui

Version 27
========================
  Source commit: ae1083d7

Version 26
========================
  Source commit: 36e9cd24
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
  Source commit: b95f8e32
  * Commits:
    * refactor(sentry): log all exceptions to sentry
    * fix(sentry): remove unused import in crash.py

Version 24
========================
  Source commit: b70f8916
  * Commits:
    * feat(actions): update refs now removes old refs
    * chore(sentry): replace comma's sentry url with my own
    * feat(sentry): improve crash logging
    * fix(sentry): upload error tags to sentry

Version 23
========================
  Source commit: b3d323d4
  * Commits:
    * fix(params): fix entering values into a list
    * fix(coasting): only update planner for updated model if coasting is enable

Version 22
========================
  Source commit: 1ac1945e
  * Commits:
    * Revert Latest torch model

Version 21
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
  Source commit: ab8f6d5a
  * Commits:
    * feat(models): update model to 5034ac8b-5703-4a49-948b-11c064d10880/780 b5e5c420-7042-4d0c-92e5-770eb09936a5/800

Version 19
========================
  Source commit: bada60f2
  * Commits:
    * db090195-8810-42de-ab38-bb835d775d87/601

Version 18
========================
  Source commit: 1419a444
  * Commits:
    * 2895ace6-a296-47ac-86e6-17ea800a74e5/550

Version 17
========================
  Source commit: a4e29af3
  * Commits:
    * chore(git): update panda submodule

Version 16
========================
  Source commit: d7b005c5
  * New OP Params:
    * 'coast_speed': Param(10.0, VT.number, 'The amount of speed to coast by before applying the brakes. Unit: MPH')
    * 'a_cruise_max_v_following': Param([1.6, 1.4, 1.4, .7, .3], [list, float], live=True)
    * ENABLE_UNSAFE_STEERING_RATE: Param(False, bool)
  * Commits:
    * feat(toyota): add optional unsafe steering torqure rate

Version 15
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

Version 14
========================
  Source commit: 784e5e90
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
  Source commit: 2f1e9cf6
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

Version 11
========================
  Source commit: 239ebfad
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
  Source commit: 4bac8e22
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
  Source commit: 2ea8066f
  * Commits:
    * feat(toyota): update corolla TSS2 safety param
    * chore(git): update opendbc submodule for corolla TSS2 safety param
    * chore(git): fix opendbc submodule to use v0.7.7

Version 8
========================
  Source commit: 88e7ed25
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

Version 6
========================
  Source commit: 8a62d538
  * Commits:
    * Better poly (#1437)

Version 5
========================
  Source commit: edfa06a8
  * New OP Params:
    * 'alca_min_speed': Param(20.0, VT.number, 'The minimum speed allowed for an automatic lane change (in MPH)')
    * 'corolla_use_indi': Param(False, bool)
  * Commits:
    * feat(toyota): made corolla indi optional

Version 4
========================
  Source commit: fbfcac23
  * Commits:
    * chore(git): update cereal submodule to point to my fork
    * chore(git): replace all submodule relative urls with github urls

Version 3
========================
  Source commit: 1821c6b1
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
  Source commit: 3305587d
  * New OP Params:
    * 'steer_actuator_delay': Param(0.57, float, live=True)
    * 'alca_nudge_required': Param(False, bool, 'Whether to wait for applied torque to the wheel (nudge)
    * 'alca_min_speed': Param(20.0, VT.number, 'The minimum speed allowed for an automatic lane change (in MPH)')
  * Commits:
    * hotfix(actions): switch release branch to r2++
    * feat(path): add auto lane change option
    * fix(path): update default lane change values
    * fix(path): fix E502 in path planner
