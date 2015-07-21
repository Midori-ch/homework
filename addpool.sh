#!/bin/bash
ceph osd pool create .rgw 128 128;
sleep 10;
ceph osd pool create .rgw.root 128 128;
sleep 10;
ceph osd pool create .rgw.control 128 128;
sleep 10;
ceph osd pool create .rgw.gc 128 128;
sleep 10;
ceph osd pool create .rgw.buckets 128 128;
sleep 10;
ceph osd pool create .rgw.buckets.index 128 128;
sleep 10;
ceph osd pool create .log 128 128;
sleep 10;
ceph osd pool create .intent-log 128 128;
sleep 10;
ceph osd pool create .usage 128 128;
sleep 10;
ceph osd pool create .users 128 128;
sleep 10;
ceph osd pool create .users.email 128 128;
sleep 10;
ceph osd pool create .users.swift 128 128;
sleep 10;
ceph osd pool create .users.uid 128 128
