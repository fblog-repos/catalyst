#!/bin/bash

. /tmp/chroot-functions.sh

update_env_settings

if [ -n "${clst_CCACHE}" ]
then
	run_emerge -C dev-util/ccache || exit 1
fi

if [ -n "${clst_DISTCC}" ]
then
	run_emerge -C sys-devel/distcc || exit 1
fi

cleanup_distcc

rm -f /var/log/emerge.log
