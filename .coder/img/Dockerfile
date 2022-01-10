# See our guides for writing custom images:
# https://coder.com/docs/guides/customization

FROM codercom/enterprise-java:ubuntu

# Run everything as root
USER root

# Packages required for multi-editor support
RUN DEBIAN_FRONTEND="noninteractive" apt-get install -y \
    libxtst6 \
    libxrender1 \
    libfontconfig1 \
    libxi6 \
    libgtk-3-0

# Install IntelliJ IDEA (2021.3.1)
#
# this will be used for the remote-dev-server as well as
# for JetBrains Projector in the web browser
RUN mkdir -p /opt/idea
RUN curl -L "https://download.jetbrains.com/idea/ideaIU-2021.3.1.tar.gz" | tar -C /opt/idea --strip-components 1 -xzvf -

# Add a binary to the PATH that points to the intellij startup script.
RUN ln -s /opt/idea/bin/idea.sh /usr/bin/intellij-idea-community

# Copy Coder folder (apps and configure)
COPY coder /coder 

# Install requirements for the local-app-helper
RUN pip3 install -r /coder/apps/local-app-helper/requirements.txt

# Set back to coder user
USER coder

ENV PATH=/home/coder/.local/bin:$PATH