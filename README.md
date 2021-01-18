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
  - [Multidimensional Breakpoints](#multidimensional-breakpoints)
    - [How they work](#how-they-work)
- [Licensing](#licensing)

- [Installation](#installation)
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
Tuning is a huge feature in this fork, there are over 100 params in opParams, most of which are live. Please see [opParams](https://github.com/jamcar23/openpilot/blob/src/common/op_params.py#L75) for the latest list of parameters.

## Op Edit / Op Params
I have made a few changes to opEdit and opParams, huge shout out to [Shane](https://github.com/ShaneSmiskol/opParams) for the original work he did.

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
- **Multidimensional List support**: _the new list feats in opEdit apply to multidimensional lists of lists too_

## Multidimensional Breakpoints
Multidimensional breakpoints are a new, highly experimental feature which allows for more complex breakpoints that take into account multiple factors.

*Note: at the moment these are only available for indi breakpoints. I'm working on adding this functionality to other breakpoints as it makes sense.*

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
    - since 22 is halfway between the first and second points, the output is halfway between the first and second values.

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

# Licensing

Flexpilot is released under the MIT license. Some parts of the software are released under other licenses as specified.

**THIS IS ALPHA QUALITY SOFTWARE FOR RESEARCH PURPOSES ONLY. THIS IS NOT A PRODUCT.
YOU ARE RESPONSIBLE FOR COMPLYING WITH LOCAL LAWS AND REGULATIONS.
NO WARRANTY EXPRESSED OR IMPLIED.**

<img src="https://d1qb2nb5cznatu.cloudfront.net/startups/i/1061157-bc7e9bf3b246ece7322e6ffe653f6af8-medium_jpg.jpg?buster=1458363130" width="75"></img> <img src="https://cdn-images-1.medium.com/max/1600/1*C87EjxGeMPrkTuVRVWVg4w.png" width="225"></img>

