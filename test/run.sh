#!/bin/bash

java org.antlr.v4.Tool -Dlanguage=Python3 Parallelize.g4
java org.antlr.v4.gui.TestRig Parallelize program -gui test1.txt test2.txt
