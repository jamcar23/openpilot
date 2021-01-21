# Flexpilot
[![openpilot tests](https://github.com/jamcar23/openpilot/workflows/openpilot%20tests/badge.svg?event=push)](https://github.com/jamcar23/openpilot/actions)

# Table of Contents

- [Flexpilot](#flexpilot)
- [Table of Contents](#table-of-contents)
- [What is flexpilot?](#what-is-flexpilot)
- [What is openpilot?](#what-is-openpilot)
- [Installation](#installation)
- [Features](#features)
  - [Live Tuning](#live-tuning)
  - [Op Edit / Op Params](#op-edit--op-params)
  - [UI](#ui)
  - [Multidimensional Breakpoints](#multidimensional-breakpoints)
    - [How they work](#how-they-work)
    - [Breakpoint Sources](#breakpoint-sources)
    - [Param Modifiers](#param-modifiers)
- [Licensing](#licensing)

# What is flexpilot?

Flexpilot is a fork of openpilot focused on flexibility, live tuning, and other experimental features.

# What is openpilot?

[openpilot](http://github.com/commaai/openpilot) is an open source driver assistance system. Currently, openpilot performs the functions of Adaptive Cruise Control (ACC), Automated Lane Centering (ALC), Forward Collision Warning (FCW) and Lane Departure Warning (LDW) for a growing variety of supported [car makes, models and model years](#supported-cars). In addition, while openpilot is engaged, a camera based Driver Monitoring (DM) feature alerts distracted and asleep drivers.

# Installation
Easiest way is with this command:

`git clone https://github.com/jamcar23/openpilot.git --branch r2++ --depth 1`

Using the `r2++` branch is the easiest way to get the latest "release" features of this fork. Generally, all features are optional so there shouldn't be any harm is always running the latest features.

# Features
This serves as a general overview of notable changes made from other forks. Note: this fork is intended to be used by advanced users who know what they're doing. This fork is focused on experimentation and as such it will allow for things that are more unsafe then other forks.

## Live Tuning
Tuning is a huge feature in this fork, there are over 100 params in opParams, most of which are live. Please see [opParams](https://github.com/jamcar23/openpilot/blob/src/common/op_params.py#L161) for the latest list of parameters.

**Warning: a `(live!)` param means that the changes will take affect ~2.5 seconds after making them without needing a reboot, it does *not* mean that you should change them while driving or that you should engage in other unsafe behavior.**

**Further more, in some cases, it's possible to enter the incorrect data into opParams which, at worst, can lead to a process crashing. You do *not* want this happening while driving.** I've done my best to make sure you can only enter safe data and to handle potential errors however, there's always edge cases that may be missed.

## Op Edit / Op Params
I have made a few changes to opEdit and opParams, huge shout-out to [Shane](https://github.com/ShaneSmiskol/opParams) for the original work he did.

- **Nested Parameters**: _Parameters can now be nested, or hidden, under other boolean parameters_
  - If the bool param has `enable` in it then it is usually used to toggle a feature on or off (ex: `enable_lat_params`)
  - if the bool param has `show` in it then it usually only affects whether that params is shown an opEdit (ex: `show_indi_opts`)
- **Better list support**: _editing list in opEdit has been expanded with new features_
  - use `+value` to append a valid value to the end of a list
    - ex: if you have `[10, 20]` and you enter `+42` you'll get `[10, 20, 42]`
  - use `-index` to delete a valid index from the list
    - ex: if you have `[10, 20, 42]` and you enter `-1` you'll get `[10, 42]`
  - you can replace an entire list by typing out a valid python list
    - ex: if you have `[10, 42]` and you enter `[2, 5, 7]` you'll get `[2, 5, 7]`
- **Multidimensional List support**: _the new list features in opEdit apply to multidimensional lists of lists too_

## UI
Something something dev ui

## Multidimensional Breakpoints
Multidimensional breakpoints are a new, highly experimental feature which allows for more complex breakpoints that take into account multiple factors. In other words, you can have multiple sets of traditional breakpoints that are selected by another set of values. These can be further extended by defining different sources for each dimension which lets you build highly customizable tunes which weren't previously possible. As an example: in lat tuning, you can now build a tune that not only takes into account the speed the car's going (like we were previously) but also the desired steering angle of the path planner.

*Note: at the moment these are only available for indi and steer actuator delay breakpoints. I'm working on adding this functionality to other breakpoints as it makes sense.*

*Note: at the moment it selects each value list as is based on the closest index. In the future, I'd like to add an option to interpolate the lists themselves first.*

### How they work
Much like traditional breakpoints already in FP / OP multidimensional breakpoints also have `bp` and a `v` list, only this time they're a list of lists. Each list inside the `bp` list is a set of breakpoint points and can represent different factors. What these factors are is defined in another param called the `breakpoint source` (more below). Each list inside the `v` list is a set of output values.

Lets take a look an example tuning the indi inner gain breakpoints:

**Example**

In this example I'll walk you through how multidimensional breakpoints work.

**Recap**

Before we take a look at multidimensional breakpoints lets first look at how normal breakpoints works. Consider the following:

```
indi_inner_gain_bp: [20, 24, 30]
indi_inner_gain_v: [7.25, 7.5, 9]
```

Here `bp` contains a set of `v_ego` points while `v` is a set of values for the indi controller. From there the controller would read the car's `v_ego` and performs a one-dimensional piecewise linear interpolation, that is: it finds the two closest points in `bp` to `v_ego` and then interpolates between the values (in `v`) at the same index as the ones found.

Examples:
  - `v_ego` = 10, output is `7.25`
    - since `v_ego` is less than the first point (in `bp`), the first value (in `v`) is returned.
  - `v_ego` = 35, output is `9`
    - because `v_ego` is larger than the last point, the last value is returned.
  - `v_ego` = 22, output is `7.375`
    - since 22 is 50% between the first and second points, the output is 50% between the first and second values. (Note: this is generalized to all %s i.e. 10% between points is 10% between values, etc.)

**Moving on**

Now back to multidimensional breakpoints. As mentioned, multidimensional breakpoints still have points (`bp`) and values (`v`) lists. Lets now define what valid multidimensional breakpoints would look like:

```
indi_inner_gain_bp_multi: [[0, 6], [20, 24, 30]]
indi_inner_gain_v_multi: [[5.25, 5.5, 6], [6, 6.75, 7]]
```

I mentioned earlier that each list inside of `bp` was a set of points for some source data but what are they in this case? Well, we need to define another parameter:

```
indi_multi_breakpoint_source: ['desired_steer', 'v_ego']
```

Here are our sources for our points (`bp`): `desired_steer` and `v_ego`. More specifically, the first list in `bp` (`[0, 6]`) are breakpoints for the `desired_steer` while the second list are the points for `v_ego`.

During evaluation, the controller compares the first source (`desired_steer`) to the closest index in the first list in `bp`(`[0, 6]`). Once it finds that index it selects the list at the same index from `v` and interpolates the second source (`v_ego`) points with the select values as if it was a single dimensional array. In other words, you can have multiple sets of `v_ego` breakpoints that are selected based on the `desired_steer` of the path planner.

In the following lets look at some example evaluations. Here we'll be evaluating the `bp` and `v` arrays above by `x`. `x` is the input, it is a list with the same size as the `breakpoint source`. Each index in `x` is the value of the `breakpoint source` at that index. (Example: `x: [2, 24]` here the `desired_steer` is `2` while `v_ego` is `24`.)

**Examples:**
  - `x: [2, 24]`, output is `5.5`
    - 1st, compares `x[0]`(`2`) to `bp[0]`(`[0, 6]`)
    - 2nd, since `2` is closer to `0` select `v[0]`(`[5.25, 5.5, 6]`)
    - 3rd, `interp` `x[1]`(`24`) with `bp[1]`(`[20, 24, 30]`) and `v` from step 2
  - `x: [5, 35]`, output is `7`
    - 1st, compares `x[0]`(`5`) to `bp[0]`(`[0, 6]`)
    - 2nd, since `5` is closer to `6` select `v[1]`(`[6, 6.75, 7]`)
    - 3rd, `interp` `x[1]`(`35`) with `bp[1]`(`[20, 24, 30]`) and `v` from step 2
  - `x: [10, 5]`, output is `6`
    - 1st, compares `x[0]`(`10`) to `bp[0]`(`[0, 6]`)
    - 2nd, since `10` is closer to `6` select `v[1]`(`[6, 6.75, 7]`)
    - 3rd, `interp` `x[1]`(`5`) with `bp[1]`(`[20, 24, 30]`) and `v` from step 2

*Note: once again, I'm planning on expanding this by optionally interpolating both value arrays in the future.*

### Breakpoint Sources
Breakpoint sources are another set of parameters in OpParams however these are more of a "meta" param. In other words, they're a parameter that describes info about another parameter. More specifically they're used to know where to look when evaluating the multidimensional breakpoint.

In the examples above, how is `x` created? There is a function which takes in the source list and other cereal messages (e.g. `CarState`, `PathPlan`, etc.), evaluates each items in the source list, and then selects the source's value from the correct message.

The following should be kept in mind for breakpoint sources:

1. Sources are predefined and you should only enter existing, valid sources (See [BreakPointSourceKeys](https://github.com/jamcar23/openpilot/blob/src/common/op_params.py#L93)).
2. The order of sources matters and has a direct affect on how the breakpoints get evaluated.

*Note: at the moment, these are only being used for multidimensional breakpoints but I'm evaluating if these should be used in other places and or in other ways.*

### Param Modifiers
Param modifiers are special "keywords" that can be attached to the end of a string param in order to modify its value. See [ParamModifierKeys](https://github.com/jamcar23/openpilot/blob/src/common/op_params.py#L98) for an up to date list of available modifiers.

*Note: at the moment, these are only being used for breakpoint sources but I'm evaluating if these should be used in other places and or in other ways.*

**Example:**

Let's walk through another multidimensional breakpoint example with param modifiers or rather, let's rewalk through the old one.

Let's start by defining our initial values again:

```
indi_inner_gain_bp_multi: [[0, 6], [20, 24, 30]]
indi_inner_gain_v_multi: [[5.25, 5.5, 6], [6, 6.75, 7]]
indi_multi_breakpoint_source: ['desired_steer', 'v_ego']
```

So far so good, right? Not quite. See, `desired_steer` is positive when the steering wheel turns counter-clockwise and negative when turning clockwise (in my Toyota Corolla, other cars may be different). Spot the error? All clockwise turns will use the smaller `v` even during sharper turns.

So how can we fix this? Two ways...

1. we can update our points (`bp`) and values (`v`) to reflect positive and negative angles. This works but it's kind of a pain to do a lot and it makes dealing with the param in `op_edit` harder.

```
indi_inner_gain_bp_multi: [[-6, 0, 6], [20, 24, 30]]
indi_inner_gain_v_multi: [[6, 6.75, 7], [5.25, 5.5, 6], [6, 6.75, 7]]
```

2. we can use the `ABS` modifier to modify the value of the breakpoint source. In other words, we can take the absolute value of the desired steer from the path planner. To do this we append `_abs` to end of the source like so:

```
indi_multi_breakpoint_source: ['desired_steer_abs', 'v_ego']
```

Now that our `desired_steer` is always positive we can have our points (`bp`) and values (`v`) look like this:

```
indi_inner_gain_bp_multi: [[0, 6], [20, 24, 30]]
indi_inner_gain_v_multi: [[5.25, 5.5, 6], [6, 6.75, 7]]
```

# Licensing

Flexpilot is released under the MIT license. Some parts of the software are released under other licenses as specified.

**THIS IS ALPHA QUALITY SOFTWARE FOR RESEARCH PURPOSES ONLY. THIS IS NOT A PRODUCT.
YOU ARE RESPONSIBLE FOR COMPLYING WITH LOCAL LAWS AND REGULATIONS.
NO WARRANTY EXPRESSED OR IMPLIED.**

<img src="https://d1qb2nb5cznatu.cloudfront.net/startups/i/1061157-bc7e9bf3b246ece7322e6ffe653f6af8-medium_jpg.jpg?buster=1458363130" width="75"></img> <img src="https://cdn-images-1.medium.com/max/1600/1*C87EjxGeMPrkTuVRVWVg4w.png" width="225"></img>

