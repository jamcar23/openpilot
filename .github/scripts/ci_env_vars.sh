#! /bin/bash

# Script that sets various environmental variables for the rest of the CI pipeline.

# Common "global" vars available to all and are used to build bigger variables.

export REPO="jamcar23/openpilot"
export REGISTRY_BASE="ghcr.io"
export MAIN_BRANCH="src"
export TEMP_IMAGE="tmppilotci"
export UNIT_TEST="coverage run --append -m unittest discover"

RUN_CMD_BASE="docker run --shm-size 1G -e PYTHONPATH=/tmp/openpilot -e GITHUB_ACTION -e GITHUB_REF -e GITHUB_HEAD_REF -e GITHUB_SHA -e GITHUB_REPOSITORY -e GITHUB_RUN_ID -v /tmp/comma_download_cache:/tmp/comma_download_cache"

# Functions
function eval_var()
{
    local __result_var=$1

    if [[ $2 = $3 ]]; then
        local __result='true'
    else
        local __result='' # Empty string because non-empty string are always true
    fi

    eval $__result_var="$__result"
}

# Evaluate Environment

eval_var IS_DEFAULT $GITHUB_REPOSITORY = $REPO

echo "Is default: $IS_DEFAULT"

# Export Environment
export IS_DEFAULT
