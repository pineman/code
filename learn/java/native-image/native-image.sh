#!/bin/sh
native-image -H:EnableURLProtocols=https -cp '/app/resources:/app/classes:/app/libs/*' eu.pineman.learn.native_image.Test
