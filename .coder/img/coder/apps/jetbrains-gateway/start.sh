#!/bin/sh

# Kill any existing sessions
kill $(ps aux | grep "opt/idea/jbr/bin/java" | awk {'print $2'})

/opt/idea/bin/remote-dev-server.sh run /home/coder --ssh-link-host coder.$CODER_ENVIRONMENT_NAME > $HOME/jetbrains-dev-server.log &