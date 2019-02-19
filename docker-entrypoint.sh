#!/bin/bash

source deploy/variables.env && pytest tests --driver Chrome
